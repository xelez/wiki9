"""
PHP pickle module for Python to unserialize PHP data.

Limited to unserialization of basic PHP types:

boolean -> bool
integer
float
string  -> str
array   -> list of tuples (key, value)
NULL    -> None

Not supported:

object
resource

"""


def stub(errormsg):
  """callback stub for parse errors"""
  pass
  
def error_print(errormsg):
  """callback that prints parse errors to output (default)"""
  print "PHP data unserialize failed: %s" % errormsg



import re

__version__ = "$Revision$"

def unserialize(data, inrec=False, errcb=None):
   """
   Unserialize PHP data.

   Supports:
    boolean value (0 or 1 -> False or True)
    >>> data = "b:0;"; unserialize(data)
    False

    integer
    >>> data = "i:-33;"; unserialize(data)
    -33
    >>> data = "i:-2147483647;"; z = unserialize(data); z
    -2147483647
    >>> type(z)
    <type 'int'>

    float
    >>> data = "d:0.670000000000000017763568394002504646778106689453125;";
    >>> unserialize(data)
    0.67000000000000004

    string - serialization format "s:<length>:<content>;"
    >>> data = 's:7:"version";'; unserialize(data)
    'version'

    array to dict, format: 
    a:2:{s:7:"version";s:3:"457";s:12:"version_beta";s:3:"461";}
       a:2:  - associative massive with two elements
       {...} - key_string;value;key_string;value;
    >>> data = 'a:2:{s:7:"version";s:3:"457";s:12:"version_beta";s:3:"461";};';
    >>> unserialize(data)
    [('version', '457'), ('version_beta', '461')]

    NULL
    >>> data = "N;"; unserialize(data)


   @param inrec: internal parameter to detect recursive calls
   @param errcb: error callback that is called when transformation
                 fails for whatever reason
   @return mixed or tuple (mixed, <chars eaten>) if inrec is True
   """

   def parse_len(data):
      """ parses ':len:data;' input
          returns eaten, data_len 
          returns None, None on error
      """
      # :<length>:;
      lenre = re.compile(r'(:(\d+):).+')
      match = lenre.match(data)
      if match == None:
         return (None,)*2
      return int(match.group(2)), len(match.group(1))


   def skip(iterable, amount):
      [iterable.next() for x in range(amount)]


   if errcb == None:
      errcb = error_print

       
   myvar = None
   diter = enumerate(data)
   eaten = 0
   for i,c in diter:
      eaten += 1
      if c == 'a':
         myvar = []
         dlen, leaten = parse_len(data[eaten:])

         if leaten == None:
            errcb("a\n\n%s" % data)
         else:
            eaten += leaten
            if data[eaten] != '{':
               errcb("{\n\n%s" % data)
            eaten += 1
            for x in range(dlen):
               (key, parsed) = unserialize(data[eaten:], True)
               eaten += parsed
               (value, parsed) = unserialize(data[eaten:], True)
               myvar.append( (key, value) )
               eaten += parsed
            if data[eaten] != '}':
               errcb("}\n\n%s" % data)
      elif c == 's':
         dlen, leaten = parse_len(data[eaten:])
         if leaten == None:
            errcb("s\n\n%s" % data)
         else:
            eaten += leaten
            if data[eaten] != '"':
               errcb("opening \"\n\n%s" % data)
            eaten += 1
            myvar = data[eaten:eaten+dlen]
            eaten += dlen
            if data[eaten] != '"':
               errcb("closing \"\n\n%s" % data)
            eaten += 1
            if data[eaten] != ';':
               errcb("closing ;\n\n%s" % data)
            eaten += 1
      elif c == 'b':
         match = re.match("(:([01]);)", data[eaten:])
         if not match:
            errcb("bool\n\n%s" % data)
         eaten += len(match.group(1))
         myvar = bool(int(match.group(2)))
      elif c == 'i':
         match = re.match("(:(-?\d+);)", data[eaten:])
         if not match:
            errcb("int\n\n%s" % data)
         eaten += len(match.group(1))
         myvar = int(match.group(2))
      elif c == 'd':
         match = re.match("(:(-?\d+(.\d+)?);)", data[eaten:])
         if not match:
            errcb("double\n\n%s" % data)
         eaten += len(match.group(1))
         myvar = float(match.group(2))
      elif c == 'N':
         myvar = None
         if not data[eaten] == ';':
            errcb("';'\n\n%s" % data)
         eaten += 1




      if not inrec:
         return myvar
      else:
         return (myvar, eaten)


if __name__ == "__main__":
   """ doc tests
   """
   import doctest
   doctest.testmod(report=True)


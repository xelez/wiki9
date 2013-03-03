$(function() {
    // Highlight current nav
    $('#sidenav ul ul').hide();
    myurl = location.href;
    $('#sidenav ul li a').filter(function() {
        return myurl.indexOf($(this)[0].href) == 0;
    }).closest('li').addClass('active').children('ul').show();


    // Close alerts on click
    $(".alert-box").click(function() {
        $(this).hide(); 
    });

    $(".alert-container").hide().fadeIn('slow').delay(5000).fadeOut('slow');
})

// Validation config TODO: rewrite or delete
/* $.validator.addMethod(
        "regex",
        function(value, element, regexp) {
            var re = new RegExp(regexp);
            return this.optional(element) || re.test(value);
        },
        "Please check your input."
);
            
jQuery.extend(jQuery.validator.messages, {
    required: "Обязательное поле.",
    remote: "Please fix this field.",
    email: "Please enter a valid email address.",
    url: "Please enter a valid URL.",
    date: "Please enter a valid date.",
    dateISO: "Please enter a valid date (ISO).",
    number: "Please enter a valid number.",
    digits: "Please enter only digits.",
    creditcard: "Please enter a valid credit card number.",
    equalTo: "Please enter the same value again.",
    accept: "Please enter a value with a valid extension.",
    maxlength: jQuery.validator.format("Please enter no more than {0} characters."),
    minlength: jQuery.validator.format("Please enter at least {0} characters."),
    rangelength: jQuery.validator.format("Please enter a value between {0} and {1} characters long."),
    range: jQuery.validator.format("Please enter a value between {0} and {1}."),
    max: jQuery.validator.format("Please enter a value less than or equal to {0}."),
    min: jQuery.validator.format("Please enter a value greater than or equal to {0}.")
});
*/

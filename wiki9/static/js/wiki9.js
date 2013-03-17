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

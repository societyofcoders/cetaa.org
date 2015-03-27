(function ($) {
    
    "use strict";

/* =================================
===  MAILCHIMP                 ====
=================================== */
    $('.mailchimp').ajaxChimp({
        callback: mailchimpCallback,
        url: "http://webdesign7.us6.list-manage.com/subscribe/post?u=9445a2e155b82208d73433060&amp;id=16dc80e353" //Replace this with your own mailchimp post URL. Don't remove the "". Just paste the url inside "".  
    });

    function mailchimpCallback(resp) {
        if (resp.result === 'success') {
            $('.subscription-success').html('<span class="icon_check_alt2"></span>' + resp.msg).fadeIn(1000);
            $('.subscription-error').fadeOut(500);
        }
        else if (resp.result === 'error') {
            $('.subscription-error').html('<span class="icon_close_alt2"></span>' + resp.msg).fadeIn(1000);
        }
    }


/* =================================
===  STICKY NAV                 ====
=================================== */
    $('.main-navigation').onePageNav({
        scrollThreshold: 0.2, // Adjust if Navigation highlights too early or too late
        scrollOffset: 75, //Height of Navigation Bar
        filter: ':not(.external)',
        changeHash: true
    }); 

    /* NAVIGATION VISIBLE ON SCROLL / NOTE: In this style, Navigation always visible. I kept the code so you can hide it if you want. */

    mainNav();
    $(window).scroll(function () {
        mainNav();
    });

    function mainNav() {
        var top = (document.documentElement && document.documentElement.scrollTop) || document.body.scrollTop;
        if (top > 40) $('.sticky-navigation').stop().animate({
            "opacity": '1',
            "top": '0'
        });
        else $('.sticky-navigation').stop().animate({
            "opacity": '1',
            "top": '0'
        });
    }


/* =================================
===  OWL CROUSEL               ====
=================================== */
    var owl = $("#screenshots");
    owl.owlCarousel({
        items: 3, //3 items above 1000px browser width
        itemsDesktop: [1000, 3], //3 items between 1000px and 901px
        itemsDesktopSmall: [900, 2], // betweem 900px and 601px
        itemsTablet: [600, 1], //1 items between 600 and 0
        itemsMobile: false, // itemsMobile disabled - inherit from itemsTablet option
        navigation: false, // Show next and prev buttons
        slideSpeed: 800,
        paginationSpeed: 400,
        autoPlay: 5000,
        stopOnHover: true
    });

    var owl = $("#feedbacks");
    owl.owlCarousel({
        items: 3, //3 items above 1000px browser width
        itemsDesktop: [1000, 2], //2 items between 1000px and 901px
        itemsDesktopSmall: [900, 2], // betweem 900px and 601px
        itemsTablet: [600, 1], //1 items between 600 and 0
        itemsMobile: false, // itemsMobile disabled - inherit from itemsTablet option
        navigation: false, // Show next and prev buttons
        stopOnHover: true
    });


/* =================================
===  Nivo Lightbox              ====
=================================== */
    $('#screenshots a').nivoLightbox({
        effect: 'fadeScale',
    });


/* =================================
===  CONTACT FORM               ====
=================================== */
    $("#contact").submit(function (e) {
        e.preventDefault();
        var name = $("#cf-name").val();
        var email = $("#cf-email").val();
        var subject = $("#cf-subject").val();
        var message = $("#cf-message").val();
        var dataString = 'name=' + name + '&email=' + email + '&subject=' + subject + '&message=' + message;

        function isValidEmail(emailAddress) {
            var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
            return pattern.test(emailAddress);
        };
        if (isValidEmail(email) && (message.length > 1) && (name.length > 1)) {
            $.ajax({
                type: "POST",
                url: "sendmail.php",
                data: dataString,
                success: function () {
                    $('.success').fadeIn(1000);
                    $('.error').fadeOut(500);
                }
            });
        }
        else {
            $('.error').fadeIn(1000);
            $('.success').fadeOut(500);
        }
        return false;
    });


/* =================================
===  EXPAND COLLAPSE            ====
=================================== */
    $('.expand-form').simpleexpand({
        'defaultTarget': '.expanded-contact-form'
    });


/* =================================
===  DOWNLOAD BUTTON CLICK SCROLL ==
=================================== */
    $('#cta-1, #cta-2, #cta-3, #cta-4, #cta-5').localScroll({
        duration: 1000
    });



/* =================================
===  RESPONSIVE VIDEO             ==
=================================== */
    $(".video-container").fitVids();


/* =================================
===  SMOOTH SCROLL             ====
=================================== */
    var scrollAnimationTime = 1200,
        scrollAnimation = 'easeInOutExpo';
    $('a.scrollto').bind('click.smoothscroll', function (event) {
        event.preventDefault();
        var target = this.hash;
        $('html, body').stop().animate({
            'scrollTop': $(target).offset().top
        }, scrollAnimationTime, scrollAnimation, function () {
            window.location.hash = target;
        });
    });


/* =================================
===  Bootstrap Internet Explorer 10 in Windows 8 and Windows Phone 8 FIX
=================================== */
    if (navigator.userAgent.match(/IEMobile\/10\.0/)) {
        var msViewportStyle = document.createElement('style')
        msViewportStyle.appendChild(
        document.createTextNode('@-ms-viewport{width:auto!important}'))
        document.querySelector('head').appendChild(msViewportStyle)
    }
})(jQuery);




$(window).resize(function () {

    "use strict";

    var ww = $(window).width();
    
    /* COLLAPSE NAVIGATION ON MOBILE AFTER CLICKING ON LINK */
    
    if (ww < 480) {
        $('.main-navigation a').on('click', function () {
            $(".navbar-toggle").click();
        });
    }
});
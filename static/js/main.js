$(document).ready(function () {
    'use strict';


    setTimeout(function () {
        $('.loader_bg').fadeToggle();
    }, 1500);

    $(window).on('scroll', function() {
        if ($(".navbar").offset().top > 50) {
            $(".navbar-fixed-top").addClass("top-nav-collapse");
        } else {
            $(".navbar-fixed-top").removeClass("top-nav-collapse");
        }
    });

    $(document).on('click', '.navbar-collapse.in', function (e) {
        if ($(e.target).is('a') && $(e.target).attr('class') != 'dropdown-toggle') {
            $(this).collapse('hide');
        }
    });

    $('body').scrollspy({
        target: '.navbar-collapse',
        offset: 195
    });

    $('a.smooth-menu,a.my-btn-1,a.my-btn-2,a.my-btn-3').on("click", function (e) {
        e.preventDefault();
        var anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $(anchor.attr('href')).offset().top - 50
        }, 1000);
    });


    $('.navbar-collapse ul li a').on('click', function() {
        $('.navbar-toggle:visible').click();
    });
    $(window).load(function(){


    });




    $('.view').magnificPopup({
        type:'image',
        gallery: {
            enabled: true
        },
        zoom: {
            enabled: true,
            duration: 300,
            opener: function(element) {
                return element.find('img');
            }
        }
    });

    $('.video-view').magnificPopup({
        type:'iframe',
        zoom: {
            enabled: true,
            duration: 300
        }
    });




    new WOW().init();


});
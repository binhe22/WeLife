$(document).ready(function(){
$(function () {
    var menuOpen = false;
    //container1
    $('#container1').highcharts({
        title:{
            text:'室内外温度'
        },
        chart: {
            width:600,
            backgroundColor: '#fff'
        },

        credits: {
            enabled: false
        },

        xAxis: {
            categories: ['09:00','10:00','11:00','12:00','13:00','14:00'],
            title:{
                text:'时间 '
            }
        },

        series: [{
            data: [24.8,25.2,24.6,24.5,24.6,25.0],
            name:'室内'
        },
        {
            data:[22.4,23.1,22.8,22.9,23.2,23.5],
            name:'室外'
        }
        ],

        navigation: {
            buttonOptions: {
                enabled: false
            }
        }
    });

    $('#container2').highcharts({
        title:{
            text:'室内湿度'
        },
        chart: {
            width:600,
            backgroundColor: '#fff'
        },

        credits: {
            enabled: false
        },

        xAxis: {
            categories: ['02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00'],
            title:{
                text:'时间 '
            }
        },

        series: [{
            data: [65,66,68,66,70,72,71,73,71,70,68,66],
            name:'湿度(%)'
        }],

        navigation: {
            buttonOptions: {
                enabled: false
            }
        }
    });
    $('#container3').highcharts({
        title:{
            text:'PM 2.5'
        },
        chart: {
            width:600,
            backgroundColor: '#fff'
        },

        credits: {
            enabled: false
        },

        xAxis: {
            categories: ['06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00'],
            title:{
                text:'时间 '
            }
        },

        series: [{
            data: [78,77,76,76,78,80,81,85,85,84,83,83],
            name:'指数'
        }],

        navigation: {
            buttonOptions: {
                enabled: false
            }
        }
    });
    // the button handler
    $('#button1').click(function() {
        var chart1 = $('#container1').highcharts();
        chart1.exportChart({
            type: 'application/png',
            filename: 'house-in-out-temp'
        });
    });
    $('#button2').click(function() {
        var chart2 = $('#container2').highcharts();
        chart2.exportChart({
                type: 'application/png',
                filename: 'house-wet'
        });
    });
    $('#button3').click(function() {
        var chart3 = $('#container3').highcharts();
        chart3.exportChart({
                type: 'application/png',
                filename: 'PM2.5'
        });
    });

    //the menu animation
     
        if ( $.fn.makisu.enabled ) {

            var $nigiri = $( '.nigiri' );

            // Create Makisus

            $nigiri.makisu({
                selector: 'dd',
                overlap: 0.85,
                speed: 1.7
            });

            // Open all
            
           // $( '.list' ).makisu( 'open' );

            // Toggle on click

            //$( '.toggle' ).on( 'click', function() {
              //  $( '.list' ).makisu( 'toggle' );
            //});
            $('.toggle-list dt').mouseenter(function() {
                /* Stuff to do when the mouse enters the element */
                if (!menuOpen) {
                    $('.list').makisu('open');
                    menuOpen = true;
                };
                
            });
            $('.toggle-list').mouseleave(function(event) {
                /* Act on the event */
                if (menuOpen) {
                    $('.list').makisu('close');
                    menuOpen = false;
                };
            });

        } else {
            $( '.warning' ).show();
        }

});
});

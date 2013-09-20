$(document).ready(function(){
$(function () {
    var menuOpen = false;
    //container1
    $('#container1').highcharts({
            chart: {
                type: 'area'
            },
            title: {
                text: '用电量情况与剩余电量'
            },
            xAxis: {
                categories: ['9.1', '9.2', '9.3', '9.4', '9.5', '9.6', '9.7'],
                tickmarkPlacement: 'on',
                title: {
                    enabled: false
                }
            },
            yAxis: {
                title: {
                    text: '度数'
                },
                
            },
            tooltip: {
                shared: true,
                valueSuffix: '度'
            },
            plotOptions: {
                area: {
                    lineColor: '#666666',
                    lineWidth: 1,
                    marker: {
                        lineWidth: 1,
                        lineColor: '#666666'
                    }
                }
            },
            series: [{
                name: '用电量',
                data: [8.6, 16.2, 22.4, 28.6, 38.8, 45.0, 54.3]
            }, 
            {
                name: '剩余电量',
                data: [91.4, 83.8, 77.6, 71.4, 61.2, 55.0, 45.7]
            }]
        });

    
    // the button handler
    $('#button1').click(function() {
        var chart1 = $('#container1').highcharts();
        chart1.exportChart({
            type: 'application/png',
            filename: 'house-electric'
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

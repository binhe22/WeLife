$(document).ready(function(){
$(function () {
    var menuOpen = false;
    //container1
    

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
            
            $( '.list' ).makisu( 'open' );

            // Toggle on click

            $( '.login-but' ).on( 'click', function() {
                var usrname = $(".account").attr("value");
                var paswd = $(".psw").attr("value");
                if (usrname=="WeLife"&&paswd=="uniquestudio") {
                    $( '.list' ).makisu( 'close' );
                    window.location.href="index.html?backurl="+window.location.href; 
                }else{
                    alert("用户名或密码不正确");
                };
                
                //window.navigate("index.html"); 
                
            });
            

        } else {
            $( '.warning' ).show();
        }

});
});

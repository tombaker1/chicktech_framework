/*
 * Please see the included README.md file for license terms and conditions.
 */


// This file is a suggested starting place for your code.
// It is completely optional and not required.
// Note the reference that includes it in the index.html file.


/*jslint browser:true, devel:true, white:true, vars:true */
/*global $:false, intel:false app:false, dev:false, cordova:false */



// This file contains your event handlers, the center of your application.
// NOTE: see app.initEvents() in init-app.js for event handler initialization code.

function myEventHandler() {
    "use strict" ;

    var ua = navigator.userAgent ;
    var str ;

    if( window.Cordova && dev.isDeviceReady.c_cordova_ready__ ) {
            str = "You have successfully joined the ChickTech Nation" ;
    }
    else if( window.intel && intel.xdk && dev.isDeviceReady.d_xdk_ready______ ) {
            str = "You have successfully joined the ChickTech Nation" ;
    }
    else {
        str = "Bad device ready, or none available because we're running in a browser." ;
    }

    alert(str) ;
}


	




// ...additional event handlers here...


$( "#id_btnSubmit" ).click(function( event ) {
  alert( "Handler for .submit() called." );
  event.preventDefault();
    console.log("Handler for .submit() called.");
    
    // fill message
    message = {}
    message.name = $("input[name='Name']").val();
    message.name = $("input[name='Email']").val();
    message.name = $("input[name='Phone']").val();
    console.log(message.name);
});
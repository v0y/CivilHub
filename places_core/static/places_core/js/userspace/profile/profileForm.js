//
// profileForm.js
// ==============
//
// Edit user's profile.
//
require(['jquery',
         'jqueryui',
         'js/editor/customCKEditor'],

function ($) {
    "use strict";
    
    $('#birth-date').datepicker({
        changeMonth: true,
        changeYear: true,
        minDate: new Date(1920, 1 - 1, 1),
        maxDate: 0
    });
    
    $('#id_description').customCKEditor('custom');
});
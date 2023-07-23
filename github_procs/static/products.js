console.log("Document is ready");
load_products();

//-----------------------------------------------------------
$( "#btn_ajaxData" ).on( "click", function() {
    load_products();
} );

//-----------------------------------------------------------
async function load_products () {
    console.log("products.js was executed");
    disableForm();
    await loadDataAjax();
}

//-----------------------------------------------------------
function disableForm() {
    console.log( "disableForm called." );
    $("#btn_ajaxData").html("Loading ...");
    $('button').prop('disabled', 'disabled');
    $('#form_wrapper :input').prop('disabled', true);
    $('#form_wrapper select').prop('disabled', true);
    $('#form_wrapper :submit').prop('disabled', true);
}

//-----------------------------------------------------------
function enableForm() {
    console.log( "enableForm called." );
    $("#btn_ajaxData").html("Refresh Data");
    $('#form_wrapper :input').prop('disabled', false);
    $('#form_wrapper select').prop('disabled', false);
    $('#form_wrapper :submit').prop('disabled', false);
}

//-----------------------------------------------------------
async function loadDataAjax() {
    console.log( "loadDataAjax called." );
    $('#products').DataTable({
        dom: 'Bfrtip',
        buttons: [
            {extend: 'copy'},
            'csv', 'excel', 'pdf', 'print'
        ],
        initComplete: function( settings, json ) {
            enableForm();
        },
        ajax: {
          url: "http://127.0.0.1:5000/data/products_api",
          method: 'GET',
          dataSrc: function (d) {return d}
        },
        destroy: true,
        columns: [
                { 'data': 'id' },
                { 'data': 'title' },
                { 'data': 'description' },
                { 'data': 'price' }
            ]
    });
    $('#products_wrapper').addClass('col-md-12 border border-secondary rounded p-3');
}

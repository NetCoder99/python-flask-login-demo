console.log("Login document is ready");

$("form").submit(function (event) {
    console.log("Form was submitted");
    disableForm();
    var formData = {
      'username': username.value,
      'password': password.value,
    };
    console.log("formData:" + formData);

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/auth/login_api",
        data: JSON.stringify(formData),
        contentType: "application/json",
        encode: true,
    }).done(function (data) {
        enableForm();
        displayResult(data);
        console.log(data);
    });

    event.preventDefault();
});
//-----------------------------------------------------------
function displayResult(data) {
    console.log( "displayResult called." );
    $(".flashes").html(data);
}

//-----------------------------------------------------------
function disableForm() {
    console.log( "disableForm called." );
    $("#btn_login").html("Processing...");
    $('button').prop('disabled', 'disabled');
    $('#form_wrapper :input').prop('disabled', true);
    $('#form_wrapper select').prop('disabled', true);
    $('#form_wrapper :submit').prop('disabled', true);
}

//-----------------------------------------------------------
function enableForm() {
    console.log( "enableForm called." );
    $("#btn_login").html("Sign in");
    $('#form_wrapper :input').prop('disabled', false);
    $('#form_wrapper select').prop('disabled', false);
    $('#form_wrapper :submit').prop('disabled', false);
}

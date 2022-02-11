function validateForm() {
    var email = document.forms["adopter_login_form"]["email"].value;
    if (email == "" || email == null) {
        alert("email must be filled out");
        return false;
    }
    var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if(!(email.match(mailformat))) {
        alert("Please enter a valid email address");
        return false;
    }
    var psw = document.forms["adopter_login_form"]["password"].value;
    if (psw == "" || psw == null) {
        alert("password must be filled out");
        return false;
    }
}
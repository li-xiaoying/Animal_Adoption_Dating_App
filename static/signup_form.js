function validateForm() {
    var email = document.forms["signup_form"]["email"].value;
    if (email == "" || email == null) {
        alert("email must be filled out");
        return false;
    }
    var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if(!(email.match(mailformat))) {
        alert("Please enter a valid email address");
        return false;
    }
    var psw = document.forms["signup_form"]["psw"].value;
    if (psw == "" || psw == null) {
        alert("password must be filled out");
        return false;
    }
    var repsw = document.forms["signup_form"]["repsw"].value;
    if (repsw == "" || repsw == null) {
        alert("repeated password must be filled out");
        return false;
    }
    if (repsw != psw) {
        alert("The password and confirmation password do not match");
        return false;
    }
}

function validateForm() {
    console.log("Validating form");

    var type = document.forms["admin_new_pets_form"]["type"].value;
    if (type == "" || type == null) {
        alert("must choose one type");
        return false;
    }

    var breed = document.forms["admin_new_pets_form"]["breed"].value;
    if (breed == "" || breed == null) {
        alert("breed must be filled out");
        return false;
    }
    var name = document.forms["admin_new_pets_form"]["name"].value;
    if (name == "" || name == null) {
        alert("name must be filled out");
        return false;
    }
    var age = document.forms["admin_new_pets_form"]["age"].value;
    if (age == "" || age == null) {
        alert("age must be filled out");
        return false;
    }
    var img = document.forms["admin_new_pets_form"]["img"].value;
    if (img == "" || img == null) {
        alert("no file selected");
        return false;
    }
}


// $(function() {
//     $('#admin_new_pets_form').submit(function(event) {
//         console.log("Form submitted");
//         // var formData = {};
//         // $.each($(this).serializeArray(), function(i, field) {
//         //     formData[field.name] = field.value;
//         // });
//         // console.log(formData);

//         // $.post('/admin_new_pets', formData);


//         // $.ajax({
//         //     type: "POST",
//         //     url: $(this).attr( 'action' ),
//         //     data: $(this).serialize(),
//         //     success: function( response ) {
//         //       console.log( response );
//         //     }
//         // });

//         event.preventDefault();

//         var formData = new FormData(this);    
//         $.post($(this).attr("action"), formData, function(data) {
//             alert(data);
//         });
//     }); 
// });
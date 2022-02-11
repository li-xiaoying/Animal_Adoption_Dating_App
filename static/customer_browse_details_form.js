$(function() {
  $(".like-button").click(function(event) {
    var petId = event.target.id;
    var isPressed = $(this).hasClass("press");
    var likebutton = $(this);

    if (!isPressed) {
      console.log("Liking pet");
      $.ajax({
        type: "POST",
        url: "/customer_like_pet/" + petId,
        success: function(response) {
          alert("Pet added to favorite list");
          console.log("succeeded:" + response);
          likebutton.toggleClass( "press", 1000 );
        },
        error: function(response) {
          alert("Something unexpected failed. Please try again later.");
        }
      });
    } else {
      console.log("Unliking pet");
      $.ajax({
        type: "DELETE",
        url: "/customer_like_pet/" + petId,
        success: function(response) {
          alert("The pet is removed from your favorite list");

          console.log("succeeded:" + response);
          likebutton.toggleClass( "press", 1000 );
        },
        error: function(response) {
          alert("Something unexpected failed. Please try again later.");
        }
      });
    }

  });
})

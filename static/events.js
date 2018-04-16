$(document).ready(() => {

  $(".event-img").on("click", () => {
    $("#popup").css("display", "block")
  })

// This doesn't work right now, but I'm trying to get the image to grey out and have a "More Details"
// thing come over the greyed out image on mouseover.
  $(".event-img").on("mouseover", "*", function(ev) {
    $(ev.target).addClass("photo-active");
    return false;
  });

  $(".close").on("click", () => {
    $(".modal").css("display", "none")
  })

  $(".submit").on("click", () => {
    $(".modal").css("display", "none")
  })

})

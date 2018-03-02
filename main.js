$(document).ready(() => {
  $('.event-thumbnail').on('click', () => {
    $(".popup-overlay, .popup-content").addClass("active");
  })
  
  $("#submit-button").on("click", () => {
    $(".popup-overlay, .popup-content").removeClass("active");
  })
})

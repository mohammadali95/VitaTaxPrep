$(document).ready(() => {
  $(".details-btn").on("click", () => {
    $("#popup").css("display", "block")
  })

  $(".close").on("click", () => {
    $(".modal").css("display", "none")
  })

  $(".submit").on("click", () => {
    $(".modal").css("display", "none")
  })

})

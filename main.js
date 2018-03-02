$(document).ready(() => {
  $("#myBtn").on("click", () => {
    $("#popup").css("display", "block")
  })
  
  $(".close").on("click", () => {
    $(".modal").css("display", "none")
  })
})

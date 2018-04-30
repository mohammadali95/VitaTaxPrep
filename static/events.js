$(document).ready(() => {
  $(".close").on("click", () => {
    $(".modal").css("display", "none")
  })

  $(".submit").on("click", () => {
    $(".modal").css("display", "none")

  })
  console.log("Logged");
})

function popup(name, description) {
  console.log("You called the popup function!")
    $("#eventName").html(name)
    $("#description").html(description)
    $("#popup").css("display", "block")
  }

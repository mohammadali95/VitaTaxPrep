$(document).ready(() => {

  $(".event-img").on("click", () => {
    $("#popup").css("display", "block")
  })
  
  function popup(name, description) {
	  $("#eventName").textContent = name
	  $("#description").textContent = description
	  $("#popup").css("display", "block")
  }

  $(".close").on("click", () => {
    $(".modal").css("display", "none")
  })

  $(".submit").on("click", () => {
    $(".modal").css("display", "none")
  })

})

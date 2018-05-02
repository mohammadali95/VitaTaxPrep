$(document).ready(() => {  

  $(".close").on("click", () => {
    $(".modal").css("display", "none")
  })

  $(".submit").on("click", () => {
    $(".modal").css("display", "none")
  })

})

function popup(name, description) {
	$("#eventName").html(name)
	$("#description").html(description)
	$("#popup").css("display", "block")
}

$(document).ready(function(){
    /*$("#Info").mouseenter(function(){
        $(".con").show();
        $("#Info").addClass('button-active');
    });

  $(".con").mouseleave(function(){
        $(".con").hide();
     $("#Info").removeClass('button-active')
    });

  $("#Info2").mouseenter(function(){
        $(".con").show();
        $("#Info2").addClass('button-active');
    });

  $(".con").mouseleave(function(){
        $(".con").hide();
     $("#Info2").removeClass('button-active')
    });*/
	 $('#info').hide();
  
 /*$('.hide-button').on('click', () => {
    $('#info').show();
 })*/
   $('#delete-box').hide();
 $('#delete').on('click', () => {
    $('#delete-box').show();
 })
  $('#delete-no').on('click', () => {
     $('#delete-box').hide();
  })
});

function displayInfo(name, address, city, state, zip, email, phone, dob, volFor, languages) {
	$('#infoName').html("Name: " + name)
	console.log(name + city, state + zip + email + phone + dob + volFor + languages)
	$('#infoAddress').html("Address: " + address)
	$('#infoCity').html("City: " + city)
	$('#infoState').html("State: " + state)
	$('#infoZIP').html("ZIP Code: " + zip)
	$('#infoEmail').html("Email: " + email)
	$('#infoPhone').html("Phone Number: " + phone)
	$('#infoDOB').html("Date of Birth: " + dob)
	$('#infoVolFor').html("Volunteering For: " + volFor)
	$('#infoLanguages').html("Languages Spoken: " + languages)
	$('#info').show()
}

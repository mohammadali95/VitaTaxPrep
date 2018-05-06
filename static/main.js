$(document).ready(function(){
  $('#info').hide();
  $('#delete-box').hide();
  //load all volunteers into table
   $('.hide-button').on('click', () => {
    $('#info').show();
 })
  $('#delete').on('click', () => {
    $('#delete-box').show();
 })
  $('#delete-no').on('click', () => {
     $('#delete-box').hide();
  })
  
  //adapted from https://jsfiddle.net/gengns/j1jm2tjx/
  function download_csv(csv, filename) {
    var csvFile;
    var downloadLink;

    // CSV FILE
    csvFile = new Blob([csv], {type: "text/csv"});

    // Download link
    downloadLink = document.createElement("a");

    // File name
    downloadLink.download = filename;

    // We have to create a link to the file
    downloadLink.href = window.URL.createObjectURL(csvFile);

    // Make sure that the link is not displayed
    downloadLink.style.display = "none";

    // Add the link to your DOM
    document.body.appendChild(downloadLink);

    // Lanzamos
    downloadLink.click();
}

function export_table_to_csv(html, filename) {
	var csv = [];
	var rows = document.querySelectorAll("table tr");
	
    for (var i = 0; i < rows.length; i++) {
		var row = [], cols = rows[i].querySelectorAll("td, th");
		
        for (var j = 0; j < cols.length; j++) 
            row.push(cols[j].innerText);
        
		csv.push(row.join(","));		
	}

    // Download CSV
    download_csv(csv.join("\n"), filename);
}

document.querySelector("#export").addEventListener("click", function () {
    var html = document.querySelector("table").outerHTML;
	export_table_to_csv(html, "Volunteers.csv");
})
});

function displayInfo(name, address, city, state, zip, email, phone, dob, volFor, hours, languages) {
	$('#infoName').html(name)
	$('#infoAddress').html(address)
	$('#infoCity').html(city)
	$('#infoState').html(state)
	$('#infoZIP').html(zip)
	$('#infoEmail').html(email)
	$('#infoPhone').html(phone)
	$('#infoDOB').html(dob)
	$('#infoVolFor').html(volFor)
	$('#infoHoursFor').html(hours)
	$('#infoLanguages').html(languages)
	$('#info').show()
}

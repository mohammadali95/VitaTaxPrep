$(document).ready(function(){
    $("#Info").mouseenter(function(){
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
    });
});

$(document).ready(function(){
  $('#Find').click(function(){
    var city=$("#city").val();
    if(city!=" ")
    {
      $.getJSON("http://api.openweathermap.org/data/2.5/weather?q="+city+"&units=metric&APPID=92871e8d584e912d60630bac72c7995b",function(data){
      console.log(data);
      var icon="https://openweathermap.org/img/w/" + data.weather[0].icon + ".png";
      console.log(icon);
      var temp=data.main.temp;
      var weather=data.weather[0].main;
      $('.icon').attr('src',icon);
      $('.weather').append(weather);
      $('.temp').append(temp);

    });


    }


  });

});

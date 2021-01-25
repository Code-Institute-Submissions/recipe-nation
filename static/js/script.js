$(document).ready(function(){
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown({ 
        hover: true,
        coverTrigger: false
     });
    $('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true,
  });
  
  });



// http://www.randomsnippets.com/2008/02/21/how-to-dynamically-add-form-elements-via-javascript/
// https://jsfiddle.net/y0urcaem/1/


// <script src="/Cookout/addInput.js" language="Javascript" type="text/javascript"></script>
// <form method="POST">
//      <div id="dynamicInput">
//           Ingredient 1<br><br><input type="text" name="myIngredients[]">
//      </div>
//      <input type="button" value="Add Another Ingredient" onClick="addInput('dynamicInput');">
// </form>

// let counter = 1;
// let limit = 30;
// function addInput(divName){
//      if (counter == limit)  {
//           alert("You have reached the limit of adding " + counter + " ingredients");
//      }
//      else {
//           let newdiv = document.createElement('div');
//           newdiv.innerHTML = "Ingredient " + (counter + 1) + ' <br><input type="text"  placeholder="Ingredient" name="myIngredients[]">';
//           document.getElementById(divName).appendChild(newdiv);
//           counter++;
//      }
// }
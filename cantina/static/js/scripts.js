function myFunction() {
  let x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

// Message Display
setTimeout(function() {
  document.getElementById("message").style.display = 'none';
}, 2500);

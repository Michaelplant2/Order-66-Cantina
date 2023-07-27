function myFunction() {
  let x = document.getElementById("myTopnav");
  let y = document.getElementById("navBar");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  };
  if (y.className === "navbar") {
    y.className += " center";
  } else {
    y.className = "navbar";
  };
}

// Message Display
setTimeout(function() {
  document.getElementById("message").style.display = 'none';
}, 2500);

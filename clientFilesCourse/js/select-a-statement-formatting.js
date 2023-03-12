// this script finds the red boxes that denote syntax errors and changes them to be transparent

let spans =
  document.getElementsByTagName("span");

// Iterate over spans
for (let span of spans) {
  if (span.style.borderColor == "rgb(255, 0, 0)") {
    span.style.borderColor = "rgb(0, 255, 255)";
  }

}

var x = document.getElementById("TEST");
x.textContent = "HI THERE";

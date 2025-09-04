var list = new Array();
list[0] = static_url + "img/R1.jpg";
list[1] = static_url + "img/R2.jpg";
list[2] = static_url + "img/R3.jpg";
list[3] = static_url + "img/R4.jpg";
list[4] = static_url + "img/R5.jpg";
list[5] = static_url + "img/R6.jpg";
var count = 0;

setInterval(right, 3000);

function right() {
  count++;
  if (count > 5) {
    count = 0;
  }
  img = "url(" + list[count] + ")";
  document.getElementById("count").style.backgroundImage = img;
}
function left() {
  count--;
  if (count < 0) {
    count = 5;
  }
  img = "url(" + list[count] + ")";
  document.getElementById("count").style.backgroundImage = img;
}

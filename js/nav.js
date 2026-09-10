document.addEventListener("click", function (e) {
  var m = document.getElementById("mnav");
  if (e.target.closest("#burger")) { e.preventDefault(); m && m.classList.add("is-open"); document.body.classList.add("no-scroll"); }
  if (e.target.closest("#mnavClose") || e.target.closest("#mnav a")) { m && m.classList.remove("is-open"); document.body.classList.remove("no-scroll"); }
});

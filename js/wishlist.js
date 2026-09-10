document.addEventListener("DOMContentLoaded",()=>{
  const ids=JSON.parse(localStorage.getItem("terra_wish_v1")||"[]");
  const g=document.getElementById("wishGrid");
  const list=ids.map(id=>TERRA_CATALOG[id]).filter(Boolean);
  g.innerHTML=list.length?list.map(terraCard).join(''):'<p class="lede">Nothing saved yet. Tap the heart on any product.</p>';
});

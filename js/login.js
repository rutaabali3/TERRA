document.addEventListener("DOMContentLoaded",()=>{
  document.querySelectorAll("[data-tab]").forEach(b=>b.onclick=()=>{
    document.querySelectorAll("[data-tab]").forEach(x=>x.classList.remove("is-on"));
    b.classList.add("is-on");
    formIn.hidden=b.dataset.tab!=="in";
    formUp.hidden=b.dataset.tab!=="up";
  });
});

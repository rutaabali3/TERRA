document.addEventListener("DOMContentLoaded",()=>{
  const id=new URLSearchParams(location.search).get("id")||"dress";
  const p=TERRA_CATALOG[id]; if(!p) return;
  document.title=p.name+" — TERRA";
  document.getElementById("pName").textContent=p.name;
  document.getElementById("pCat").textContent=p.cat;
  document.getElementById("pPrice").innerHTML=(p.was?"<s>$"+p.was.toFixed(2)+"</s> ":"")+"$"+p.price.toFixed(2);
  document.getElementById("mainImg").src=p.img;
  document.getElementById("thumbs").innerHTML=[p.img,p.img,p.img,p.img].map((src,i)=>`<button class="${i===0?"is-on":""}"><img src="${src}" alt=""></button>`).join("");
  document.getElementById("colors").innerHTML=p.colors.map((c,i)=>`<button class="swatch ${i===0?"is-on":""}" style="background:${c}"></button>`).join("");
  document.getElementById("sizes").innerHTML=p.sizes.map((s,i)=>`<button class="sizebtn ${i===0?"is-on":""}" data-size="${s}">${s}</button>`).join("");
  document.querySelectorAll(".swatch").forEach(b=>b.onclick=()=>{document.querySelectorAll(".swatch").forEach(x=>x.classList.remove("is-on"));b.classList.add("is-on")});
  document.querySelectorAll(".sizebtn").forEach(b=>b.onclick=()=>{document.querySelectorAll(".sizebtn").forEach(x=>x.classList.remove("is-on"));b.classList.add("is-on")});
  let q=1; const qs=document.getElementById("pqty");
  document.getElementById("qinc").onclick=()=>{q++;qs.textContent=q};
  document.getElementById("qdec").onclick=()=>{q=Math.max(1,q-1);qs.textContent=q};
  document.getElementById("addPdp").onclick=()=>{
    const size=document.querySelector(".sizebtn.is-on").dataset.size;
    for(let i=0;i<q;i++) terraAdd(id,size);
  };
});

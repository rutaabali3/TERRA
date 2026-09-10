document.addEventListener("DOMContentLoaded",()=>{
  const t=terraCart().reduce((n,i)=>n+i.qty*i.price,0);
  const el=document.getElementById("chkTotal"); if(el) el.textContent="$"+t.toFixed(2);
});

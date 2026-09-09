(function(){
  const BASE = document.body.dataset.base || '';
  const P = (p) => BASE + p;

  const CATALOG = {
    dress:{id:'dress',name:'Bias-Cut Linen Dress',cat:'Clothing',price:168,was:210,img:'https://images.unsplash.com/photo-1496747611176-843222e1e57c?auto=format&fit=crop&w=800&q=80',flag:'Bestseller',rating:4.9,reviews:412,colors:['#c9b59a','#5e6b45','#2f2a23'],sizes:['XS','S','M','L','XL']},
    shirt:{id:'shirt',name:'Oversized Poplin Shirt',cat:'Clothing',price:108,was:null,img:'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80',flag:'Organic',rating:4.8,reviews:286,colors:['#fffdf8','#e6dcc9','#5e6b45'],sizes:['XS','S','M','L','XL']},
    coat:{id:'coat',name:'Wool Wrap Coat',cat:'Clothing',price:340,was:null,img:'https://images.unsplash.com/photo-1539533018447-63fcce2678e3?auto=format&fit=crop&w=800&q=80',flag:'Low stock',flagCls:'--clay',rating:5,reviews:131,colors:['#2f2a23','#6f6659'],sizes:['S','M','L']},
    sneaker:{id:'sneaker',name:'Everyday Low Sneaker',cat:'Shoes',price:132,was:158,img:'https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=800&q=80',flag:'Recycled',rating:4.7,reviews:198,colors:['#e6dcc9','#2f2a23'],sizes:['36','37','38','39','40','41']},
    bag:{id:'bag',name:'Vegetable-Tanned Tote',cat:'Accessories',price:225,was:null,img:'https://images.unsplash.com/photo-1590874103328-eac38a94180d?auto=format&fit=crop&w=800&q=80',flag:'New',flagCls:'--clay',rating:4.9,reviews:97,colors:['#c9a57a','#2f2a23'],sizes:['One size']},
    sandal:{id:'sandal',name:'Woven Leather Sandal',cat:'Shoes',price:98,was:null,img:'https://images.unsplash.com/photo-1603808033192-082d6919d3e1?auto=format&fit=crop&w=800&q=80',flag:'New',rating:4.6,reviews:64,colors:['#c9a57a'],sizes:['36','37','38','39','40']},
    scarf:{id:'scarf',name:'Plant-Dyed Wool Scarf',cat:'Accessories',price:64,was:null,img:'https://images.unsplash.com/photo-1520903920243-00d482d9f5c0?auto=format&fit=crop&w=800&q=80',flag:'Organic',rating:4.8,reviews:88,colors:['#b5573a','#5e6b45'],sizes:['One size']},
    trouser:{id:'trouser',name:'Wide-Leg Linen Trouser',cat:'Clothing',price:128,was:148,img:'https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?auto=format&fit=crop&w=800&q=80',flag:'Bestseller',rating:4.8,reviews:210,colors:['#e6dcc9','#2f2a23'],sizes:['XS','S','M','L','XL']}
  };
  window.TERRA_CATALOG = CATALOG;
  const ORDER = Object.keys(CATALOG);
  const money = n => '$' + Number(n).toFixed(2);
  const STAR = '<svg viewBox="0 0 24 24"><path d="m12 2.6 2.9 6 6.6.9-4.8 4.6 1.2 6.5L12 17.5 6.1 20.6l1.2-6.5L2.5 9.5l6.6-.9z"/></svg>';
  window.terraMoney = money;

  const KEY='terra_cart_v1', WKEY='terra_wish_v1';
  let cart=[], wish=[];
  try{cart=JSON.parse(localStorage.getItem(KEY))||[]}catch(e){cart=[]}
  try{wish=JSON.parse(localStorage.getItem(WKEY))||[]}catch(e){wish=[]}

  const $ = s => document.querySelector(s);
  const persist=()=>{try{localStorage.setItem(KEY,JSON.stringify(cart));localStorage.setItem(WKEY,JSON.stringify(wish))}catch(e){}}
  const count=()=>cart.reduce((n,i)=>n+i.qty,0);
  const total=()=>cart.reduce((n,i)=>n+i.qty*i.price,0);

  const ICONS = {
    search:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>',
    user:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="8.5" r="3.6"/><path d="M4.5 20c1.2-3.7 4-5.6 7.5-5.6s6.3 1.9 7.5 5.6"/></svg>',
    bag:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M5.5 8h13l-1 12.2H6.5L5.5 8Z"/><path d="M9 8V6.6a3 3 0 0 1 6 0V8"/></svg>',
    menu:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M3 7h18M3 12h18M3 17h18"/></svg>',
    x:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="m6 6 12 12M18 6 6 18"/></svg>',
    heart:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M12 20s-7-4.4-7-9.4A4.1 4.1 0 0 1 12 8a4.1 4.1 0 0 1 7 2.6c0 5-7 9.4-7 9.4Z"/></svg>'
  };

  function injectChrome(){ /* header/footer are real HTML on each page */ }

  function productCard(p){
    return `<article class="pcard">
      <div class="pcard__media">
        <span class="pcard__flag ${p.flagCls?'pcard__flag'+p.flagCls:''}">${p.flag||''}</span>
        <button class="pcard__fav ${wish.includes(p.id)?'is-on':''}" data-fav="${p.id}" aria-label="Save">${ICONS.heart}</button>
        <img src="${p.img}" alt="${p.name}" loading="lazy">
        <button class="btn btn--soft pcard__qv" data-qv="${p.id}">Quick view</button>
      </div>
      <div class="pcard__body">
        <p class="pcard__cat">${p.cat}</p>
        <h3><a href="${P('product.html')}?id=${p.id}">${p.name}</a></h3>
        <div class="pcard__stars">${STAR.repeat(5)}<small>${p.rating} (${p.reviews})</small></div>
        <div class="pcard__foot">
          <span class="price">${p.was?`<s>${money(p.was)}</s>`:''}${money(p.price)}</span>
          <button class="addbtn" data-add="${p.id}">Add +</button>
        </div>
      </div>
    </article>`;
  }
  window.terraCard = productCard;
  window.terraProducts = (cat) => ORDER.map(id=>CATALOG[id]).filter(p=>!cat||p.cat===cat);

  function renderCart(){
    const body = $('#cartBody'); if(!body) return;
    if(!cart.length){
      body.innerHTML = `<div class="drawer__empty"><h4>Your basket is empty</h4><p>Start with the linen dress or poplin shirt.</p>
        <a class="btn btn--soft" href="${P('shop.html')}">Browse the shop</a></div>`;
      if($('#cartFoot')) $('#cartFoot').hidden = true;
    } else {
      body.innerHTML = cart.map(i=>`<div class="citem">
        <img src="${i.img}" alt="">
        <div style="flex:1">
          <h5 style="font-size:15px;font-weight:500">${i.name}</h5>
          <small style="color:var(--faint)">${i.cat} · ${i.size||''}</small>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-top:10px">
            <div class="qty">
              <button data-dec="${i.key}">−</button><span>${i.qty}</span><button data-inc="${i.key}">+</button>
            </div>
            <span class="price">${money(i.price*i.qty)}</span>
          </div>
          <button class="citem__rm" data-rm="${i.key}" style="margin-top:8px;font-size:12px;text-decoration:underline;color:var(--faint)">Remove</button>
        </div></div>`).join('');
      if($('#cartFoot')){ $('#cartFoot').hidden=false; $('#cartTotal').textContent=money(total()); }
    }
    if($('#drawerQty')) $('#drawerQty').textContent=count();
    const badge=$('#cartCount');
    if(badge){ badge.textContent=count(); badge.classList.toggle('is-on',count()>0); }
    const wb=$('#wishCount');
    if(wb){ wb.textContent=wish.length; wb.classList.toggle('is-on',wish.length>0); }
    document.querySelectorAll('[data-cart-page]').forEach(()=>renderCartPage());
  }

  function renderCartPage(){
    const el = document.getElementById('cartPage');
    if(!el) return;
    if(!cart.length){ el.innerHTML='<p class="lede">Your cart is empty. <a href="shop.html" style="color:var(--clay)">Shop the collection</a>.</p>'; return; }
    el.innerHTML = cart.map(i=>`<div class="citem">
      <img src="${i.img}" alt="">
      <div style="flex:1"><h3 style="font-size:17px">${i.name}</h3>
      <small style="color:var(--faint)">${i.size||''}</small>
      <div style="display:flex;gap:16px;align-items:center;margin-top:10px" class="qty">
        <button data-dec="${i.key}">−</button><span>${i.qty}</span><button data-inc="${i.key}">+</button>
      </div></div>
      <div><b>${money(i.price*i.qty)}</b><br><button data-rm="${i.key}" style="text-decoration:underline;font-size:12px;color:var(--faint)">Remove</button></div>
    </div>`).join('');
    const sub=$('#subtotalVal'); if(sub) sub.textContent=money(total());
    const ship=$('#shipVal'); if(ship) ship.textContent = total()>=90?'Free':'$8.00';
    const tot=$('#grandVal'); if(tot) tot.textContent=money(total()+(total()>=90?0:8));
  }

  function add(id,size){
    const p=CATALOG[id]; if(!p) return;
    size = size || p.sizes[0];
    const key=id+':'+size;
    const found=cart.find(i=>i.key===key);
    if(found) found.qty++;
    else cart.push({key,id,name:p.name,cat:p.cat,size,price:p.price,img:p.img,qty:1});
    persist(); renderCart(); toast(p.name+' added'); openCart();
  }

  function toast(msg){
    const t=$('#toast'); if(!t) return;
    $('#toastMsg').textContent=msg;
    t.classList.add('is-on');
    clearTimeout(toast._t); toast._t=setTimeout(()=>t.classList.remove('is-on'),2200);
  }
  window.terraToast=toast;
  window.terraAdd=add;
  window.terraCart=()=>cart;
  window.terraWish=()=>wish;

  const openCart=()=>{ $('#drawer')?.classList.add('is-open'); $('#scrim')?.classList.add('is-open'); document.body.classList.add('no-scroll'); };
  const closeCart=()=>{ $('#drawer')?.classList.remove('is-open'); $('#scrim')?.classList.remove('is-open'); document.body.classList.remove('no-scroll'); };

  function openQV(id){
    const p=CATALOG[id]; if(!p) return;
    $('#qvBox').innerHTML=`<img src="${p.img}" alt="${p.name}">
      <div style="padding:24px">
        <p class="pcard__cat">${p.cat}</p>
        <h3 class="h-sec" style="font-size:1.7rem;margin:8px 0">${p.name}</h3>
        <p class="price" style="margin:8px 0 16px">${money(p.price)}</p>
        <p class="lede" style="margin-bottom:18px">Natural fibres, small-batch sewing. Choose a size and add to basket.</p>
        <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px">${p.sizes.map((s,i)=>`<button class="sizebtn ${i===0?'is-on':''}" data-size="${s}">${s}</button>`).join('')}</div>
        <button class="btn btn--block" data-add="${p.id}" id="qvAdd">Add to basket</button>
        <p style="margin-top:14px"><a href="${P('product.html')}?id=${p.id}" style="color:var(--clay)">View full details →</a></p>
      </div>`;
    $('#qv').classList.add('is-open');
    document.body.classList.add('no-scroll');
    $('#qvBox').querySelectorAll('.sizebtn').forEach(b=>b.addEventListener('click',()=>{
      $('#qvBox').querySelectorAll('.sizebtn').forEach(x=>x.classList.remove('is-on')); b.classList.add('is-on');
    }));
  }

  function bind(){
    $('#cartOpen')?.addEventListener('click',openCart);
    $('#cartClose')?.addEventListener('click',closeCart);
    $('#scrim')?.addEventListener('click',closeCart);
    $('#burger')?.addEventListener('click',()=>{$('#mnav').classList.add('is-open');document.body.classList.add('no-scroll')});
    $('#mnavClose')?.addEventListener('click',()=>{$('#mnav').classList.remove('is-open');document.body.classList.remove('no-scroll')});
    $('#searchOpen')?.addEventListener('click',()=>{$('#searchov').classList.add('is-open'); setTimeout(()=>$('#searchInput')?.focus(),50)});
    $('#searchClose')?.addEventListener('click',()=>$('#searchov').classList.remove('is-open'));
    $('#qvScrim')?.addEventListener('click',()=>{$('#qv').classList.remove('is-open');document.body.classList.remove('no-scroll')});
    const header=$('#header');
    const onScroll=()=>header?.classList.toggle('is-stuck',window.scrollY>8);
    onScroll(); window.addEventListener('scroll',onScroll,{passive:true});

    $('#searchInput')?.addEventListener('input',e=>{
      const q=e.target.value.toLowerCase().trim();
      const box=$('#searchResults');
      if(!q){box.innerHTML='';return}
      const hits=ORDER.map(id=>CATALOG[id]).filter(p=>p.name.toLowerCase().includes(q)||p.cat.toLowerCase().includes(q));
      box.innerHTML = hits.length? `<div class="pg" style="grid-template-columns:1fr">${hits.map(p=>`<a href="${P('product.html')}?id=${p.id}" class="citem"><img src="${p.img}" alt=""><div><b>${p.name}</b><br><small>${p.cat} · ${money(p.price)}</small></div></a>`).join('')}</div>` : '<p class="lede">No matches. Try linen, tote, sneaker.</p>';
    });

    document.addEventListener('click',e=>{
      const addEl=e.target.closest('[data-add]');
      const inc=e.target.closest('[data-inc]');
      const dec=e.target.closest('[data-dec]');
      const rm=e.target.closest('[data-rm]');
      const fav=e.target.closest('[data-fav]');
      const qv=e.target.closest('[data-qv]');
      if(addEl){
        const size=$('#qvBox .sizebtn.is-on')?.dataset.size || document.querySelector('.sizebtn.is-on')?.dataset.size;
        add(addEl.dataset.add,size);
      }
      if(inc){const i=cart.find(x=>x.key===inc.dataset.inc);if(i){i.qty++;persist();renderCart();}}
      if(dec){const i=cart.find(x=>x.key===dec.dataset.dec);if(i){i.qty--;if(i.qty<1)cart=cart.filter(x=>x.key!==i.key);persist();renderCart();}}
      if(rm){cart=cart.filter(x=>x.key!==rm.dataset.rm);persist();renderCart();toast('Removed');}
      if(fav){
        const id=fav.dataset.fav;
        if(wish.includes(id)) wish=wish.filter(x=>x!==id); else wish.push(id);
        persist(); fav.classList.toggle('is-on'); renderCart(); toast(wish.includes(id)?'Saved to wishlist':'Removed from wishlist');
      }
      if(qv) openQV(qv.dataset.qv);
    });
    document.addEventListener('keydown',e=>{ if(e.key==='Escape'){closeCart();$('#searchov')?.classList.remove('is-open');$('#qv')?.classList.remove('is-open');document.body.classList.remove('no-scroll');}});
  }

  document.addEventListener('DOMContentLoaded',()=>{
    injectChrome(); bind(); renderCart();
    document.querySelectorAll('[data-grid]').forEach(el=>{
      const cat=el.dataset.grid;
      const list=window.terraProducts(cat||undefined);
      el.innerHTML=list.map(productCard).join('');
    });
    const news=document.getElementById('newsForm');
    news?.addEventListener('submit',e=>{e.preventDefault();e.target.reset();toast('Welcome — 10% off is in your inbox');});
  });
})();

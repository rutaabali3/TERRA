from pathlib import Path
ROOT = Path("/home/user")

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — TERRA</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/terra.css">
</head>
<body data-page="{page}" data-base="">
<div class="topbar"><div class="wrap">
  <span>Plant a tree with every order</span>
  <span>Free plastic-free delivery over <b>$90</b></span>
  <span>30-day easy returns</span>
</div></div>
<header class="header" id="header"><div class="wrap header__in">
  <a href="index.html" class="brand"><i></i>TERRA</a>
  <nav class="tnav">
    <a href="index.html">Home</a>
    <a href="shop.html">Shop</a>
    <a href="category-clothing.html">Clothing</a>
    <a href="category-shoes.html">Shoes</a>
    <a href="category-accessories.html">Accessories</a>
    <a href="about.html">About</a>
  </nav>
  <div class="header__act">
    <button class="ibtn" id="searchOpen" type="button" aria-label="Search"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg></button>
    <a class="ibtn" href="wishlist.html" aria-label="Wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M12 20s-7-4.4-7-9.4A4.1 4.1 0 0 1 12 8a4.1 4.1 0 0 1 7 2.6c0 5-7 9.4-7 9.4Z"/></svg><i class="badge" id="wishCount">0</i></a>
    <a class="ibtn" href="login.html" aria-label="Account"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="8.5" r="3.6"/><path d="M4.5 20c1.2-3.7 4-5.6 7.5-5.6s6.3 1.9 7.5 5.6"/></svg></a>
    <button class="ibtn" id="cartOpen" type="button" aria-label="Open basket"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M5.5 8h13l-1 12.2H6.5L5.5 8Z"/><path d="M9 8V6.6a3 3 0 0 1 6 0V8"/></svg><i class="badge" id="cartCount">0</i></button>
    <button class="ibtn burger" id="burger" type="button" aria-label="Menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M3 7h18M3 12h18M3 17h18"/></svg></button>
  </div>
</div></header>
<div class="mnav" id="mnav">
  <button class="ibtn mnav__close" id="mnavClose" type="button" aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="m6 6 12 12M18 6 6 18"/></svg></button>
  <a href="index.html">Home <span>→</span></a>
  <a href="shop.html">Shop <span>→</span></a>
  <a href="category-clothing.html">Clothing <span>→</span></a>
  <a href="category-shoes.html">Shoes <span>→</span></a>
  <a href="category-accessories.html">Accessories <span>→</span></a>
  <a href="about.html">About <span>→</span></a>
  <a href="contact.html">Contact <span>→</span></a>
  <a href="faq.html">FAQ <span>→</span></a>
  <a href="login.html">Account <span>→</span></a>
</div>
<main>
'''

FOOT = '''
</main>
<div id="site-footer"></div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script>
document.addEventListener("click", function (e) {
  var m = document.getElementById("mnav");
  if (e.target.closest("#burger")) { e.preventDefault(); m && m.classList.add("is-open"); document.body.classList.add("no-scroll"); }
  if (e.target.closest("#mnavClose") || e.target.closest("#mnav a")) { m && m.classList.remove("is-open"); document.body.classList.remove("no-scroll"); }
});
</script>
<script src="js/terra.js"></script>
{extra}
</body>
</html>
'''

def write(fname, title, pagename, body, extra=""):
    html = HEAD.format(title=title, page=pagename) + body + FOOT.format(extra=extra)
    (ROOT/fname).write_text(html)
    print("wrote", fname)

write("index.html","Home","home",'''
<section class="hero"><div class="wrap hero__in">
  <div>
    <span class="pill">New season · Raw linen</span>
    <h1 class="h-xl"><span>Dress simply.</span><span>Live <em>gently.</em></span></h1>
    <p class="lede">Everyday pieces in organic cotton, raw linen and wool — dyed with plants, sewn in small batches.</p>
    <div class="hero__cta">
      <a href="shop.html" class="btn btn--lg">Shop the collection</a>
      <a href="about.html" class="btn btn--outline btn--lg">How we make it</a>
    </div>
    <div class="hero__note"><span class="avs"><i>A</i><i>M</i><i>J</i></span><span><b>4,200+</b> people wear TERRA every week</span></div>
  </div>
  <div class="hero__media">
    <div class="hero__arch"><img src="https://images.unsplash.com/photo-1469334031218-e382a71b716b?auto=format&fit=crop&w=1200&q=80" alt="Linen look"></div>
    <span class="hero__badge">Carbon neutral</span>
    <div class="hero__card">
      <img src="https://images.unsplash.com/photo-1496747611176-843222e1e57c?auto=format&fit=crop&w=200&q=80" alt="">
      <div><b>Bias Linen Dress</b><small>$168 · 12 left in Sand</small></div>
    </div>
  </div>
</div></section>
<section class="wrap"><div class="promise">
  <div class="pitem"><span></span><div><h4>Natural fibres only</h4><p>GOTS cotton, European flax and mulesing-free wool.</p></div></div>
  <div class="pitem"><span></span><div><h4>Plastic-free packing</h4><p>Recycled paper mailers and soy inks since day one.</p></div></div>
  <div class="pitem"><span></span><div><h4>Repairs, always free</h4><p>Send anything back for mending — worn hems included.</p></div></div>
</div></section>
<section class="section"><div class="wrap">
  <div class="sec-head"><span class="pill pill--sand">Shop by category</span>
    <h2 class="h-sec">Fewer things, <em>better made</em></h2></div>
  <div class="cats">
    <a class="cat" href="category-clothing.html"><div class="cat__img"><img src="https://images.unsplash.com/photo-1496747611176-843222e1e57c?auto=format&fit=crop&w=600&q=80" alt=""></div><div class="cat__row"><div><h3>Clothing</h3><small>28 pieces</small></div></div></a>
    <a class="cat" href="category-shoes.html"><div class="cat__img"><img src="https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=600&q=80" alt=""></div><div class="cat__row"><div><h3>Shoes</h3><small>9 pieces</small></div></div></a>
    <a class="cat" href="category-accessories.html"><div class="cat__img"><img src="https://images.unsplash.com/photo-1590874103328-eac38a94180d?auto=format&fit=crop&w=600&q=80" alt=""></div><div class="cat__row"><div><h3>Accessories</h3><small>12 pieces</small></div></div></a>
    <a class="cat" href="shop.html"><div class="cat__img"><img src="https://images.unsplash.com/photo-1539533018447-63fcce2678e3?auto=format&fit=crop&w=600&q=80" alt=""></div><div class="cat__row"><div><h3>New arrivals</h3><small>This week</small></div></div></a>
  </div>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
  <div class="sec-head"><span class="pill">Loved most</span><h2 class="h-sec">Bestsellers</h2></div>
  <div class="pg" data-grid></div>
  <p class="text-center mt-4"><a class="btn btn--soft" href="shop.html">Browse all pieces</a></p>
</div></section>
<section class="wrap" style="padding-bottom:var(--sec)">
  <div class="news">
    <div><span class="pill">Letters from the studio</span><h2 class="h-sec" style="margin-top:14px">A slower inbox</h2>
      <p>Two letters a month and 10% off your first order.</p></div>
    <form class="form" id="newsForm"><input type="email" required placeholder="Your email"><button type="submit">Join us</button></form>
  </div>
</section>
''')

def listing(fname, title, pagename, cat, crumb, h, lede):
    write(fname, title, pagename, f'''
<div class="wrap page-hero">
  <div class="crumb"><a href="index.html">Home</a> / {crumb}</div>
  <span class="pill pill--sand">{title}</span>
  <h1 class="h-sec" style="margin:14px 0">{h}</h1>
  <p class="lede">{lede}</p>
</div>
<div class="wrap" style="padding-bottom:var(--sec)">
  <div class="toolbar">
    <div style="display:flex;gap:8px;flex-wrap:wrap">
      <button class="filter-chip is-on">All</button>
      <button class="filter-chip">New</button>
      <button class="filter-chip">Under $150</button>
    </div>
    <select class="selectish"><option>Sort: Featured</option><option>Price low–high</option><option>Price high–low</option></select>
  </div>
  <div class="pg" data-grid="{cat}"></div>
</div>''')

listing("shop.html","Shop","shop","","All products","The full collection","Forty-one pieces. No more, on purpose.")
listing("category-clothing.html","Clothing","shop","Clothing","<a href='shop.html'>Shop</a> / Clothing","Clothing","Linen, poplin and wool for every day of the week.")
listing("category-shoes.html","Shoes","shop","Shoes","<a href='shop.html'>Shop</a> / Shoes","Shoes","Vegetable-tanned leather and recycled soles.")
listing("category-accessories.html","Accessories","shop","Accessories","<a href='shop.html'>Shop</a> / Accessories","Accessories","Totes, scarves and the small things that last.")

write("product.html","Product","pdp",'''
<div class="wrap page-hero pdp" id="pdp">
  <div class="gallery">
    <div class="gallery__main"><img id="mainImg" alt=""></div>
    <div class="gallery__thumbs" id="thumbs"></div>
  </div>
  <div>
    <div class="crumb"><a href="index.html">Home</a> / <a href="shop.html">Shop</a> / <span id="pCat"></span></div>
    <h1 class="h-sec" id="pName"></h1>
    <p class="price" id="pPrice" style="margin:12px 0"></p>
    <p class="lede" id="pLede">Grown, spun and sewn in small batches. Plant-dyed where colour is used.</p>
    <p style="font-size:13px;margin:16px 0 8px;letter-spacing:.08em;text-transform:uppercase;color:var(--faint)">Colour</p>
    <div id="colors" style="display:flex;gap:8px;margin-bottom:16px"></div>
    <p style="font-size:13px;margin:0 0 8px;letter-spacing:.08em;text-transform:uppercase;color:var(--faint)">Size · <a href="size-guide.html" style="color:var(--clay);text-transform:none;letter-spacing:0">Size guide</a></p>
    <div id="sizes" style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px"></div>
    <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center">
      <div class="qty"><button type="button" id="qdec">−</button><span id="pqty">1</span><button type="button" id="qinc">+</button></div>
      <button class="btn" id="addPdp">Add to basket</button>
      <button class="btn btn--outline" data-fav-p>Wishlist</button>
    </div>
    <div class="acc" style="margin-top:28px">
      <details open><summary>Details</summary><p>100% natural fibres. Made in Porto. Machine wash cold, hang dry.</p></details>
      <details><summary>Shipping</summary><p>Plastic-free packing. Free over $90. 3–6 working days.</p></details>
      <details><summary>Returns</summary><p>30 days, unworn with tags. Free exchanges on size.</p></details>
    </div>
  </div>
</div>
<section class="section" style="padding-top:0"><div class="wrap">
  <h2 class="h-sec" style="margin-bottom:24px">You may also like</h2>
  <div class="pg" data-grid></div>
</div></section>
''', extra='''<script>
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
</script>''')

write("cart.html","Cart","cart",'''
<div class="wrap page-hero">
  <div class="crumb"><a href="index.html">Home</a> / Cart</div>
  <h1 class="h-sec">Your basket</h1>
</div>
<div class="wrap cart-layout" style="padding-bottom:var(--sec)" data-cart-page>
  <div id="cartPage" class="cart-table"></div>
  <aside class="summary">
    <h3 style="font-size:20px;margin-bottom:16px">Summary</h3>
    <div class="rowl"><span>Subtotal</span><b id="subtotalVal">$0</b></div>
    <div class="rowl"><span>Shipping</span><span id="shipVal">—</span></div>
    <div class="rowl" style="border-top:1px solid var(--line);padding-top:12px;margin-top:8px"><span>Total</span><b id="grandVal">$0</b></div>
    <a class="btn btn--block" style="margin-top:18px" href="checkout.html">Checkout</a>
    <a class="btn btn--outline btn--block" style="margin-top:10px" href="shop.html">Continue shopping</a>
  </aside>
</div>
''')

write("checkout.html","Checkout","checkout",'''
<div class="wrap page-hero">
  <div class="steps"><span class="is-on">1 · Information</span><span>2 · Shipping</span><span>3 · Payment</span></div>
  <h1 class="h-sec">Checkout</h1>
</div>
<div class="wrap checkout-layout" style="padding-bottom:var(--sec)">
  <form class="summary" action="thank-you.html">
    <h3 style="margin-bottom:16px">Contact &amp; shipping</h3>
    <div class="field"><label>Email</label><input type="email" required placeholder="you@example.com"></div>
    <div class="row g-2">
      <div class="col-6 field"><label>First name</label><input required></div>
      <div class="col-6 field"><label>Last name</label><input required></div>
    </div>
    <div class="field"><label>Address</label><input required placeholder="Street, number"></div>
    <div class="row g-2">
      <div class="col-6 field"><label>City</label><input required></div>
      <div class="col-6 field"><label>Postcode</label><input required></div>
    </div>
    <div class="field"><label>Country</label><select><option>Portugal</option><option>Pakistan</option><option>United Kingdom</option><option>United States</option></select></div>
    <h3 style="margin:18px 0 12px">Payment (demo)</h3>
    <div class="field"><label>Card number</label><input placeholder="4242 4242 4242 4242" required></div>
    <div class="row g-2">
      <div class="col-6 field"><label>Expiry</label><input placeholder="MM/YY" required></div>
      <div class="col-6 field"><label>CVC</label><input placeholder="123" required></div>
    </div>
    <button class="btn btn--block" type="submit">Place order</button>
  </form>
  <aside class="summary">
    <h3 style="margin-bottom:14px">Your order</h3>
    <p class="lede">One tree planted. Plastic-free packing. 30-day returns.</p>
    <div class="rowl" style="margin-top:16px"><span>Estimated total</span><b id="chkTotal">—</b></div>
  </aside>
</div>
''', extra='''<script>document.addEventListener("DOMContentLoaded",()=>{
  const t=terraCart().reduce((n,i)=>n+i.qty*i.price,0);
  const el=document.getElementById("chkTotal"); if(el) el.textContent="$"+t.toFixed(2);
});</script>''')

write("thank-you.html","Thank you","thanks",'''
<div class="wrap page-hero" style="text-align:center;max-width:640px;margin:0 auto;padding-bottom:var(--sec)">
  <span class="pill">Order confirmed</span>
  <h1 class="h-sec" style="margin:18px 0">Thank you — we are packing it slowly.</h1>
  <p class="lede" style="margin-inline:auto">Order <b>#TR-4821</b> is confirmed. A tree will be planted this week. You will get tracking in 24 hours.</p>
  <div class="hero__cta" style="justify-content:center">
    <a class="btn" href="account.html">View in my account</a>
    <a class="btn btn--outline" href="shop.html">Keep browsing</a>
  </div>
</div>
''')

write("login.html","Login","login",'''
<div class="wrap" style="padding:var(--sec) 0">
  <div class="auth">
    <div class="tabs">
      <button class="is-on" type="button" data-tab="in">Sign in</button>
      <button type="button" data-tab="up">Create account</button>
    </div>
    <form id="formIn" action="account.html">
      <div class="field"><label>Email</label><input type="email" required></div>
      <div class="field"><label>Password</label><input type="password" required></div>
      <button class="btn btn--block" type="submit">Sign in</button>
    </form>
    <form id="formUp" action="account.html" hidden>
      <div class="field"><label>Name</label><input required></div>
      <div class="field"><label>Email</label><input type="email" required></div>
      <div class="field"><label>Password</label><input type="password" required></div>
      <button class="btn btn--block" type="submit">Create account</button>
    </form>
  </div>
</div>
''', extra='''<script>document.addEventListener("DOMContentLoaded",()=>{
  document.querySelectorAll("[data-tab]").forEach(b=>b.onclick=()=>{
    document.querySelectorAll("[data-tab]").forEach(x=>x.classList.remove("is-on"));
    b.classList.add("is-on");
    formIn.hidden=b.dataset.tab!=="in";
    formUp.hidden=b.dataset.tab!=="up";
  });
});</script>''')

write("account.html","My account","account",'''
<div class="wrap page-hero"><h1 class="h-sec">My account</h1><p class="lede">Orders, addresses and details.</p></div>
<div class="wrap dash" style="padding-bottom:var(--sec)">
  <nav class="dash-nav">
    <a class="is-on" href="#orders">Orders</a>
    <a href="#addr">Addresses</a>
    <a href="#details">Account details</a>
    <a href="wishlist.html">Wishlist</a>
    <a href="index.html">Sign out</a>
  </nav>
  <div>
    <div id="orders" class="order-card"><b>Order #TR-4821</b><p style="color:var(--muted)">Placed 12 Sep 2026 · Processing</p><span class="pill" style="margin-top:10px">In studio</span></div>
    <div id="addr" class="order-card"><b>Default address</b><p style="color:var(--muted)">Rua das Flores 18<br>4050-262 Porto, Portugal</p></div>
    <div id="details" class="summary">
      <h3 style="margin-bottom:12px">Account details</h3>
      <div class="field"><label>Name</label><input value="Clara Nogueira"></div>
      <div class="field"><label>Email</label><input value="clara@example.com"></div>
      <button class="btn">Save changes</button>
    </div>
  </div>
</div>
''')

write("wishlist.html","Wishlist","wish",'''
<div class="wrap page-hero"><h1 class="h-sec">Wishlist</h1><p class="lede">Pieces you are holding onto.</p></div>
<div class="wrap" style="padding-bottom:var(--sec)"><div class="pg" id="wishGrid"></div></div>
''', extra='''<script>document.addEventListener("DOMContentLoaded",()=>{
  const ids=JSON.parse(localStorage.getItem("terra_wish_v1")||"[]");
  const g=document.getElementById("wishGrid");
  const list=ids.map(id=>TERRA_CATALOG[id]).filter(Boolean);
  g.innerHTML=list.length?list.map(terraCard).join(''):'<p class="lede">Nothing saved yet. Tap the heart on any product.</p>';
});</script>''')

write("about.html","About","about",'''
<div class="wrap page-hero">
  <span class="pill">Since 2016 · Porto</span>
  <h1 class="h-sec" style="margin:16px 0">Grown, spun, sewn — <em>and traced</em></h1>
  <p class="lede">TERRA makes natural-fibre clothing in small batches. We publish the journey of every fabric, from farm gate to finished seam.</p>
</div>
<div class="wrap" style="padding-bottom:var(--sec)">
  <div class="hero__arch" style="max-width:900px;margin-bottom:32px"><img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=1400&q=80" alt="Atelier"></div>
  <div class="prose">
    <p>Nine partner farms in Portugal, Turkey and India. Plant-based dyes. Closed-loop washing that uses 82% less water than the industry average for cotton.</p>
    <p>We repair anything we have ever sold, for free. That is not a marketing line — it is how the clothes are designed.</p>
  </div>
</div>
''')

write("contact.html","Contact","contact",'''
<div class="wrap page-hero"><h1 class="h-sec">Contact us</h1><p class="lede">Studio hours Monday–Friday, 10–18 WET.</p></div>
<div class="wrap contact-grid" style="padding-bottom:var(--sec)">
  <form class="summary" onsubmit="event.preventDefault();terraToast('Message sent — we reply within two days');this.reset();">
    <div class="field"><label>Name</label><input required></div>
    <div class="field"><label>Email</label><input type="email" required></div>
    <div class="field"><label>Message</label><textarea rows="5" required></textarea></div>
    <button class="btn" type="submit">Send</button>
  </form>
  <div>
    <div class="map">Porto studio · Rua das Flores 18</div>
    <p style="margin-top:16px;color:var(--muted)">hello@terra.example<br>+351 22 000 0000</p>
  </div>
</div>
''')

write("size-guide.html","Size guide","guide",'''
<div class="wrap page-hero"><h1 class="h-sec">Size guide</h1><p class="lede">Apparel in cm. Shoes in EU.</p></div>
<div class="wrap" style="padding-bottom:var(--sec)">
  <h2 class="h-sec" style="font-size:1.4rem;margin-bottom:12px">Apparel</h2>
  <div style="overflow:auto"><table class="table-size">
    <tr><th>Size</th><th>Bust</th><th>Waist</th><th>Hip</th></tr>
    <tr><td>XS</td><td>80–84</td><td>62–66</td><td>88–92</td></tr>
    <tr><td>S</td><td>84–88</td><td>66–70</td><td>92–96</td></tr>
    <tr><td>M</td><td>88–94</td><td>70–76</td><td>96–102</td></tr>
    <tr><td>L</td><td>94–100</td><td>76–82</td><td>102–108</td></tr>
    <tr><td>XL</td><td>100–108</td><td>82–90</td><td>108–116</td></tr>
  </table></div>
  <h2 class="h-sec" style="font-size:1.4rem;margin:32px 0 12px">Shoes (EU)</h2>
  <div style="overflow:auto"><table class="table-size">
    <tr><th>EU</th><th>UK</th><th>US</th><th>Foot (cm)</th></tr>
    <tr><td>36</td><td>3.5</td><td>6</td><td>23.0</td></tr>
    <tr><td>37</td><td>4</td><td>6.5</td><td>23.5</td></tr>
    <tr><td>38</td><td>5</td><td>7.5</td><td>24.2</td></tr>
    <tr><td>39</td><td>6</td><td>8.5</td><td>24.8</td></tr>
    <tr><td>40</td><td>6.5</td><td>9</td><td>25.4</td></tr>
    <tr><td>41</td><td>7.5</td><td>10</td><td>26.0</td></tr>
  </table></div>
</div>
''')

write("faq.html","FAQ","faq",'''
<div class="wrap page-hero"><h1 class="h-sec">Questions</h1></div>
<div class="wrap faq" style="padding-bottom:var(--sec);max-width:760px">
  <details open><summary>When will my order ship?</summary><p>Orders leave Porto in 1–2 working days. Delivery is 3–6 days after that.</p></details>
  <details><summary>Do you ship to Pakistan?</summary><p>Yes. Duties may apply at customs. We pack plastic-free.</p></details>
  <details><summary>How do repairs work?</summary><p>Email photos of the wear. We send a prepaid label. Mending is free for life.</p></details>
  <details><summary>Are the dyes natural?</summary><p>Where we use colour, yes — madder, indigo, pomegranate. Some undyed pieces are the fibre’s own tone.</p></details>
  <details><summary>Can I change an order?</summary><p>Write within two hours of checkout and we will try. After that it is already being packed.</p></details>
</div>
''')

write("shipping.html","Shipping","ship",'''
<div class="wrap page-hero"><h1 class="h-sec">Shipping &amp; delivery</h1></div>
<div class="wrap prose" style="padding-bottom:var(--sec)">
  <p>Free plastic-free delivery on orders over $90. Under $90, a flat $8. Express is $18 where available.</p>
  <h2>Times</h2>
  <p>EU 3–5 working days. UK 4–6. Rest of world 6–12. We do not ship to PO boxes.</p>
  <h2>Packing</h2>
  <p>Recycled paper mailers, soy inks, no plastic tape. If a courier adds a polybag, tell us — we chase them.</p>
</div>
''')

write("returns.html","Returns","returns",'''
<div class="wrap page-hero"><h1 class="h-sec">Returns &amp; exchanges</h1></div>
<div class="wrap prose" style="padding-bottom:var(--sec)">
  <p>30 days from delivery. Unworn, unwashed, tags on. Shoes must be tried on carpets only.</p>
  <h2>Exchanges</h2>
  <p>Size exchanges are free. Start from your order email or the account page.</p>
  <h2>Refunds</h2>
  <p>Issued to the original payment method within 5 working days of the parcel reaching Porto.</p>
</div>
''')

write("legal.html","Privacy & Terms","legal",'''
<div class="wrap page-hero"><h1 class="h-sec">Privacy policy &amp; terms</h1></div>
<div class="wrap prose" style="padding-bottom:var(--sec)">
  <h2>Privacy</h2>
  <p>We collect the minimum needed to fulfil orders: name, address, email, and payment tokens via our processor. We never sell lists.</p>
  <p>Analytics are cookieless where possible. Newsletter is double opt-in. You can delete your account from My account.</p>
  <h2>Terms of service</h2>
  <p>TERRA Studio, Porto, Portugal. Goods remain ours until paid. Colours on screen may differ from fibre in daylight.</p>
  <p>Limitation of liability is limited to the value of the order except where law forbids it. Governing law: Portugal.</p>
</div>
''')

print("done")

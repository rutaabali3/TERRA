from pathlib import Path
ROOT = Path("/home/user")
CSS = (ROOT/"css"/"terra.css").read_text()

PRODUCTS = [
    dict(id="dress", name="Bias-Cut Linen Dress", cat="Clothing", price="$168.00", was="$210.00", img="images/dress.jpg", flag="Bestseller", href="product.html"),
    dict(id="shirt", name="Oversized Poplin Shirt", cat="Clothing", price="$108.00", was="", img="images/shirt.jpg", flag="Organic", href="product-shirt.html"),
    dict(id="coat", name="Wool Wrap Coat", cat="Clothing", price="$340.00", was="", img="images/coat.jpg", flag="Low stock", href="product-coat.html"),
    dict(id="trouser", name="Wide-Leg Linen Trouser", cat="Clothing", price="$128.00", was="$148.00", img="images/trouser.jpg", flag="Bestseller", href="product-trouser.html"),
    dict(id="sneaker", name="Everyday Low Sneaker", cat="Shoes", price="$132.00", was="$158.00", img="images/sneaker.jpg", flag="Recycled", href="product-sneaker.html"),
    dict(id="sandal", name="Woven Leather Sandal", cat="Shoes", price="$98.00", was="", img="images/sandal.jpg", flag="New", href="product-sandal.html"),
    dict(id="bag", name="Vegetable-Tanned Tote", cat="Accessories", price="$225.00", was="", img="images/bag.jpg", flag="New", href="product-bag.html"),
    dict(id="scarf", name="Plant-Dyed Wool Scarf", cat="Accessories", price="$64.00", was="", img="images/scarf.jpg", flag="Organic", href="product-scarf.html"),
]

def card(p):
    was = f"<s>{p['was']}</s>" if p['was'] else ""
    return f'''<article class="pcard">
      <a class="pcard__media" href="{p['href']}">
        <span class="pcard__flag">{p['flag']}</span>
        <img src="{p['img']}" alt="{p['name']}">
      </a>
      <div class="pcard__body">
        <p class="pcard__cat">{p['cat']}</p>
        <h3><a href="{p['href']}">{p['name']}</a></h3>
        <div class="pcard__foot">
          <span class="price">{was}{p['price']}</span>
          <a class="addbtn" href="cart.html">Add</a>
        </div>
      </div>
    </article>'''

def cards(cat=None):
    return "\n".join(card(p) for p in PRODUCTS if cat is None or p["cat"]==cat)

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — TERRA</title>
<link rel="stylesheet" href="css/{page}.css">
</head>
<body>
<input type="checkbox" id="nav-toggle" class="nav-toggle" aria-hidden="true">
<div class="topbar"><div class="wrap">
  <span>Plant a tree with every order</span>
  <span>Free plastic-free delivery over <b>$90</b></span>
  <span>30-day easy returns</span>
</div></div>
<header class="header"><div class="wrap header__in">
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
    <a class="ibtn" href="shop.html" aria-label="Search"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg></a>
    <a class="ibtn" href="wishlist.html" aria-label="Wishlist"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M12 20s-7-4.4-7-9.4A4.1 4.1 0 0 1 12 8a4.1 4.1 0 0 1 7 2.6c0 5-7 9.4-7 9.4Z"/></svg></a>
    <a class="ibtn" href="login.html" aria-label="Account"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="12" cy="8.5" r="3.6"/><path d="M4.5 20c1.2-3.7 4-5.6 7.5-5.6s6.3 1.9 7.5 5.6"/></svg></a>
    <a class="ibtn" href="cart.html" aria-label="Basket"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M5.5 8h13l-1 12.2H6.5L5.5 8Z"/><path d="M9 8V6.6a3 3 0 0 1 6 0V8"/></svg><i class="badge is-on">2</i></a>
    <label class="ibtn burger" for="nav-toggle" aria-label="Menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M3 7h18M3 12h18M3 17h18"/></svg></label>
  </div>
</div></header>
<nav class="mnav">
  <label class="ibtn mnav__close" for="nav-toggle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="m6 6 12 12M18 6 6 18"/></svg></label>
  <a href="index.html">Home <span>→</span></a>
  <a href="shop.html">Shop <span>→</span></a>
  <a href="category-clothing.html">Clothing <span>→</span></a>
  <a href="category-shoes.html">Shoes <span>→</span></a>
  <a href="category-accessories.html">Accessories <span>→</span></a>
  <a href="about.html">About <span>→</span></a>
  <a href="contact.html">Contact <span>→</span></a>
  <a href="faq.html">FAQ <span>→</span></a>
  <a href="login.html">Account <span>→</span></a>
</nav>
<main>
'''

FOOT = '''
</main>
<footer class="footer"><div class="wrap footer__grid">
  <div><a href="index.html" class="brand"><i></i>TERRA</a>
    <p style="color:var(--muted);margin:16px 0;max-width:34ch">Natural-fibre clothing, made slowly in Portugal. Plastic-free since 2016.</p>
  </div>
  <div><h5>Shop</h5><ul>
    <li><a href="shop.html">All products</a></li>
    <li><a href="category-clothing.html">Clothing</a></li>
    <li><a href="category-shoes.html">Shoes</a></li>
    <li><a href="category-accessories.html">Accessories</a></li>
  </ul></div>
  <div><h5>Help</h5><ul>
    <li><a href="size-guide.html">Size guide</a></li>
    <li><a href="shipping.html">Shipping</a></li>
    <li><a href="returns.html">Returns</a></li>
    <li><a href="faq.html">FAQ</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul></div>
  <div><h5>Studio</h5><ul>
    <li><a href="about.html">About us</a></li>
    <li><a href="legal.html">Privacy &amp; terms</a></li>
    <li><a href="account.html">My account</a></li>
    <li><a href="wishlist.html">Wishlist</a></li>
  </ul></div>
</div>
<div class="wrap footer__bot">
  <span>© 2026 TERRA Studio · Porto</span>
  <div class="pay"><span>Visa</span><span>Mastercard</span><span>PayPal</span></div>
  <span><a href="legal.html">Privacy · Terms</a></span>
</div></footer>
</body></html>
'''

def write(fname, title, body):
    page = Path(fname).stem
    css_path = ROOT/"css"/f"{page}.css"
    css_path.parent.mkdir(parents=True, exist_ok=True)
    css_path.write_text(CSS, encoding="utf-8")
    html = HEAD.format(title=title, page=page) + body + FOOT
    (ROOT/fname).write_text(html, encoding="utf-8")
    print("wrote", fname, "bytes", len(html), "+", f"css/{page}.css")

write("index.html", "Home", f'''
<section class="hero"><div class="wrap hero__in">
  <div>
    <span class="pill">New season · Raw linen</span>
    <h1 class="h-xl"><span>Dress simply.</span><span>Live <em>gently.</em></span></h1>
    <p class="lede">Everyday pieces in organic cotton, raw linen and wool — dyed with plants, sewn in small batches.</p>
    <div class="hero__cta">
      <a href="shop.html" class="btn btn--lg">Shop the collection</a>
      <a href="about.html" class="btn btn--outline btn--lg">How we make it</a>
    </div>
  </div>
  <div class="hero__media">
    <div class="hero__arch"><img src="images/hero.jpg" alt="Linen look in a field"></div>
    <span class="hero__badge">Carbon neutral</span>
    <div class="hero__card">
      <img src="images/dress.jpg" alt="">
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
    <a class="cat" href="category-clothing.html"><div class="cat__img"><img src="images/dress.jpg" alt="Clothing"></div><div class="cat__row"><div><h3>Clothing</h3><small>28 pieces</small></div></div></a>
    <a class="cat" href="category-shoes.html"><div class="cat__img"><img src="images/sneaker.jpg" alt="Shoes"></div><div class="cat__row"><div><h3>Shoes</h3><small>9 pieces</small></div></div></a>
    <a class="cat" href="category-accessories.html"><div class="cat__img"><img src="images/bag.jpg" alt="Accessories"></div><div class="cat__row"><div><h3>Accessories</h3><small>12 pieces</small></div></div></a>
    <a class="cat" href="shop.html"><div class="cat__img"><img src="images/coat.jpg" alt="New"></div><div class="cat__row"><div><h3>New arrivals</h3><small>This week</small></div></div></a>
  </div>
</div></section>
<section class="section" style="padding-top:0"><div class="wrap">
  <div class="sec-head"><span class="pill">Loved most</span><h2 class="h-sec">Bestsellers</h2></div>
  <div class="pg">{cards()}</div>
  <p class="text-center" style="text-align:center;margin-top:28px"><a class="btn btn--soft" href="shop.html">Browse all pieces</a></p>
</div></section>
<section class="wrap" style="padding-bottom:var(--sec)">
  <div class="news">
    <div><span class="pill">Letters from the studio</span><h2 class="h-sec" style="margin-top:14px">A slower inbox</h2>
      <p>Two letters a month and 10% off your first order.</p></div>
    <form class="form" action="index.html"><input type="email" required placeholder="Your email"><button type="submit">Join us</button></form>
  </div>
</section>
''')

def listing(fname, title, cat, crumb, h, lede):
    write(fname, title, f'''
<div class="wrap page-hero">
  <div class="crumb"><a href="index.html">Home</a> / {crumb}</div>
  <span class="pill pill--sand">{title}</span>
  <h1 class="h-sec" style="margin:14px 0">{h}</h1>
  <p class="lede">{lede}</p>
</div>
<div class="wrap" style="padding-bottom:var(--sec)">
  <div class="pg">{cards(cat)}</div>
</div>''')

listing("shop.html","Shop", None, "Shop", "The full collection", "Eight pieces on this sample — natural fibres only.")
listing("category-clothing.html","Clothing", "Clothing", "<a href='shop.html'>Shop</a> / Clothing", "Clothing", "Linen, poplin and wool for every day of the week.")
listing("category-shoes.html","Shoes", "Shoes", "<a href='shop.html'>Shop</a> / Shoes", "Shoes", "Vegetable-tanned leather and recycled soles.")
listing("category-accessories.html","Accessories", "Accessories", "<a href='shop.html'>Shop</a> / Accessories", "Accessories", "Totes, scarves and the small things that last.")

SIZES_AP = '<button class="sizebtn">XS</button><button class="sizebtn is-on">S</button><button class="sizebtn">M</button><button class="sizebtn">L</button><button class="sizebtn">XL</button>'
SIZES_SH = '<button class="sizebtn">36</button><button class="sizebtn is-on">38</button><button class="sizebtn">40</button><button class="sizebtn">41</button>'
SIZES_OS = '<button class="sizebtn is-on">One size</button>'

def pdp(p):
    sizes = SIZES_OS if p["cat"]=="Accessories" else (SIZES_SH if p["cat"]=="Shoes" else SIZES_AP)
    write(p["href"], p["name"], f'''
<div class="wrap page-hero pdp">
  <div class="gallery">
    <div class="gallery__main"><img src="{p['img']}" alt="{p['name']}"></div>
    <div class="gallery__thumbs">
      <span class="is-on" style="display:block;border-radius:14px;overflow:hidden;border:2px solid var(--clay)"><img src="{p['img']}" alt=""></span>
      <span style="display:block;border-radius:14px;overflow:hidden"><img src="{p['img']}" alt=""></span>
      <span style="display:block;border-radius:14px;overflow:hidden"><img src="images/atelier.jpg" alt=""></span>
      <span style="display:block;border-radius:14px;overflow:hidden"><img src="images/hero.jpg" alt=""></span>
    </div>
  </div>
  <div>
    <div class="crumb"><a href="index.html">Home</a> / <a href="shop.html">Shop</a> / {p['cat']}</div>
    <h1 class="h-sec">{p['name']}</h1>
    <p class="price" style="margin:12px 0">{('<s>'+p['was']+'</s> ') if p['was'] else ''}{p['price']}</p>
    <p class="lede">Grown, spun and sewn in small batches. Plant-dyed where colour is used.</p>
    <p style="font-size:13px;margin:16px 0 8px;letter-spacing:.08em;text-transform:uppercase;color:var(--faint)">Size · <a href="size-guide.html" style="color:var(--clay);text-transform:none;letter-spacing:0">Size guide</a></p>
    <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px">{sizes}</div>
    <div style="display:flex;gap:12px;flex-wrap:wrap">
      <a class="btn" href="cart.html">Add to basket</a>
      <a class="btn btn--outline" href="wishlist.html">Wishlist</a>
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
  <div class="pg">{cards()}</div>
</div></section>
''')

for p in PRODUCTS:
    pdp(p)

write("cart.html","Cart",'''
<div class="wrap page-hero"><div class="crumb"><a href="index.html">Home</a> / Cart</div><h1 class="h-sec">Your basket</h1></div>
<div class="wrap cart-layout" style="padding-bottom:var(--sec)">
  <div class="cart-table">
    <div class="citem"><img src="images/dress.jpg" alt=""><div style="flex:1"><h3>Bias-Cut Linen Dress</h3><small style="color:var(--faint)">Size S</small></div><b>$168.00</b></div>
    <div class="citem"><img src="images/shirt.jpg" alt=""><div style="flex:1"><h3>Oversized Poplin Shirt</h3><small style="color:var(--faint)">Size M</small></div><b>$108.00</b></div>
  </div>
  <aside class="summary">
    <h3 style="font-size:20px;margin-bottom:16px">Summary</h3>
    <div class="rowl"><span>Subtotal</span><b>$276.00</b></div>
    <div class="rowl"><span>Shipping</span><span>Free</span></div>
    <div class="rowl" style="border-top:1px solid var(--line);padding-top:12px"><span>Total</span><b>$276.00</b></div>
    <a class="btn btn--block" style="margin-top:18px" href="checkout.html">Checkout</a>
    <a class="btn btn--outline btn--block" style="margin-top:10px" href="shop.html">Continue shopping</a>
  </aside>
</div>
''')

write("checkout.html","Checkout",'''
<div class="wrap page-hero"><div class="steps"><span class="is-on">1 · Information</span><span>2 · Shipping</span><span>3 · Payment</span></div><h1 class="h-sec">Checkout</h1></div>
<div class="wrap checkout-layout" style="padding-bottom:var(--sec)">
  <form class="summary" action="thank-you.html" method="get">
    <h3 style="margin-bottom:16px">Contact &amp; shipping</h3>
    <div class="field"><label>Email</label><input type="email" required></div>
    <div class="field"><label>First name</label><input required></div>
    <div class="field"><label>Last name</label><input required></div>
    <div class="field"><label>Address</label><input required></div>
    <div class="field"><label>City</label><input required></div>
    <div class="field"><label>Card number</label><input placeholder="4242 4242 4242 4242" required></div>
    <button class="btn btn--block" type="submit">Place order</button>
  </form>
  <aside class="summary"><h3>Your order</h3>
    <div class="citem" style="margin-top:12px"><img src="images/dress.jpg" alt=""><div>Linen Dress · S</div></div>
    <div class="rowl" style="margin-top:16px"><span>Total</span><b>$276.00</b></div>
  </aside>
</div>
''')

write("thank-you.html","Thank you",'''
<div class="wrap page-hero" style="text-align:center;max-width:640px;margin:0 auto;padding-bottom:var(--sec)">
  <span class="pill">Order confirmed</span>
  <h1 class="h-sec" style="margin:18px 0">Thank you — we are packing it slowly.</h1>
  <p class="lede" style="margin-inline:auto">Order <b>#TR-4821</b> is confirmed.</p>
  <div class="hero__cta" style="justify-content:center">
    <a class="btn" href="account.html">View in my account</a>
    <a class="btn btn--outline" href="shop.html">Keep browsing</a>
  </div>
</div>
''')

write("login.html","Login",'''
<div class="wrap" style="padding:var(--sec) 0">
  <div class="auth">
    <h1 class="h-sec" style="font-size:1.8rem;margin-bottom:18px">Sign in</h1>
    <form action="account.html" method="get">
      <div class="field"><label>Email</label><input type="email" required></div>
      <div class="field"><label>Password</label><input type="password" required></div>
      <button class="btn btn--block" type="submit">Sign in</button>
    </form>
    <hr style="border:0;border-top:1px solid var(--line);margin:28px 0">
    <h2 class="h-sec" style="font-size:1.4rem;margin-bottom:14px">Create account</h2>
    <form action="account.html" method="get">
      <div class="field"><label>Name</label><input required></div>
      <div class="field"><label>Email</label><input type="email" required></div>
      <div class="field"><label>Password</label><input type="password" required></div>
      <button class="btn btn--outline btn--block" type="submit">Create account</button>
    </form>
  </div>
</div>
''')

write("account.html","My account",'''
<div class="wrap page-hero"><h1 class="h-sec">My account</h1></div>
<div class="wrap dash" style="padding-bottom:var(--sec)">
  <nav class="dash-nav">
    <a class="is-on" href="#orders">Orders</a>
    <a href="#addr">Addresses</a>
    <a href="wishlist.html">Wishlist</a>
    <a href="index.html">Sign out</a>
  </nav>
  <div>
    <div class="order-card"><b>Order #TR-4821</b><p style="color:var(--muted)">12 Sep 2026 · Processing</p></div>
    <div class="order-card"><b>Default address</b><p style="color:var(--muted)">Rua das Flores 18, Porto</p></div>
  </div>
</div>
''')

write("wishlist.html","Wishlist", f'''
<div class="wrap page-hero"><h1 class="h-sec">Wishlist</h1></div>
<div class="wrap" style="padding-bottom:var(--sec)"><div class="pg">{card(PRODUCTS[0])}{card(PRODUCTS[4])}</div></div>
''')

write("about.html","About",'''
<div class="wrap page-hero">
  <span class="pill">Since 2016 · Porto</span>
  <h1 class="h-sec" style="margin:16px 0">Grown, spun, sewn — <em>and traced</em></h1>
  <p class="lede">TERRA makes natural-fibre clothing in small batches.</p>
</div>
<div class="wrap" style="padding-bottom:var(--sec)">
  <div class="hero__arch" style="max-width:900px;margin-bottom:32px"><img src="images/atelier.jpg" alt="Atelier"></div>
  <div class="prose"><p>Nine partner farms. Plant-based dyes. Free repairs for life.</p></div>
</div>
''')

write("contact.html","Contact",'''
<div class="wrap page-hero"><h1 class="h-sec">Contact us</h1></div>
<div class="wrap contact-grid" style="padding-bottom:var(--sec)">
  <form class="summary" action="contact.html" method="get">
    <div class="field"><label>Name</label><input required></div>
    <div class="field"><label>Email</label><input type="email" required></div>
    <div class="field"><label>Message</label><textarea rows="5" required></textarea></div>
    <button class="btn" type="submit">Send</button>
  </form>
  <div class="map">Porto studio · Rua das Flores 18<br>hello@terra.example</div>
</div>
''')

write("size-guide.html","Size guide",'''
<div class="wrap page-hero"><h1 class="h-sec">Size guide</h1></div>
<div class="wrap" style="padding-bottom:var(--sec)">
  <table class="table-size">
    <tr><th>Size</th><th>Bust</th><th>Waist</th><th>Hip</th></tr>
    <tr><td>XS</td><td>80–84</td><td>62–66</td><td>88–92</td></tr>
    <tr><td>S</td><td>84–88</td><td>66–70</td><td>92–96</td></tr>
    <tr><td>M</td><td>88–94</td><td>70–76</td><td>96–102</td></tr>
    <tr><td>L</td><td>94–100</td><td>76–82</td><td>102–108</td></tr>
    <tr><td>XL</td><td>100–108</td><td>82–90</td><td>108–116</td></tr>
  </table>
  <table class="table-size" style="margin-top:28px">
    <tr><th>EU</th><th>UK</th><th>US</th><th>cm</th></tr>
    <tr><td>36</td><td>3.5</td><td>6</td><td>23.0</td></tr>
    <tr><td>38</td><td>5</td><td>7.5</td><td>24.2</td></tr>
    <tr><td>40</td><td>6.5</td><td>9</td><td>25.4</td></tr>
  </table>
</div>
''')

write("faq.html","FAQ",'''
<div class="wrap page-hero"><h1 class="h-sec">Questions</h1></div>
<div class="wrap faq" style="padding-bottom:var(--sec);max-width:760px">
  <details open><summary>When will my order ship?</summary><p>1–2 working days from Porto, then 3–6 in transit.</p></details>
  <details><summary>Do you ship to Pakistan?</summary><p>Yes. Duties may apply at customs.</p></details>
  <details><summary>How do repairs work?</summary><p>Email photos. Prepaid label. Mending is free for life.</p></details>
</div>
''')

write("shipping.html","Shipping",'''
<div class="wrap page-hero"><h1 class="h-sec">Shipping &amp; delivery</h1></div>
<div class="wrap prose" style="padding-bottom:var(--sec)">
  <p>Free over $90. Otherwise $8. Express $18.</p>
  <h2>Times</h2><p>EU 3–5 days. Rest of world 6–12.</p>
</div>
''')

write("returns.html","Returns",'''
<div class="wrap page-hero"><h1 class="h-sec">Returns &amp; exchanges</h1></div>
<div class="wrap prose" style="padding-bottom:var(--sec)">
  <p>30 days. Unworn, tags on. Size exchanges are free.</p>
</div>
''')

write("legal.html","Privacy & Terms",'''
<div class="wrap page-hero"><h1 class="h-sec">Privacy &amp; terms</h1></div>
<div class="wrap prose" style="padding-bottom:var(--sec)">
  <h2>Privacy</h2><p>We collect only what we need to fulfil orders. We never sell lists.</p>
  <h2>Terms</h2><p>TERRA Studio, Porto. Governing law: Portugal.</p>
</div>
''')

print("done")

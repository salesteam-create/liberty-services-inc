"""Layout and reusable sections for the Liberty Services prototype."""

import math

from data import BIZ, SERVICES, STATES, TESTIMONIALS, HOME_FAQ
from icons import icon

CTX = {"prefix": "", "path": ""}


def u(target=""):
    """Relative URL from the current page to a site path (e.g. 'services/')."""
    p = CTX["prefix"]
    if not target:
        return p or "./"
    return p + target


def a(target):
    if target.startswith("photos/"):
        target = "img/" + target
    return u("assets/" + target)


def cur(target):
    return ' aria-current="page"' if CTX["path"] == target else ""


# ---------------------------------------------------------------- head/foot

def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#0E1428">
<link rel="icon" href="{a('img/logo-liberty.png')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{a('css/main.css')}">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


def services_menu_items():
    out = []
    for s in SERVICES:
        t = f"services/{s['slug']}/"
        out.append(
            f'<a href="{u(t)}"{cur(t)}><span class="mi-icon">{icon(s["icon"])}</span>'
            f'<span><strong>{s["name"]}</strong><small>{s["menu"]}</small></span></a>'
        )
    return "".join(out)


def header():
    about_cur = " is-current" if CTX["path"].startswith("about-") else ""
    svc_cur = " is-current" if CTX["path"].startswith("services/") else ""
    blog_cur = ' aria-current="page"' if CTX["path"].startswith("blogs/") else ""
    return f"""<header class="site-header">
  <div class="utility">
    <div class="container">
      <span class="utility__offer">First service free. <a href="{u('contact/')}?offer=first-service-free">Claim your offer</a></span>
      <div class="utility__links">
        <a href="{BIZ['portal']}">Customer Portal Login</a>
        <a href="{BIZ['tollfree_href']}"><strong>Toll-free {BIZ['tollfree']}</strong></a>
      </div>
    </div>
  </div>
  <div class="navbar">
    <div class="container">
      <a class="brand" href="{u()}" aria-label="Liberty Services home"><img src="{a('img/logo-liberty-horizontal.png')}" alt="Liberty Services Inc." width="144" height="46"></a>
      <nav class="nav" aria-label="Main">
        <div class="nav__item has-menu{about_cur}">
          <button class="nav__link" aria-expanded="false" aria-haspopup="true">About Us {icon('chevron-down')}</button>
          <div class="nav__menu">
            <a href="{u('about-liberty-services/')}"{cur('about-liberty-services/')}><span class="mi-icon">{icon('shield')}</span><span><strong>Liberty Services</strong><small>Two decades of certified exhaust cleaning</small></span></a>
            <a href="{u('about-filtershine/')}"{cur('about-filtershine/')}><span class="mi-icon">{icon('filter')}</span><span><strong>FilterShine</strong><small>Our filter exchange partner</small></span></a>
          </div>
        </div>
        <div class="nav__item has-menu{svc_cur}">
          <button class="nav__link" aria-expanded="false" aria-haspopup="true">Services {icon('chevron-down')}</button>
          <div class="nav__menu">
            {services_menu_items()}
            <a class="menu-all" href="{u('services/')}">View all services {icon('arrow')}</a>
          </div>
        </div>
        <div class="nav__item"><a class="nav__link" href="{u('blogs/')}"{blog_cur}>Blog</a></div>
        <div class="nav__item"><a class="nav__link" href="{u('contact/')}"{cur('contact/')}>Contact</a></div>
      </nav>
      <div class="header-cta">
        <a class="header-phone" href="{BIZ['phone_href']}">{icon('phone')}<span>{BIZ['phone']}</span></a>
        <a class="btn btn--blue" href="{u('contact/')}">Get a Quote {icon('arrow')}</a>
        <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="drawer">{icon('menu')}</button>
      </div>
    </div>
  </div>
</header>
<div class="drawer" id="drawer" aria-hidden="true">
  <div class="drawer__scrim" data-close-drawer></div>
  <div class="drawer__panel" role="dialog" aria-modal="true" aria-label="Menu">
    <div class="drawer__top">
      <img src="{a('img/logo-liberty-horizontal.png')}" alt="Liberty Services Inc." width="144" height="46">
      <button class="nav-toggle drawer__close" style="display:inline-flex" aria-label="Close menu" data-close-drawer>{icon('x')}</button>
    </div>
    <nav class="drawer__nav" aria-label="Mobile">
      <a href="{u()}">Home</a>
      <div class="drawer__group">
        <button aria-expanded="false">About Us {icon('chevron-down')}</button>
        <div class="drawer__sub"><a href="{u('about-liberty-services/')}">Liberty Services</a><a href="{u('about-filtershine/')}">FilterShine</a></div>
      </div>
      <div class="drawer__group">
        <button aria-expanded="false">Services {icon('chevron-down')}</button>
        <div class="drawer__sub"><a href="{u('services/')}">All services</a>{''.join(f'<a href="{u("services/" + s["slug"] + "/")}">{s["name"]}</a>' for s in SERVICES)}</div>
      </div>
      <a href="{u('blogs/')}">Blog</a>
      <a href="{u('contact/')}">Contact</a>
    </nav>
    <div class="drawer__foot">
      <a class="btn btn--red" href="{u('contact/')}">Schedule Free Survey {icon('arrow')}</a>
      <a class="btn btn--outline btn-phone" href="{BIZ['phone_href']}">{icon('phone')} Call {BIZ['phone']}</a>
    </div>
  </div>
</div>
"""


def footer(proto=False):
    svc = "".join(f'<li><a href="{u("services/" + s["slug"] + "/")}">{s["name"]}</a></li>' for s in SERVICES)
    proto_html = ""
    if proto:
        proto_html = f"""<div class="proto">
  <div class="proto__panel" id="proto-panel">
    <strong>Home hero</strong>
    <div class="proto__seg" role="group" aria-label="Hero mode">
      <button type="button" data-mode="slider" aria-pressed="true">Slider</button>
      <button type="button" data-mode="static" aria-pressed="false">Static</button>
    </div>
    <p>Prototype control for client review. Set the launch default in assets/js/config.js.</p>
  </div>
  <button class="proto__toggle" type="button" aria-expanded="false" aria-controls="proto-panel">{icon('sliders')} Prototype options</button>
</div>
"""
    return f"""<footer class="footer">
  <div class="container footer__main">
    <div class="footer__brand">
      <a href="{u()}" aria-label="Liberty Services home"><img src="{a('img/logo-liberty-horizontal.png')}" alt="Liberty Services Inc." width="144" height="46" loading="lazy"></a>
      <p>Kitchen hood cleaning and grease containment specialists serving commercial kitchens across the Midwest for over two decades.</p>
      <div class="footer__badges"><span>IKECA certified</span><span>NFPA member</span><span>Bonded & insured</span></div>
    </div>
    <div class="footer__cols">
      <div class="footer__col">
        <h3>Services</h3>
        <ul>{svc}<li><a href="{u('services/')}">All services</a></li></ul>
      </div>
      <div class="footer__col">
        <h3>Company</h3>
        <ul>
          <li><a href="{u('about-liberty-services/')}">About Liberty</a></li>
          <li><a href="{u('about-filtershine/')}">About FilterShine</a></li>
          <li><a href="{u('blogs/')}">Blog & news</a></li>
          <li><a href="{u('contact/')}">Contact & quote</a></li>
          <li><a href="{BIZ['portal']}">Customer portal</a></li>
        </ul>
      </div>
      <div class="footer__col">
        <h3>Contact</h3>
        <ul>
          <li>{BIZ['street']}<br>{BIZ['city']}</li>
          <li><a href="{BIZ['phone_href']}">{BIZ['phone']}</a></li>
          <li><a href="{BIZ['tollfree_href']}">Toll-free {BIZ['tollfree']}</a></li>
          <li>Fax {BIZ['fax']}</li>
          <li><a href="{BIZ['linkedin']}" target="_blank" rel="noopener">LinkedIn</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="container">
    <div class="footer__bottom">
      <span>&copy; <span data-year>2026</span> Liberty Services, Inc. All rights reserved.</span>
      <span><a href="{u('privacy-page/')}">Privacy</a> &middot; <a href="{u('legal/')}">Terms & Conditions</a></span>
      <span>Powered by Kilowott</span>
    </div>
  </div>
</footer>
{proto_html}<script src="{a('js/config.js')}"></script>
<script src="{a('js/main.js')}"></script>
</body>
</html>
"""


def page(title, desc, body, proto=False):
    return head(title, desc) + header() + f'<main id="main">\n{body}\n</main>\n' + footer(proto)


# ---------------------------------------------------------------- pieces

def btn_quote(label="Schedule Free Survey", cls="btn--red", target="contact/"):
    return f'<a class="btn {cls}" href="{u(target)}">{label} {icon("arrow")}</a>'


def btn_call(cls="btn--sky"):
    return f'<a class="btn {cls} btn-phone" href="{BIZ["phone_href"]}">{icon("phone")} Call {BIZ["phone"]}</a>'


def crumbs(items):
    parts = [f'<a href="{u()}">Home</a>']
    for label, target in items[:-1]:
        parts.append(icon("chevron-right") + f'<a href="{u(target)}">{label}</a>')
    parts.append(icon("chevron-right") + f'<span aria-current="page">{items[-1][0]}</span>')
    return f'<nav class="crumbs" aria-label="Breadcrumb">{"".join(parts)}</nav>'


def page_hero(crumb_items, eyebrow, title_html, text, img=None, img_alt="", badge=None, ctas=True, compact=False, extra=""):
    media = ""
    if img and not compact:
        b = f'<div class="page-hero__badge">{badge}</div>' if badge else ""
        media = f'<div class="page-hero__img"><img src="{a(img)}" alt="{img_alt}" width="640" height="480">{b}</div>'
    cta = f'<div class="btn-row">{btn_quote()}{btn_call()}</div>' if ctas else ""
    cls = "page-hero page-hero--compact" if compact else "page-hero"
    return f"""<section class="{cls}">
  <div class="container">
    <div class="page-hero__copy">
      {crumbs(crumb_items)}
      <span class="eyebrow eyebrow--rule" style="color:#D8D8D8">{eyebrow}</span>
      <h1 class="display h-xl">{title_html}</h1>
      <p>{text}</p>
      {extra}{cta}
    </div>
    {media}
  </div>
</section>"""


def float_card(icon_name, title, text):
    return f'<div class="float-card"><span class="fc-star">{icon(icon_name)}</span><div><h3>{title}</h3><p>{text}</p></div></div>'


def trust_strip():
    items = [
        ("award", "IKECA certified", "Technicians trained to industry cleaning standards"),
        ("shield", "NFPA 96 compliant", "Every job meets or exceeds NFPA 96"),
        ("clipboard", "Bonded & insured", "Fully covered work, every visit"),
        ("gps", "GPS-verified service", "Arrival and completion times on every report"),
    ]
    inner = "".join(
        f'<div class="trust__item"><span class="trust__icon">{icon(i)}</span><div><h3>{t}</h3><p>{d}</p></div></div>'
        for i, t, d in items
    )
    return f'<section class="trust" aria-label="Why kitchens trust Liberty"><div class="container">{inner}</div></section>'


def logo_strip(label="Trusted across commercial kitchens"):
    mcd = open_svg_path("assets/img/logos/mcdonalds.svg")
    customers = (
        f'<div class="logo-item logo-item--brand" title="McDonald\'s"><svg viewBox="0 0 24 24" fill="currentColor" role="img" aria-label="McDonald\'s">{mcd}</svg></div>'
        # Placeholder wordmarks: swap for authorized logo files once brand-use approval is confirmed.
        '<div class="logo-item logo-item--word" title="Arby\'s" data-logo-placeholder="arbys">Arby\'s</div>'
        '<div class="logo-item logo-item--word" title="Buffalo Wild Wings" data-logo-placeholder="buffalo-wild-wings">Buffalo<br>Wild Wings</div>'
    )
    partners = "".join(
        f'<div class="logo-item" title="{t}"><img src="{a("img/logos/partner-" + f + ".jpg")}" alt="{t}" loading="lazy"></div>'
        for f, t in [("ikeca", "IKECA member"), ("nfpa", "NFPA member"), ("service-trade", "ServiceTrade reporting")]
    )
    return f"""<section class="logos logos--customers" aria-label="{label}">
  <div class="container">
    <h2 class="logos__label">{label}</h2>
    <div class="logos__row">{customers}{partners}</div>
  </div>
</section>"""


_svg_cache = {}


def open_svg_path(path):
    """Return the inner markup of a single-path SVG file (relative to repo root)."""
    if path not in _svg_cache:
        import os, re
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(root, path)) as f:
            s = f.read()
        _svg_cache[path] = "".join(re.findall(r"<path[^>]*/>", s))
    return _svg_cache[path]


def service_cards(exclude=None, head=True):
    cards = []
    n = 0
    for s in SERVICES:
        if s["slug"] == exclude:
            continue
        n += 1
        t = f"services/{s['slug']}/"
        cards.append(f"""<a class="service-card reveal" href="{u(t)}">
  <div class="service-card__media"><img src="{a(s['card_img'])}" alt="{s['name']}" loading="lazy" width="294" height="189"><span class="service-card__icon">{icon(s['icon'])}</span></div>
  <div class="service-card__body">
    <span class="service-card__num">0{n} /</span>
    <h3>{s['name']}</h3>
    <p>{s['summary']}</p>
    <span class="link-arrow">Learn more {icon('arrow')}</span>
  </div>
</a>""")
    heading = ""
    if head:
        heading = f"""<div class="section-head section-head--split">
      <div class="section-head">
        <span class="eyebrow">Our services</span>
        <h2 class="display h-md">Four services.<br>One partner.<br><span class="accent">From hood to roof.</span></h2>
      </div>
      <p class="lead">Complete kitchen care, from the hood to the rooftop fan. One schedule, one set of records and one team that knows your system.</p>
    </div>"""
    return f'{heading}<div class="service-grid service-grid--{len(cards)}">{"".join(cards)}</div>'


def services_section():
    return f'<section class="section" id="services"><div class="container">{service_cards()}</div></section>'


def other_services(slug):
    return f"""<section class="section section--softer">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="section-head"><span class="eyebrow">One partner</span><h2 class="display h-md">Complete kitchen care.<br><span class="accent">From hood to roof.</span></h2></div>
      <p class="lead">Bundle services under one schedule and one set of digital records.</p>
    </div>
    {service_cards(exclude=slug, head=False)}
  </div>
</section>"""


def nfpa_section(soft=True, title='How often should your <span style="white-space:nowrap">kitchen hood</span> be cleaned?'):
    rows = [
        ("Solid fuel cooking", "Wood-fired, charcoal, pizza ovens", "Monthly", ""),
        ("High-volume cooking", "24-hour, charbroiling, wok cooking", "Quarterly", ""),
        ("Moderate-volume cooking", "Most full-service restaurants", "Semi-annually", "is-blue"),
        ("Low-volume cooking", "Churches, day camps, seasonal kitchens", "Annually", "is-blue"),
    ]
    r = "".join(f'<div class="freq__row"><div><strong>{a1}</strong><small>{b}</small></div><em class="{c}">{f}</em></div>' for a1, b, f, c in rows)
    return f"""<section class="section {'section--soft' if soft else ''}" id="nfpa-96">
  <div class="container nfpa">
    <div class="nfpa__copy reveal">
      <span class="eyebrow">NFPA 96 compliance</span>
      <h2 class="display h-md">{title}</h2>
      <p class="lead">NFPA 96 is the fire code standard for commercial kitchen exhaust. It sets a minimum cleaning frequency based on what and how much you cook. Your local fire marshal, landlord or insurer may require more.</p>
      <p class="lead">Liberty Services cleans every system to meet or exceed NFPA 96, and we set your schedule during a free site survey so you are never guessing.</p>
      <a class="btn btn--red btn--block" href="{u('contact/')}">Find My Cleaning Schedule {icon('arrow')}</a>
    </div>
    <div class="freq reveal" role="table" aria-label="NFPA 96 cleaning frequency">
      <div class="freq__head"><span>Type of cooking operation</span><span>NFPA 96 frequency</span></div>
      {r}
      <div class="freq__note">Minimum inspection and cleaning frequencies per NFPA 96. Local requirements may be stricter.</div>
    </div>
  </div>
</section>"""


def process_section(soft=False):
    steps = [
        ("Free site survey", "photos/site-survey.jpg", "We walk your kitchen and roof", "We inspect your hoods, ducts, fans and rooftop, then hand you a written quote and an NFPA 96 schedule."),
        ("After-hours service", "photos/line-flame.jpg", "Your line never stops", "Crews arrive after close or before open, protect your equipment and leave the kitchen ready for the next shift."),
        ("Hood-to-fan cleaning", "photos/hood-hero.jpg", "Cleaned to bare metal", "Hoods, plenums, ducts and fans are cleaned to bare metal, including what owners and fire inspectors cannot see."),
        ("Photo report & certificate", "photos/digital-report.jpg", "Proof in your inbox", "Before-and-after photos, GPS timestamps, deficiency notes and a service certificate, uploaded to your portal."),
    ]
    cards = "".join(f"""<article class="process-card">
  <img src="{a(img)}" alt="">
  <div class="process-card__top"><span class="process-card__step">0{i + 1} /</span><span class="process-card__label"><span class="pulse"></span>{label}</span></div>
  <div class="process-card__bottom"><h3 class="process-card__title">{title}</h3><p>{text}</p></div>
</article>""" for i, (label, img, title, text) in enumerate(steps))
    return f"""<section class="section {'section--softer' if soft else ''}" id="process">
  <div class="container" style="max-width:1100px">
    <div class="section-head section-head--center">
      <span class="eyebrow">The process</span>
      <h2 class="display h-md">Inspection-ready<br><span class="accent">in four steps.</span></h2>
    </div>
    <div class="process__cards">{cards}</div>
  </div>
</section>"""


def proof_section():
    return f"""<section class="section section--blue" id="portal">
  <div class="container proof">
    <div class="proof__copy reveal">
      <span class="eyebrow eyebrow--light">Proof, not promises</span>
      <h2 class="display h-lg">See every clean.<br>Prove every inspection.</h2>
      <p class="lead" style="max-width:340px">Your Liberty customer portal stores every service report, so you can hand a fire inspector, insurer or landlord the proof in seconds.</p>
      <ul class="numlist">
        <li><span class="n">01</span>Before & after photos of every component we clean</li>
        <li><span class="n">02</span>GPS-stamped arrival and completion times</li>
        <li><span class="n">03</span>Deficiency notes and repair recommendations</li>
        <li><span class="n">04</span>Auto-sync to ServiceChannel and Corrigo for operators</li>
      </ul>
      <div class="btn-row" style="margin-top:20px"><a class="btn btn--white" href="{BIZ['portal']}">Customer Portal Login {icon('arrow')}</a></div>
    </div>
    <div class="report reveal" aria-label="Sample service report">
      <div class="report__head">
        <div><small>Service report</small><strong>Downtown location &middot; Hood 1</strong></div>
        <span class="report__tag">NFPA 96: cleaned to bare metal</span>
      </div>
      <div class="ba">
        <img src="{a('photos/liberty-hood-cleaning.jpg')}" alt="Hood after cleaning">
        <div class="ba__before" style="position:absolute;inset:0"><img src="{a('photos/liberty-hood-cleaning.jpg')}" alt="Hood before cleaning"></div>
        <span class="ba__line"></span><span class="ba__handle">DRAG</span>
        <span class="ba__tag ba__tag--before">BEFORE</span><span class="ba__tag ba__tag--after">AFTER</span>
        <span class="ba__note">Illustrative example</span>
        <input type="range" min="0" max="100" value="55" aria-label="Compare before and after">
      </div>
      <div class="report__meta">
        <div><small>Tech arrival time</small><strong>11:42 PM &middot; GPS</strong></div>
        <div><small>Components</small><strong>Hood &middot; Duct &middot; Fan</strong></div>
        <div><small>Next service</small><strong>14 January 2027</strong></div>
      </div>
    </div>
  </div>
</section>"""


def industries_section(soft=False):
    items = [
        ("utensils", "Restaurants & bars", "Independent & full-service"),
        ("store", "Multi-unit operators", "QSR & franchise groups"),
        ("school", "Schools & universities", "Cafeterias & dining halls"),
        ("health", "Healthcare & senior living", "Hospital & care kitchens"),
        ("building", "Hotels & hospitality", "Banquet & room service"),
        ("church", "Churches & community", "Seasonal & low-volume kitchens"),
    ]
    cards = "".join(f'<div class="industry reveal"><span class="industry__icon">{icon(i)}</span><div><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in items)
    return f"""<section class="section {'section--softer' if soft else ''}" id="industries">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow eyebrow--red">Industries we serve</span>
      <h2 class="display h-sm">Built for kitchens that can't afford downtime.</h2>
    </div>
    <div class="industry-grid">{cards}</div>
  </div>
</section>"""


def testimonials_block(title="What kitchen operators say", eyebrow="Customer stories"):
    q = "".join(f"""<figure class="quote reveal">
  <div class="stars" aria-label="5 out of 5">{icon('star') * 5}</div>
  <blockquote>"{t['quote']}"</blockquote>
  <figcaption><span class="avatar" aria-hidden="true">{t['init']}</span><span>{t['who']}</span></figcaption>
</figure>""" for t in TESTIMONIALS)
    # Draft testimonials for layout review: replace with approved client quotes before launch.
    return f"""<div class="testimonials-head">
      <div class="section-head"><span class="eyebrow">{eyebrow}</span><h2 class="display h-sm">{title}</h2></div>
      {btn_quote('Join them', 'btn--outline')}
    </div>
    <div class="testimonials" style="margin-top:32px">{q}</div>"""


def testimonials_section(soft=True):
    return f'<section class="section {"section--soft" if soft else ""}" id="testimonials"><div class="container">{testimonials_block()}</div></section>'


def why_section():
    q = "".join(f"""<figure class="quote reveal">
  <div class="stars" aria-label="5 out of 5">{icon('star') * 5}</div>
  <blockquote>"{t['quote']}"</blockquote>
  <figcaption><span class="avatar" aria-hidden="true">{t['init']}</span><span>{t['who']}</span></figcaption>
</figure>""" for t in TESTIMONIALS)
    return f"""<section class="section section--soft" id="why-liberty">
  <div class="container">
    <div class="why">
      <div class="why__media reveal">
        <img src="{a('photos/plating-line.jpg')}" alt="Commercial kitchen line during service" loading="lazy">
        <div class="why__loc"><span class="pin">{icon('pin')}</span><div><strong>West Milton, Ohio</strong><small>Serving five states across the Midwest</small></div></div>
      </div>
      <div class="why__copy reveal">
        <span class="eyebrow" style="font-weight:600">Why choose us</span>
        <h2 class="display h-why">Cleaner kitchens.<br><span style="color:var(--red-900)">Cleaner water.</span></h2>
        <p class="lead" style="font-size:14px;max-width:475px">Filter exchange captures grease before it reaches drains and waterways, keeping up to 60-70% of it out of your plumbing. Responsible cleaning practices and eco-friendly cleaning chemicals help reduce our environmental impact on every job.</p>
        <div class="stats">
          <div class="stat"><strong>20+</strong><span>Years in business</span></div>
          <div class="stat"><strong>5</strong><span>States served</span></div>
          <div class="stat"><strong>100%</strong><span>Jobs photo-documented</span></div>
          <div class="stat"><strong>NFPA 96</strong><span>Met or exceeded on every job</span></div>
        </div>
      </div>
    </div>
    <div class="testimonials">{q}</div>
  </div>
</section>"""


def compliance_section(title="Compliance made simple.", eyebrow="Less to manage. More peace of mind."):
    return f"""<section class="section section--navy" id="compliance">
  <div class="container compliance">
    <div class="proof__copy reveal">
      <span class="eyebrow eyebrow--light">{eyebrow}</span>
      <h2 class="display h-lg">{title}</h2>
      <p class="lead" style="max-width:340px">Recurring kitchen compliance subscriptions with scheduled service, digital records, photos and deficiency reporting. Service is aligned with applicable NFPA 96 and ANSI/IKECA kitchen exhaust cleaning standards.</p>
      <ul class="numlist numlist--lg" style="margin-top:20px">
        <li><span class="n">01</span>NFPA 96 & ANSI/IKECA alignment</li>
        <li><span class="n">02</span>Digital records & photos</li>
        <li><span class="n">03</span>Deficiency reporting</li>
      </ul>
      <div class="btn-row" style="margin-top:24px">{btn_quote('Start Risk-Free')}<span style="font-size:13px;color:#C9D3F0">First service free for new programs</span></div>
    </div>
    <div class="compliance__media reveal">
      <div class="compliance__img"><img src="{a('photos/digital-report.jpg')}" alt="Technician reviewing digital service records" loading="lazy"></div>
      <div class="compliance__badge">Documented. Every visit.</div>
    </div>
  </div>
</section>"""


# ----------------------------------------------------------- service area map

# Rough state outlines (lon, lat). Accurate enough for a stylised dot map.
POLYS = {
    "OH": [(-84.82, 41.70), (-83.45, 41.73), (-82.7, 41.45), (-81.7, 41.50), (-80.52, 41.98), (-80.52, 40.64), (-80.67, 40.58), (-80.87, 39.90), (-81.70, 39.20), (-82.60, 38.60), (-83.00, 38.73), (-83.70, 38.63), (-84.30, 38.98), (-84.82, 39.10)],
    "IN": [(-87.53, 41.76), (-84.81, 41.76), (-84.82, 39.10), (-84.90, 38.80), (-85.40, 38.70), (-85.90, 38.00), (-86.50, 38.00), (-87.00, 37.80), (-87.60, 37.90), (-87.53, 38.30), (-87.60, 38.70), (-87.53, 39.40)],
    "KY": [(-89.50, 36.50), (-88.00, 36.50), (-86.00, 36.62), (-83.70, 36.60), (-81.97, 37.54), (-82.60, 38.17), (-82.60, 38.60), (-83.00, 38.73), (-83.70, 38.63), (-84.30, 38.98), (-84.82, 39.10), (-85.40, 38.70), (-85.90, 38.00), (-86.50, 38.00), (-87.00, 37.80), (-87.60, 37.90), (-88.10, 37.50), (-89.10, 37.10)],
    "WV": [(-82.60, 38.17), (-81.97, 37.54), (-81.20, 37.25), (-80.30, 37.50), (-79.90, 38.20), (-79.30, 38.40), (-78.40, 39.25), (-77.75, 39.32), (-78.00, 39.60), (-79.48, 39.72), (-80.52, 39.72), (-80.52, 40.64), (-80.67, 40.58), (-80.87, 39.90), (-81.70, 39.20), (-82.60, 38.60)],
    "MI": [(-86.82, 41.76), (-84.81, 41.76), (-83.45, 41.73), (-83.10, 42.10), (-82.50, 42.60), (-82.40, 43.00), (-82.50, 43.60), (-83.30, 44.00), (-83.40, 44.80), (-83.50, 45.40), (-84.70, 45.80), (-85.40, 45.30), (-85.60, 44.80), (-86.20, 44.60), (-86.50, 43.60), (-86.20, 42.70)],
    "MI2": [(-90.40, 46.55), (-87.00, 46.55), (-84.80, 46.50), (-84.60, 46.05), (-85.00, 45.95), (-86.50, 45.75), (-87.60, 45.10), (-88.00, 45.60), (-89.00, 46.00), (-90.40, 46.30)],
}
LAKES = [
    [(-87.9, 41.6), (-87.0, 41.65), (-86.5, 42.2), (-86.2, 43.0), (-86.5, 43.9), (-86.0, 44.9), (-85.0, 45.9), (-85.9, 45.95), (-86.8, 45.4), (-87.6, 44.6), (-87.9, 43.5), (-87.8, 42.4)],
    [(-83.45, 41.73), (-82.6, 41.62), (-81.6, 41.55), (-80.5, 42.0), (-79.0, 42.6), (-78.9, 42.9), (-80.2, 42.75), (-81.5, 42.65), (-82.5, 42.1), (-83.15, 42.0)],
    [(-82.45, 43.05), (-81.7, 43.3), (-81.6, 44.2), (-81.3, 45.2), (-83.0, 45.9), (-84.0, 46.0), (-84.7, 45.85), (-83.5, 45.4), (-83.4, 44.8), (-83.3, 44.05), (-82.6, 43.8), (-82.5, 43.6)],
]
CITIES = [(-84.19, 39.76), (-84.51, 39.10), (-82.99, 39.96), (-83.54, 41.66), (-86.16, 39.77), (-85.14, 41.08), (-85.76, 38.25), (-84.50, 38.04), (-83.05, 42.33), (-85.67, 42.96), (-81.63, 38.35), (-82.45, 38.42), (-83.74, 42.28), (-81.56, 39.27)]
HQ = (-84.33, 39.96)


def _inside(pt, poly):
    x, y = pt
    inside = False
    j = len(poly) - 1
    for i in range(len(poly)):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi:
            inside = not inside
        j = i
    return inside


def service_map_svg():
    lon0, lon1, lat0, lat1 = -90.6, -76.6, 35.9, 46.7
    k = 56.0
    cosm = math.cos(math.radians(41.3))
    W = (lon1 - lon0) * cosm * k
    H = (lat1 - lat0) * k
    step = 0.21

    def xy(lon, lat):
        return ((lon - lon0) * cosm * k, (lat1 - lat) * k)

    dots = []
    lat = lat0 + step / 2
    while lat < lat1:
        lon = lon0 + step / 2
        while lon < lon1:
            p = (lon, lat)
            if not any(_inside(p, l) for l in LAKES):
                st = None
                for key, poly in POLYS.items():
                    if _inside(p, poly):
                        st = key[:2]
                        break
                x, y = xy(lon, lat)
                if st:
                    dots.append(f'<rect class="dot st" data-s="{st}" x="{x - 2.1:.1f}" y="{y - 2.1:.1f}" width="4.2" height="4.2" rx="1"/>')
                else:
                    dots.append(f'<rect class="dot" x="{x - 2.1:.1f}" y="{y - 2.1:.1f}" width="4.2" height="4.2" rx="1"/>')
            lon += step / cosm
        lat += step
    pins = []
    for lon, lat in CITIES:
        x, y = xy(lon, lat)
        pins.append(f'<circle class="pinring" cx="{x:.1f}" cy="{y:.1f}" r="9"/><circle class="pinpt" cx="{x:.1f}" cy="{y:.1f}" r="4"/>')
    hx, hy = xy(*HQ)
    pins.append(f'<circle class="pinring" cx="{hx:.1f}" cy="{hy:.1f}" r="13" style="opacity:.5"/><circle class="hq" cx="{hx:.1f}" cy="{hy:.1f}" r="6"/>')
    hq_left = hx / W * 100
    hq_top = hy / H * 100
    svg = (f'<svg viewBox="0 0 {W:.0f} {H:.0f}" role="img" aria-label="Dotted map of the Liberty Services five-state service area: Ohio, Indiana, Kentucky, Michigan and West Virginia">'
           f'{"".join(dots)}{"".join(pins)}</svg>')
    return svg, hq_left, hq_top


def service_areas_section(soft=False):
    svg, hl, ht = service_map_svg()
    opts = "".join(f'<option value="{s["key"]}">{s["name"]}</option>' for s in STATES)
    cards = "".join(f"""<div class="state-card" data-state="{s['key']}">
  <span class="state-card__icon">{icon('pin')}</span>
  <h3>{s['name']}</h3>
  <ul>{''.join(f'<li>{c}</li>' for c in s['cities'])}</ul>
</div>""" for s in STATES)
    return f"""<section class="section areas {'section--softer' if soft else ''}" id="service-areas" data-areas>
  <div class="container">
    <div class="areas__top">
      <div class="areas__copy reveal">
        <span class="eyebrow eyebrow--red">Service areas</span>
        <h2 class="display h-sm">Hood cleaning near you.</h2>
        <p class="lead" style="font-size:14px;max-width:320px">Based in West Milton, Ohio, our crews serve commercial kitchens across five Midwest states.</p>
        <form class="area-check" novalidate>
          <label class="select"><span class="sr-only">Choose your state</span>
            {icon('pin')}
            <select name="state"><option value="">Select your state</option>{opts}<option value="other">Another state</option></select>
            {icon('chevron-down')}
          </label>
          <button class="btn btn--red" type="submit">Check your area</button>
        </form>
        <p class="area-result" role="status" aria-live="polite"></p>
      </div>
      <div class="map">
        {svg}
        <div class="map__hq" style="left:calc({hl:.1f}% - 190px);top:calc({ht:.1f}% - 28px)">{icon('pin-plus')}<div><strong>Headquarters</strong><small>West Milton, Ohio</small></div></div>
      </div>
    </div>
    <div class="state-grid">
      {cards}
      <div class="state-card state-card--hq">
        <span class="state-card__icon">{icon('pin-plus')}</span>
        <h3>Headquarters</h3>
        <p>{BIZ['street']},<br>{BIZ['city']}</p>
        <p><a href="{BIZ['tollfree_href']}">{BIZ['tollfree']}</a><br><a href="{BIZ['phone_href']}">{BIZ['phone']}</a></p>
      </div>
    </div>
  </div>
</section>"""


def faq_section(items=None, title="Hood cleaning questions, answered.", soft=True, more=True):
    items = items or HOME_FAQ
    d = "".join(
        f'<details{" open" if i == 0 else ""}><summary>{q}<span class="pm" aria-hidden="true"></span></summary><div class="faq__a">{ans}</div></details>'
        for i, (q, ans) in enumerate(items)
    )
    more_html = f'<div class="faq-cta"><a class="btn btn--blue" href="{u("contact/")}">Ask us a question {icon("arrow")}</a></div>' if more else ""
    return f"""<section class="section {'section--softer' if soft else ''}" id="faq">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow eyebrow--red">FAQs</span>
      <h2 class="display h-sm">{title}</h2>
    </div>
    <div class="faq">{d}</div>
    {more_html}
  </div>
</section>"""


SHORT_STATES = ["Ohio", "Indiana", "Kentucky", "Michigan", "West Virginia", "Other"]


def quote_form(prefix, title="Get a free quote", sub="First service free for new compliance programs.", service=None):
    """Short quote form used in the home hero and the closing CTA section.
    Front-end only: validation and success state, no data is sent."""
    states = "".join(f"<option>{x}</option>" for x in SHORT_STATES)
    opts = "".join(
        f'<option value="{s["slug"]}"{" selected" if s["slug"] == service else ""}>{s["name"]}</option>' for s in SERVICES
    ) + '<option value="not-sure">Not sure yet</option>'
    f = prefix
    return f"""<div class="form-card form-card--compact">
  <form class="js-quote" novalidate>
    <h2 class="qf-title">{title}</h2>
    <p class="qf-sub">{sub}</p>
    <div class="form-grid form-grid--compact">
      <div class="field"><label for="{f}-name">Full name *</label><input id="{f}-name" name="name" autocomplete="name" required><span class="err">Please enter your name.</span></div>
      <div class="field"><label for="{f}-biz">Business name *</label><input id="{f}-biz" name="business" autocomplete="organization" required><span class="err">Please enter your business name.</span></div>
      <div class="field"><label for="{f}-phone">Phone *</label><input id="{f}-phone" name="phone" type="tel" autocomplete="tel" required><span class="err">Please enter a valid phone number.</span></div>
      <div class="field"><label for="{f}-email">Email *</label><input id="{f}-email" name="email" type="email" autocomplete="email" required><span class="err">Please enter a valid email.</span></div>
      <div class="field"><label for="{f}-state">State *</label><select id="{f}-state" name="state" required><option value="">Select</option>{states}</select><span class="err">Please choose a state.</span></div>
      <div class="field"><label for="{f}-svc">Service *</label><select id="{f}-svc" name="service" required><option value="">Select</option>{opts}</select><span class="err">Please choose a service.</span></div>
    </div>
    <button class="btn btn--red btn--block" type="submit">Request My Free Quote {icon('arrow')}</button>
    <small class="qf-note">No obligation. We reply within one business day.</small>
  </form>
  <div class="form-success" role="status" aria-live="polite">
    <div class="ok">{icon('check', width=2.4)}</div>
    <h2 class="qf-title">Thanks. We have your request.</h2>
    <p>We will contact you within one business day to schedule your free site survey. Need us sooner? Call {BIZ['phone']}.</p>
    <div class="btn-row" style="justify-content:center;margin-top:16px"><button class="btn btn--outline" type="button" data-reset-form>Send another request</button></div>
  </div>
</div>"""


def cta_band(title="Next fire inspection coming up?", text="Book a free site survey today and get a written quote for your kitchen exhaust cleaning.", primary=True, form=True, service=None):
    if form:
        ticks = "".join(f"<li>{icon('check-circle')}{t}</li>" for t in ["Free site survey and written quote", "First service free for new programs", "NFPA 96 compliant, IKECA certified"])
        return f"""<section class="cta-band cta-band--form" id="request-quote">
  <div class="container">
    <div class="cta-band__copy">
      <span class="eyebrow" style="color:#FFD9D9">Request a quote</span>
      <h2>{title}</h2><p>{text}</p>
      <ul class="cta-band__ticks">{ticks}</ul>
      <div class="btn-row">{btn_call("btn--ghost")}</div>
    </div>
    {quote_form("bq", "Request a quote", "Tell us a little about your kitchen. It takes under a minute.", service)}
  </div>
</section>"""
    btns = (btn_quote(cls="btn--white") if primary else "") + btn_call("btn--ghost")
    return f"""<section class="cta-band">
  <div class="container">
    <div><h2>{title}</h2><p>{text}</p></div>
    <div class="btn-row">{btns}</div>
  </div>
</section>"""


def filtershine_callout():
    return f"""<div class="callout reveal">
  <img src="{a('img/logos/filtershine-midwest.png')}" alt="FilterShine Midwest" loading="lazy" width="170" height="90">
  <div><h3>Filter exchange powered by FilterShine Midwest</h3><p>Liberty Services partners with FilterShine Midwest to provide filter exchange services for our clients. Clean stainless steel filters, delivered on schedule.</p></div>
  <a class="btn btn--blue" href="{u('about-filtershine/')}">About FilterShine {icon('arrow')}</a>
</div>"""


def feature_grid(items, cols=3):
    cls = "feature-grid feature-grid--4" if cols == 4 else "feature-grid"
    return f'<div class="{cls}">' + "".join(
        f'<div class="feature reveal"><span class="feature__icon">{icon(i)}</span><h3>{t}</h3><p>{d}</p></div>' for i, t, d in items
    ) + "</div>"


def steps(items):
    cls = "steps steps--3" if len(items) == 3 else "steps"
    return f'<div class="{cls}">' + "".join(
        f'<div class="step reveal"><span class="step__n">0{i + 1}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(items)
    ) + "</div>"


def checklist(items, cls=""):
    return f'<ul class="checklist {cls}">' + "".join(f"<li>{icon('check-circle')}<span>{x}</span></li>" for x in items) + "</ul>"

"""Page bodies for every page in the sitemap."""

from components import (
    CTX, u, a, page, page_hero, btn_quote, btn_call, float_card, trust_strip, logo_strip,
    services_section, service_cards, other_services, nfpa_section, process_section, proof_section,
    industries_section, why_section, testimonials_section, compliance_section, service_areas_section,
    faq_section, cta_band, filtershine_callout, feature_grid, steps, checklist, testimonials_block,
)
from data import BIZ, SERVICES, POSTS, SERVICE_FAQ, HOME_FAQ
from icons import icon

SITE = "Liberty Services Inc."


# ======================================================================= HOME

HERO_SLIDES = [
    {
        "label": "Hood cleaning", "eyebrow": "Trusted by kitchens in the Midwest",
        "title": "Commercial kitchen cleaning built for safer operations",
        "text": "You focus on customers. We handle grease. For over 20 years, restaurants in Dayton and the Midwest have trusted Liberty Services for exhaust cleaning and grease containment.",
        "img": "photos/hood-hero.jpg", "thumb": "photos/liberty-hood-cleaning.jpg",
        "card": ("shield", "Inspection-ready, every visit.", "Certified service, before-and-after photos and clear reports."),
        "badge": ("star", "First service free", "Start your compliance program risk-free."),
        "primary": None,
    },
    {
        "label": "Filter exchange", "eyebrow": "Filter exchange",
        "title": "Clean filters. Every visit. Zero scrubbing.",
        "text": "Professionally cleaned stainless steel filters swapped in on schedule, so your staff never scrubs a filter again and far less grease goes down your drains.",
        "img": "photos/chef-heatlamps.jpg", "thumb": "photos/liberty-clean-hood-filters.jpg",
        "card": ("filter", "Better airflow, lower risk.", "Clean filters are your first line of defense against fire."),
        "badge": ("leaf", "Cleaner water", "Grease captured before it reaches drains and waterways."),
        "primary": ("Explore Filter Exchange", "services/filter-exchange/"),
    },
    {
        "label": "Grease management", "eyebrow": "Grease management",
        "title": "Keep grease off your roof and out of your drains",
        "text": "Containment for exhaust systems, rooftops, drains and grease traps that protects your facility and helps keep you on the right side of EPA codes.",
        "img": "photos/line-flame.jpg", "thumb": "photos/liberty-grease-containment.jpg",
        "card": ("droplet", "Collect. Contain. Drain.", "Systems that hold grease and let rainwater run off."),
        "badge": ("shield", "Protect your roof", "Stop grease from breaking down roofing materials."),
        "primary": ("Explore Grease Management", "services/grease-management/"),
    },
    {
        "label": "Rooftop services", "eyebrow": "Rooftop services",
        "title": "Rooftop exhaust fans that keep running",
        "text": "Exhaust fan service and repairs, including belts, motors, hinge kits, access panels and cleanup, so your equipment stays reliable and your roof stays protected.",
        "img": "photos/technician-work.jpg", "thumb": "photos/technician.jpg",
        "card": ("wrench", "Repairs on the spot.", "Belts, motors and bearings handled while we are on the roof."),
        "badge": ("fan", "Hinge kits installed", "Safe, code-ready access to every exhaust fan."),
        "primary": ("Explore Rooftop Services", "services/rooftop-services/"),
    },
]


def home_hero():
    slides, dots = [], []
    for i, s in enumerate(HERO_SLIDES):
        tag = "h1" if i == 0 else "h2"
        primary = btn_quote() if not s["primary"] else btn_quote(s["primary"][0], target=s["primary"][1])
        ci, ct, cd = s["card"]
        slides.append(f"""<div class="hero__slide{' is-active' if i == 0 else ''}" role="group" aria-roledescription="slide" aria-label="{i + 1} of {len(HERO_SLIDES)}: {s['label']}">
  <div class="container hero__inner">
    <div class="hero__copy">
      <span class="eyebrow eyebrow--rule">{s['eyebrow']}</span>
      <{tag} class="display h-xl">{s['title']}</{tag}>
      <p>{s['text']}</p>
      <div class="btn-row">{primary}{btn_call()}</div>
    </div>
    <div class="hero__media">
      <div class="hero__img"><img src="{a(s['img'])}" alt="" width="590" height="550"{'' if i == 0 else ' loading="lazy"'}></div>
      <div class="hero__cards">
        <div class="hero__cardrow">
          <div class="hero__thumb"><img src="{a(s['thumb'])}" alt="" loading="lazy"></div>
          <div class="float-card float-card--col"><span class="fc-icon">{icon(ci)}</span><div><h3>{ct}</h3><p>{cd}</p></div></div>
        </div>
        {float_card(*s['badge'])}
      </div>
    </div>
  </div>
</div>""")
        dots.append(f'<button class="hero__dot{" is-active" if i == 0 else ""}" type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-label="Show {s["label"]}"><span class="num">0{i + 1}</span><span class="lbl">0{i + 1} {s["label"]}</span><span class="bar"></span></button>')
    return f"""<section class="hero" data-hero data-mode="slider" aria-roledescription="carousel" aria-label="Liberty Services highlights">
  <div class="hero__bg"></div>
  <div class="hero__track">{''.join(slides)}</div>
  <div class="hero__controls">
    <div class="container">
      <div class="hero__dots" role="tablist" aria-label="Choose a slide">{''.join(dots)}</div>
      <div class="hero__arrows">
        <button class="hero__arrow hero__arrow--prev" type="button" aria-label="Previous slide">{icon('arrow-left')}</button>
        <button class="hero__arrow hero__arrow--next" type="button" aria-label="Next slide">{icon('arrow')}</button>
      </div>
    </div>
  </div>
</section>"""


def home():
    body = "\n".join([
        home_hero(), trust_strip(), logo_strip(), services_section(), nfpa_section(), process_section(),
        proof_section(), industries_section(), why_section(), compliance_section(), service_areas_section(),
        faq_section(), cta_band(),
    ])
    return page(f"Commercial Kitchen Hood Cleaning | {SITE}",
                "Certified commercial kitchen hood cleaning, filter exchange, grease management and rooftop services across Ohio, Indiana, Kentucky, Michigan and West Virginia.",
                body, proto=True)


# ====================================================================== ABOUT

def about_liberty():
    hero = page_hero(
        [("About", "about-liberty-services/"), ("Liberty Services", "about-liberty-services/")],
        "About Liberty Services",
        'A certified hood cleaning and <span class="accent">grease containment</span> company',
        "For over two decades, Liberty Services has kept commercial and restaurant kitchen exhaust systems clean, safe and inspection-ready across the Midwest.",
        img="photos/chef-cooking.jpg", img_alt="Chef cooking on a commercial line",
        badge=float_card("award", "IKECA certified", "Bonded, insured and an NFPA member."),
    )
    story = f"""<section class="section">
  <div class="container split">
    <div class="media-frame reveal"><img src="{a('photos/liberty-hood-cleaning.jpg')}" alt="Clean commercial kitchen hood and cooking line" loading="lazy"><span class="media-frame__tag">Over two decades in business</span></div>
    <div class="section-head reveal">
      <span class="eyebrow">Who we are</span>
      <h2 class="display h-md">We clean more than<br><span class="accent">what is visible.</span></h2>
      <p class="lead">Liberty Services Inc. is a certified hood and duct cleaning company with over two decades of experience cleaning commercial and restaurant kitchen exhaust systems.</p>
      <p class="lead">We clean each kitchen exhaust system correctly and thoroughly by cleaning the entire fan, ductwork and hood to bare metal. Our certified technicians are knowledgeable, professional and understand the responsibility they have to clean your system completely and to report any deficiencies.</p>
      <div style="margin-top:12px">{checklist(['Complete cleaning of your exhaust system', 'Flexible scheduling, including after hours', 'Competitive pricing with written quotes', 'One partner for hood, filter, grease and rooftop service'])}</div>
      <div class="btn-row" style="margin-top:20px">{btn_quote()}</div>
    </div>
  </div>
</section>"""
    stats = """<section class="section section--navy section--tight">
  <div class="container">
    <div class="feature-grid feature-grid--4" style="margin-top:0">
      <div class="big-stat reveal"><strong>20+</strong><span>Years cleaning commercial kitchen exhaust systems</span></div>
      <div class="big-stat reveal"><strong>5</strong><span>States served: OH, IN, KY, MI and WV</span></div>
      <div class="big-stat reveal"><strong>100%</strong><span>Of jobs photo-documented before and after</span></div>
      <div class="big-stat reveal"><strong>NFPA 96</strong><span>Met or exceeded on every service</span></div>
    </div>
  </div>
</section>"""
    why = f"""<section class="section section--softer">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow eyebrow--red">Why choose Liberty Services</span>
      <h2 class="display h-md">Established. Certified.<br><span class="accent">Accountable.</span></h2>
      <p class="lead">Everything we do is built so you can prove your kitchen is safe, any time someone asks.</p>
    </div>
    {feature_grid([
        ('award', 'IKECA certification', 'Our technicians are trained to International Kitchen Exhaust Cleaning Association standards.'),
        ('shield', 'NFPA member', 'We are members of the National Fire Protection Association and clean to meet or exceed NFPA 96.'),
        ('clipboard', 'Bonded & insured', 'Every job is fully covered, so your property and your business are protected.'),
        ('file', 'Electronic reporting', 'A fully electronic reporting system with customer access to every report and photo.'),
        ('gps', 'GPS confirmations', 'GPS confirmation of technician arrival and completion on every visit.'),
        ('refresh', 'ServiceTrade powered', 'On-the-spot deficiency reporting, easy scheduling and uploads to ServiceChannel and Corrigo.'),
    ])}
  </div>
</section>"""
    fs = f'<section class="section section--tight"><div class="container">{filtershine_callout()}</div></section>'
    body = "\n".join([hero, logo_strip(), story, stats, why, nfpa_section(soft=False, title="We meet or exceed NFPA 96 standards."), fs,
                      service_areas_section(soft=True), testimonials_section(soft=False), cta_band()])
    return page(f"About Liberty Services | {SITE}",
                "Liberty Services is a certified hood and duct cleaning company with over two decades of experience cleaning commercial kitchen exhaust systems in the Midwest.", body)


def about_filtershine():
    hero = page_hero(
        [("About", "about-liberty-services/"), ("FilterShine", "about-filtershine/")],
        "About FilterShine",
        'Clean filters,<br><span class="accent">swapped on schedule.</span>',
        "With FilterShine filter exchange services, certified technicians remove grease-laden filters from your kitchen exhaust system and replace them with completely clean stainless steel filters.",
        img="photos/chef-heatlamps.jpg", img_alt="Chef working under clean kitchen hood",
        badge=f'<div class="float-card" style="align-items:center"><img src="{a("img/logos/filtershine-midwest.png")}" alt="FilterShine Midwest" style="width:110px;height:auto"><div><h3>Our exchange partner</h3><p>Cleaned down to bare metal.</p></div></div>',
    )
    partner = f"""<section class="section">
  <div class="container split">
    <div class="section-head reveal">
      <span class="eyebrow">The partnership</span>
      <h2 class="display h-md">Liberty Services <span class="accent">+ FilterShine Midwest</span></h2>
      <p class="lead">Liberty Services partners with FilterShine Midwest to provide filter exchange services for our clients. You get one schedule and one point of contact for your hoods, filters, grease and rooftop equipment.</p>
      <p class="lead">The dirty filters are taken back to the FilterShine facility, where they are thoroughly cleaned inside and out, down to bare metal. By using FilterShine for filter exchange, you can lower operating costs while implementing fats, oils and grease (FOG) best practices.</p>
      <div class="btn-row" style="margin-top:16px">{btn_quote('Start Filter Exchange', target='services/filter-exchange/')}<a class="link-arrow" href="{BIZ['filtershine']}" target="_blank" rel="noopener">Visit FilterShine Midwest {icon('arrow')}</a></div>
    </div>
    <div class="media-frame reveal"><img src="{a('photos/liberty-filter-exchange.jpg')}" alt="Stainless steel hood filters installed in a commercial kitchen hood" loading="lazy"><span class="media-frame__tag">Stainless steel filters</span></div>
  </div>
</section>"""
    how = f"""<section class="section section--softer">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow eyebrow--red">How it works</span>
      <h2 class="display h-md">Three steps.<br><span class="accent">No scrubbing.</span></h2>
    </div>
    {steps([
        ('Swap', 'A certified technician removes your grease-laden filters and installs clean stainless steel replacements. It takes minutes, not a closing shift.'),
        ('Clean to bare metal', 'Dirty filters go back to the FilterShine facility and are cleaned inside and out, down to bare metal, without grease going down your drains.'),
        ('Repeat on schedule', 'Exchanges repeat on a schedule matched to your cooking volume, so clean filters are always in place.'),
    ])}
  </div>
</section>"""
    reduce = f"""<section class="section">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="section-head"><span class="eyebrow">The benefits</span><h2 class="display h-md">With FilterShine,<br><span class="accent">you can reduce:</span></h2></div>
      <p class="lead">Lower operating costs and a safer kitchen, with FOG best practices built into your routine.</p>
    </div>
    {feature_grid([
        ('dollar', 'Labor costs', 'No more end-of-night filter scrubbing for your team.'),
        ('box', 'Cleaning supply costs', 'Skip the caustic degreasers and soak tanks.'),
        ('shield', 'Liability', 'Clean filters lower the risk of a grease fire spreading into ductwork.'),
        ('wind', 'Grease-laden pollutants', 'Keep grease out of the air, your drains and local waterways.'),
        ('health', 'Health risks', 'Less exposure to harsh chemicals and greasy surfaces.'),
        ('alert', 'Staff injuries', 'Fewer burns, cuts and slips from handling hot, heavy filters.'),
    ])}
  </div>
</section>"""
    water = f"""<section class="section section--navy">
  <div class="container split">
    <div class="section-head reveal">
      <span class="eyebrow eyebrow--light">Cleaner kitchens. Cleaner water.</span>
      <h2 class="display h-lg">Grease stays out<br>of your drains.</h2>
      <p class="lead" style="max-width:420px">When filters are cleaned on site, the grease ends up down the drain. Off-site cleaning captures it before it reaches your plumbing, grease trap and local waterways.</p>
      <div class="btn-row" style="margin-top:16px">{btn_quote('Get a Filter Exchange Quote', target='contact/?service=filter-exchange')}</div>
    </div>
    <div class="feature-grid" style="grid-template-columns:1fr 1fr;margin-top:0">
      <div class="big-stat reveal"><strong>60-70%</strong><span>Less grease going down your drains with off-site filter cleaning</span></div>
      <div class="big-stat reveal"><strong>0</strong><span>Caustic degreasers needed in your kitchen</span></div>
      <div class="big-stat reveal"><strong>FOG</strong><span>Fats, oils and grease best practices built in</span></div>
      <div class="big-stat reveal"><strong>Bare metal</strong><span>The cleaning standard for every filter</span></div>
    </div>
  </div>
</section>"""
    body = "\n".join([hero, partner, how, reduce, water, testimonials_section(soft=True),
                      cta_band("Ready to stop scrubbing filters?", "Set up a filter exchange schedule and see the difference in your airflow, drains and closing routine.")])
    return page(f"About FilterShine Filter Exchange | {SITE}",
                "Liberty Services partners with FilterShine Midwest for commercial kitchen hood filter exchange. Clean stainless steel filters on schedule, cleaned to bare metal.", body)


# =================================================================== SERVICES

def services_index():
    hero = page_hero(
        [("Services", "services/")], "Our services",
        'Four services. One partner. <span class="accent">From hood to roof.</span>',
        "Allow Liberty Services to help you keep your commercial kitchen in compliance with EPA and fire codes. For over 20 years, we have been trusted to do just that throughout Ohio, Indiana, Kentucky, Michigan and West Virginia.",
        img="photos/line-flame.jpg", img_alt="High-volume commercial cooking line",
        badge=float_card("calendar", "Schedule your service today", "One partner for every system in your kitchen."),
    )
    rows = []
    for i, s in enumerate(SERVICES):
        rows.append(f"""<article class="service-row reveal" id="{s['slug']}">
  <div class="service-row__media"><img src="{a(s['hero_img'])}" alt="{s['name']}" loading="lazy"></div>
  <div class="service-row__body">
    <span class="service-card__num">0{i + 1} / {s['name'].upper()}</span>
    <h3>{s['name']}</h3>
    <p>{s['summary']}</p>
    {checklist(s['bullets'], 'checklist--2')}
    <div class="btn-row" style="margin-top:8px"><a class="btn btn--blue" href="{u('services/' + s['slug'] + '/')}">Learn more {icon('arrow')}</a><a class="link-arrow" href="{u('contact/')}?service={s['slug']}">Request a quote {icon('arrow')}</a></div>
  </div>
</article>""")
    listing = f"""<section class="section">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="section-head"><span class="eyebrow">What we do</span><h2 class="display h-md">Complete kitchen care,<br><span class="accent">one schedule.</span></h2></div>
      <p class="lead">Choose a single service or bundle all four into one recurring compliance program.</p>
    </div>
    <div class="service-rows">{''.join(rows)}</div>
  </div>
</section>"""
    body = "\n".join([hero, trust_strip(), listing,
                      compliance_section("Stay clean. Stay safe. Stay compliant.", "Recurring compliance programs"),
                      process_section(), industries_section(soft=True), testimonials_section(soft=False), faq_section(), cta_band()])
    return page(f"Commercial Kitchen Exhaust Services | {SITE}",
                "Hood cleaning, filter exchange, grease management and rooftop exhaust fan services for commercial kitchens in OH, IN, KY, MI and WV.", body)


SERVICE_PAGES = {
    "hood-cleaning": {
        "eyebrow": "Kitchen hood cleaning",
        "title": 'Hood cleaning, <span class="accent">to bare metal.</span>',
        "intro": "Grease buildup in kitchen hood systems puts you, your employees and your business at risk of injury and property damage from kitchen fires. We clean your entire system, from the fan to the hood.",
        "badge": ("shield", "NFPA 96 compliant", "Photo report and certificate every visit."),
        "overview_title": 'We clean more than <span class="accent">inspectors can see.</span>',
        "overview": [
            "Keeping your hood system clean to bare metal is one of the most important things you can do to protect your kitchen. Unfortunately, in many kitchens there are not enough hours in the day, and hood cleaning slips to the bottom of the to-do list.",
            "Rather than worry whether your staff have the time or tools to clean to NFPA 96 standards, set up regular, complete cleanings with Liberty Services. Our certified technicians clean your hoods and help you reduce the risks of flammable grease buildup.",
        ],
        "img": "photos/liberty-hood-cleaning.jpg", "tag": "Fan to hood",
        "included_title": "Our hood cleaning includes",
        "included": ["Exhaust fans", "Vertical ducts", "Horizontal ducts", "Plenum", "Inside & outside of hood system", "Inside access panels", "Before & after photos", "Dated service label & certificate"],
        "benefits": [
            ("flame", "Reduce fire risk", "Grease in all forms is highly flammable. Removing it from the full system stops a flare-up from spreading."),
            ("clipboard", "Pass inspections", "Clean to NFPA 96 with a dated label and photo report ready for your fire marshal."),
            ("shield", "Protect your coverage", "Documented cleanings help you meet insurer and landlord requirements."),
            ("wind", "Better airflow", "Clean ducts and fans pull smoke and heat out of the kitchen more effectively."),
            ("moon", "No downtime", "We work after close or before open, so service never interrupts your line."),
            ("camera", "Proof of every clean", "GPS-stamped photos and deficiency notes stored in your customer portal."),
        ],
        "extra": "nfpa",
    },
    "filter-exchange": {
        "eyebrow": "Hood filter exchange",
        "title": 'Filter exchange, <span class="accent">on your schedule.</span>',
        "intro": "Clean filters are your first line of defense against a kitchen fire. We swap your grease-laden filters for professionally cleaned stainless steel replacements, on a schedule that fits your volume.",
        "badge": ("droplet", "Up to 60-70% less grease", "kept out of your drains with off-site cleaning."),
        "overview_title": 'Clean filters <span class="accent">without the cleanup.</span>',
        "overview": [
            "Filters need to be cleaned on a regular schedule and cleaned down to bare metal. Many kitchens do not have the time or staff to keep up, and when filters are cleaned on the premises, the resulting grease ends up down the drain.",
            "With filter exchange, your filters are cleaned off site. That lowers the amount of grease going down your drain by up to 60-70%, saves your team hours every week and keeps airflow where it should be.",
        ],
        "img": "photos/liberty-clean-hood-filters.jpg", "tag": "Stainless steel filters",
        "included_title": "Benefits of filter exchange",
        "included": ["Reduce labor & cleaning costs", "Conserve energy & water", "Reduce drain line blockages", "Reduce grease trap servicing", "Improve air flow", "Reduce staff injuries", "Reduce risk of property damage", "Reduce sanitary sewer overflows", "Helps with EPA compliance", "Caustic degreaser no longer needed"],
        "benefits": [
            ("refresh", "Scheduled swaps", "Weekly, bi-weekly or monthly exchanges matched to your cooking volume."),
            ("leaf", "Cleaner water", "Grease is captured off site instead of washing into drains and waterways."),
            ("dollar", "Lower costs", "Less labor, fewer chemicals and fewer grease trap pump-outs."),
            ("wind", "Better airflow", "Clean filters let your exhaust system work the way it was designed to."),
            ("users", "Safer staff", "No more handling hot, heavy, greasy filters at the end of a shift."),
            ("flame", "Lower fire risk", "Clean filters keep grease from collecting in your ductwork."),
        ],
        "extra": "filtershine",
    },
    "grease-management": {
        "eyebrow": "Grease management & containment",
        "title": 'Grease management, <span class="accent">roof to drain.</span>',
        "intro": "When grease builds up in kitchen exhaust systems, it can make its way to your roof and your drains if it is not properly contained. We assess your system and install containment that protects your facility.",
        "badge": ("droplet", "Collect. Contain. Drain.", "Systems that hold grease and let rainwater run off."),
        "overview_title": 'Once grease reaches your roof, <span class="accent">it costs you.</span>',
        "overview": [
            "Uncontained grease can cause extensive damage to your roof, make it deteriorate faster and pose a fire hazard. When it rains or snow melts, that grease runs off into the sewer system and can put you in violation of EPA codes.",
            "Liberty Services certified technicians assess where your exhaust system meets your roof and install a grease containment system that collects and contains grease while allowing rainwater to drain and run off.",
        ],
        "img": "photos/liberty-grease-containment.jpg", "tag": "Exhaust to roof",
        "included_title": "Uncontained grease can",
        "included": ["Cause extensive roof damage", "Make your roof deteriorate", "Pose a fire hazard", "Run off when it rains or snow melts", "Seep into the sewer system", "Put you in violation of EPA codes"],
        "benefits": [
            ("box", "Collect grease", "Containment units capture grease where it leaves the exhaust fan."),
            ("shield", "Contain grease", "Grease is held in place instead of spreading across your roof."),
            ("droplet", "Let water drain", "Rainwater and snowmelt drain away while grease stays contained."),
            ("roof", "Protect your roof", "Prevent grease from breaking down roofing materials and seams."),
            ("leaf", "Support EPA compliance", "Reduce runoff of fats, oils and grease into storm drains and sewers."),
            ("refresh", "Serviced with your cleaning", "We replace media and clean units on the same visit as your hood cleaning."),
        ],
        "extra": "products",
    },
    "rooftop-services": {
        "eyebrow": "Rooftop exhaust services",
        "title": 'Rooftop services that <span class="accent">keep fans running.</span>',
        "intro": "Your exhaust fan is the hardest-working part of your kitchen ventilation. We service and repair rooftop exhaust fans, install hinge kits and access panels, and leave your roof clean and protected.",
        "badge": ("wrench", "Repairs while we are on the roof", "Belts, motors, bearings and hinge kits."),
        "overview_title": 'When the fan stops, <span class="accent">the kitchen stops.</span>',
        "overview": [
            "A worn belt or failing motor can shut down your exhaust and your cooking line with it. Grease-loaded fans also run out of balance, which wears out bearings and shortens equipment life.",
            "Our technicians inspect your rooftop equipment every time we clean, flag issues before they become failures and handle repairs on the spot when possible. We also install the hinge kits and access panels NFPA 96 calls for, so every future cleaning is safe and complete.",
        ],
        "img": "photos/technician.jpg", "tag": "On the roof",
        "included_title": "Rooftop services include",
        "included": ["Exhaust fan inspection", "Belt replacement", "Motor & bearing repair", "Exhaust fan hinge kits", "Access panels & doors", "Grease containment systems", "Fan cleaning", "Roof cleanup"],
        "benefits": [
            ("zap", "Fewer breakdowns", "Catch worn belts, noisy bearings and failing motors before they shut you down."),
            ("settings", "Repairs on the spot", "Common parts replaced during the same visit whenever possible."),
            ("door", "Safe access", "Hinge kits and access panels make fan cleaning safe and code-ready."),
            ("roof", "Protected roofs", "Containment and cleanup keep grease from damaging your roof."),
            ("file", "Documented condition", "Photos and deficiency notes on fan condition after every visit."),
            ("calendar", "One schedule", "Rooftop service bundled with your hood cleaning and filter exchange."),
        ],
        "extra": "rooftop",
    },
}


def service_page(slug):
    s = next(x for x in SERVICES if x["slug"] == slug)
    d = SERVICE_PAGES[slug]
    hero = page_hero(
        [("Services", "services/"), (s["name"], f"services/{slug}/")], d["eyebrow"], d["title"], d["intro"],
        img=s["hero_img"], img_alt=s["name"], badge=float_card(*d["badge"]),
    )
    overview = f"""<section class="section">
  <div class="container split">
    <div class="section-head reveal">
      <span class="eyebrow">Overview</span>
      <h2 class="display h-md">{d['overview_title']}</h2>
      {''.join(f'<p class="lead">{p}</p>' for p in d['overview'])}
      <div class="btn-row" style="margin-top:16px">{btn_quote('Schedule Your Service', target='contact/?service=' + slug)}{btn_call('btn--outline')}</div>
    </div>
    <div class="media-frame reveal"><img src="{a(d['img'])}" alt="{s['name']}" loading="lazy"><span class="media-frame__tag">{d['tag']}</span></div>
  </div>
</section>"""
    included = f"""<section class="section section--navy section--tight">
  <div class="container split split--wide-right">
    <div class="section-head reveal">
      <span class="eyebrow eyebrow--light">{s['name']}</span>
      <h2 class="display h-md">{d['included_title']}</h2>
    </div>
    <div class="reveal">{checklist(d['included'], 'checklist--2 checklist--light')}</div>
  </div>
</section>"""
    benefits = f"""<section class="section section--softer">
  <div class="container">
    <div class="section-head section-head--center">
      <span class="eyebrow eyebrow--red">Why it matters</span>
      <h2 class="display h-md">What you get with Liberty</h2>
    </div>
    {feature_grid(d['benefits'])}
  </div>
</section>"""
    extra = ""
    if d["extra"] == "nfpa":
        extra = nfpa_section(soft=False)
    elif d["extra"] == "filtershine":
        extra = f'<section class="section section--tight"><div class="container">{filtershine_callout()}</div></section>'
    elif d["extra"] == "products":
        products = [("box", "Exhaust fan interceptors"), ("box", "Grease boxes"), ("droplet", "Grease gutters"), ("roof", "Roof guardian"),
                    ("shield", "Curb deflector"), ("settings", "Fan hinges"), ("door", "Access doors")]
        extra = f"""<section class="section">
  <div class="container split split--wide-right">
    <div class="section-head reveal"><span class="eyebrow">Products</span><h2 class="display h-md">We sell <span class="accent">and install</span></h2><p class="lead">Every system is matched to your fan type, roof material and cooking volume.</p></div>
    <ul class="tag-list reveal">{''.join(f'<li>{icon(i)}{t}</li>' for i, t in products)}</ul>
  </div>
</section>"""
    elif d["extra"] == "rooftop":
        extra = f"""<section class="section">
  <div class="container">
    <div class="section-head section-head--center"><span class="eyebrow eyebrow--red">How it works</span><h2 class="display h-md">Rooftop service in four steps</h2></div>
    {steps([
        ('Inspect', 'We check fan condition, belts, motor, bearings, hinges, access and containment.'),
        ('Report', 'You get photos and a clear list of deficiencies with repair recommendations.'),
        ('Repair', 'Approved repairs are handled on the spot or scheduled with your next visit.'),
        ('Protect', 'We clean up the roof and service containment so grease stays where it belongs.'),
    ])}
  </div>
</section>"""
    body = "\n".join([
        hero, trust_strip(), overview, included, benefits, extra,
        f'<section class="section section--soft"><div class="container">{testimonials_block()}</div></section>',
        other_services(slug),
        faq_section(SERVICE_FAQ[slug], title=f"{s['name']} questions, answered.", soft=False),
        cta_band("Schedule your service today", "One partner for hood cleaning, filter exchange, grease management and rooftop services. Start with a free site survey."),
    ])
    return page(f"{s['name']} | Commercial Kitchen {s['name']} | {SITE}", s["summary"], body)


# ======================================================================= BLOG

def post_card(p, featured=False):
    href = u(f"blogs/{p['slug']}/")
    meta = f'<div class="post-meta"><span class="cat">{p["cat"]}</span><span>{p["date"]}</span><span>{p["read"]}</span></div>'
    if featured:
        return f"""<article class="post-featured reveal">
  <a class="post-featured__media" href="{href}" tabindex="-1" aria-hidden="true"><img src="{a(p['img'])}" alt="" loading="lazy"></a>
  <div class="post-featured__body">
    <span class="eyebrow eyebrow--red">Featured guide</span>
    <h2><a href="{href}">{p['title']}</a></h2>
    {meta}
    <p>{p['excerpt']}</p>
    <div><a class="btn btn--blue" href="{href}">Read the guide {icon('arrow')}</a></div>
  </div>
</article>"""
    return f"""<a class="post-card reveal" href="{href}" data-cat="{p['cat']}">
  <div class="post-card__media"><img src="{a(p['img'])}" alt="" loading="lazy"></div>
  <div class="post-card__body">
    {meta}
    <h3>{p['title']}</h3>
    <p>{p['excerpt']}</p>
    <span class="link-arrow">Read article {icon('arrow')}</span>
  </div>
</a>"""


def blog_index():
    hero = page_hero([("Blog", "blogs/")], "Blog & news", 'Kitchen safety, <span class="accent">made simple.</span>',
                     "Practical guides on NFPA 96 compliance, fire safety and running a cleaner commercial kitchen, from the Liberty Services team.",
                     compact=True, ctas=False)
    cats = sorted({p["cat"] for p in POSTS})
    chips = '<button class="chip is-active" type="button" data-filter="all" aria-pressed="true">All articles</button>' + "".join(
        f'<button class="chip" type="button" data-filter="{c}" aria-pressed="false">{c}</button>' for c in cats)
    listing = f"""<section class="section" style="padding-top:56px">
  <div class="container">
    {post_card(POSTS[0], featured=True)}
    <div class="blog-filters" role="group" aria-label="Filter articles by topic">{chips}</div>
    <div class="post-grid">{''.join(post_card(p) for p in POSTS)}</div>
  </div>
</section>"""
    body = "\n".join([hero, listing, testimonials_section(soft=True), cta_band()])
    return page(f"Blog & News | {SITE}", "Guides on NFPA 96 compliance, kitchen fire safety, filter exchange and grease management from Liberty Services.", body)


def render_body(blocks):
    out = []
    for kind, val in blocks:
        if kind == "ul":
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in val) + "</ul>")
        else:
            out.append(f"<{kind}>{val}</{kind}>")
    return "\n".join(out)


def blog_post(p):
    hero = page_hero([("Blog", "blogs/"), (p["cat"], "blogs/")], p["cat"], p["title"], p["excerpt"], compact=True, ctas=False,
                     extra=f'<div class="post-meta"><span>By the Liberty Services team</span><span>{p["date"]}</span><span>{p["read"]}</span></div>')
    related = [x for x in POSTS if x["slug"] != p["slug"]][:3]
    svc_links = "".join(f'<li><a href="{u("services/" + s["slug"] + "/")}">{s["name"]} {icon("arrow")}</a></li>' for s in SERVICES)
    article = f"""<section class="section" style="padding-top:56px">
  <div class="container article">
    <article>
      <div class="article__cover"><img src="{a(p['img'])}" alt="" loading="lazy"></div>
      <div class="prose">{render_body(p['body'])}</div>
    </article>
    <aside class="sidebar" aria-label="Related">
      <div class="side-card side-card--red">
        <h3>First service free</h3>
        <p>Start your commercial kitchen compliance program risk-free with a free site survey.</p>
        <a class="btn btn--white" href="{u('contact/')}">Schedule Free Survey {icon('arrow')}</a>
      </div>
      <div class="side-card">
        <h3>Our services</h3>
        <ul class="side-links" style="margin-top:8px">{svc_links}</ul>
      </div>
      <div class="side-card">
        <h3>Talk to a technician</h3>
        <p>Questions about your schedule or system?</p>
        {btn_call('btn--outline')}
      </div>
    </aside>
  </div>
</section>"""
    more = f"""<section class="section section--softer">
  <div class="container">
    <div class="section-head section-head--split"><div class="section-head"><span class="eyebrow">Keep reading</span><h2 class="display h-sm">More from the blog</h2></div><a class="btn btn--outline" href="{u('blogs/')}">All articles {icon('arrow')}</a></div>
    <div class="post-grid">{''.join(post_card(x) for x in related)}</div>
  </div>
</section>"""
    body = "\n".join([hero, article, more, cta_band()])
    return page(f"{p['title']} | {SITE}", p["excerpt"], body)


# ==================================================================== CONTACT

def contact():
    hero = page_hero([("Contact", "contact/")], "Contact & quote", 'Get your <span class="accent">free site survey.</span>',
                     "Tell us about your kitchen and we will schedule a free site survey and send a written quote. Prefer to talk? Call us any time during business hours.",
                     compact=True, ctas=False,
                     extra=f'<div class="btn-row">{btn_call()}<a class="btn btn--ghost" href="{BIZ["tollfree_href"]}">Toll-free {BIZ["tollfree"]}</a></div>')
    svc_checks = "".join(f'<label class="check"><input type="checkbox" name="services" value="{s["slug"]}"> {s["name"]}</label>' for s in SERVICES)
    states = "".join(f"<option>{x}</option>" for x in ["Ohio", "Indiana", "Kentucky", "Michigan", "West Virginia", "Other"])
    form = f"""<section class="section" style="padding-top:56px">
  <div class="container contact">
    <div class="form-card" id="quote">
      <!-- Front-end prototype: validation and success state only. Connect to a form handler or CRM before launch. -->
      <form id="quote-form" novalidate>
        <h2>Request a quote</h2>
        <p>Fields marked * are required. We usually reply within one business day.</p>
        <div class="form-grid">
          <div class="field"><label for="f-name">Full name *</label><input id="f-name" name="name" autocomplete="name" required><span class="err">Please enter your name.</span></div>
          <div class="field"><label for="f-biz">Business name *</label><input id="f-biz" name="business" autocomplete="organization" required><span class="err">Please enter your business name.</span></div>
          <div class="field"><label for="f-email">Email *</label><input id="f-email" name="email" type="email" autocomplete="email" required><span class="err">Please enter a valid email address.</span></div>
          <div class="field"><label for="f-phone">Phone *</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" required><span class="err">Please enter a valid phone number.</span></div>
          <div class="field field--full"><label for="f-addr">Street address <span class="opt">(optional)</span></label><input id="f-addr" name="address" autocomplete="street-address"></div>
          <div class="field"><label for="f-city">City <span class="opt">(optional)</span></label><input id="f-city" name="city" autocomplete="address-level2"></div>
          <div class="field"><label for="f-state">State *</label><select id="f-state" name="state" required><option value="">Select a state</option>{states}</select><span class="err">Please choose a state.</span></div>
          <div class="field"><label for="f-type">Kitchen type</label><select id="f-type" name="kitchen"><option value="">Select one</option><option>Restaurant or bar</option><option>Multi-unit / franchise</option><option>School or university</option><option>Healthcare or senior living</option><option>Hotel or hospitality</option><option>Church or community kitchen</option><option>Other</option></select></div>
          <div class="field"><label for="f-loc">Number of locations</label><select id="f-loc" name="locations"><option>1</option><option>2-5</option><option>6-20</option><option>20+</option></select></div>
          <fieldset class="field field--full" data-group="services"><legend>Services you are interested in *</legend><div class="checks">{svc_checks}<label class="check"><input type="checkbox" name="services" value="not-sure"> Not sure yet</label></div><span class="err">Please choose at least one option.</span></fieldset>
          <div class="field field--full"><label for="f-msg">Tell us about your kitchen <span class="opt">(optional)</span></label><textarea id="f-msg" name="message" placeholder="Number of hoods, cooking style, last cleaning date, upcoming inspection..."></textarea></div>
        </div>
        <div class="form-foot">
          <small>By submitting, you agree to be contacted about your request. See our <a href="{u('privacy-page/')}" style="text-decoration:underline">Privacy Policy</a>.</small>
          <button class="btn btn--red" type="submit">Request My Free Survey {icon('arrow')}</button>
        </div>
      </form>
      <div class="form-success" role="status" aria-live="polite">
        <div class="ok">{icon('check', width=2.4)}</div>
        <h2 class="display h-sm" style="font-size:36px">Thanks. We have your request.</h2>
        <p>A member of our team will contact you within one business day to schedule your free site survey. Need us sooner? Call {BIZ['phone']}.</p>
        <div class="btn-row" style="justify-content:center;margin-top:20px"><button class="btn btn--outline" type="button" data-reset-form>Send another request</button><a class="btn btn--blue" href="{u('services/')}">Explore services {icon('arrow')}</a></div>
      </div>
    </div>
    <div class="info-stack">
      <div class="info-card info-card--offer"><span class="ic">{icon('star')}</span><div><h3>First service free</h3><p>Start your commercial kitchen compliance program risk-free.</p></div></div>
      <div class="info-card"><span class="ic">{icon('phone')}</span><div><h3>Call us</h3><p><a href="{BIZ['phone_href']}">{BIZ['phone']}</a><br>Toll-free <a href="{BIZ['tollfree_href']}">{BIZ['tollfree']}</a></p></div></div>
      <div class="info-card"><span class="ic">{icon('pin')}</span><div><h3>Mailing address</h3><p>{BIZ['street']}<br>{BIZ['city']}</p></div></div>
      <div class="info-card"><span class="ic">{icon('printer')}</span><div><h3>Fax</h3><p>{BIZ['fax']}</p></div></div>
      <div class="info-card"><span class="ic">{icon('gps')}</span><div><h3>Service area</h3><p>Ohio, Indiana, Kentucky, Michigan and West Virginia</p></div></div>
    </div>
  </div>
</section>"""
    faq = faq_section(HOME_FAQ[2:] + [("Which areas do you serve?", "We serve commercial kitchens across Ohio, Indiana, Kentucky, Michigan and West Virginia from our headquarters in West Milton, Ohio. If you are just outside that area, call us and we will let you know what is possible.")],
                      title="Before you reach out.", soft=True, more=False)
    body = "\n".join([hero, form, logo_strip(), faq, testimonials_section(soft=False),
                      cta_band("Prefer to talk it through?", "Our team can answer questions about scheduling, NFPA 96 frequency and pricing over the phone.", primary=False)])
    return page(f"Contact & Free Quote | {SITE}", "Request a free site survey and written quote for commercial kitchen hood cleaning, filter exchange, grease management or rooftop services.", body)


# ====================================================================== LEGAL

def legal_page(path, crumb, title, intro, sections):
    hero = page_hero([(crumb, path)], "Legal", title, intro, compact=True, ctas=False)
    toc = "".join(f'<a href="#s{i}">{h}</a>' for i, (h, _) in enumerate(sections))
    content = "".join(f'<h2 id="s{i}">{h}</h2>' + "".join(f"<p>{p}</p>" for p in ps) for i, (h, ps) in enumerate(sections))
    body = f"""{hero}
<section class="section" style="padding-top:56px">
  <div class="container legal-wrap">
    <nav class="toc" aria-label="On this page"><h2>On this page</h2>{toc}</nav>
    <div class="prose">
      <div class="notice">Placeholder text for prototype review. Final legal copy to be supplied and approved by Liberty Services before launch.</div>
      <p><strong>Last updated:</strong> October 2026</p>
      {content}
    </div>
  </div>
</section>
{cta_band()}"""
    return page(f"{crumb} | {SITE}", intro, body)


def privacy():
    return legal_page("privacy-page/", "Privacy Policy", "Privacy policy", "How Liberty Services, Inc. collects, uses and protects information shared through this website.", [
        ("Information we collect", ["We collect information you choose to provide, such as your name, business name, email address, phone number, service address and details about your kitchen when you request a quote or contact us.", "We may also collect basic technical information automatically, such as browser type, device information and pages visited, to help us understand how the website is used."]),
        ("How we use information", ["We use the information you provide to respond to your inquiries, schedule site surveys and services, send quotes and service reports, and improve our website and services.", "We do not sell your personal information."]),
        ("Cookies and analytics", ["This website may use cookies and similar technologies, including analytics tools, to measure traffic and improve the user experience. You can control cookies through your browser settings."]),
        ("Sharing information", ["We may share information with service providers who help us operate our business, such as scheduling, reporting and facility management platforms, only as needed to provide our services.", "We may disclose information if required by law or to protect our rights, customers or others."]),
        ("Data security", ["We use reasonable administrative, technical and physical safeguards to protect information. No method of transmission over the internet is completely secure."]),
        ("Your choices", ["You may request access to, correction of or deletion of your personal information by contacting us using the details below."]),
        ("Contact us", [f"Liberty Services, Inc., {BIZ['street']}, {BIZ['city']}. Phone {BIZ['phone']}."]),
    ])


def terms():
    return legal_page("legal/", "Terms & Conditions", "Terms & conditions", "The terms that apply to your use of the Liberty Services, Inc. website.", [
        ("Acceptance of terms", ["By accessing or using this website, you agree to these terms. If you do not agree, please do not use the website."]),
        ("Use of the website", ["The content on this website is provided for general information about our services. You agree not to misuse the website or interfere with its normal operation."]),
        ("Quotes and services", ["Information on this website, including service descriptions and offers, does not constitute a binding quote. All services are subject to a site survey and a written agreement.", "Promotional offers, including first service free, are subject to eligibility and terms confirmed in writing."]),
        ("Intellectual property", ["All content on this website, including text, graphics and logos, is owned by or licensed to Liberty Services, Inc. Third-party trademarks and logos belong to their respective owners."]),
        ("Third-party links", ["This website may link to third-party websites. We are not responsible for the content or practices of those websites."]),
        ("Limitation of liability", ["To the fullest extent permitted by law, Liberty Services, Inc. is not liable for any indirect or consequential damages arising from use of this website."]),
        ("Changes to these terms", ["We may update these terms from time to time. Continued use of the website after changes means you accept the updated terms."]),
        ("Contact", [f"Questions about these terms can be sent to Liberty Services, Inc., {BIZ['street']}, {BIZ['city']}, or by phone at {BIZ['phone']}."]),
    ])

# Liberty Services Inc. website prototype

Static, responsive prototype of the Liberty Services website, built from the Figma home page design and the page scope below. Text content is based on libertyservicesinc.net, with drafted copy where the current site has none.

## Pages

| Page | URL |
| --- | --- |
| Home | `/` |
| About: Liberty Services | `/about-liberty-services/` |
| About: FilterShine | `/about-filtershine/` |
| Services | `/services/` |
| Hood Cleaning | `/services/hood-cleaning/` |
| Filter Exchange | `/services/filter-exchange/` |
| Grease Management | `/services/grease-management/` |
| Rooftop Services | `/services/rooftop-services/` |
| Blog / news (listing + 6 posts) | `/blogs/` |
| Contact / Quote | `/contact/` |
| Privacy | `/privacy-page/` |
| Terms & Conditions | `/legal/` |

## Home hero: slider or static

The home hero can run as a four-slide service slider or as a single static hero.

- Launch default: set `heroMode` to `'slider'` or `'static'` in `assets/js/config.js`.
- Client preview: use the **Prototype options** button (bottom left of the home page), or add `?hero=static` / `?hero=slider` to the URL.
- The quote form on the right stays in place in both modes. In slider mode only the headline and background photo change, and the form's Service field follows the slide until the visitor picks one.
- Before launch, set `showPrototypePanel: false` in `assets/js/config.js` to hide the options button.

## Editing and rebuilding

Pages are generated from Python templates so the header, footer, testimonials and CTAs stay consistent everywhere.

```
src/data.py        business details, services, testimonials, FAQs, blog posts
src/pages.py       page layouts and page-specific copy
src/components.py  shared header, footer and sections
assets/css/main.css, assets/js/main.js
```

After editing, run `python3 src/build.py` (Python 3, no dependencies) to regenerate the HTML files.

## Preview locally

```
python3 -m http.server 8000
```

Then open http://localhost:8000. Links use folder URLs, so opening files directly from disk will not navigate correctly.

## Hosting on GitHub Pages

Settings > Pages > Deploy from a branch > choose the branch and `/ (root)`. All links are relative, so the site works at `username.github.io/repo-name/` as well as on a custom domain. A `.nojekyll` file is included.

## To confirm or replace before launch

- **Customer logos:** McDonald's uses its real mark. Arby's and Buffalo Wild Wings are text placeholders (`data-logo-placeholder` in the logo strip). Add the official files once brand-use approval is confirmed.
- **Photos:** Liberty's own photos are used where available. The other photos are Unsplash stock stand-ins. The before/after image in the service report is a simulated example and is labelled "Illustrative example".
- **Testimonials:** drafted for layout. Replace them with approved customer quotes.
- **Cities per state:** drafted. The current site lists states only.
- **Stats:** 20+ years, 5 states and 100% photo-documented come from the current site. The "100,000 gallons of grease" claim is not used yet.
- **FilterShine copy:** taken from the FilterShine section of libertyservicesinc.net.
- **Legal pages:** generic placeholder text, marked on the page.
- **Quote forms:** three places, all front-end only (validation and success state): the short form in the home hero, the short form in the closing red section on every page except Home and Contact, and the full form on Contact. Connect them to a form handler or CRM before launch.
- **Customer portal login:** links to `#` until the portal URL is supplied.

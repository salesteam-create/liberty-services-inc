(function () {
  'use strict';

  var cfg = window.LIBERTY_CONFIG || {};
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }
  function store(key, val) {
    try {
      if (val === undefined) return window.localStorage.getItem(key);
      window.localStorage.setItem(key, val);
    } catch (e) { return null; }
  }

  /* ---------- Desktop dropdowns (click/keyboard support) ---------- */
  $$('.nav__item.has-menu').forEach(function (item) {
    var btn = $('.nav__link', item);
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var open = !item.classList.contains('is-open');
      $$('.nav__item.is-open').forEach(function (o) { o.classList.remove('is-open'); $('.nav__link', o).setAttribute('aria-expanded', 'false'); });
      item.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', String(open));
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav__item')) {
      $$('.nav__item.is-open').forEach(function (o) { o.classList.remove('is-open'); $('.nav__link', o).setAttribute('aria-expanded', 'false'); });
    }
  });

  /* ---------- Mobile drawer ---------- */
  var drawer = $('#drawer');
  var toggle = $('.nav-toggle');
  function setDrawer(open) {
    if (!drawer) return;
    drawer.classList.toggle('is-open', open);
    drawer.setAttribute('aria-hidden', String(!open));
    toggle.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
    if (open) { var f = $('.drawer__close', drawer); if (f) f.focus(); } else { toggle.focus(); }
  }
  if (toggle && drawer) {
    toggle.addEventListener('click', function () { setDrawer(true); });
    $$('[data-close-drawer]', drawer).forEach(function (el) { el.addEventListener('click', function () { setDrawer(false); }); });
    $$('.drawer__group > button', drawer).forEach(function (b) {
      b.addEventListener('click', function () {
        var g = b.parentElement; var open = !g.classList.contains('is-open');
        g.classList.toggle('is-open', open); b.setAttribute('aria-expanded', String(open));
      });
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && drawer.classList.contains('is-open')) setDrawer(false); });
  }

  /* ---------- Hero slider ---------- */
  var hero = $('.hero[data-hero]');
  var heroApi = null;
  if (hero) {
    var slides = $$('.hero__slide', hero);
    var dots = $$('.hero__dot', hero);
    var interval = cfg.heroInterval || 7000;
    hero.style.setProperty('--hero-interval', interval + 'ms');
    var idx = 0, timer = null, paused = false;

    function show(i) {
      idx = (i + slides.length) % slides.length;
      slides.forEach(function (s, n) {
        var on = n === idx;
        s.classList.toggle('is-active', on);
        s.setAttribute('aria-hidden', String(!on));
        $$('a, button', s).forEach(function (el) { el.tabIndex = on ? 0 : -1; });
      });
      dots.forEach(function (d, n) {
        d.classList.toggle('is-active', n === idx);
        d.setAttribute('aria-selected', String(n === idx));
        var bar = $('.bar', d); if (bar) { bar.style.animation = 'none'; void bar.offsetWidth; bar.style.animation = ''; }
      });
    }
    function start() { stop(); if (hero.dataset.mode === 'slider' && !paused && !reduceMotion) timer = setInterval(function () { show(idx + 1); }, interval); }
    function stop() { if (timer) clearInterval(timer); timer = null; }
    dots.forEach(function (d, n) { d.addEventListener('click', function () { show(n); start(); }); });
    var prev = $('.hero__arrow--prev', hero), next = $('.hero__arrow--next', hero);
    if (prev) prev.addEventListener('click', function () { show(idx - 1); start(); });
    if (next) next.addEventListener('click', function () { show(idx + 1); start(); });
    hero.addEventListener('mouseenter', function () { paused = true; hero.classList.add('is-paused'); stop(); });
    hero.addEventListener('mouseleave', function () { paused = false; hero.classList.remove('is-paused'); start(); });
    hero.addEventListener('focusin', function () { paused = true; hero.classList.add('is-paused'); stop(); });
    hero.addEventListener('focusout', function () { paused = false; hero.classList.remove('is-paused'); start(); });
    if (reduceMotion) hero.classList.add('is-paused');

    // Touch swipe
    var x0 = null;
    hero.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    hero.addEventListener('touchend', function (e) {
      if (x0 === null || hero.dataset.mode !== 'slider') return;
      var dx = e.changedTouches[0].clientX - x0; x0 = null;
      if (Math.abs(dx) > 50) { show(idx + (dx < 0 ? 1 : -1)); start(); }
    });

    heroApi = {
      setMode: function (mode) {
        hero.dataset.mode = mode;
        if (mode === 'static') { stop(); show(0); } else { show(idx); start(); }
        $$('.proto__seg button').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.mode === mode)); });
      }
    };

    var urlMode = new URLSearchParams(window.location.search).get('hero');
    var mode = (urlMode === 'static' || urlMode === 'slider') ? urlMode : (store('liberty-hero-mode') || cfg.heroMode || 'slider');
    show(0);
    heroApi.setMode(mode);
  }

  /* ---------- Prototype options panel (home only) ---------- */
  var proto = $('.proto');
  if (proto) {
    if (cfg.showPrototypePanel === false || !heroApi) { proto.remove(); }
    else {
      $('.proto__toggle', proto).addEventListener('click', function () {
        var open = !proto.classList.contains('is-open');
        proto.classList.toggle('is-open', open);
        this.setAttribute('aria-expanded', String(open));
      });
      $$('.proto__seg button', proto).forEach(function (b) {
        b.addEventListener('click', function () { store('liberty-hero-mode', b.dataset.mode); heroApi.setMode(b.dataset.mode); });
      });
    }
  }

  /* ---------- Before / after ---------- */
  $$('.ba').forEach(function (ba) {
    var input = $('input', ba);
    function upd() { ba.style.setProperty('--pos', input.value + '%'); }
    input.addEventListener('input', upd); upd();
  });

  /* ---------- Service area checker + map ---------- */
  var areas = $('[data-areas]');
  if (areas) {
    var map = $('.map', areas);
    var sel = $('select', areas);
    var result = $('.area-result', areas);
    var cards = $$('.state-card[data-state]', areas);
    function activate(state) {
      if (map) {
        if (state) map.setAttribute('data-active', state); else map.removeAttribute('data-active');
        $$('.dot.st', map).forEach(function (d) { d.classList.toggle('on', !state || d.getAttribute('data-s') === state); });
      }
      cards.forEach(function (c) { c.classList.toggle('is-active', c.dataset.state === state); });
    }
    activate(null);
    var form = $('.area-check', areas);
    if (form) form.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = sel.value; var label = sel.options[sel.selectedIndex].text;
      if (!v) { result.textContent = 'Choose a state to check coverage.'; return; }
      if (v === 'other') {
        result.textContent = 'We focus on Ohio, Indiana, Kentucky, Michigan and West Virginia. Call 937-698-3322 and we will tell you what is possible.';
        activate(null); return;
      }
      result.textContent = 'Good news: Liberty Services covers ' + label + '. Book your free site survey.';
      activate(v);
    });
    if (sel) sel.addEventListener('change', function () { if (sel.value && sel.value !== 'other') activate(sel.value); else activate(null); result.textContent = ''; });
    cards.forEach(function (c) {
      c.addEventListener('mouseenter', function () { activate(c.dataset.state); });
      c.addEventListener('mouseleave', function () { activate(sel && sel.value && sel.value !== 'other' ? sel.value : null); });
    });
  }

  /* ---------- Blog filters ---------- */
  var filters = $('.blog-filters');
  if (filters) {
    var posts = $$('.post-card[data-cat]');
    $$('.chip', filters).forEach(function (chip) {
      chip.addEventListener('click', function () {
        $$('.chip', filters).forEach(function (c) { c.classList.remove('is-active'); c.setAttribute('aria-pressed', 'false'); });
        chip.classList.add('is-active'); chip.setAttribute('aria-pressed', 'true');
        var cat = chip.dataset.filter;
        posts.forEach(function (p) { p.hidden = !(cat === 'all' || p.dataset.cat === cat); });
      });
    });
  }

  /* ---------- Quote form (front-end only) ---------- */
  var qform = $('#quote-form');
  if (qform) {
    var params = new URLSearchParams(window.location.search);
    var pre = params.get('service');
    if (pre) { var box = qform.querySelector('input[name="services"][value="' + pre + '"]'); if (box) box.checked = true; }

    function check(field) {
      var input = $('input, select, textarea', field);
      if (!input) return true;
      var ok = true;
      if (input.required && !String(input.value).trim()) ok = false;
      if (ok && input.type === 'email' && input.value) ok = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(input.value);
      if (ok && input.type === 'tel' && input.value) ok = input.value.replace(/\D/g, '').length >= 10;
      if (ok && field.dataset.group) ok = $$('input:checked', field).length > 0;
      field.classList.toggle('has-error', !ok);
      return ok;
    }
    $$('.field', qform).forEach(function (f) {
      var input = $('input, select, textarea', f);
      if (input) input.addEventListener('blur', function () { if (f.classList.contains('has-error') || input.value) check(f); });
      f.addEventListener('change', function () { if (f.classList.contains('has-error')) check(f); });
    });
    qform.addEventListener('submit', function (e) {
      e.preventDefault();
      var bad = $$('.field', qform).filter(function (f) { return !check(f); });
      if (bad.length) { var first = $('input, select, textarea', bad[0]); if (first) first.focus(); return; }
      var card = qform.closest('.form-card');
      card.classList.add('is-sent');
      var name = qform.elements.name.value.trim().split(' ')[0];
      var t = $('.form-success h2', card); if (t && name) t.textContent = 'Thanks, ' + name + '. We have your request.';
      card.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'start' });
    });
    var again = $('[data-reset-form]');
    if (again) again.addEventListener('click', function () { qform.reset(); qform.closest('.form-card').classList.remove('is-sent'); });
  }

  /* ---------- Reveal on scroll ---------- */
  if ('IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    $$('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    $$('.reveal').forEach(function (el) { el.classList.add('is-in'); });
  }

  var y = $('[data-year]'); if (y) y.textContent = new Date().getFullYear();
})();

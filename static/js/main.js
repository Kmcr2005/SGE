(function () {
  var nav = document.getElementById("nav");
  var toggle = document.getElementById("nav-toggle");
  var links = document.getElementById("nav-links");

  function onScroll() {
    if (window.scrollY > 24) {
      nav.classList.add("is-scrolled");
    } else {
      nav.classList.remove("is-scrolled");
    }
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        links.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }
})();

/* =========================
   3D GALLERY TILT
   ========================= */

(function () {
  var cards = document.querySelectorAll(".gallery__item");

  cards.forEach(function (card) {

    card.addEventListener("mousemove", function (e) {
      var rect = card.getBoundingClientRect();

      var x = e.clientX - rect.left;
      var y = e.clientY - rect.top;

      var centerX = rect.width / 2;
      var centerY = rect.height / 2;

      var rotateY = ((x - centerX) / centerX) * 5;
      var rotateX = ((centerY - y) / centerY) * 5;

      card.style.transform =
        "translateY(-8px) " +
        "rotateX(" + rotateX + "deg) " +
        "rotateY(" + rotateY + "deg) " +
        "scale(1.025)";
    });

    card.addEventListener("mouseleave", function () {
      card.style.transform = "";
    });

  });
})();

/* =========================
   COMPASS CURSOR TRACKING
   ========================= */

(function () {
  var compass = document.querySelector(".hero__compass");
  var arrow = document.getElementById("compass-n-arrow");

  // Only run on devices with a real mouse
  if (!compass || !arrow) return;

  if (!window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    return;
  }

  var targetAngle = 0;
  var currentAngle = 0;

  function updateTarget(e) {
    var rect = compass.getBoundingClientRect();

    // Center of the compass on screen
    var centerX = rect.left + rect.width / 2;
    var centerY = rect.top + rect.height / 2;

    // Direction from compass center to cursor
    var dx = e.clientX - centerX;
    var dy = e.clientY - centerY;

    // Convert cursor direction to angle
    targetAngle = Math.atan2(dy, dx) * (180 / Math.PI) + 90;
  }

  function animate() {
    // Smooth lag toward cursor
    currentAngle += (targetAngle - currentAngle) * 0.08;

    arrow.style.transform =
      "rotate(" + currentAngle + "deg)";

    arrow.style.transformOrigin = "100px 100px";

    requestAnimationFrame(animate);
  }

  window.addEventListener("mousemove", updateTarget, {
    passive: true
  });

  animate();
})();

/* =========================================================
   SCROLL REVEAL
   ========================================================= */

(function () {

  var elements = document.querySelectorAll(".reveal");

  if (!elements.length) return;

  var observer = new IntersectionObserver(
    function (entries, observer) {

      entries.forEach(function (entry) {

        if (!entry.isIntersecting) return;

        entry.target.classList.add("is-visible");

        observer.unobserve(entry.target);

      });

    },
    {
      threshold: 0.15,
      rootMargin: "0px 0px -10% 0px"
    }
  );

  elements.forEach(function (element) {
    observer.observe(element);
  });

})();


/* =========================================================
   EVENTS — HORIZONTAL REVEAL
   ========================================================= */

(function () {

  var events = document.querySelectorAll(".section--events .event");

  if (!events.length) return;


  var eventObserver = new IntersectionObserver(
    function (entries, observer) {

      entries.forEach(function (entry) {

        if (!entry.isIntersecting) return;

        entry.target.classList.add("is-visible");

        observer.unobserve(entry.target);

      });

    },
    {
      threshold: 0.18,
      rootMargin: "0px 0px -12% 0px"
    }
  );


  events.forEach(function (event) {
    eventObserver.observe(event);
  });

})();

/* =========================================================
   SECTION HEADING SCROLL REVEAL
   ========================================================= */

(function () {

  var headings = document.querySelectorAll(".section__head");

  if (!headings.length) return;

  if (
    window.matchMedia("(prefers-reduced-motion: reduce)").matches
  ) {
    headings.forEach(function (heading) {
      heading.classList.add("is-visible");
    });

    return;
  }

  var headingObserver = new IntersectionObserver(
    function (entries, observer) {

      entries.forEach(function (entry) {

        if (!entry.isIntersecting) return;

        entry.target.classList.add("is-visible");

        observer.unobserve(entry.target);

      });

    },
    {
      threshold: 0.2,
      rootMargin: "0px 0px -12% 0px"
    }
  );


  headings.forEach(function (heading) {
    headingObserver.observe(heading);
  });

})();

/* =========================================================
   EVENTS — HORIZONTAL SCROLL REVEAL
   ========================================================= */

(function () {

  var events = document.querySelectorAll(
    ".section--events .event"
  );

  if (!events.length) return;

  if (
    window.matchMedia("(prefers-reduced-motion: reduce)").matches
  ) {

    events.forEach(function (event) {

      event.classList.add("is-visible");

    });

    return;
  }


  var eventObserver = new IntersectionObserver(
    function (entries, observer) {

      entries.forEach(function (entry) {

        if (!entry.isIntersecting) return;

        entry.target.classList.add("is-visible");

        observer.unobserve(entry.target);

      });

    },
    {
      threshold: 0.18,

      rootMargin: "0px 0px -10% 0px"
    }
  );


  events.forEach(function (event) {

    eventObserver.observe(event);

  });

})();

/* =========================================================
   VISION & MISSION — SCROLL REVEAL
   ========================================================= */

(function () {

  var items = document.querySelectorAll(
    ".section--vision-mission .split__col"
  );

  if (!items.length) return;


  /* Respect reduced-motion preference */

  if (
    window.matchMedia(
      "(prefers-reduced-motion: reduce)"
    ).matches
  ) {

    items.forEach(function (item) {

      item.classList.add("is-visible");

    });

    return;
  }


  /* Intersection Observer */

  var observer = new IntersectionObserver(
    function (entries, observer) {

      entries.forEach(function (entry) {

        if (!entry.isIntersecting) return;

        entry.target.classList.add("is-visible");

        observer.unobserve(entry.target);

      });

    },
    {
      threshold: 0.18,

      rootMargin: "0px 0px -10% 0px"
    }
  );


  items.forEach(function (item) {

    observer.observe(item);

  });

})();

/* =========================================================
   ABOUT — IMAGE ↔ INTERACTIVE MAP
   ========================================================= */

(function () {

  var visual = document.getElementById("about-visual");
  var toggle = document.getElementById("about-map-toggle");
  var mapElement = document.getElementById("about-map");

  if (!visual || !toggle || !mapElement) return;

  if (typeof L === "undefined") {
    console.error("Leaflet has not loaded.");
    return;
  }


  /* -------------------------------------------------------
     Institute of Remote Sensing
     Anna University, Chennai
     ------------------------------------------------------- */

  var IRS_LAT = 13.009270634864535;
  var IRS_LNG = 80.2364268870216;


  /* -------------------------------------------------------
     Create map
     ------------------------------------------------------- */

  var map = L.map(mapElement, {
    zoomControl: true,
    scrollWheelZoom: true
  }).setView(
    [IRS_LAT, IRS_LNG],
    17
  );


  /* -------------------------------------------------------
     OpenStreetMap
     ------------------------------------------------------- */

  var osm = L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
      maxZoom: 19,

      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }
  );

  osm.addTo(map);


  /* -------------------------------------------------------
     IRS marker
     ------------------------------------------------------- */

  var marker = L.marker([
    IRS_LAT,
    IRS_LNG
  ]).addTo(map);


  marker.bindPopup(
    "<strong>Institute of Remote Sensing</strong><br>" +
    "Anna University, Chennai"
  );


  /* -------------------------------------------------------
     Toggle
     ------------------------------------------------------- */

  var mapActive = false;


  toggle.addEventListener("click", function () {

    mapActive = !mapActive;


    if (mapActive) {

      /* Show map */

      visual.classList.add("is-map-active");

      toggle.setAttribute(
        "aria-pressed",
        "true"
      );

      toggle.setAttribute(
        "aria-label",
        "Show original image"
      );


      /*
       * Wait for the CSS transition before
       * telling Leaflet to recalculate its size.
       */

      setTimeout(function () {

        map.invalidateSize();

        map.setView(
          [IRS_LAT, IRS_LNG],
          17,
          {
            animate: true
          }
        );

      }, 600);


    } else {

      /* Return to original image */

      visual.classList.remove(
        "is-map-active"
      );

      toggle.setAttribute(
        "aria-pressed",
        "false"
      );

      toggle.setAttribute(
        "aria-label",
        "Show Institute of Remote Sensing location on map"
      );

    }

  });

})();
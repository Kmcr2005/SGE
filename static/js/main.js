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

    toggle.addEventListener("click", function (event) {

      event.preventDefault();
      event.stopPropagation();

      var open = links.classList.toggle("is-open");

      toggle.setAttribute(
        "aria-expanded",
        open ? "true" : "false"
      );

    });

    links.querySelectorAll("a").forEach(function (a) {

      a.addEventListener("click", function () {

        links.classList.remove("is-open");

        toggle.setAttribute(
          "aria-expanded",
          "false"
        );

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

(function () {

  "use strict";

  /* ================================================================ */
  /* EVENTS ANIMATION                                                 */
  /* ================================================================ */

  var eventCards =
    document.querySelectorAll(
      ".section--events .event"
    );


  if (!eventCards.length) {

    return;

  }


  /*
   * If the browser doesn't support IntersectionObserver,
   * simply activate all animations.
   */

  if (
    !("IntersectionObserver" in window)
  ) {

    eventCards.forEach(
      function (event) {

        event.classList.add(
          "event--animate"
        );

      }
    );

    return;

  }


  var eventObserver =
    new IntersectionObserver(

      function (entries, observer) {

        entries.forEach(
          function (entry) {

            if (
              entry.isIntersecting
            ) {

              entry.target.classList.add(
                "event--animate"
              );


              /*
               * Only animate each event once.
               */

              observer.unobserve(
                entry.target
              );

            }

          }
        );

      },

      {
        threshold: 0.12,

        rootMargin:
          "0px 0px -8% 0px"
      }

    );


  eventCards.forEach(
    function (event) {

      eventObserver.observe(
        event
      );

    }
  );


})();

/* ====================================================================== */
/* GALLERY PAGE CAROUSEL                                                  */
/* ====================================================================== */

(function () {

  const track = document.getElementById("gallery-track");
  const prevButton = document.getElementById("gallery-prev");
  const nextButton = document.getElementById("gallery-next");
  const pagination = document.getElementById("gallery-pagination");

  if (!track || !prevButton || !nextButton) {
    return;
  }


  /* -------------------------------------------------------------- */
  /* Find actual gallery pages                                      */
  /* -------------------------------------------------------------- */

  const pages = Array.from(
    track.querySelectorAll(".gallery-page")
  );

  if (!pages.length) {
    return;
  }


  let currentPage = 0;


  /* -------------------------------------------------------------- */
  /* Create page indicators                                         */
  /* -------------------------------------------------------------- */

  function createPagination() {

    if (!pagination) {
      return;
    }

    pagination.innerHTML = "";

    pages.forEach(function (_, index) {

      const dot = document.createElement("button");

      dot.type = "button";

      dot.className = "gallery-pagination__dot";

      dot.setAttribute(
        "aria-label",
        "Go to gallery page " + (index + 1)
      );

      dot.addEventListener("click", function () {

        currentPage = index;

        updateGallery();

      });

      pagination.appendChild(dot);

    });

  }


  /* -------------------------------------------------------------- */
  /* Update page indicators                                         */
  /* -------------------------------------------------------------- */

  function updatePagination() {

    if (!pagination) {
      return;
    }

    const dots = pagination.querySelectorAll(
      ".gallery-pagination__dot"
    );

    dots.forEach(function (dot, index) {

      dot.classList.toggle(
        "is-active",
        index === currentPage
      );

    });

  }


  /* -------------------------------------------------------------- */
  /* Move gallery to current page                                   */
  /* -------------------------------------------------------------- */

  function updateGallery() {

    /*
     * Each .gallery-page is exactly 100%
     * of the gallery viewport.
     */

    const offset = currentPage * 100;

    track.style.transform =
      "translateX(-" + offset + "%)";


    /* ------------------------------------------------------------ */
    /* Button states                                                */
    /* ------------------------------------------------------------ */

    prevButton.disabled =
      currentPage === 0;

    nextButton.disabled =
      currentPage === pages.length - 1;


    /* ------------------------------------------------------------ */
    /* Dots                                                         */
    /* ------------------------------------------------------------ */

    updatePagination();

  }


  /* -------------------------------------------------------------- */
  /* WEST BUTTON                                                    */
  /* -------------------------------------------------------------- */

  prevButton.addEventListener(
    "click",
    function () {

      if (currentPage > 0) {

        currentPage--;

        updateGallery();

      }

    }
  );


  /* -------------------------------------------------------------- */
  /* EAST BUTTON                                                    */
  /* -------------------------------------------------------------- */

  nextButton.addEventListener(
    "click",
    function () {

      if (currentPage < pages.length - 1) {

        currentPage++;

        updateGallery();

      }

    }
  );


  /* -------------------------------------------------------------- */
  /* Keyboard navigation                                            */
  /* -------------------------------------------------------------- */

  document.addEventListener(
    "keydown",
    function (event) {

      const gallery =
        document.getElementById("gallery");

      if (!gallery) {
        return;
      }


      const rect =
        gallery.getBoundingClientRect();


      const visible =
        rect.top < window.innerHeight &&
        rect.bottom > 0;


      if (!visible) {
        return;
      }


      /* WEST */

      if (event.key === "ArrowLeft") {

        if (currentPage > 0) {

          currentPage--;

          updateGallery();

        }

      }


      /* EAST */

      if (event.key === "ArrowRight") {

        if (currentPage < pages.length - 1) {

          currentPage++;

          updateGallery();

        }

      }

    }
  );


  /* -------------------------------------------------------------- */
  /* Initial setup                                                  */
  /* -------------------------------------------------------------- */

  createPagination();

  updateGallery();


})();
/* ============================================================= */
/* STUDENT OFFICE BEARERS - 3D CARD SLIDER                      */
/* ============================================================= */

(function () {

  "use strict";

  const stage =
    document.querySelector(".bearer-stage");

  if (!stage) return;


  const cards =
    Array.from(
      document.querySelectorAll(".bearer-card")
    );


  const dots =
    Array.from(
      document.querySelectorAll(".bearer-dot")
    );


  const prev =
    document.getElementById("bearer-prev");


  const next =
    document.getElementById("bearer-next");


  const currentLabel =
    document.getElementById("bearer-current");


  if (!cards.length) return;


  let current = 0;


  /* ----------------------------------------------------------- */
  /* UPDATE CARDS                                                */
  /* ----------------------------------------------------------- */

  function updateCards() {

    const total = cards.length;


    cards.forEach(function (card, index) {

      let offset =
        index - current;


      /*
       * Circular carousel.
       *
       * This allows card 16 to move
       * naturally to card 1.
       */

      if (offset > total / 2) {

        offset -= total;

      }


      if (offset < -total / 2) {

        offset += total;

      }


      /*
       * Only show the closest
       * cards around the active card.
       */

      const distance =
        Math.abs(offset);


      const visible =
        distance <= 2;


      /*
       * Horizontal movement
       */

      const x =
        offset * 245;


      /*
       * Depth
       */

      const z =
        -distance * 180;


      /*
       * 3D rotation
       */

      const rotateY =
        offset * -20;


      /*
       * Scale
       */

      const scale =
        offset === 0
          ? 1
          : Math.max(
              .72,
              1 - distance * .09
            );


      /*
       * Opacity
       */

      const opacity =
        visible
          ? (
              offset === 0
                ? 1
                : Math.max(
                    .35,
                    1 - distance * .3
                  )
            )
          : 0;


      /*
       * Blur side cards.
       */

      const blur =
        offset === 0
          ? 0
          : Math.min(
              3,
              distance * 1.2
            );


      /*
       * Z-index
       */

      const zIndex =
        100 - distance;


      card.style.transform =
        "translate(-50%, -50%) " +
        "translate3d(" +
        x +
        "px, 0, " +
        z +
        "px) " +
        "rotateY(" +
        rotateY +
        "deg) " +
        "scale(" +
        scale +
        ")";


      card.style.opacity =
        opacity;


      card.style.filter =
        "blur(" +
        blur +
        "px)";


      card.style.zIndex =
        zIndex;


      card.classList.toggle(
        "active",
        offset === 0
      );

    });


    /* --------------------------------------------------------- */
    /* DOTS                                                       */
    /* --------------------------------------------------------- */

    dots.forEach(function (dot, index) {

      dot.classList.toggle(
        "active",
        index === current
      );

    });


    /* --------------------------------------------------------- */
    /* COUNTER                                                    */
    /* --------------------------------------------------------- */

    if (currentLabel) {

      currentLabel.textContent =
        String(current + 1)
          .padStart(2, "0");

    }

  }


  /* ----------------------------------------------------------- */
  /* GO TO CARD                                                   */
  /* ----------------------------------------------------------- */

  function goTo(index) {

    if (index < 0) {

      current =
        cards.length - 1;

    }

    else if (
      index >= cards.length
    ) {

      current = 0;

    }

    else {

      current = index;

    }


    updateCards();

  }


  /* ----------------------------------------------------------- */
  /* PREVIOUS                                                     */
  /* ----------------------------------------------------------- */

  if (prev) {

    prev.addEventListener(
      "click",
      function () {

        goTo(current - 1);

      }
    );

  }


  /* ----------------------------------------------------------- */
  /* NEXT                                                         */
  /* ----------------------------------------------------------- */

  if (next) {

    next.addEventListener(
      "click",
      function () {

        goTo(current + 1);

      }
    );

  }


  /* ----------------------------------------------------------- */
  /* DOT NAVIGATION                                               */
  /* ----------------------------------------------------------- */

  dots.forEach(function (dot) {

    dot.addEventListener(
      "click",
      function () {

        const index =
          Number(
            dot.dataset.index
          );

        goTo(index);

      }
    );

  });


  /* ----------------------------------------------------------- */
  /* CLICK SIDE CARD                                              */
  /* ----------------------------------------------------------- */



  /* ----------------------------------------------------------- */
  /* KEYBOARD                                                     */
  /* ----------------------------------------------------------- */

  document.addEventListener(
    "keydown",
    function (event) {

      if (
        event.key === "ArrowLeft"
      ) {

        goTo(current - 1);

      }


      if (
        event.key === "ArrowRight"
      ) {

        goTo(current + 1);

      }

    }
  );


  /* ----------------------------------------------------------- */
  /* TOUCH SWIPE                                                  */
  /* ----------------------------------------------------------- */

  let touchStartX = 0;


  stage.addEventListener(
    "touchstart",
    function (event) {

      touchStartX =
        event.changedTouches[0]
          .screenX;

    },
    {
      passive: true
    }
  );


  stage.addEventListener(
    "touchend",
    function (event) {

      const touchEndX =
        event.changedTouches[0]
          .screenX;


      const difference =
        touchStartX - touchEndX;


      /*
       * Ignore very small movements.
       */

      if (
        Math.abs(difference) < 50
      ) {

        return;

      }


      if (difference > 0) {

        goTo(current + 1);

      }

      else {

        goTo(current - 1);

      }

    },
    {
      passive: true
    }
  );


  /* ----------------------------------------------------------- */
  /* INITIALIZE                                                   */
  /* ----------------------------------------------------------- */

  updateCards();

})();
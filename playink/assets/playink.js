// Scratch demo (a foil canvas under a black wax canvas) and the click-to-load video.
(() => {
  const sheet = document.getElementById("sheet");
  if (sheet) initScratch(sheet);
  document.querySelectorAll(".video-play").forEach(initVideo);

  function initScratch(sheet) {
    const holo = document.getElementById("holo");
    const wax = document.getElementById("wax");
    const hint = document.getElementById("hint");
    const hctx = holo.getContext("2d");
    const wctx = wax.getContext("2d");
    const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
    const stops = ["#ff9ad5", "#c7a6ff", "#8fe3ff", "#a8ffcf", "#fff2a3", "#ffb38a", "#ff9ad5", "#c7a6ff", "#8fe3ff"];
    let W = 0, H = 0, tiltX = .3, tiltY = .4, last = null, scratched = false;

    function drawFoil(t) {
      const shift = tiltX * W * 1.2 + (reduce ? 0 : Math.sin(t / 2400) * W * .12);
      const g = hctx.createLinearGradient(-W + shift, 0, W * 1.6 + shift, H * (.6 + tiltY * .5));
      stops.forEach((c, i) => g.addColorStop(i / (stops.length - 1), c));
      hctx.globalCompositeOperation = "source-over";
      hctx.fillStyle = g;
      hctx.fillRect(0, 0, W, H);
      // A sheen band that follows the pointer, like light on the foil.
      const s = hctx.createLinearGradient(0, H * tiltY * 1.4 - H * .3, W, H * tiltY * 1.4 + H * .2);
      s.addColorStop(0, "rgba(255,255,255,0)");
      s.addColorStop(.45, "rgba(255,255,255,.55)");
      s.addColorStop(.55, "rgba(255,255,255,0)");
      hctx.globalCompositeOperation = "soft-light";
      hctx.fillStyle = s;
      hctx.fillRect(0, 0, W, H);
      hctx.globalCompositeOperation = "source-over";
    }

    function fillWax() {
      wctx.globalCompositeOperation = "source-over";
      wctx.fillStyle = "#0b0a10";
      wctx.fillRect(0, 0, W, H);
    }

    function scratchPath(points, width) {
      wctx.globalCompositeOperation = "destination-out";
      wctx.lineCap = "round";
      wctx.lineJoin = "round";
      wctx.lineWidth = width;
      wctx.beginPath();
      wctx.moveTo(points[0][0], points[0][1]);
      points.slice(1).forEach(p => wctx.lineTo(p[0], p[1]));
      wctx.stroke();
    }

    // A star, a heart and a sparkle already scratched, so the sheet shows the idea before anyone touches it.
    function seedDrawing() {
      const cx = W * .5, cy = H * .42, r = Math.min(W, H) * .24, star = [];
      for (let i = 0; i <= 10; i++) {
        const a = -Math.PI / 2 + i * Math.PI / 5, rr = i % 2 ? r * .45 : r;
        star.push([cx + Math.cos(a) * rr, cy + Math.sin(a) * rr]);
      }
      scratchPath(star, Math.max(10, W * .035));
      const heart = [], hx = W * .78, hy = H * .78, hs = W * .06;
      for (let i = 0; i <= 40; i++) {
        const t = i / 40 * Math.PI * 2;
        heart.push([hx + hs * Math.pow(Math.sin(t), 3), hy - hs * (13 * Math.cos(t) - 5 * Math.cos(2 * t) - 2 * Math.cos(3 * t) - Math.cos(4 * t)) / 16]);
      }
      scratchPath(heart, Math.max(8, W * .028));
      const sx = W * .2, sy = H * .8;
      scratchPath([[sx - 14, sy], [sx + 14, sy]], 10);
      scratchPath([[sx, sy - 14], [sx, sy + 14]], 10);
    }

    function resize() {
      const rect = sheet.getBoundingClientRect();
      const dpr = Math.min(2, window.devicePixelRatio || 1);
      W = rect.width;
      H = rect.height;
      [holo, wax].forEach(c => { c.width = Math.round(W * dpr); c.height = Math.round(H * dpr); });
      hctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      wctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      fillWax();
      seedDrawing();
      drawFoil(performance.now());
    }

    function pos(e) {
      const rect = wax.getBoundingClientRect();
      return [e.clientX - rect.left, e.clientY - rect.top];
    }

    wax.addEventListener("pointerdown", e => {
      wax.setPointerCapture(e.pointerId);
      last = pos(e);
      scratchPath([last, [last[0] + .1, last[1]]], 22);
    });
    wax.addEventListener("pointermove", e => {
      const p = pos(e);
      tiltX = Math.min(1, Math.max(0, p[0] / W));
      tiltY = Math.min(1, Math.max(0, p[1] / H));
      if (reduce) drawFoil(0);
      if (!last) return;
      scratchPath([last, p], 22);
      last = p;
      if (!scratched) { scratched = true; hint.style.opacity = "0"; }
    });
    ["pointerup", "pointercancel"].forEach(t => wax.addEventListener(t, () => { last = null; }));
    document.getElementById("reset").addEventListener("click", () => {
      fillWax();
      seedDrawing();
      hint.style.opacity = "1";
      scratched = false;
    });

    if (!reduce) (function loop(t) { drawFoil(t); requestAnimationFrame(loop); })(performance.now());
    new ResizeObserver(resize).observe(sheet);
  }

  // Nothing from YouTube loads until the visitor presses play.
  function initVideo(button) {
    button.addEventListener("click", () => {
      const iframe = document.createElement("iframe");
      iframe.src = "https://www.youtube-nocookie.com/embed/" + button.dataset.video + "?autoplay=1&rel=0";
      iframe.title = button.dataset.title;
      iframe.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
      iframe.allowFullscreen = true;
      button.replaceWith(iframe);
    });
  }
})();

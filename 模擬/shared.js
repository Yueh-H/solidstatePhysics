/* 固態物理互動模擬 — 共用繪圖工具（純 SVG，無外部依賴） */
(function (global) {
  "use strict";

  function clamp(x, a, b) {
    return Math.max(a, Math.min(b, x));
  }

  function linspace(a, b, n) {
    const out = [];
    if (n <= 1) return [a];
    for (let i = 0; i < n; i++) out.push(a + ((b - a) * i) / (n - 1));
    return out;
  }

  function fmt(x, digits) {
    if (!isFinite(x)) return "—";
    const d = digits == null ? 3 : digits;
    const ax = Math.abs(x);
    if (ax !== 0 && (ax >= 1e4 || ax < 1e-3)) return x.toExponential(2);
    return Number(x.toFixed(d)).toString();
  }

  /** 2D 座標框 */
  function Plot2D(svg, opts) {
    this.svg = svg;
    this.W = opts.width || 640;
    this.H = opts.height || 420;
    this.pad = Object.assign({ l: 58, r: 18, t: 22, b: 48 }, opts.pad || {});
    this.xDomain = opts.xDomain || [0, 1];
    this.yDomain = opts.yDomain || [0, 1];
    this.xLabel = opts.xLabel || "";
    this.yLabel = opts.yLabel || "";
    this.bg = opts.bg || "#ffffff";
    svg.setAttribute("viewBox", `0 0 ${this.W} ${this.H}`);
    svg.setAttribute("xmlns", "http://www.w3.org/2000/svg");
    this.clear();
  }

  Plot2D.prototype.clear = function () {
    while (this.svg.firstChild) this.svg.removeChild(this.svg.firstChild);
    this._defs = el(this.svg, "defs", {});
    // clip
    const clip = el(this._defs, "clipPath", { id: uid("clip") });
    this.clipId = clip.getAttribute("id");
    el(clip, "rect", {
      x: this.pad.l,
      y: this.pad.t,
      width: this.innerW(),
      height: this.innerH(),
    });
    el(this.svg, "rect", {
      x: 0, y: 0, width: this.W, height: this.H, fill: this.bg,
    });
    el(this.svg, "rect", {
      x: this.pad.l,
      y: this.pad.t,
      width: this.innerW(),
      height: this.innerH(),
      fill: "#fcfdff",
      stroke: "#c5d5e5",
      "stroke-width": 1,
    });
    this.gGrid = el(this.svg, "g", { class: "grid" });
    this.gData = el(this.svg, "g", {
      class: "data",
      "clip-path": `url(#${this.clipId})`,
    });
    this.gAnno = el(this.svg, "g", { class: "anno" });
    this.gAxes = el(this.svg, "g", { class: "axes" });
    this._drawAxes();
  };

  Plot2D.prototype.innerW = function () {
    return this.W - this.pad.l - this.pad.r;
  };
  Plot2D.prototype.innerH = function () {
    return this.H - this.pad.t - this.pad.b;
  };

  Plot2D.prototype.setDomains = function (xDomain, yDomain) {
    if (xDomain) this.xDomain = xDomain;
    if (yDomain) this.yDomain = yDomain;
  };

  Plot2D.prototype.x = function (v) {
    const [a, b] = this.xDomain;
    return this.pad.l + ((v - a) / (b - a)) * this.innerW();
  };
  Plot2D.prototype.y = function (v) {
    const [a, b] = this.yDomain;
    return this.pad.t + (1 - (v - a) / (b - a)) * this.innerH();
  };

  Plot2D.prototype._niceTicks = function (a, b, nApprox) {
    const span = b - a;
    if (span <= 0) return [a];
    const raw = span / (nApprox || 5);
    const pow = Math.pow(10, Math.floor(Math.log10(raw)));
    const err = raw / pow;
    let step;
    if (err < 1.5) step = 1 * pow;
    else if (err < 3) step = 2 * pow;
    else if (err < 7) step = 5 * pow;
    else step = 10 * pow;
    const start = Math.ceil(a / step) * step;
    const ticks = [];
    for (let t = start; t <= b + step * 1e-9; t += step) ticks.push(+t.toFixed(10));
    return ticks;
  };

  Plot2D.prototype._drawAxes = function () {
    const g = this.gAxes;
    while (g.firstChild) g.removeChild(g.firstChild);
    while (this.gGrid.firstChild) this.gGrid.removeChild(this.gGrid.firstChild);

    const xTicks = this._niceTicks(this.xDomain[0], this.xDomain[1], 6);
    const yTicks = this._niceTicks(this.yDomain[0], this.yDomain[1], 6);

    xTicks.forEach((t) => {
      const px = this.x(t);
      el(this.gGrid, "line", {
        x1: px, x2: px, y1: this.pad.t, y2: this.pad.t + this.innerH(),
        stroke: "#e8eef4", "stroke-width": 1,
      });
      el(g, "line", {
        x1: px, x2: px,
        y1: this.pad.t + this.innerH(), y2: this.pad.t + this.innerH() + 5,
        stroke: "#567", "stroke-width": 1,
      });
      text(g, px, this.pad.t + this.innerH() + 18, fmtTick(t), {
        "text-anchor": "middle", fill: "#456", "font-size": 12,
      });
    });
    yTicks.forEach((t) => {
      const py = this.y(t);
      el(this.gGrid, "line", {
        x1: this.pad.l, x2: this.pad.l + this.innerW(), y1: py, y2: py,
        stroke: "#e8eef4", "stroke-width": 1,
      });
      el(g, "line", {
        x1: this.pad.l - 5, x2: this.pad.l, y1: py, y2: py,
        stroke: "#567", "stroke-width": 1,
      });
      text(g, this.pad.l - 8, py + 4, fmtTick(t), {
        "text-anchor": "end", fill: "#456", "font-size": 12,
      });
    });

    // axis lines
    el(g, "line", {
      x1: this.pad.l, x2: this.pad.l + this.innerW(),
      y1: this.pad.t + this.innerH(), y2: this.pad.t + this.innerH(),
      stroke: "#334", "stroke-width": 1.2,
    });
    el(g, "line", {
      x1: this.pad.l, x2: this.pad.l,
      y1: this.pad.t, y2: this.pad.t + this.innerH(),
      stroke: "#334", "stroke-width": 1.2,
    });

    if (this.xLabel) {
      text(g, this.pad.l + this.innerW() / 2, this.H - 10, this.xLabel, {
        "text-anchor": "middle", fill: "#1a4d7c", "font-size": 13, "font-weight": 600,
      });
    }
    if (this.yLabel) {
      const tx = 16;
      const ty = this.pad.t + this.innerH() / 2;
      const t = text(g, tx, ty, this.yLabel, {
        "text-anchor": "middle", fill: "#1a4d7c", "font-size": 13, "font-weight": 600,
      });
      t.setAttribute("transform", `rotate(-90 ${tx} ${ty})`);
    }
  };

  Plot2D.prototype.polyline = function (pts, style) {
    // pts: [{x,y}, ...] or [[x,y],...]
    const parts = [];
    for (let i = 0; i < pts.length; i++) {
      const p = pts[i];
      const xv = Array.isArray(p) ? p[0] : p.x;
      const yv = Array.isArray(p) ? p[1] : p.y;
      if (!isFinite(xv) || !isFinite(yv)) continue;
      parts.push(`${this.x(xv)},${this.y(yv)}`);
    }
    if (!parts.length) return null;
    return el(this.gData, "polyline", Object.assign({
      points: parts.join(" "),
      fill: "none",
      stroke: style.stroke || "#1a4d7c",
      "stroke-width": style.width || 2.2,
      "stroke-linejoin": "round",
      "stroke-linecap": "round",
      "stroke-dasharray": style.dash || "none",
      opacity: style.opacity == null ? 1 : style.opacity,
    }, style.attrs || {}));
  };

  Plot2D.prototype.fillBetween = function (ptsTop, ptsBot, style) {
    if (!ptsTop.length || !ptsBot.length) return null;
    let d = "";
    ptsTop.forEach((p, i) => {
      const xv = Array.isArray(p) ? p[0] : p.x;
      const yv = Array.isArray(p) ? p[1] : p.y;
      d += `${i === 0 ? "M" : "L"}${this.x(xv)},${this.y(yv)} `;
    });
    for (let i = ptsBot.length - 1; i >= 0; i--) {
      const p = ptsBot[i];
      const xv = Array.isArray(p) ? p[0] : p.x;
      const yv = Array.isArray(p) ? p[1] : p.y;
      d += `L${this.x(xv)},${this.y(yv)} `;
    }
    d += "Z";
    return el(this.gData, "path", {
      d,
      fill: style.fill || "rgba(26,77,124,0.12)",
      stroke: "none",
    });
  };

  Plot2D.prototype.vline = function (x, style) {
    return el(this.gAnno, "line", {
      x1: this.x(x), x2: this.x(x),
      y1: this.pad.t, y2: this.pad.t + this.innerH(),
      stroke: (style && style.stroke) || "#999",
      "stroke-width": (style && style.width) || 1.2,
      "stroke-dasharray": (style && style.dash) || "4 3",
      opacity: (style && style.opacity) || 0.9,
    });
  };

  Plot2D.prototype.hline = function (y, style) {
    return el(this.gAnno, "line", {
      x1: this.pad.l, x2: this.pad.l + this.innerW(),
      y1: this.y(y), y2: this.y(y),
      stroke: (style && style.stroke) || "#999",
      "stroke-width": (style && style.width) || 1.2,
      "stroke-dasharray": (style && style.dash) || "4 3",
      opacity: (style && style.opacity) || 0.9,
    });
  };

  Plot2D.prototype.circle = function (x, y, r, style) {
    return el(this.gAnno, "circle", {
      cx: this.x(x), cy: this.y(y), r: r || 4,
      fill: (style && style.fill) || "#c0392b",
      stroke: (style && style.stroke) || "#fff",
      "stroke-width": 1.2,
    });
  };

  Plot2D.prototype.label = function (x, y, s, style) {
    return text(this.gAnno, this.x(x), this.y(y), s, Object.assign({
      fill: "#234", "font-size": 12,
    }, style || {}));
  };

  Plot2D.prototype.raw = function () {
    return this.gAnno;
  };

  // 幾何 SVG 工具（非資料座標）
  function el(parent, tag, attrs) {
    const n = document.createElementNS("http://www.w3.org/2000/svg", tag);
    if (attrs) {
      Object.keys(attrs).forEach((k) => {
        if (attrs[k] != null && attrs[k] !== "none") n.setAttribute(k, attrs[k]);
      });
    }
    parent.appendChild(n);
    return n;
  }

  function text(parent, x, y, s, attrs) {
    const n = el(parent, "text", Object.assign({ x, y }, attrs || {}));
    n.textContent = s;
    return n;
  }

  let _uid = 0;
  function uid(prefix) {
    _uid += 1;
    return `${prefix || "id"}${_uid}`;
  }

  function fmtTick(t) {
    if (Math.abs(t) < 1e-12) return "0";
    if (Math.abs(t - Math.round(t)) < 1e-9) return String(Math.round(t));
    return fmt(t, 2);
  }

  /** 綁定 range input：回傳讀取器，oninput 呼叫 cb */
  function bindSlider(id, cb) {
    const elInput = document.getElementById(id);
    if (!elInput) return () => 0;
    const valEl = document.querySelector(`[data-for="${id}"]`);
    const read = () => parseFloat(elInput.value);
    const paint = () => {
      if (valEl) {
        const digits = parseInt(elInput.dataset.digits || "3", 10);
        const suffix = elInput.dataset.suffix || "";
        valEl.textContent = fmt(read(), digits) + suffix;
      }
    };
    elInput.addEventListener("input", () => {
      paint();
      cb();
    });
    paint();
    return read;
  }

  function bindAll(ids, cb) {
    const readers = {};
    ids.forEach((id) => {
      readers[id] = bindSlider(id, cb);
    });
    return readers;
  }

  global.SSP = {
    clamp, linspace, fmt, Plot2D, el, text, bindSlider, bindAll, uid,
  };
})(window);

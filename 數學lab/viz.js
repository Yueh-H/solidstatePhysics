/* 數學 Lab — SVG / 小模擬共用工具（無外部依賴） */
(function (global) {
  "use strict";

  const NS = "http://www.w3.org/2000/svg";

  function el(parent, tag, attrs, text) {
    const n = document.createElementNS(NS, tag);
    if (attrs) {
      Object.keys(attrs).forEach((k) => {
        if (attrs[k] != null) n.setAttribute(k, attrs[k]);
      });
    }
    if (text != null) n.textContent = text;
    if (parent) parent.appendChild(n);
    return n;
  }

  function clear(node) {
    while (node.firstChild) node.removeChild(node.firstChild);
  }

  function fmt(x, d) {
    if (!isFinite(x)) return "—";
    const n = d == null ? 3 : d;
    const a = Math.abs(x);
    if (a !== 0 && (a >= 1e4 || a < 1e-3)) return x.toExponential(2);
    return Number(x.toFixed(n)).toString();
  }

  function linspace(a, b, n) {
    const o = [];
    for (let i = 0; i < n; i++) o.push(a + ((b - a) * i) / (n - 1 || 1));
    return o;
  }

  /** 簡易 2D 圖框 */
  function Plot(svg, opt) {
    this.svg = svg;
    this.W = opt.w || 520;
    this.H = opt.h || 280;
    this.pad = Object.assign({ l: 48, r: 14, t: 16, b: 40 }, opt.pad || {});
    this.xD = opt.xD || [0, 1];
    this.yD = opt.yD || [0, 1];
    this.xLabel = opt.xLabel || "";
    this.yLabel = opt.yLabel || "";
    svg.setAttribute("viewBox", `0 0 ${this.W} ${this.H}`);
    this.redrawFrame();
  }

  Plot.prototype.iw = function () {
    return this.W - this.pad.l - this.pad.r;
  };
  Plot.prototype.ih = function () {
    return this.H - this.pad.t - this.pad.b;
  };
  Plot.prototype.X = function (v) {
    const [a, b] = this.xD;
    return this.pad.l + ((v - a) / (b - a || 1)) * this.iw();
  };
  Plot.prototype.Y = function (v) {
    const [a, b] = this.yD;
    return this.pad.t + (1 - (v - a) / (b - a || 1)) * this.ih();
  };

  Plot.prototype.redrawFrame = function () {
    clear(this.svg);
    el(this.svg, "rect", {
      x: 0, y: 0, width: this.W, height: this.H, fill: "#fcfdff",
    });
    el(this.svg, "rect", {
      x: this.pad.l,
      y: this.pad.t,
      width: this.iw(),
      height: this.ih(),
      fill: "#fff",
      stroke: "#c5d5e5",
    });
    this.gGrid = el(this.svg, "g", {});
    this.gData = el(this.svg, "g", {});
    this.gAnno = el(this.svg, "g", {});
    // axes
    el(this.svg, "line", {
      x1: this.pad.l,
      x2: this.pad.l + this.iw(),
      y1: this.pad.t + this.ih(),
      y2: this.pad.t + this.ih(),
      stroke: "#445",
      "stroke-width": 1.2,
    });
    el(this.svg, "line", {
      x1: this.pad.l,
      x2: this.pad.l,
      y1: this.pad.t,
      y2: this.pad.t + this.ih(),
      stroke: "#445",
      "stroke-width": 1.2,
    });
    if (this.xLabel) {
      el(
        this.svg,
        "text",
        {
          x: this.pad.l + this.iw() / 2,
          y: this.H - 8,
          fill: "#1a4d7c",
          "font-size": 12,
          "text-anchor": "middle",
          "font-weight": 600,
        },
        this.xLabel
      );
    }
    if (this.yLabel) {
      const tx = 14;
      const ty = this.pad.t + this.ih() / 2;
      const t = el(
        this.svg,
        "text",
        {
          x: tx,
          y: ty,
          fill: "#1a4d7c",
          "font-size": 12,
          "text-anchor": "middle",
          "font-weight": 600,
        },
        this.yLabel
      );
      t.setAttribute("transform", `rotate(-90 ${tx} ${ty})`);
    }
    // ticks rough
    const xt = 5,
      yt = 4;
    for (let i = 0; i <= xt; i++) {
      const v = this.xD[0] + ((this.xD[1] - this.xD[0]) * i) / xt;
      const x = this.X(v);
      el(this.gGrid, "line", {
        x1: x, x2: x, y1: this.pad.t, y2: this.pad.t + this.ih(),
        stroke: "#eef2f6",
      });
      el(
        this.svg,
        "text",
        {
          x, y: this.pad.t + this.ih() + 14,
          fill: "#567", "font-size": 10, "text-anchor": "middle",
        },
        fmt(v, 2)
      );
    }
    for (let i = 0; i <= yt; i++) {
      const v = this.yD[0] + ((this.yD[1] - this.yD[0]) * i) / yt;
      const y = this.Y(v);
      el(this.gGrid, "line", {
        x1: this.pad.l, x2: this.pad.l + this.iw(), y1: y, y2: y,
        stroke: "#eef2f6",
      });
      el(
        this.svg,
        "text",
        {
          x: this.pad.l - 6, y: y + 3,
          fill: "#567", "font-size": 10, "text-anchor": "end",
        },
        fmt(v, 2)
      );
    }
  };

  Plot.prototype.setDomain = function (xD, yD) {
    if (xD) this.xD = xD;
    if (yD) this.yD = yD;
    this.redrawFrame();
  };

  Plot.prototype.poly = function (pts, style) {
    const s = style || {};
    const parts = pts
      .filter((p) => isFinite(p[0]) && isFinite(p[1]))
      .map((p) => `${this.X(p[0])},${this.Y(p[1])}`);
    if (!parts.length) return null;
    return el(this.gData, "polyline", {
      points: parts.join(" "),
      fill: "none",
      stroke: s.stroke || "#1a4d7c",
      "stroke-width": s.width || 2.2,
      "stroke-dasharray": s.dash || null,
      opacity: s.opacity == null ? 1 : s.opacity,
      "stroke-linejoin": "round",
    });
  };

  Plot.prototype.vline = function (x, style) {
    const s = style || {};
    return el(this.gAnno, "line", {
      x1: this.X(x), x2: this.X(x),
      y1: this.pad.t, y2: this.pad.t + this.ih(),
      stroke: s.stroke || "#999",
      "stroke-width": s.width || 1.2,
      "stroke-dasharray": s.dash || "4 3",
    });
  };

  Plot.prototype.hline = function (y, style) {
    const s = style || {};
    return el(this.gAnno, "line", {
      x1: this.pad.l, x2: this.pad.l + this.iw(),
      y1: this.Y(y), y2: this.Y(y),
      stroke: s.stroke || "#999",
      "stroke-width": s.width || 1.2,
      "stroke-dasharray": s.dash || "4 3",
    });
  };

  Plot.prototype.dot = function (x, y, r, fill) {
    return el(this.gAnno, "circle", {
      cx: this.X(x), cy: this.Y(y), r: r || 4,
      fill: fill || "#c0392b", stroke: "#fff", "stroke-width": 1,
    });
  };

  Plot.prototype.label = function (x, y, text, style) {
    const s = style || {};
    return el(
      this.gAnno,
      "text",
      {
        x: this.X(x) + (s.dx || 0),
        y: this.Y(y) + (s.dy || 0),
        fill: s.fill || "#234",
        "font-size": s.size || 11,
        "text-anchor": s.anchor || "start",
        "font-weight": s.weight || 400,
      },
      text
    );
  };

  function bindRange(id, onChange) {
    const input = document.getElementById(id);
    const val = document.querySelector(`[data-val="${id}"]`);
    if (!input) return () => 0;
    const read = () => parseFloat(input.value);
    const paint = () => {
      if (val) {
        const d = parseInt(input.dataset.digits || "2", 10);
        val.textContent = fmt(read(), d) + (input.dataset.suffix || "");
      }
    };
    input.addEventListener("input", () => {
      paint();
      onChange();
    });
    paint();
    return read;
  }

  function arrow(parent, x1, y1, x2, y2, color, label, labelOff) {
    const id = "mk" + Math.random().toString(36).slice(2, 8);
    let defs = parent.querySelector("defs");
    if (!defs) defs = el(parent, "defs", {});
    const m = el(defs, "marker", {
      id,
      viewBox: "0 0 10 10",
      refX: 9,
      refY: 5,
      markerWidth: 6,
      markerHeight: 6,
      orient: "auto-start-reverse",
    });
    el(m, "path", { d: "M0 0 L10 5 L0 10 z", fill: color });
    el(parent, "line", {
      x1, y1, x2, y2,
      stroke: color,
      "stroke-width": 2.2,
      "marker-end": `url(#${id})`,
    });
    if (label) {
      el(
        parent,
        "text",
        {
          x: (x1 + x2) / 2 + (labelOff && labelOff.x || 6),
          y: (y1 + y2) / 2 + (labelOff && labelOff.y || -6),
          fill: color,
          "font-size": 12,
          "font-weight": 700,
        },
        label
      );
    }
  }

  global.LabViz = {
    el, clear, fmt, linspace, Plot, bindRange, arrow, NS,
  };
})(window);

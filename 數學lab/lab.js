/* 數學推導 Lab — 逐步揭露 + 填空驗收 */
(function (global) {
  "use strict";

  function norm(s) {
    return String(s || "")
      .trim()
      .toLowerCase()
      .replace(/\s+/g, "")
      .replace(/·/g, "*")
      .replace(/×/g, "*")
      .replace(/⋅/g, "*")
      .replace(/（/g, "(")
      .replace(/）/g, ")")
      .replace(/，/g, ",")
      .replace(/＝/g, "=")
      .replace(/−/g, "-")
      .replace(/–/g, "-")
      .replace(/—/g, "-")
      .replace(/√/g, "sqrt")
      .replace(/π/g, "pi")
      .replace(/ℏ/g, "hbar")
      .replace(/ħ/g, "hbar")
      .replace(/α/g, "alpha")
      .replace(/β/g, "beta")
      .replace(/γ/g, "gamma")
      .replace(/δ/g, "delta")
      .replace(/θ/g, "theta")
      .replace(/ω/g, "omega")
      .replace(/μ/g, "mu")
      .replace(/σ/g, "sigma")
      .replace(/χ/g, "chi")
      .replace(/²/g, "^2")
      .replace(/³/g, "^3")
      .replace(/₁/g, "1")
      .replace(/₂/g, "2")
      .replace(/₃/g, "3");
  }

  function matchAnswer(user, accepted) {
    const u = norm(user);
    if (!u) return false;
    const list = Array.isArray(accepted) ? accepted : [accepted];
    return list.some((a) => {
      const t = norm(a);
      if (u === t) return true;
      // allow numeric closeness
      const nu = parseFloat(u);
      const nt = parseFloat(t);
      if (!isNaN(nu) && !isNaN(nt) && /^-?\d/.test(u) && /^-?\d/.test(t)) {
        return Math.abs(nu - nt) < 1e-6 * Math.max(1, Math.abs(nt));
      }
      return false;
    });
  }

  function checkBlank(inputEl, accepted, fbEl, msgs) {
    const ok = matchAnswer(inputEl.value, accepted);
    inputEl.classList.remove("ok", "bad");
    inputEl.classList.add(ok ? "ok" : "bad");
    if (fbEl) {
      fbEl.className = "fb " + (ok ? "ok" : "bad");
      fbEl.textContent = ok
        ? (msgs && msgs.ok) || "✓ 正確"
        : (msgs && msgs.bad) || "再想想；可按提示";
    }
    return ok;
  }

  function showHint(fbEl, text) {
    if (!fbEl) return;
    fbEl.className = "fb hint";
    fbEl.textContent = "提示：" + text;
  }

  /** Step controller */
  function StepLab(opts) {
    this.steps = Array.from(document.querySelectorAll(opts.stepSelector || ".step"));
    this.idx = 0;
    this.progress = document.getElementById(opts.progressId || "progress");
    this.meta = document.getElementById(opts.metaId || "stepMeta");
    this.btnPrev = document.getElementById(opts.prevId || "btnPrev");
    this.btnNext = document.getElementById(opts.nextId || "btnNext");
    this.btnReveal = document.getElementById(opts.revealId || "btnReveal");
    this.doneBanner = document.getElementById(opts.doneId || "doneBanner");
    this.requireBlanks = opts.requireBlanks !== false;
    this._buildProgress();
    this._bind();
    this.go(0);
  }

  StepLab.prototype._buildProgress = function () {
    if (!this.progress) return;
    this.progress.innerHTML = "";
    this.dots = this.steps.map((_, i) => {
      const d = document.createElement("span");
      d.className = "dot";
      d.textContent = String(i + 1);
      d.title = "Step " + (i + 1);
      d.addEventListener("click", () => {
        if (i <= this.idx) this.go(i);
      });
      this.progress.appendChild(d);
      return d;
    });
  };

  StepLab.prototype._bind = function () {
    if (this.btnPrev) this.btnPrev.addEventListener("click", () => this.go(this.idx - 1));
    if (this.btnNext) this.btnNext.addEventListener("click", () => this.tryNext());
    if (this.btnReveal) {
      this.btnReveal.addEventListener("click", () => {
        this.go(this.steps.length - 1);
        this.steps.forEach((s) => s.classList.add("visible"));
        this.idx = this.steps.length - 1;
        this._paint();
        if (this.doneBanner) this.doneBanner.classList.add("show");
      });
    }
    // blank buttons
    document.querySelectorAll("[data-check]").forEach((btn) => {
      btn.addEventListener("click", () => {
        const id = btn.getAttribute("data-check");
        const input = document.getElementById(id);
        const fb = document.getElementById(id + "Fb");
        const raw = btn.getAttribute("data-answers") || input.getAttribute("data-answers") || "";
        const answers = raw.split("|").filter(Boolean);
        checkBlank(input, answers, fb, {
          ok: btn.getAttribute("data-ok") || "✓ 正確",
          bad: btn.getAttribute("data-bad") || "還不对，再試或看提示",
        });
      });
    });
    document.querySelectorAll("[data-hint-for]").forEach((btn) => {
      btn.addEventListener("click", () => {
        const id = btn.getAttribute("data-hint-for");
        const fb = document.getElementById(id + "Fb");
        showHint(fb, btn.getAttribute("data-hint") || "");
      });
    });
    document.querySelectorAll("[data-choice]").forEach((btn) => {
      btn.addEventListener("click", () => {
        const group = btn.parentElement;
        const correct = btn.getAttribute("data-choice") === "1";
        group.querySelectorAll("button").forEach((b) => {
          b.classList.remove("picked-ok", "picked-bad");
        });
        btn.classList.add(correct ? "picked-ok" : "picked-bad");
        const fb = group.parentElement.querySelector(".fb");
        if (fb) {
          fb.className = "fb " + (correct ? "ok" : "bad");
          fb.textContent = correct
            ? btn.getAttribute("data-okmsg") || "✓ 正確"
            : btn.getAttribute("data-badmsg") || "再想想";
        }
        if (correct) btn.dataset.solved = "1";
      });
    });
  };

  StepLab.prototype._currentBlanksOk = function () {
    if (!this.requireBlanks) return true;
    const step = this.steps[this.idx];
    if (!step) return true;
    const inputs = step.querySelectorAll("input[data-answers]");
    if (!inputs.length) {
      // choice groups: if any choice present, need one solved
      const choices = step.querySelectorAll("[data-choice]");
      if (!choices.length) return true;
      return Array.from(choices).some((b) => b.dataset.solved === "1");
    }
    let all = true;
    inputs.forEach((input) => {
      const answers = (input.getAttribute("data-answers") || "").split("|").filter(Boolean);
      const fb = document.getElementById(input.id + "Fb");
      const ok = checkBlank(input, answers, fb, {
        ok: "✓ 正確",
        bad: "請先完成本步填空再繼續",
      });
      if (!ok) all = false;
    });
    return all;
  };

  StepLab.prototype.tryNext = function () {
    if (!this._currentBlanksOk()) return;
    if (this.idx >= this.steps.length - 1) {
      if (this.doneBanner) this.doneBanner.classList.add("show");
      return;
    }
    this.go(this.idx + 1);
  };

  StepLab.prototype.go = function (i) {
    if (i < 0 || i >= this.steps.length) return;
    // reveal all up to i
    this.idx = i;
    this.steps.forEach((s, j) => {
      if (j <= i) s.classList.add("visible");
      else s.classList.remove("visible");
    });
    this._paint();
    const el = this.steps[i];
    if (el) el.scrollIntoView({ behavior: "smooth", block: "nearest" });
  };

  StepLab.prototype._paint = function () {
    if (this.dots) {
      this.dots.forEach((d, j) => {
        d.classList.remove("done", "curr");
        if (j < this.idx) d.classList.add("done");
        if (j === this.idx) d.classList.add("curr");
      });
    }
    if (this.meta) {
      this.meta.textContent = "Step " + (this.idx + 1) + " / " + this.steps.length;
    }
    if (this.btnPrev) this.btnPrev.disabled = this.idx <= 0;
    if (this.btnNext) {
      this.btnNext.textContent =
        this.idx >= this.steps.length - 1 ? "完成 ✓" : "下一步 →";
    }
    if (this.idx >= this.steps.length - 1 && this.doneBanner) {
      // don't auto-show until they click complete or last next
    }
  };

  global.MathLab = {
    norm,
    matchAnswer,
    checkBlank,
    showHint,
    StepLab,
  };
})(window);

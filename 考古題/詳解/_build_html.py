#!/usr/bin/env python3
"""Build standalone MathJax+marked HTML viewers for the 固態物理導論 詳解.

Mirrors AItotur/exam/refexam/tutorials/build_html.py (same PAGE template:
MathJax3 tex-chtml + marked + floating TOC + collapsible <details>).
Converts every  固態_<year>_詳解.md  and  _共用觀念與公式.md  in this folder,
plus an index.html.  Re-run after editing/adding any .md.
"""
import glob
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

PAGE = r"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<script>
window.MathJax = {
  loader: { load: ['[tex]/boldsymbol'] },
  tex: { packages: {'[+]': ['boldsymbol']}, inlineMath: [['$','$']], displayMath: [['$$','$$']], processEscapes: true, tags: 'none' },
  options: { skipHtmlTags: ['script','noscript','style','textarea','pre','code'] },
  svg: { fontCache: 'global' }
};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
         max-width: 960px; margin: 2em auto; padding: 0 1.2em 4em; line-height: 1.75; color: #222; background: #fafafa; }
  h1, h2, h3 { color: #1a4d7c; margin-top: 1.6em; line-height: 1.35; }
  h1 { border-bottom: 3px solid #1a4d7c; padding-bottom: 0.3em; }
  h2 { border-bottom: 1px solid #999; padding-bottom: 0.2em; }
  h3 { color: #2b6ca0; }
  h4 { color: #2b6ca0; }
  blockquote { border-left: 4px solid #6aa1d6; background: #eef5fb; margin: 0.8em 0; padding: 0.6em 1em; color: #334; border-radius: 4px; }
  code { background: #f0f0f0; padding: 2px 5px; border-radius: 3px; font-family: "SF Mono", Menlo, Monaco, Consolas, monospace; font-size: 0.92em; }
  pre { background: #f5f5f5; padding: 1em; overflow-x: auto; border-radius: 6px; border: 1px solid #ddd; }
  pre code { background: none; padding: 0; }
  img { max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 6px; background: #fff; padding: 4px; }
  table { border-collapse: collapse; margin: 1em 0; overflow-x: auto; display: block; }
  th, td { border: 1px solid #bbb; padding: 6px 12px; text-align: left; }
  th { background: #e8eef4; }
  hr { border: none; border-top: 1px solid #ccc; margin: 2.5em 0; }
  #loading { text-align: center; padding: 3em; color: #888; font-size: 1.1em; }
  details { background: #f7fafd; border: 1px solid #c5d5e5; border-radius: 8px; padding: 0.5em 1em; margin: 0.6em 0; }
  details[open] { background: #fff; border-color: #6aa1d6; box-shadow: 0 2px 6px rgba(0,0,0,0.05); }
  summary { cursor: pointer; padding: 0.4em 0; color: #1a4d7c; font-size: 1.05em; user-select: none; }
  summary:hover { color: #2b6ca0; }
  .MathJax_Display, mjx-container[jax="CHTML"][display="true"] { overflow-x: auto; overflow-y: hidden; max-width: 100%; }
  details[open] > :not(summary) { animation: fadeIn 0.2s ease-out; }
  @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
  .nav { font-size: 0.92em; margin: 0 0 1em; color: #555; }
  .nav a { color: #1a4d7c; text-decoration: none; }
  .nav a:hover { text-decoration: underline; }
</style>
</head>
<body>
<div class="nav">__NAV__</div>
<div id="loading">載入中… 正在渲染數學式</div>
<div id="content" style="display:none;"></div>
<script id="md-source" type="text/markdown">
__MARKDOWN_CONTENT__
</script>
<script>
function renderMarkdownWithMath(md) {
  const mathBlocks = [];
  function escapeHtmlChars(str) {
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  md = md.replace(/\$\$([\s\S]+?)\$\$/g, m => {
    let clean = m.replace(/\n\s*>\s*/g, '\n');
    mathBlocks.push(escapeHtmlChars(clean));
    return '@@MATHBLK' + (mathBlocks.length-1) + '@@';
  });
  md = md.replace(/\$([^\$\n]+?)\$/g, m => {
    mathBlocks.push(escapeHtmlChars(m));
    return '@@MATHBLK' + (mathBlocks.length-1) + '@@';
  });
  let html = marked.parse(md);
  html = html.replace(/@@MATHBLK(\d+)@@/g, (_, i) => mathBlocks[parseInt(i,10)]);
  return html;
}
window.addEventListener('DOMContentLoaded', () => {
  const md = document.getElementById('md-source').textContent;
  document.getElementById('content').innerHTML = renderMarkdownWithMath(md);
  document.getElementById('content').style.display = '';
  const loading = document.getElementById('loading');
  document.querySelectorAll('details').forEach(d => {
    d.addEventListener('toggle', () => {
      if (d.open && !d.dataset.rendered) {
        d.dataset.rendered = '1';
        if (window.MathJax && MathJax.typesetPromise) MathJax.typesetPromise([d]);
      }
    });
  });
  function typeset() {
    if (window.MathJax && MathJax.typesetPromise) {
      MathJax.typesetPromise([document.getElementById('content')])
        .then(() => { loading.style.display = 'none'; })
        .catch(e => { loading.textContent = 'MathJax error: ' + e; });
    } else setTimeout(typeset, 300);
  }
  typeset();
});
</script>
<!-- toc-sidebar -->
<button id="toc-toggle" type="button" aria-label="開關目錄">☰ 目錄</button>
<nav id="toc" aria-label="本頁目錄"></nav>
<style>
  #toc-toggle { position: fixed; top: 12px; left: 12px; z-index: 1001; background: #1a4d7c; color: #fff;
    border: none; border-radius: 6px; padding: 6px 11px; font-size: 0.9em; cursor: pointer;
    box-shadow: 0 1px 4px rgba(0,0,0,0.25); opacity: 0.9; }
  #toc-toggle:hover { opacity: 1; }
  #toc { position: fixed; top: 0; left: 0; width: 250px; height: 100vh; overflow-y: auto; box-sizing: border-box;
    background: #f4f8fc; border-right: 1px solid #c5d5e5; padding: 3.4em 0.7em 2em; z-index: 1000;
    transform: translateX(-100%); transition: transform 0.2s ease; font-size: 0.9em; }
  #toc.open { transform: translateX(0); box-shadow: 2px 0 14px rgba(0,0,0,0.15); }
  #toc .toc-title { font-weight: 700; color: #1a4d7c; font-size: 1.0em; margin: 0 0 0.5em; padding: 0 0.4em; }
  #toc a { display: block; text-decoration: none; color: #34506b; padding: 3px 0.5em; border-radius: 4px;
    line-height: 1.4; border-left: 2px solid transparent; }
  #toc a:hover { background: #e3eef8; color: #1a4d7c; }
  #toc a.h3 { padding-left: 1.5em; font-size: 0.92em; color: #5d728a; }
  #toc a.h4 { padding-left: 2.7em; font-size: 0.86em; color: #6f8197; }
  #toc a.active { background: #e8f0f9; color: #1a4d7c; border-left-color: #1a4d7c; font-weight: 600; }
  @media (min-width: 1280px) {
    #toc { transform: none; box-shadow: none; }
    #toc-toggle { display: none; }
    body { margin-left: 290px; }
  }
  @media print { #toc, #toc-toggle { display: none !important; } body { margin-left: auto !important; } }
</style>
<script>
(function () {
  function buildTOC() {
    var content = document.getElementById('content');
    var toc = document.getElementById('toc');
    var toggle = document.getElementById('toc-toggle');
    if (!content || !toc) return;
    var heads = content.querySelectorAll('h2, h3, h4');
    var frag = document.createDocumentFragment();
    var title = document.createElement('div');
    title.className = 'toc-title'; title.textContent = '本頁目錄';
    frag.appendChild(title);
    var items = [];
    heads.forEach(function (h, i) {
      if (h.closest('details')) return;
      if (!h.id) h.id = 'sec-' + i;
      var a = document.createElement('a');
      a.href = '#' + h.id;
      var label = h.textContent.replace(/\s+/g, ' ').trim();
      a.innerHTML = label.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      a.className = h.tagName.toLowerCase();
      a.addEventListener('click', function (e) {
        e.preventDefault();
        h.scrollIntoView({ behavior: 'smooth', block: 'start' });
        history.replaceState(null, '', '#' + h.id);
        if (window.matchMedia('(max-width: 1279px)').matches) toc.classList.remove('open');
      });
      frag.appendChild(a);
      items.push({ el: h, link: a });
    });
    if (!items.length) { toc.style.display = 'none'; if (toggle) toggle.style.display = 'none'; return; }
    toc.innerHTML = ''; toc.appendChild(frag);
    if (toggle) toggle.addEventListener('click', function () { toc.classList.toggle('open'); });
    var ticking = false;
    function spy() {
      ticking = false;
      var y = window.scrollY + 120, cur = items[0];
      for (var k = 0; k < items.length; k++) {
        if (items[k].el.getBoundingClientRect().top + window.scrollY <= y) cur = items[k];
      }
      items.forEach(function (it) { it.link.classList.toggle('active', it === cur); });
    }
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; window.requestAnimationFrame(spy); }
    }, { passive: true });
    spy();
    (function typesetTOC() {
      if (window.MathJax && MathJax.typesetPromise) { MathJax.typesetPromise([toc]).catch(function () {}); }
      else { setTimeout(typesetTOC, 300); }
    })();
  }
  function whenReady() {
    var content = document.getElementById('content');
    if (content && content.querySelector('h1, h2, h3')) { buildTOC(); return; }
    var tries = 0;
    var timer = setInterval(function () {
      var c = document.getElementById('content');
      if ((c && c.querySelector('h1, h2, h3')) || ++tries > 100) { clearInterval(timer); buildTOC(); }
    }, 50);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', whenReady);
  else whenReady();
})();
</script>
</body>
</html>
"""


def md_to_html(md_path, title, nav):
    with open(md_path, encoding="utf-8") as f:
        md = f.read()
    # cross-doc links point at the .html siblings, not the .md
    md = md.replace("_共用觀念與公式.md", "_共用觀念與公式.html")
    md_safe = md.replace("</script>", "<\\/script>")
    return (PAGE.replace("__MARKDOWN_CONTENT__", md_safe)
                .replace("__TITLE__", title)
                .replace("__NAV__", nav))


def year_of(name):
    m = re.search(r"固態_(\d{4})_詳解", name)
    return m.group(1) if m else None


def main():
    nav_home = '<a href="index.html">← 詳解目錄</a> &nbsp;·&nbsp; <a href="_共用觀念與公式.html">🧰 共用觀念與公式</a>'
    built = []

    # shared concepts page
    sym = os.path.join(HERE, "_共用觀念與公式.md")
    if os.path.exists(sym):
        out = md_to_html(sym, "固態物理導論詳解 — 共用觀念與公式",
                         '<a href="index.html">← 詳解目錄</a>')
        p = os.path.join(HERE, "_共用觀念與公式.html")
        open(p, "w", encoding="utf-8").write(out)
        built.append(os.path.basename(p))

    # per-year tutorials
    years = []
    for md_path in sorted(glob.glob(os.path.join(HERE, "固態_*_詳解.md"))):
        yr = year_of(os.path.basename(md_path))
        title = f"固態物理導論 {yr} 資格考 — 詳解" if yr else os.path.basename(md_path)
        out = md_to_html(md_path, title, nav_home)
        p = md_path[:-3] + ".html"
        open(p, "w", encoding="utf-8").write(out)
        built.append(os.path.basename(p))
        if yr:
            years.append(yr)

    # index.html
    cards = []
    cards.append('  <a class="card ref" href="_共用觀念與公式.html">\n'
                 '    <div class="card-title">🧰 共用觀念與公式</div>\n'
                 '    <div class="card-sub">Bravais/倒晶格/繞射/Bloch/BvK/2D DOS/tight-binding/磁性/超導 — 高中類比→定義→範例</div>\n'
                 '  </a>')
    for yr in sorted(set(years), reverse=True):
        cards.append(f'  <a class="card" href="固態_{yr}_詳解.html">\n'
                     f'    <div class="card-title">固態物理導論 {yr} 資格考 — 逐題詳解</div>\n'
                     f'    <div class="card-sub">符號就地展開 · 每題 題目→Step→自我檢核→信心</div>\n'
                     f'  </a>')
    index = INDEX.replace("__CARDS__", "\n".join(cards))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(index)
    built.append("index.html")

    # 導讀（位於上一層 考古題/，連結進 詳解/）
    guide_md = os.path.join(os.path.dirname(HERE), "導讀.md")
    if os.path.exists(guide_md):
        out = md_to_html(guide_md, "固態物理導論 — 導讀（近10年 × 教材三層）",
                         '<a href="詳解/index.html">詳解目錄 →</a> &nbsp;·&nbsp; <a href="單元整理.html">單元整理</a> &nbsp;·&nbsp; <a href="../單元教學/index.html">🎓 單元學科</a> &nbsp;·&nbsp; <a href="../教材/index.html">📖 教材直讀</a>')
        open(os.path.join(os.path.dirname(HERE), "導讀.html"), "w", encoding="utf-8").write(out)
        built.append("../導讀.html")

    # 單元整理（位於上一層 考古題/，跨年份單元彙整＋出題頻率，連結進 詳解/）
    unit_md = os.path.join(os.path.dirname(HERE), "單元整理.md")
    if os.path.exists(unit_md):
        out = md_to_html(unit_md, "固態物理導論 — 單元整理（2013–2025 依 Kittel 章節）",
                         '<a href="導讀.html">← 導讀</a> &nbsp;·&nbsp; <a href="詳解/index.html">詳解目錄 →</a> &nbsp;·&nbsp; <a href="../單元教學/index.html">🎓 單元學科</a> &nbsp;·&nbsp; <a href="../教材/index.html">📖 教材直讀</a>')
        open(os.path.join(os.path.dirname(HERE), "單元整理.html"), "w", encoding="utf-8").write(out)
        built.append("../單元整理.html")

    # 教材（root/教材/）— 把直接閱讀的課本各檔轉成可讀 HTML + 一個教材目錄頁
    built += build_jiaocai()

    # 單元教學（root/單元教學/）— 10 單元「從高中到資格考」學科完整版 + 目錄
    built += build_units()

    # Kittel 章節導讀（教材/Kittel章節導讀/）— 讀 Kittel 翻譯本的對照地圖（概念橋＋術語速查）
    built += build_kittel_guide()

    # Kittel 習題詳解（教材/Kittel習題詳解/）— 加碼範例＋課本習題完整逐步解
    built += build_kittel_problems()

    # 先備知識補帖（教材/先備知識/）— 讀教材時的數學/物理先備，含範例與圖
    built += build_prereq()

    for b in built:
        print("Wrote", b)
    print(f"\nDone. {len(built)} files.")


# (md相對教材根, 卡片標題, 卡片副標)；簡報在子資料夾，nav 深度自動處理
JIAOCAI_FILES = [
    ("Kittel_原文.md",        "Kittel《Introduction to Solid State Physics》8e — 原文",
     "英文指定教材，考試符號依此（打底主力）"),
    ("Kittel_翻譯.md",        "Kittel《固體物理導論》— 中文翻譯",
     "中文對照；看不懂英文先讀本書同節"),
    ("固態物理導論_林盛煇.md", "林盛煇《固態物理導論》（中）",
     "中文上手橋樑，與 Kittel 對照同讀"),
    ("講義.md",               "Lecture Notes 講義（研究所級）",
     "進階深度：能帶 / 半導體 / 聲子 / 輸運 / 磁性"),
    ("Kittel_解答手冊.md",     "Kittel 8e — 解答手冊",
     "Solution Manual，對課本習題"),
    ("簡介簡報/solid-1.md",    "蕭智仁《深入淺出固態物理》簡報 (1)", "快入門 · 晶體結構與週期性"),
    ("簡介簡報/solid-2.md",    "蕭智仁《深入淺出固態物理》簡報 (2)", "快入門 · 繞射 / 鍵結 / 聲子"),
    ("簡介簡報/solid-3.md",    "蕭智仁《深入淺出固態物理》簡報 (3)", "快入門 · 自由電子 / 能帶"),
    ("簡介簡報/solid-4.md",    "蕭智仁《深入淺出固態物理》簡報 (4)", "快入門 · 半導體 / 磁性 / 超導"),
]


def build_jiaocai():
    """Render每本教材 .md → 可讀 HTML + 教材/index.html。回傳已寫檔清單。"""
    root = os.path.dirname(os.path.dirname(HERE))   # solidstatePhysics/
    jc = os.path.join(root, "教材")
    out_built = []
    if not os.path.isdir(jc):
        return out_built
    cards = []
    for rel, title, sub in JIAOCAI_FILES:
        src = os.path.join(jc, rel)
        if not os.path.exists(src):
            continue
        deep = "/" in rel                            # 簡報在子資料夾
        if deep:
            nav = ('<a href="../index.html">← 教材目錄</a> &nbsp;·&nbsp; '
                   '<a href="../../考古題/導讀.html">導讀</a> &nbsp;·&nbsp; '
                   '<a href="../../考古題/單元整理.html">單元整理</a>')
        else:
            nav = ('<a href="index.html">← 教材目錄</a> &nbsp;·&nbsp; '
                   '<a href="../考古題/導讀.html">導讀</a> &nbsp;·&nbsp; '
                   '<a href="../考古題/單元整理.html">單元整理</a>')
        out = md_to_html(src, f"教材 — {title}", nav)
        dst = os.path.join(jc, rel[:-3] + ".html")
        open(dst, "w", encoding="utf-8").write(out)
        out_built.append("教材/" + rel[:-3] + ".html")
        href = rel[:-3] + ".html"
        cards.append(f'  <a class="card" href="{href}">\n'
                     f'    <div class="card-title">{title}</div>\n'
                     f'    <div class="card-sub">{sub}</div>\n'
                     f'  </a>')
    index = JIAOCAI_INDEX.replace("__CARDS__", "\n".join(cards))
    open(os.path.join(jc, "index.html"), "w", encoding="utf-8").write(index)
    out_built.append("教材/index.html")
    return out_built


# 單元 → (卡片標題, 卡片副標, 梯隊標籤)
UNITS_META = {
    "unit01_晶體結構":        ("單元 01 — 晶體結構（Crystal Structure）", "Bravais / 原胞 / 填充率 / Miller 指標", "第一梯隊"),
    "unit02_倒晶格與繞射":     ("單元 02 — 倒晶格與繞射（Reciprocal Lattice & Diffraction）", "倒晶格 / Bragg / 結構因子 / 消光", "第一梯隊"),
    "unit03_晶體鍵結":        ("單元 03 — 晶體鍵結（Crystal Binding）", "凡得瓦 / Lennard–Jones / Madelung", "第三梯隊"),
    "unit04_聲子與晶格振動":   ("單元 04 — 聲子／晶格振動（Phonons）", "色散關係 / 聲學光學支 / Debye T³", "第一梯隊"),
    "unit05_自由電子費米氣體": ("單元 05 — 自由電子費米氣體（Free Electron Fermi Gas）", "費米能 / DOS / Wiedemann–Franz", "第二梯隊"),
    "unit06_能帶與Bloch電子":  ("單元 06 — 能帶／Bloch 電子（Energy Bands）", "Bloch 定理 / 能隙 / 有效質量 / tight-binding", "第一梯隊"),
    "unit07_半導體":          ("單元 07 — 半導體（Semiconductors）", "電洞 / 施主受主 / pn 接面 / Hall", "第三梯隊"),
    "unit08_磁性":           ("單元 08 — 磁性（Magnetism）", "Langevin / Curie / Landau 能階", "第四梯隊"),
    "unit09_超導":           ("單元 09 — 超導（Superconductivity）", "Meissner / type I·II / 渦旋", "第四梯隊"),
    "unit10_實驗與進階":      ("單元 10 — 實驗技術／進階（Experimental / Advanced）", "STM·AFM / 反射率 / Dirac·graphene", "第四梯隊"),
}


def build_units():
    """Render 單元教學/unit*.md → HTML（每單元一頁）+ 單元教學/index.html。"""
    root = os.path.dirname(os.path.dirname(HERE))   # solidstatePhysics/
    ud = os.path.join(root, "單元教學")
    out_built = []
    if not os.path.isdir(ud):
        return out_built
    nav = ('<a href="index.html">單元目錄</a> &nbsp;·&nbsp; '
           '<a href="../考古題/單元整理.html">單元整理</a> &nbsp;·&nbsp; '
           '<a href="../考古題/詳解/index.html">逐題詳解</a> &nbsp;·&nbsp; '
           '<a href="../教材/index.html">📖 教材直讀</a>')
    cards = []
    for md_path in sorted(glob.glob(os.path.join(ud, "unit*.md"))):
        stem = os.path.basename(md_path)[:-3]
        title, sub, tier = UNITS_META.get(stem, (stem, "", ""))
        out = md_to_html(md_path, f"固態物理 {title}", nav)
        open(md_path[:-3] + ".html", "w", encoding="utf-8").write(out)
        out_built.append("單元教學/" + stem + ".html")
        badge = f'<span class="tier">{tier}</span>' if tier else ""
        cards.append(f'  <a class="card" href="{stem}.html">\n'
                     f'    <div class="card-title">{title} {badge}</div>\n'
                     f'    <div class="card-sub">{sub}</div>\n'
                     f'  </a>')
    index = UNITS_INDEX.replace("__CARDS__", "\n".join(cards))
    open(os.path.join(ud, "index.html"), "w", encoding="utf-8").write(index)
    out_built.append("單元教學/index.html")
    return out_built


# Kittel 章節導讀 → (卡片標題, 卡片副標)
KGUIDE_META = {
    "ch01_晶體結構":        ("Kittel 第1章 — 晶體結構（Crystal Structure）", "Bravais / 原胞 / 填充率 / Miller 指標"),
    "ch02_倒晶格與繞射":     ("Kittel 第2章 — 波繞射與倒晶格（Wave Diffraction & Reciprocal Lattice）", "Bragg / 倒晶格 / 結構因子 / BZ"),
    "ch03_晶體鍵結":        ("Kittel 第3章 — 晶體鍵結（Crystal Binding）", "凡得瓦 / 離子 / Madelung / Lennard–Jones"),
    "ch04_聲子":           ("Kittel 第4–5章 — 聲子與晶格振動（Phonons）", "色散 / 聲學光學支 / Debye / 比熱"),
    "ch05_自由電子費米氣體": ("Kittel 第6章 — 自由電子費米氣體（Free Electron Fermi Gas）", "費米能 / DOS / Drude–Sommerfeld"),
    "ch06_能帶":           ("Kittel 第7章 — 能帶（Energy Bands）", "Bloch / 能隙 / 有效質量 / tight-binding"),
    "ch07_半導體":          ("Kittel 第8章 — 半導體晶體（Semiconductor Crystals）", "電洞 / 有效質量 / pn 接面"),
    "ch08_磁性":           ("Kittel 第11–12章 — 抗磁順磁與鐵磁（Magnetism）", "Langevin / Curie / Landau / 鐵磁"),
    "ch09_超導":           ("Kittel 第10章 — 超導現象（Superconductivity）", "Meissner / type I·II / 磁通量子化"),
    "ch10_費米面與進階":     ("Kittel 第9章＋進階 — 費米面與金屬（Fermi Surfaces & beyond）", "費米面 / 量測 / Dirac·graphene"),
}
KGUIDE_UNIT = {  # 章 → 對應單元教學檔 stem
    "ch01_晶體結構": "unit01_晶體結構", "ch02_倒晶格與繞射": "unit02_倒晶格與繞射",
    "ch03_晶體鍵結": "unit03_晶體鍵結", "ch04_聲子": "unit04_聲子與晶格振動",
    "ch05_自由電子費米氣體": "unit05_自由電子費米氣體", "ch06_能帶": "unit06_能帶與Bloch電子",
    "ch07_半導體": "unit07_半導體", "ch08_磁性": "unit08_磁性",
    "ch09_超導": "unit09_超導", "ch10_費米面與進階": "unit10_實驗與進階",
}


def build_kittel_guide():
    """Render 教材/Kittel章節導讀/ch*.md → HTML（每章一頁）+ index.html。"""
    root = os.path.dirname(os.path.dirname(HERE))   # solidstatePhysics/
    gd = os.path.join(root, "教材", "Kittel章節導讀")
    out_built = []
    if not os.path.isdir(gd):
        return out_built
    nav = ('<a href="index.html">章節導讀目錄</a> &nbsp;·&nbsp; '
           '<a href="../Kittel_翻譯.html">完整翻譯</a> &nbsp;·&nbsp; '
           '<a href="../../單元教學/index.html">🎓 單元學科</a> &nbsp;·&nbsp; '
           '<a href="../../考古題/詳解/index.html">逐題詳解</a>')
    cards = []
    for md_path in sorted(glob.glob(os.path.join(gd, "ch*.md"))):
        stem = os.path.basename(md_path)[:-3]
        title, sub = KGUIDE_META.get(stem, (stem, ""))
        out = md_to_html(md_path, f"Kittel 章節導讀 — {title}", nav)
        open(md_path[:-3] + ".html", "w", encoding="utf-8").write(out)
        out_built.append("教材/Kittel章節導讀/" + stem + ".html")
        cards.append(f'  <a class="card" href="{stem}.html">\n'
                     f'    <div class="card-title">{title}</div>\n'
                     f'    <div class="card-sub">{sub}</div>\n'
                     f'  </a>')
    index = KGUIDE_INDEX.replace("__CARDS__", "\n".join(cards))
    open(os.path.join(gd, "index.html"), "w", encoding="utf-8").write(index)
    out_built.append("教材/Kittel章節導讀/index.html")
    return out_built


# Kittel 習題詳解 → (卡片標題, 卡片副標)
KPROB_META = {
    "ch01_晶體結構":        ("第1章 晶體結構 — 習題詳解＋範例", "Kittel Ch1 課本習題全解 + 加碼例題"),
    "ch02_倒晶格與繞射":     ("第2章 倒晶格與繞射 — 習題詳解＋範例", "Kittel Ch2 課本習題全解 + 加碼例題"),
    "ch03_晶體鍵結":        ("第3章 晶體鍵結 — 習題詳解＋範例", "Kittel Ch3 課本習題全解 + 加碼例題"),
    "ch04_聲子":           ("第4–5章 聲子 — 習題詳解＋範例", "Kittel Ch4–5 課本習題全解 + 加碼例題"),
    "ch05_自由電子費米氣體": ("第6章 自由電子費米氣體 — 習題詳解＋範例", "Kittel Ch6 課本習題全解 + 加碼例題"),
    "ch06_能帶":           ("第7章 能帶 — 習題詳解＋範例", "Kittel Ch7 課本習題全解 + 加碼例題"),
    "ch07_半導體":          ("第8章 半導體 — 習題詳解＋範例", "Kittel Ch8 課本習題全解 + 加碼例題"),
    "ch08_磁性":           ("第11–12章 磁性 — 習題詳解＋範例", "Kittel Ch11–12 課本習題全解 + 加碼例題"),
    "ch09_超導":           ("第10章 超導 — 習題詳解＋範例", "Kittel Ch10 課本習題全解 + 加碼例題"),
    "ch10_費米面與進階":     ("第9章 費米面與金屬 — 習題詳解＋範例", "Kittel Ch9 課本習題全解 + 加碼例題"),
}


def build_kittel_problems():
    """Render 教材/Kittel習題詳解/ch*.md → HTML（每章一頁）+ index.html。"""
    root = os.path.dirname(os.path.dirname(HERE))   # solidstatePhysics/
    pd = os.path.join(root, "教材", "Kittel習題詳解")
    out_built = []
    if not os.path.isdir(pd):
        return out_built
    nav = ('<a href="index.html">習題詳解目錄</a> &nbsp;·&nbsp; '
           '<a href="../Kittel章節導讀/index.html">章節導讀</a> &nbsp;·&nbsp; '
           '<a href="../../單元教學/index.html">🎓 單元學科</a> &nbsp;·&nbsp; '
           '<a href="../../考古題/詳解/index.html">逐題詳解</a>')
    cards = []
    for md_path in sorted(glob.glob(os.path.join(pd, "ch*.md"))):
        stem = os.path.basename(md_path)[:-3]
        title, sub = KPROB_META.get(stem, (stem, ""))
        out = md_to_html(md_path, f"Kittel 習題詳解 — {title}", nav)
        open(md_path[:-3] + ".html", "w", encoding="utf-8").write(out)
        out_built.append("教材/Kittel習題詳解/" + stem + ".html")
        cards.append(f'  <a class="card" href="{stem}.html">\n'
                     f'    <div class="card-title">{title}</div>\n'
                     f'    <div class="card-sub">{sub}</div>\n'
                     f'  </a>')
    index = KPROB_INDEX.replace("__CARDS__", "\n".join(cards))
    open(os.path.join(pd, "index.html"), "w", encoding="utf-8").write(index)
    out_built.append("教材/Kittel習題詳解/index.html")
    return out_built


PREREQ_META = {
    "數學先備": ("🔢 數學先備知識", "向量/複數/傅立葉/級數/微積分 — 讀 Kittel 前要會的數學，附範例與圖"),
    "物理先備": ("⚛️ 物理先備知識", "波/簡諧/量子井/波茲曼/庫侖/磁矩 — 讀 Kittel 前要會的物理，附範例與圖"),
}


def build_prereq():
    """Render 教材/先備知識/*.md → HTML（含數學/物理先備）+ index.html。"""
    root = os.path.dirname(os.path.dirname(HERE))   # solidstatePhysics/
    pq = os.path.join(root, "教材", "先備知識")
    out_built = []
    if not os.path.isdir(pq):
        return out_built
    nav = ('<a href="index.html">先備知識目錄</a> &nbsp;·&nbsp; '
           '<a href="../index.html">← 教材直讀</a> &nbsp;·&nbsp; '
           '<a href="../Kittel章節導讀/index.html">📑 章節導讀</a> &nbsp;·&nbsp; '
           '<a href="../../單元教學/index.html">🎓 單元學科</a>')
    cards = []
    for stem in ("數學先備", "物理先備"):
        md_path = os.path.join(pq, stem + ".md")
        if not os.path.exists(md_path):
            continue
        title, sub = PREREQ_META.get(stem, (stem, ""))
        out = md_to_html(md_path, f"固態物理先備知識 — {title}", nav)
        open(os.path.join(pq, stem + ".html"), "w", encoding="utf-8").write(out)
        out_built.append("教材/先備知識/" + stem + ".html")
        cards.append(f'  <a class="card" href="{stem}.html">\n'
                     f'    <div class="card-title">{title}</div>\n'
                     f'    <div class="card-sub">{sub}</div>\n'
                     f'  </a>')
    index = PREREQ_INDEX.replace("__CARDS__", "\n".join(cards))
    open(os.path.join(pq, "index.html"), "w", encoding="utf-8").write(index)
    out_built.append("教材/先備知識/index.html")
    return out_built


INDEX = r"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>固態物理導論資格考 — 逐題詳解</title>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
         max-width: 900px; margin: 2em auto; padding: 0 1.2em 4em; line-height: 1.7; color: #222; background: #fafafa; }
  h1 { color: #1a4d7c; border-bottom: 3px solid #1a4d7c; padding-bottom: 0.3em; }
  p.intro { color: #444; }
  .card { display: block; text-decoration: none; color: inherit; background: #fff; border: 1px solid #c5d5e5;
          border-radius: 10px; padding: 0.9em 1.2em; margin: 0.8em 0; box-shadow: 0 1px 3px rgba(0,0,0,0.04);
          transition: box-shadow 0.15s, border-color 0.15s, transform 0.05s; }
  .card:hover { border-color: #1a4d7c; box-shadow: 0 3px 10px rgba(26,77,124,0.15); transform: translateY(-1px); }
  .card.ref { background: #f3f8ee; border-color: #b6cf9a; }
  .card.ref:hover { border-color: #5c8a2f; box-shadow: 0 3px 10px rgba(92,138,47,0.18); }
  .card.ref .card-title { color: #3f6b1e; }
  .card-title { color: #1a4d7c; font-weight: 700; font-size: 1.12em; }
  .card-sub { color: #555; font-size: 0.95em; margin-top: 0.25em; }
  .note { background: #eef5fb; border-left: 4px solid #6aa1d6; border-radius: 4px; padding: 0.6em 1em; color: #334; font-size: 0.93em; }
</style>
</head>
<body>
<div class="note" style="margin-bottom:1em;"><a href="../導讀.html">導讀</a> &nbsp;·&nbsp; <a href="../單元整理.html">單元整理</a> &nbsp;·&nbsp; <a href="../../單元教學/index.html">🎓 單元學科（從高中教起）</a> &nbsp;·&nbsp; <a href="../../教材/index.html">📖 教材直讀</a></div>
<h1>📚 固態物理導論資格考 — 逐題詳解</h1>
<p class="intro">NTU 應物所博士班資格考「固態物理導論」歷年考題的「符號就地展開」教學版。仿 QFT tutorial 方法。先學科後練題：先看 <a href="../../單元教學/index.html">🎓 單元學科</a> 從高中建到考試級，再回這裡練歷年題。</p>
<div class="note">📖 想知道「先讀什麼、配哪本教材」？先看 <a href="../導讀.html"><b>固態物理導讀（近10年 × 教材三層）</b></a>。<br>讀法：卡在哪個觀念就先點開「🧰 共用觀念與公式」的 <code>▸</code> → 回到該年詳解，跟著每題的 Step 一步步走 → 看「自我檢核」與「信心」。圖形題會內嵌原卷算繪圖。</div>
__CARDS__
<hr style="border:none;border-top:1px solid #ccc;margin:2.5em 0;">
<p style="color:#888;font-size:0.85em;">由 <code>_build_html.py</code> 產生（MathJax + marked，與 QFT tutorials 同模板）。新增 <code>固態_&lt;年&gt;_詳解.md</code> 後重跑即自動收錄。</p>
</body>
</html>
"""


JIAOCAI_INDEX = r"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>固態物理導論 — 教材直讀目錄</title>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
         max-width: 900px; margin: 2em auto; padding: 0 1.2em 4em; line-height: 1.7; color: #222; background: #fafafa; }
  h1 { color: #1a4d7c; border-bottom: 3px solid #1a4d7c; padding-bottom: 0.3em; }
  p.intro { color: #444; }
  .card { display: block; text-decoration: none; color: inherit; background: #fff; border: 1px solid #c5d5e5;
          border-radius: 10px; padding: 0.9em 1.2em; margin: 0.8em 0; box-shadow: 0 1px 3px rgba(0,0,0,0.04);
          transition: box-shadow 0.15s, border-color 0.15s, transform 0.05s; }
  .card:hover { border-color: #1a4d7c; box-shadow: 0 3px 10px rgba(26,77,124,0.15); transform: translateY(-1px); }
  .card-title { color: #1a4d7c; font-weight: 700; font-size: 1.12em; }
  .card-sub { color: #555; font-size: 0.95em; margin-top: 0.25em; }
  .note { background: #eef5fb; border-left: 4px solid #6aa1d6; border-radius: 4px; padding: 0.6em 1em; color: #334; font-size: 0.93em; }
  .nav { font-size: 0.92em; margin: 0 0 1em; color: #555; }
  .nav a { color: #1a4d7c; text-decoration: none; } .nav a:hover { text-decoration: underline; }
</style>
</head>
<body>
<div class="nav"><a href="../考古題/導讀.html">導讀</a> &nbsp;·&nbsp; <a href="../考古題/單元整理.html">單元整理</a> &nbsp;·&nbsp; <a href="../單元教學/index.html">🎓 單元學科</a> &nbsp;·&nbsp; <a href="../考古題/詳解/index.html">逐題詳解</a></div>
<h1>📖 固態物理導論 — 教材直讀</h1>
<p class="intro">把 <code>教材/</code> 各本課本轉成可直接閱讀的網頁（公式以純文字呈現，原圖在 PDF→md 轉檔時已略去）。每頁有左側目錄、可全文 <kbd>⌘F</kbd> 搜尋。建議讀法見 <a href="../考古題/導讀.html">導讀（三層讀法）</a>。</p>
<div class="note">📚 <b>三層讀法</b>：快入門→<b>簡報 / 林盛煇</b>；打底（考試符號）→<b>Kittel 原文＋林盛煇對照</b>；進階→<b>講義</b>。卡住就回到對應那層。</div>
  <a class="card" href="先備知識/index.html" style="background:#eef9ee;border-color:#9ccc9c;">
    <div class="card-title" style="color:#2e7d32;">🧰 先備知識補帖（讀不下去先補這個）</div>
    <div class="card-sub">數學/物理先備（向量·複數·傅立葉·波茲曼·簡諧·庫侖…）每項：高中起點＋範例＋圖＋用在哪</div>
  </a>
  <a class="card" href="Kittel章節導讀/index.html" style="background:#fff8ee;border-color:#e0b97a;">
    <div class="card-title" style="color:#9a6a1e;">📑 Kittel 章節對照導讀（讀翻譯本前先看這個）</div>
    <div class="card-sub">每章：三層概念對應（高中→大學→固態）＋專有名詞×範例速查，把機器翻譯翻成人話</div>
  </a>
  <a class="card" href="Kittel習題詳解/index.html" style="background:#fff8ee;border-color:#e0b97a;">
    <div class="card-title" style="color:#9a6a1e;">🧮 Kittel 習題詳解 ＋ 加碼範例</div>
    <div class="card-sub">每章加碼範例 ＋ Kittel 課本習題（~90 題）完整逐步解答、答案 boxed</div>
  </a>
__CARDS__
<hr style="border:none;border-top:1px solid #ccc;margin:2.5em 0;">
<p style="color:#888;font-size:0.85em;">由 <code>考古題/詳解/_build_html.py</code> 產生（MathJax + marked，與其餘頁面同模板）。原始 PDF 全數保留在 <code>ref/</code>。</p>
</body>
</html>
"""


UNITS_INDEX = r"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>固態物理導論 — 單元學科完整版 ＆ 全公式速查大全（含出處 Ref）</title>
<script>
window.MathJax = {
  loader: { load: ['[tex]/boldsymbol'] },
  tex: { packages: {'[+]': ['boldsymbol']}, inlineMath: [['$','$']], displayMath: [['$$','$$']], processEscapes: true, tags: 'none' },
  options: { skipHtmlTags: ['script','noscript','style','textarea','pre','code'] },
  svg: { fontCache: 'global' }
};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
<style>
  :root {
    --primary: #1a4d7c;
    --primary-light: #2b6ca0;
    --primary-subtle: #eef5fb;
    --border-color: #c5d5e5;
    --text-main: #222;
    --text-muted: #555;
    --bg-page: #f8fafc;
    --bg-card: #ffffff;
    --sidebar-w: 260px;
    --radius: 10px;
  }
  * { box-sizing: border-box; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
    margin: 0; padding: 0; color: var(--text-main); background: var(--bg-page); line-height: 1.7;
    display: flex; min-height: 100vh;
  }
  html { scroll-behavior: smooth; }

  /* Sidebar */
  #sidebar {
    position: fixed; top: 0; left: 0; bottom: 0; width: var(--sidebar-w);
    background: #ffffff; border-right: 1px solid var(--border-color);
    padding: 1.5em 1em 2em; overflow-y: auto; z-index: 100;
    transition: transform 0.25s ease;
  }
  .brand { font-size: 1.15em; font-weight: 700; color: var(--primary); margin-bottom: 0.3em; display: flex; align-items: center; gap: 0.4em; }
  .brand-sub { font-size: 0.8em; color: var(--text-muted); margin-bottom: 1.2em; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.8em; }
  .search-box { margin-bottom: 1.2em; }
  .search-box input {
    width: 100%; padding: 7px 10px; font-size: 0.88em; border: 1px solid var(--border-color);
    border-radius: 6px; outline: none; background: #fafcfe;
  }
  .search-box input:focus { border-color: var(--primary); background: #fff; box-shadow: 0 0 0 2px rgba(26,77,124,0.15); }
  .nav-group-title { font-size: 0.76em; font-weight: 700; color: #8898aa; text-transform: uppercase; letter-spacing: 0.05em; margin: 1.2em 0 0.4em 0.3em; }
  .nav-link {
    display: block; padding: 5px 8px; font-size: 0.88em; color: #334e68; text-decoration: none;
    border-radius: 6px; transition: background 0.12s, color 0.12s; margin-bottom: 2px;
  }
  .nav-link:hover, .nav-link.active { background: var(--primary-subtle); color: var(--primary); font-weight: 600; }
  .nav-link.sub { padding-left: 1.6em; font-size: 0.84em; color: #627d98; }

  /* Main Container */
  #main {
    margin-left: var(--sidebar-w); flex: 1; padding: 2.2em 2.5em 5em; max-width: 1100px;
  }
  #toc-toggle {
    display: none; position: fixed; top: 12px; left: 12px; z-index: 101;
    background: var(--primary); color: #fff; border: none; border-radius: 6px;
    padding: 7px 12px; font-size: 0.9em; cursor: pointer; box-shadow: 0 2px 6px rgba(0,0,0,0.18);
  }

  /* Header & Breadcrumb */
  .top-nav { font-size: 0.9em; margin-bottom: 1.2em; color: var(--text-muted); display: flex; flex-wrap: wrap; gap: 0.6em; }
  .top-nav a { color: var(--primary); text-decoration: none; }
  .top-nav a:hover { text-decoration: underline; }
  h1 { color: var(--primary); font-size: 1.85em; margin: 0 0 0.4em; border-bottom: 3px solid var(--primary); padding-bottom: 0.3em; }
  .intro { color: #486581; font-size: 1.02em; margin-bottom: 1.4em; line-height: 1.65; }

  /* Alerts / Notes */
  .note {
    background: var(--primary-subtle); border-left: 4px solid var(--primary-light);
    border-radius: 6px; padding: 0.9em 1.2em; color: #102a43; font-size: 0.93em; margin: 1.4em 0;
  }

  /* Unit Cards Grid */
  .grid-units {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(310px, 1fr)); gap: 1em; margin: 1.5em 0 2.5em;
  }
  .card {
    display: flex; flex-direction: column; text-decoration: none; color: inherit;
    background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius);
    padding: 1.1em 1.3em; box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    transition: transform 0.15s, border-color 0.15s, box-shadow 0.15s;
  }
  .card:hover { border-color: var(--primary); transform: translateY(-2px); box-shadow: 0 4px 14px rgba(26,77,124,0.12); }
  .card-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.3em; }
  .card-title { color: var(--primary); font-weight: 700; font-size: 1.08em; }
  .card-sub { color: #486581; font-size: 0.9em; flex-grow: 1; }
  .tier {
    font-size: 0.72em; font-weight: 700; color: #fff; background: #486581;
    border-radius: 12px; padding: 2px 9px; white-space: nowrap; margin-left: 0.5em;
  }
  .tier.tier-1 { background: #d9383a; }
  .tier.tier-2 { background: #e06c00; }
  .tier.tier-3 { background: #2f855a; }
  .tier.tier-4 { background: #627d98; }

  /* Formula Master Section */
  h2.section-title {
    color: var(--primary); font-size: 1.4em; border-bottom: 2px solid #cbd5e1;
    padding-bottom: 0.3em; margin: 2.2em 0 1em; display: flex; align-items: center; justify-content: space-between;
  }
  .unit-formula-block {
    background: #ffffff; border: 1px solid var(--border-color); border-radius: var(--radius);
    padding: 1.3em 1.6em; margin: 1.2em 0 1.8em; box-shadow: 0 1px 4px rgba(0,0,0,0.02);
  }
  .unit-formula-header {
    display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e2e8f0;
    padding-bottom: 0.6em; margin-bottom: 1em;
  }
  .unit-formula-title { font-size: 1.15em; font-weight: 700; color: var(--primary); display: flex; align-items: center; gap: 0.5em; }
  .formula-item {
    background: #fbfcfe; border: 1px solid #e1eaf2; border-radius: 8px;
    padding: 0.9em 1.2em; margin: 0.8em 0; position: relative;
  }
  .formula-name { font-weight: 700; color: #102a43; font-size: 0.95em; margin-bottom: 0.3em; display: flex; justify-content: space-between; align-items: center; }
  .formula-desc { font-size: 0.88em; color: #486581; margin-top: 0.3em; }
  .formula-ref {
    font-size: 0.82em; color: #1a4d7c; background: #f0f7fd; border-left: 3px solid #6aa1d6;
    padding: 4px 9px; border-radius: 4px; margin-top: 0.6em; display: flex; align-items: center; flex-wrap: wrap; gap: 0.4em;
  }
  .formula-ref a { color: #1a4d7c; text-decoration: underline; }
  .btn-copy {
    background: #f0f4f8; border: 1px solid #cbd5e1; border-radius: 4px;
    font-size: 0.75em; padding: 2px 7px; color: #486581; cursor: pointer; transition: all 0.12s;
  }
  .btn-copy:hover { background: var(--primary-subtle); color: var(--primary); border-color: var(--primary); }

  /* Toast Notification */
  #toast {
    position: fixed; bottom: 25px; right: 25px; background: #102a43; color: #fff;
    padding: 8px 16px; border-radius: 6px; font-size: 0.85em; display: none; z-index: 1000;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
  }

  @media (max-width: 900px) {
    #sidebar { transform: translateX(-100%); }
    #sidebar.open { transform: translateX(0); box-shadow: 4px 0 20px rgba(0,0,0,0.18); }
    #toc-toggle { display: block; }
    #main { margin-left: 0; padding: 4em 1.2em 4em; }
  }
  @media print {
    #sidebar, #toc-toggle { display: none !important; }
    #main { margin: 0 !important; padding: 0 !important; max-width: 100% !important; }
  }
</style>
</head>
<body>

<button id="toc-toggle" type="button" aria-label="開關側邊導覽">☰ 目錄</button>

<nav id="sidebar">
  <div class="brand">🎓 固態物理導論</div>
  <div class="brand-sub">單元學科 ＆ 全公式速查大全</div>

  <div class="search-box">
    <input type="text" id="formula-search" placeholder="🔍 搜尋公式、概念、出處或年份..." autocomplete="off">
  </div>

  <div class="nav-group-title">快捷跳轉</div>
  <a class="nav-link" href="#overview">🧭 總覽與路線</a>
  <a class="nav-link" href="#units-grid">📚 十大單元全覽</a>
  <a class="nav-link" href="#formula-master">🧮 全單元公式速查（含 Ref）</a>

  <div class="nav-group-title">公式速查分單元</div>
  <a class="nav-link sub" href="#f-unit01">01 晶體結構</a>
  <a class="nav-link sub" href="#f-unit02">02 倒晶格與繞射</a>
  <a class="nav-link sub" href="#f-unit03">03 晶體鍵結</a>
  <a class="nav-link sub" href="#f-unit04">04 聲子振動</a>
  <a class="nav-link sub" href="#f-unit05">05 自由電子氣</a>
  <a class="nav-link sub" href="#f-unit06">06 能帶理論</a>
  <a class="nav-link sub" href="#f-unit07">07 半導體物理</a>
  <a class="nav-link sub" href="#f-unit08">08 磁性</a>
  <a class="nav-link sub" href="#f-unit09">09 超導現象</a>
  <a class="nav-link sub" href="#f-unit10">10 實驗與進階</a>

  <div class="nav-group-title">全站導航</div>
  <a class="nav-link" href="../考古題/導讀.html">🧭 備考導讀</a>
  <a class="nav-link" href="../考古題/單元整理.html">📊 單元考頻整理</a>
  <a class="nav-link" href="../考古題/詳解/index.html">✍️ 歷年逐題詳解</a>
  <a class="nav-link" href="../教材/index.html">📖 教材直讀</a>
  <a class="nav-link" href="../_質檢報告_主表.html">✅ 質檢真值報告</a>
  <a class="nav-link" href="https://github.com/Yueh-H/AItotur/tree/main/solidstatePhysics/單元教學" target="_blank" rel="noopener">🐙 GitHub 專案目錄</a>
</nav>

<div id="main">
  <div class="top-nav">
    <a href="../index.html">總入口</a> &nbsp;/&nbsp;
    <a href="../考古題/導讀.html">導讀</a> &nbsp;/&nbsp;
    <a href="../考古題/單元整理.html">單元整理</a> &nbsp;/&nbsp;
    <a href="../考古題/詳解/index.html">逐題詳解</a> &nbsp;/&nbsp;
    <a href="../教材/index.html">教材直讀</a> &nbsp;/&nbsp;
    <span style="color:#627d98;">單元學科 ＆ 公式大全（含 Ref）</span>
  </div>

  <h1 id="overview">🎓 固態物理導論 — 單元學科完整版 ＆ 全公式速查大全（含出處 Ref）</h1>
  <p class="intro">
    以 <b>C. Kittel《Introduction to Solid State Physics》8th ed.</b> 經典範疇為核心，將全科目重構為 10 大單元，教學堅持「<b>高中起步 $\to$ 符號就地展開 $\to$ 資格考真題推導</b>」。<br>
    本頁整合 <b>10 大單元完整講義</b> 與 <b>資格考全公式速查手冊（Master Formula Sheet）</b>，所有物理量與公式皆附帶 <b>Kittel 教材章節頁碼、公式編號與歷年台大資格考真題出處（Ref）</b>。支援公式即時搜尋、MathJax 完美排版與一鍵複製 LaTeX 原始碼。
  </p>

  <div class="note">
    📐 <b>高效備考四梯隊路線</b>：<br>
    • <b>第一梯隊（先吃滿 ≥60% 分數）</b>：01 晶體結構、02 倒晶格與繞射、04 聲子振動、06 能帶理論。<br>
    • <b>第二梯隊（高頻重點）</b>：03 晶體鍵結、05 自由電子費米氣體。<br>
    • <b>第三梯隊（週期必考）</b>：07 半導體物理。<br>
    • <b>第四梯隊（近年回溫）</b>：08 磁性、09 超導現象、10 實驗技術與進階主題。
  </div>

  <h2 class="section-title" id="units-grid">
    <span>📚 十大單元全覽（點選進入個別單元深入講義）</span>
  </h2>
  <div class="grid-units">
__CARDS__
  </div>

  <h2 class="section-title" id="formula-master">
    <span>🧮 固態物理全單元核心公式速查大全（Master Formula Sheet ＆ Ref）</span>
    <span style="font-size:0.65em;font-weight:400;color:#627d98;">支援搜尋快篩 ＆ 點擊複製 LaTeX</span>
  </h2>

  <!-- Unit 01 Formula Block -->
  <div class="unit-formula-block" id="f-unit01" data-tags="unit01 晶體結構 crystal structure packing fraction bcc fcc sc diamond hcp miller 密勒指標 填充率 晶格 kittel ch1 2013 2014 2015 2020 2021 2023 2024 2025">
    <div class="unit-formula-header">
      <div class="unit-formula-title">單元 01：晶體結構（Crystal Structure）</div>
      <a href="unit01_晶體結構.html" style="font-size:0.85em;color:var(--primary);text-decoration:none;">查看詳細講義 →</a>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>晶格向量與平移週期性</span>
        <button class="btn-copy" onclick="copyLatex('\\mathbf R = n_1 \\mathbf a_1 + n_2 \\mathbf a_2 + n_3 \\mathbf a_3, \\quad n_i \\in \\mathbb Z')">📋 複製 LaTeX</button>
      </div>
      <div>$$\mathbf R = n_1 \mathbf a_1 + n_2 \mathbf a_2 + n_3 \mathbf a_3, \quad n_i \in \mathbb Z$$</div>
      <div class="formula-desc">實空間布拉菲晶格（Bravais lattice）之點陣定義，三整數線性組合生成全晶格。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 1 p. 4 ｜ 林盛煇 §1.2 ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013</a>, <a href="../考古題/詳解/固態_2014_詳解.html">2014</a>, <a href="../考古題/詳解/固態_2024_詳解.html">2024 Q1</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>原胞體積（Primitive Cell Volume）</span>
        <button class="btn-copy" onclick="copyLatex('V_p = |\\mathbf a_1 \\cdot (\\mathbf a_2 \\times \\mathbf a_3)|')">📋 複製 LaTeX</button>
      </div>
      <div>$$V_p = |\mathbf a_1 \cdot (\mathbf a_2 \times \mathbf a_3)|$$</div>
      <div class="formula-desc">基底向量構成之純量三重積。每個原胞（primitive cell）只包含恰好 1 個格點。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 1 p. 7 ｜ 歷年考題：<a href="../考古題/詳解/固態_2024_詳解.html">2024 Q1</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>密勒指標晶面間距（正交立方晶系）</span>
        <button class="btn-copy" onclick="copyLatex('d_{hkl} = \\frac{a}{\\sqrt{h^2 + k^2 + l^2}}')">📋 複製 LaTeX</button>
      </div>
      <div>$$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}, \quad [hkl] \perp (hkl)$$</div>
      <div class="formula-desc">立方晶系中相鄰兩 $(hkl)$ 面間距，且晶向 $[hkl]$ 嚴格垂直於 $(hkl)$ 晶面。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 1 Eq. (16) p. 13 ｜ 林盛煇 §1.4 ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013</a>, <a href="../考古題/詳解/固態_2014_詳解.html">2014</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>各結構填充率（Packing Fraction, PF）</span>
        <button class="btn-copy" onclick="copyLatex('\\text{SC}=\\frac{\\pi}{6}\\approx0.524,\\; \\text{BCC}=\\frac{\\sqrt{3}\\pi}{8}\\approx0.680,\\; \\text{FCC}=\\frac{\\sqrt{2}\\pi}{6}\\approx0.740,\\; \\text{Dia}=\\frac{\\sqrt{3}\\pi}{16}\\approx0.340')">📋 複製 LaTeX</button>
      </div>
      <div>$$\text{SC}: \frac{\pi}{6} \approx 0.524, \quad \text{BCC}: \frac{\sqrt{3}\pi}{8} \approx 0.680, \quad \text{FCC}: \frac{\sqrt{2}\pi}{6} \approx 0.740, \quad \text{Diamond}: \frac{\sqrt{3}\pi}{16} \approx 0.340$$</div>
      <div class="formula-desc">以球心剛球相切幾何推導。HCP 理想填充率與 FCC 相同（0.740）。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 1 Table 2 p. 11 ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013</a>, <a href="../考古題/詳解/固態_2015_詳解.html">2015</a>, <a href="../考古題/詳解/固態_2020_詳解.html">2020</a>, <a href="../考古題/詳解/固態_2021_詳解.html">2021</a>, <a href="../考古題/詳解/固態_2023_詳解.html">2023</a>, <a href="../考古題/詳解/固態_2024_詳解.html">2024</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>HCP 理想軸比</span>
        <button class="btn-copy" onclick="copyLatex('\\frac{c}{a} = \\sqrt{\\frac{8}{3}} \\approx 1.633')">📋 複製 LaTeX</button>
      </div>
      <div>$$\frac{c}{a} = \sqrt{\frac{8}{3}} \approx 1.633$$</div>
      <div class="formula-desc">六方最密堆積相鄰三原子與上一層原子構成正四面體之幾何解。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 1 p. 15 ｜ 歷年考題：<a href="../考古題/詳解/固態_2015_詳解.html">2015</a>, <a href="../考古題/詳解/固態_2021_詳解.html">2021</a>, <a href="../考古題/詳解/固態_2024_詳解.html">2024</a></div>
    </div>
  </div>

  <!-- Unit 02 Formula Block -->
  <div class="unit-formula-block" id="f-unit02" data-tags="unit02 倒晶格與繞射 reciprocal lattice diffraction bragg laue structure factor extinction 消光 結構因子 kittel ch2 2013 2014 2015 2016 2018 2021 2022 2023 2025">
    <div class="unit-formula-header">
      <div class="unit-formula-title">單元 02：倒晶格與繞射（Reciprocal Lattice & Diffraction）</div>
      <a href="unit02_倒晶格與繞射.html" style="font-size:0.85em;color:var(--primary);text-decoration:none;">查看詳細講義 →</a>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>倒晶格基底向量（Reciprocal Lattice Vectors）</span>
        <button class="btn-copy" onclick="copyLatex('\\mathbf b_1 = 2\\pi \\frac{\\mathbf a_2 \\times \\mathbf a_3}{\\mathbf a_1 \\cdot (\\mathbf a_2 \\times \\mathbf a_3)}, \\quad \\mathbf a_i \\cdot \\mathbf b_j = 2\\pi \\delta_{ij}')">📋 複製 LaTeX</button>
      </div>
      <div>$$\mathbf b_1 = 2\pi \frac{\mathbf a_2 \times \mathbf a_3}{\mathbf a_1 \cdot (\mathbf a_2 \times \mathbf a_3)}, \quad \mathbf b_2 = 2\pi \frac{\mathbf a_3 \times \mathbf a_1}{\mathbf a_1 \cdot (\mathbf a_2 \times \mathbf a_3)}, \quad \mathbf b_3 = 2\pi \frac{\mathbf a_1 \times \mathbf a_2}{\mathbf a_1 \cdot (\mathbf a_2 \times \mathbf a_3)}$$</div>
      <div class="formula-desc">倒空間基底定義，$\mathbf G = h\mathbf b_1 + k\mathbf b_2 + l\mathbf b_3$ 且長度 $|\mathbf G| = 2\pi / d_{hkl}$。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 2 Eq. (13) p. 34 ｜ 林盛煇 §2.2 ｜ 歷年考題：<a href="../考古題/詳解/固態_2015_詳解.html">2015</a>, <a href="../考古題/詳解/固態_2016_詳解.html">2016</a>, <a href="../考古題/詳解/固態_2022_詳解.html">2022</a>, <a href="../考古題/詳解/固態_2024_詳解.html">2024</a>, <a href="../考古題/詳解/固態_2025_詳解.html">2025</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>布拉格定律與勞厄繞射條件（等價性）</span>
        <button class="btn-copy" onclick="copyLatex('2d\\sin\\theta = n\\lambda \\iff \\Delta\\mathbf k = \\mathbf G \\iff 2\\mathbf k \\cdot \\mathbf G = |\\mathbf G|^2')">📋 複製 LaTeX</button>
      </div>
      <div>$$2d\sin\theta = n\lambda \iff \Delta\mathbf k = \mathbf k' - \mathbf k = \mathbf G \iff 2\mathbf k \cdot \mathbf G = |\mathbf G|^2$$</div>
      <div class="formula-desc">實空間幾何光徑差與倒空間動量轉移守恆之等價描述；Ewald 球與 BZ 邊界平分面之幾何起源。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 2 Eq. (1), (18)–(25) p. 30, 36–37 ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013</a>, <a href="../考古題/詳解/固態_2014_詳解.html">2014</a>, <a href="../考古題/詳解/固態_2016_詳解.html">2016</a>, <a href="../考古題/詳解/固態_2018_詳解.html">2018</a>, <a href="../考古題/詳解/固態_2023_詳解.html">2023</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>幾何結構因子與四大晶格消光規則</span>
        <button class="btn-copy" onclick="copyLatex('S_{\\mathbf G} = \\sum_{j=1}^p f_j e^{-i \\mathbf G \\cdot \\mathbf r_j}')">📋 複製 LaTeX</button>
      </div>
      <div>$$S_{\mathbf G} = \sum_{j=1}^p f_j e^{-i \mathbf G \cdot \mathbf r_j}, \quad I \propto |S_{\mathbf G}|^2$$</div>
      <div class="formula-desc">
        • <b>BCC</b>：$h+k+l$ 偶數允許反射，奇數消光 ($S=0$)<br>
        • <b>FCC</b>：$h,k,l$ 全奇或全偶允許反射，奇偶混雜消光 ($S=0$)<br>
        • <b>Diamond</b>：全奇數允許；全偶數且 $h+k+l=4n$ 允許；$h+k+l=4n+2$ 消光（例如 (200), (222) 消光）
      </div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 2 Eq. (39), (42)–(44) p. 42–45 ｜ 林盛煇 §2.4 ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013</a>, <a href="../考古題/詳解/固態_2014_詳解.html">2014</a>, <a href="../考古題/詳解/固態_2016_詳解.html">2016</a>, <a href="../考古題/詳解/固態_2018_詳解.html">2018</a>, <a href="../考古題/詳解/固態_2021_詳解.html">2021</a></div>
    </div>
  </div>

  <!-- Unit 03 Formula Block -->
  <div class="unit-formula-block" id="f-unit03" data-tags="unit03 晶體鍵結 crystal binding lennard-jones madelung cohesive energy 凡得瓦 馬德隆 內聚能 kittel ch3 2013 2014 2015 2016 2020 2023 2024">
    <div class="unit-formula-header">
      <div class="unit-formula-title">單元 03：晶體鍵結（Crystal Binding）</div>
      <a href="unit03_晶體鍵結.html" style="font-size:0.85em;color:var(--primary);text-decoration:none;">查看詳細講義 →</a>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>藍納–瓊斯（Lennard-Jones）12-6 位能與 FCC 平衡內聚能</span>
        <button class="btn-copy" onclick="copyLatex('U(r) = 4\\varepsilon \\left[ \\left(\\frac{\\sigma}{r}\\right)^{12} - \\left(\\frac{\\sigma}{r}\\right)^6 \\right], \\quad R_0 \\approx 1.09\\sigma, \\quad U_{\\text{tot}}(R_0) \\approx -8.61 N\\varepsilon')">📋 複製 LaTeX</button>
      </div>
      <div>$$U(r) = 4\varepsilon \left[ \left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^6 \right] \implies R_0 \approx 1.09\sigma, \quad U_{\text{tot}}(R_0) \approx -8.61 N\varepsilon$$</div>
      <div class="formula-desc">$r^{-12}$ 為泡利排斥，$r^{-6}$ 為誘導偶極凡得瓦吸引。由晶格和 $A_{12}\approx12.13, A_6\approx14.45$ 導出。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 3 Eq. (2), (8)–(12) Table 4 p. 55–60 ｜ 林盛煇 §3.2 ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013</a>, <a href="../考古題/詳解/固態_2014_詳解.html">2014</a>, <a href="../考古題/詳解/固態_2015_詳解.html">2015</a>, <a href="../考古題/詳解/固態_2016_詳解.html">2016</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>離子晶體位能與馬德隆常數（Madelung Constant）</span>
        <button class="btn-copy" onclick="copyLatex('U_{\\text{tot}} = N \\left( -\\frac{\\alpha e^2}{4\\pi\\varepsilon_0 R} + \\frac{z B}{R^n} \\right), \\quad \\alpha_{\\text{1D}} = 2\\ln 2')">📋 複製 LaTeX</button>
      </div>
      <div>$$U_{\text{tot}} = N \left( -\frac{\alpha e^2}{4\pi\varepsilon_0 R} + \frac{z B}{R^n} \right), \quad \alpha_{\text{1D}} = 2\ln 2 \approx 1.386, \quad \alpha_{\text{NaCl}} \approx 1.7476$$</div>
      <div class="formula-desc">長程庫侖交錯級數求和。1D 離子鏈：$\alpha = 2(1 - 1/2 + 1/3 - 1/4 + \dots) = 2\ln 2$。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 3 Eq. (20)–(23), Table 7 p. 64–65 ｜ 歷年考題：<a href="../考古題/詳解/固態_2020_詳解.html">2020</a>, <a href="../考古題/詳解/固態_2023_詳解.html">2023 Q1</a>, <a href="../考古題/詳解/固態_2024_詳解.html">2024 Q2</a></div>
    </div>
  </div>

  <!-- Unit 04 Formula Block -->
  <div class="unit-formula-block" id="f-unit04" data-tags="unit04 聲子 晶格振動 phonons vibrations dispersion debye dulong-petit 色散 德拜 比熱 kittel ch4 ch5 2013 2014 2015 2016 2018 2019 2020 2021 2023 2024">
    <div class="unit-formula-header">
      <div class="unit-formula-title">單元 04：聲子與晶格振動（Phonons / Vibrations）</div>
      <a href="unit04_聲子與晶格振動.html" style="font-size:0.85em;color:var(--primary);text-decoration:none;">查看詳細講義 →</a>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>單原子鏈色散關係與群速度</span>
        <button class="btn-copy" onclick="copyLatex('\\omega(K) = 2\\sqrt{\\frac{C}{M}}\\left|\\sin\\left(\\frac{Ka}{2}\\right)\\right|, \\quad v_g = \\frac{d\\omega}{dK} = a\\sqrt{\\frac{C}{M}}\\cos\\left(\\frac{Ka}{2}\\right)')">📋 複製 LaTeX</button>
      </div>
      <div>$$\omega(K) = 2\sqrt{\frac{C}{M}}\left|\sin\left(\frac{Ka}{2}\right)\right|, \quad \omega_{\max} = 2\sqrt{\frac{C}{M}}, \quad v_s = a\sqrt{\frac{C}{M}}$$</div>
      <div class="formula-desc">最高頻發生在 BZ 邊界 $K=\pi/a$，群速度 $v_g = 0$（駐波）；長波極限 $K\to 0$ 呈現線性聲波。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 4 Eq. (9)–(16) p. 89–92 ｜ 林盛煇 §4.2 ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013</a>, <a href="../考古題/詳解/固態_2019_詳解.html">2019</a>, <a href="../考古題/詳解/固態_2021_詳解.html">2021</a>, <a href="../考古題/詳解/固態_2023_詳解.html">2023</a>, <a href="../考古題/詳解/固態_2024_詳解.html">2024</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>雙原子鏈聲學支、光學支與邊界能隙</span>
        <button class="btn-copy" onclick="copyLatex('\\omega^2 = C\\left(\\frac{1}{M_1}+\\frac{1}{M_2}\\right) \\pm C\\sqrt{\\left(\\frac{1}{M_1}+\\frac{1}{M_2}\\right)^2 - \\frac{4\\sin^2(Ka/2)}{M_1 M_2}}')">📋 複製 LaTeX</button>
      </div>
      <div>$$\omega^2 = C\left(\frac{1}{M_1}+\frac{1}{M_2}\right) \pm C\sqrt{\left(\frac{1}{M_1}+\frac{1}{M_2}\right)^2 - \frac{4\sin^2(Ka/2)}{M_1 M_2}}$$</div>
      <div class="formula-desc">光學支（$+$號，$K\to 0$ 振幅反相）；聲學支（$-$號，$K\to 0$ 振幅同相）。邊界能隙 $\Delta\omega = \sqrt{2C/M_2} - \sqrt{2C/M_1}$。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 4 Eq. (20)–(27) p. 94–97 ｜ 歷年考題：<a href="../考古題/詳解/固態_2018_詳解.html">2018</a>, <a href="../考古題/詳解/固態_2020_詳解.html">2020</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>德拜模型（Debye Model）與低溫 $T^3$ 定律</span>
        <button class="btn-copy" onclick="copyLatex('\\omega_D = v_s (6\\pi^2 n)^{1/3}, \\quad D(\\omega) = \\frac{9N}{\\omega_D^3}\\omega^2, \\quad C_v \\approx \\frac{12\\pi^4}{5} N k_B \\left(\\frac{T}{\\Theta_D}\\right)^3')">📋 複製 LaTeX</button>
      </div>
      <div>$$\omega_D = v_s (6\pi^2 n)^{1/3}, \quad D(\omega) = \frac{3V\omega^2}{2\pi^2 v_s^3} = \frac{9N}{\omega_D^3}\omega^2, \quad C_v \approx \frac{12\pi^4}{5} N k_B \left(\frac{T}{\Theta_D}\right)^3 \propto T^3$$</div>
      <div class="formula-desc">低溫下激發之聲子模態體積正比於 $T^3$；高溫則還原 Dulong-Petit 極限 $C_v \to 3Nk_B$。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 5 Eq. (15)–(28) p. 110–116 ｜ 林盛煇 §5.3 ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013</a>, <a href="../考古題/詳解/固態_2014_詳解.html">2014</a>, <a href="../考古題/詳解/固態_2015_詳解.html">2015</a>, <a href="../考古題/詳解/固態_2016_詳解.html">2016</a></div>
    </div>
  </div>

  <!-- Unit 05 Formula Block -->
  <div class="unit-formula-block" id="f-unit05" data-tags="unit05 自由電子 費米氣體 fermi gas dos sommerfeld wiedemann-franz 比熱 態密度 kittel ch6 2014 2015 2016 2017 2020 2021 2022 2023 2024 2025">
    <div class="unit-formula-header">
      <div class="unit-formula-title">單元 05：自由電子費米氣體（Free Electron Fermi Gas）</div>
      <a href="unit05_自由電子費米氣體.html" style="font-size:0.85em;color:var(--primary);text-decoration:none;">查看詳細講義 →</a>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>3D 費米面物理量（Fermi Surface）</span>
        <button class="btn-copy" onclick="copyLatex('k_F = (3\\pi^2 n)^{1/3}, \\quad E_F = \\frac{\\hbar^2 k_F^2}{2m} = \\frac{\\hbar^2}{2m}(3\\pi^2 n)^{2/3}, \\quad U_0 = \\frac{3}{5} N E_F')">📋 複製 LaTeX</button>
      </div>
      <div>$$k_F = (3\pi^2 n)^{1/3}, \quad E_F = \frac{\hbar^2 k_F^2}{2m} = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}, \quad U_0 = \frac{3}{5} N E_F$$</div>
      <div class="formula-desc">基態電子填滿半徑 $k_F$ 之費米球。0K 總能量為 $3/5 N E_F$。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 6 Eq. (17)–(23) p. 138–139 ｜ 林盛煇 §6.3 ｜ 歷年考題：<a href="../考古題/詳解/固態_2016_詳解.html">2016</a>, <a href="../考古題/詳解/固態_2017_詳解.html">2017</a>, <a href="../考古題/詳解/固態_2022_詳解.html">2022</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>1D / 2D / 3D 能態密度（DOS）</span>
        <button class="btn-copy" onclick="copyLatex('g_{\\text{3D}}(E) \\propto E^{1/2}, \\quad g_{\\text{2D}}(E) = \\frac{A m}{\\pi \\hbar^2} = \\text{const}, \\quad g_{\\text{1D}}(E) \\propto E^{-1/2}')">📋 複製 LaTeX</button>
      </div>
      <div>$$g_{\text{3D}}(E) = \frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\sqrt{E} \propto E^{1/2}, \quad g_{\text{2D}}(E) = \frac{Am}{\pi\hbar^2} = \text{常數}, \quad g_{\text{1D}}(E) \propto E^{-1/2}$$</div>
      <div class="formula-desc">不同空間維度下，自旋簡併度為 2 的自由電子能態密度能量相依關係。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 6 Eq. (20)–(21) p. 139 ｜ 歷年考題：<a href="../考古題/詳解/固態_2016_詳解.html">2016（2D）</a>, <a href="../考古題/詳解/固態_2023_詳解.html">2023（1D）</a>, <a href="../考古題/詳解/固態_2024_詳解.html">2024</a>, <a href="../考古題/詳解/固態_2025_詳解.html">2025（2D）</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>電子熱容與維德曼–夫蘭茲定律（Wiedemann-Franz Law）</span>
        <button class="btn-copy" onclick="copyLatex('C_{el} = \\frac{\\pi^2}{3} k_B^2 g(E_F) T = \\gamma T, \\quad \\frac{K}{\\sigma T} = \\frac{\\pi^2 k_B^2}{3e^2} = L \\approx 2.44\\times10^{-8}\\,\\text{W}\\Omega/\\text{K}^2')">📋 複製 LaTeX</button>
      </div>
      <div>$$C_{el} = \gamma T, \quad C/T = \gamma + A T^2, \quad \frac{K}{\\sigma T} = \frac{\pi^2 k_B^2}{3e^2} = L \approx 2.443\times 10^{-8} \, \text{W}\cdot\Omega/\text{K}^2$$</div>
      <div class="formula-desc">索末菲展開說明只有費米面附近 $k_BT$ 範圍之電子參與熱激發。勞侖茲數 $L$ 與金屬種類無關。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 6 Eq. (37)–(43), (54) p. 143–154 ｜ 歷年考題：<a href="../考古題/詳解/固態_2014_詳解.html">2014（30分）</a>, <a href="../考古題/詳解/固態_2015_詳解.html">2015</a>, <a href="../考古題/詳解/固態_2020_詳解.html">2020</a></div>
    </div>
  </div>

  <!-- Unit 06 Formula Block -->
  <div class="unit-formula-block" id="f-unit06" data-tags="unit06 能帶 bloch energy bands kronig-penney effective mass tight-binding 布洛赫 有效質量 緊束縛 kittel ch7 ch9 2013 2014 2015 2016 2017 2018 2020 2021 2025">
    <div class="unit-formula-header">
      <div class="unit-formula-title">單元 06：能帶理論與 Bloch 電子（Energy Bands & Bloch Electrons）</div>
      <a href="unit06_能帶與Bloch電子.html" style="font-size:0.85em;color:var(--primary);text-decoration:none;">查看詳細講義 →</a>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>布洛赫定理（Bloch's Theorem）與 NFE 能隙</span>
        <button class="btn-copy" onclick="copyLatex('\\psi_{\\mathbf k}(\\mathbf r) = u_{\\mathbf k}(\\mathbf r) e^{i\\mathbf k \\cdot \\mathbf r}, \\quad \\Delta E_g = 2|U_{\\mathbf G}|')">📋 複製 LaTeX</button>
      </div>
      <div>$$\psi_{\mathbf k}(\mathbf r) = u_{\mathbf k}(\mathbf r) e^{i\mathbf k \cdot \mathbf r}, \quad u_{\mathbf k}(\mathbf r+\mathbf R) = u_{\mathbf k}(\mathbf r), \quad \Delta E_g = 2|U_{\mathbf G}|$$</div>
      <div class="formula-desc">週期位能下電子波函數形式。在第一 BZ 邊界，正反向行波疊加成駐波，位能積分差值開出能隙 $2|U_G|$。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 7 Eq. (5)–(7), (24)–(27) p. 165–167 ｜ 林盛煇 §7.2–7.3 ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013</a>, <a href="../考古題/詳解/固態_2014_詳解.html">2014</a>, <a href="../考古題/詳解/固態_2018_詳解.html">2018</a>, <a href="../考古題/詳解/固態_2020_詳解.html">2020</a>, <a href="../考古題/詳解/固態_2025_詳解.html">2025</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>克勒尼希–潘尼模型超越方程（Kronig-Penney Model）</span>
        <button class="btn-copy" onclick="copyLatex('P \\frac{\\sin(Ka)}{Ka} + \\cos(Ka) = \\cos(ka)')">📋 複製 LaTeX</button>
      </div>
      <div>$$P \frac{\sin(Ka)}{Ka} + \cos(Ka) = \cos(ka), \quad P = \frac{m V_0 b a}{\hbar^2}$$</div>
      <div class="formula-desc">左式絕對值大於 1 時對應能量禁帶（Forbidden Gap），嚴格證明能帶結構之存在。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 7 Eq. (21b) p. 169–171 ｜ 林盛煇 §7.4 ｜ 歷年考題：<a href="../考古題/詳解/固態_2014_詳解.html">2014</a>, <a href="../考古題/詳解/固態_2015_詳解.html">2015</a>, <a href="../考古題/詳解/固態_2016_詳解.html">2016</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>有效質量張量與緊束縛模型（Tight-Binding）</span>
        <button class="btn-copy" onclick="copyLatex('\\left(\\frac{1}{m^*}\\right)_{ij} = \\frac{1}{\\hbar^2}\\frac{\\partial^2 E}{\\partial k_i \\partial k_j}, \\quad E(k) = -\\alpha - 2\\gamma \\cos(ka)')">📋 複製 LaTeX</button>
      </div>
      <div>$$\left(\frac{1}{m^*}\right)_{ij} = \frac{1}{\hbar^2}\frac{\partial^2 E}{\partial k_i \partial k_j}, \quad E(k) = -\alpha - 2\gamma \cos(ka) \implies m^* = \frac{\hbar^2}{2\gamma a^2}$$</div>
      <div class="formula-desc">帶頂曲率為負對應負質量（電洞）；緊束縛帶寬 $W=4\gamma$，帶底有效質量反比於跳躍積分 $\gamma$。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 7 Eq. (37)–(40) p. 176 ＆ Ch. 9 p. 232 ｜ 歷年考題：<a href="../考古題/詳解/固態_2016_詳解.html">2016</a>, <a href="../考古題/詳解/固態_2017_詳解.html">2017</a>, <a href="../考古題/詳解/固態_2021_詳解.html">2021</a>, <a href="../考古題/詳解/固態_2025_詳解.html">2025 Q2</a></div>
    </div>
  </div>

  <!-- Unit 07 Formula Block -->
  <div class="unit-formula-block" id="f-unit07" data-tags="unit07 半導體 semiconductors mass action pn junction hall 載子濃度 霍爾 質量作用 kittel ch8 ch17 2013 2016 2021 2022 2023">
    <div class="unit-formula-header">
      <div class="unit-formula-title">單元 07：半導體物理（Semiconductors）</div>
      <a href="unit07_半導體.html" style="font-size:0.85em;color:var(--primary);text-decoration:none;">查看詳細講義 →</a>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>質量作用定律與本質載子濃度</span>
        <button class="btn-copy" onclick="copyLatex('n p = n_i^2 = N_c N_v e^{-E_g / k_BT}, \\quad n_i \\propto T^{3/2} e^{-E_g / 2k_BT}')">📋 複製 LaTeX</button>
      </div>
      <div>$$np = n_i^2 = N_c N_v e^{-E_g / k_BT}, \quad n_i = \sqrt{N_c N_v} e^{-E_g / 2k_BT} \propto T^{3/2} e^{-E_g / 2k_BT}$$</div>
      <div class="formula-desc">不論純半導體或摻雜外質半導體，熱平衡下載子濃度乘積均為定值 $n_i^2$。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 8 Eq. (29)–(43) p. 206–209 ｜ 林盛煇 §8.2 ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013</a>, <a href="../考古題/詳解/固態_2016_詳解.html">2016</a>, <a href="../考古題/詳解/固態_2022_詳解.html">2022</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>pn 接面內建電位與霍爾係數（Hall Coefficient）</span>
        <button class="btn-copy" onclick="copyLatex('V_{bi} = \\frac{k_B T}{e}\\ln\\left(\\frac{N_A N_D}{n_i^2}\\right), \\quad R_H = -\\frac{1}{ne} \\;(\\text{電子}), \\quad R_H = +\\frac{1}{pe} \\;(\\text{電洞})')">📋 複製 LaTeX</button>
      </div>
      <div>$$V_{bi} = \frac{k_B T}{e}\ln\left(\frac{N_A N_D}{n_i^2}\right), \quad R_H = \frac{E_y}{j_x B_z} = -\frac{1}{ne} \text{ 或 } +\frac{1}{pe}$$</div>
      <div class="formula-desc">內建電位維持擴散與漂移平衡；霍爾係數符號直接判定主導載子為電子或電洞。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 6 Eq. (56), Ch. 8 Eq. (52), Ch. 17 p. 488 ｜ 歷年考題：<a href="../考古題/詳解/固態_2016_詳解.html">2016</a>, <a href="../考古題/詳解/固態_2022_詳解.html">2022 Q2（40分）</a></div>
    </div>
  </div>

  <!-- Unit 08 Formula Block -->
  <div class="unit-formula-block" id="f-unit08" data-tags="unit08 磁性 magnetism curie langevin landau 居里 朗之萬 朗道能階 kittel ch11 ch12 ch9 2013 2018 2025">
    <div class="unit-formula-header">
      <div class="unit-formula-title">單元 08：磁性（Magnetism）</div>
      <a href="unit08_磁性.html" style="font-size:0.85em;color:var(--primary);text-decoration:none;">查看詳細講義 →</a>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>朗之萬順磁函數與居里定律（Curie's Law）</span>
        <button class="btn-copy" onclick="copyLatex('M = N m L(\\alpha), \\quad L(\\alpha) = \\coth\\alpha - \\frac{1}{\\alpha}, \\quad \\chi = \\frac{C}{T}')">📋 複製 LaTeX</button>
      </div>
      <div>$$M = N m L(\alpha), \quad L(\alpha) = \coth\alpha - \frac{1}{\alpha}, \quad \alpha = \frac{m B}{k_B T} \xrightarrow{\alpha \ll 1} \chi = \frac{N\mu_0 m^2}{3k_BT} = \frac{C}{T}$$</div>
      <div class="formula-desc">弱場極限還原居里定律；強場低溫下 $L(\alpha) \to 1$，磁化強度達到飽和 $Nm$。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 11 Eq. (13)–(23) p. 303–305 ｜ 林盛煇 §11.3 ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013 Q4（20分）</a>, <a href="../考古題/詳解/固態_2025_詳解.html">2025</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>朗道能階（Landau Levels）量子化</span>
        <button class="btn-copy" onclick="copyLatex('E_n = \\left(n + \\frac{1}{2}\\right)\\hbar\\omega_c, \\quad \\omega_c = \\frac{e B}{m^*}, \\quad D = \\frac{eB}{h} = \\frac{B}{\\Phi_0}')">📋 複製 LaTeX</button>
      </div>
      <div>$$E_n = \left(n + \frac{1}{2}\right)\hbar\omega_c, \quad \omega_c = \frac{e B}{m^*}, \quad D = \frac{eB}{h} = \frac{B}{\Phi_0}$$</div>
      <div class="formula-desc">外加磁場使 2D 連續態崩縮為分離朗道階梯，每個階梯面簡併度正比於磁場 $B$。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 9 p. 254–256 ｜ 歷年考題：<a href="../考古題/詳解/固態_2018_詳解.html">2018 Q3（20分）</a></div>
    </div>
  </div>

  <!-- Unit 09 Formula Block -->
  <div class="unit-formula-block" id="f-unit09" data-tags="unit09 超導 superconductivity meissner london bcs vortex 邁斯納 倫敦方程 渦旋 kittel ch10 2013 2025">
    <div class="unit-formula-header">
      <div class="unit-formula-title">單元 09：超導現象（Superconductivity）</div>
      <a href="unit09_超導.html" style="font-size:0.85em;color:var(--primary);text-decoration:none;">查看詳細講義 →</a>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>倫敦方程與倫敦穿透深度（London Penetration Depth）</span>
        <button class="btn-copy" onclick="copyLatex('\\nabla^2 \\mathbf B = \\frac{1}{\\lambda_L^2} \\mathbf B, \\quad \\lambda_L = \\sqrt{\\frac{m}{\\mu_0 n_s e^2}}, \\quad B(x) = B_0 e^{-x/\\lambda_L}')">📋 複製 LaTeX</button>
      </div>
      <div>$$\nabla^2 \mathbf B = \frac{1}{\lambda_L^2} \mathbf B, \quad \lambda_L = \sqrt{\frac{m}{\mu_0 n_s e^2}}, \quad B(x) = B_0 e^{-x/\lambda_L}$$</div>
      <div class="formula-desc">邁斯納完全抗磁性（$\chi=-1$）的定量描述，磁場進入超導體表面呈指數衰減。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 10 Eq. (14)–(19) p. 269–271 ｜ 林盛煇 §10.3 ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013 Q5</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>磁通量子與 BCS 零溫能隙</span>
        <button class="btn-copy" onclick="copyLatex('\\Phi_0 = \\frac{h}{2e} \\approx 2.07\\times 10^{-15} \\,\\text{Wb}, \\quad \\Delta(0) \\approx 1.764 k_B T_c')">📋 複製 LaTeX</button>
      </div>
      <div>$$\Phi_0 = \frac{h}{2e} \approx 2.0678 \times 10^{-15} \, \text{Wb} \, (\text{T}\cdot\text{m}^2), \quad \Delta(0) \approx 1.764 \, k_B T_c$$</div>
      <div class="formula-desc">Cooper 電子配對（電荷 $q=2e$）引發磁通量子化；BCS 理論給出能隙與臨界溫度的普適比值。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 10 Eq. (36), (40), Table 3 p. 273, 283 ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013</a>, <a href="../考古題/詳解/固態_2025_詳解.html">2025 Q4</a></div>
    </div>
  </div>

  <!-- Unit 10 Formula Block -->
  <div class="unit-formula-block" id="f-unit10" data-tags="unit10 實驗 進階 stm graphene dirac arpes 石墨烯 穿隧 反射率 kittel ch1 ch18 2013 2018 2022 2023">
    <div class="unit-formula-header">
      <div class="unit-formula-title">單元 10：實驗技術與進階主題（Experimental & Advanced）</div>
      <a href="unit10_實驗與進階.html" style="font-size:0.85em;color:var(--primary);text-decoration:none;">查看詳細講義 →</a>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>STM 穿隧電流對間距的指數敏感性</span>
        <button class="btn-copy" onclick="copyLatex('I \\propto e^{-2\\kappa d}, \\quad \\kappa = \\frac{\\sqrt{2m\\phi}}{\\hbar} \\approx 0.512 \\sqrt{\\phi(\\text{eV})} \\,\\text{Å}^{-1}')">📋 複製 LaTeX</button>
      </div>
      <div>$$I \propto e^{-2\kappa d}, \quad \kappa = \frac{\sqrt{2m\phi}}{\hbar} \approx 0.512 \sqrt{\phi(\text{eV})} \,\, \text{Å}^{-1}$$</div>
      <div class="formula-desc">探針每後退 $1\,\text{Å}$，電流約縮減一個數量級，構成原子級垂直解析度的物理基礎。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 1 p. 20 ｜ 講義.md ｜ 歷年考題：<a href="../考古題/詳解/固態_2013_詳解.html">2013 Q3</a>, <a href="../考古題/詳解/固態_2018_詳解.html">2018</a></div>
    </div>

    <div class="formula-item">
      <div class="formula-name">
        <span>石墨烯（Graphene）無質量 Dirac 錐線性色散</span>
        <button class="btn-copy" onclick="copyLatex('E(\\mathbf q) = \\pm \\hbar v_F |\\mathbf q|, \\quad g(E) = \\frac{2}{\\pi \\hbar^2 v_F^2}|E|')">📋 複製 LaTeX</button>
      </div>
      <div>$$E(\mathbf q) = \pm \hbar v_F |\mathbf q|, \quad v_F \approx 10^6 \, \text{m/s}, \quad g(E) = \frac{2}{\pi \hbar^2 v_F^2} |E|$$</div>
      <div class="formula-desc">在 $K, K'$ 點附近靜止質量為零（無質量狄拉克費米子），能態密度隨能量線性增加。</div>
      <div class="formula-ref">📖 <b>出處 (Ref)</b>: Kittel 8e Ch. 18 ｜ Rev. Mod. Phys. 81, 109 (2009) ｜ 歷年考題：<a href="../考古題/詳解/固態_2018_詳解.html">2018 Q4</a>, <a href="../考古題/詳解/固態_2023_詳解.html">2023 Q1</a></div>
    </div>
  </div>

  <hr style="border:none;border-top:1px solid #cbd5e1;margin:3em 0 1.5em;">
  <div style="font-size:0.85em;color:#627d98;text-align:center;">
    NTU 應用物理所博士班資格考備考系統 · 由 <code>考古題/詳解/_build_html.py</code> 統一建置交付
  </div>
</div>

<div id="toast">已複製 LaTeX 到剪貼簿！</div>

<script>
// Sidebar Toggle (Mobile)
const toggle = document.getElementById('toc-toggle');
const sidebar = document.getElementById('sidebar');
if (toggle && sidebar) {
  toggle.addEventListener('click', () => sidebar.classList.toggle('open'));
}

// Live Search Filter
const searchInput = document.getElementById('formula-search');
if (searchInput) {
  searchInput.addEventListener('input', (e) => {
    const q = e.target.value.toLowerCase().trim();
    const blocks = document.querySelectorAll('.unit-formula-block');
    blocks.forEach(b => {
      const tags = (b.dataset.tags || '').toLowerCase();
      const text = b.innerText.toLowerCase();
      if (!q || tags.includes(q) || text.includes(q)) {
        b.style.display = '';
      } else {
        b.style.display = 'none';
      }
    });
  });
}

// Copy LaTeX
function copyLatex(tex) {
  navigator.clipboard.writeText(tex).then(() => {
    const toast = document.getElementById('toast');
    toast.style.display = 'block';
    setTimeout(() => { toast.style.display = 'none'; }, 2000);
  });
}

// Sidebar Active Spy
window.addEventListener('scroll', () => {
  const sections = document.querySelectorAll('.unit-formula-block, #overview, #units-grid, #formula-master');
  const scrollY = window.scrollY + 100;
  let currentId = '';
  sections.forEach(sec => {
    if (sec.offsetTop <= scrollY) {
      currentId = sec.id;
    }
  });
  if (currentId) {
    document.querySelectorAll('#sidebar .nav-link').forEach(link => {
      const href = link.getAttribute('href') || '';
      if (href === '#' + currentId) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }
});
</script>
</body>
</html>
"""


KGUIDE_INDEX = r"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kittel 章節對照導讀 — 概念橋 × 術語速查</title>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
         max-width: 900px; margin: 2em auto; padding: 0 1.2em 4em; line-height: 1.7; color: #222; background: #fafafa; }
  h1 { color: #1a4d7c; border-bottom: 3px solid #1a4d7c; padding-bottom: 0.3em; }
  p.intro { color: #444; }
  .card { display: block; text-decoration: none; color: inherit; background: #fff; border: 1px solid #c5d5e5;
          border-radius: 10px; padding: 0.9em 1.2em; margin: 0.8em 0; box-shadow: 0 1px 3px rgba(0,0,0,0.04);
          transition: box-shadow 0.15s, border-color 0.15s, transform 0.05s; }
  .card:hover { border-color: #1a4d7c; box-shadow: 0 3px 10px rgba(26,77,124,0.15); transform: translateY(-1px); }
  .card-title { color: #1a4d7c; font-weight: 700; font-size: 1.08em; }
  .card-sub { color: #555; font-size: 0.95em; margin-top: 0.25em; }
  .note { background: #eef5fb; border-left: 4px solid #6aa1d6; border-radius: 4px; padding: 0.6em 1em; color: #334; font-size: 0.93em; }
  .nav { font-size: 0.92em; margin: 0 0 1em; color: #555; }
  .nav a { color: #1a4d7c; text-decoration: none; } .nav a:hover { text-decoration: underline; }
</style>
</head>
<body>
<div class="nav"><a href="../index.html">← 教材直讀</a> &nbsp;·&nbsp; <a href="../Kittel_翻譯.html">完整翻譯</a> &nbsp;·&nbsp; <a href="../Kittel習題詳解/index.html">🧮 習題詳解</a> &nbsp;·&nbsp; <a href="../../單元教學/index.html">🎓 單元學科</a> &nbsp;·&nbsp; <a href="../../考古題/詳解/index.html">逐題詳解</a></div>
<h1>📑 Kittel 章節對照導讀</h1>
<p class="intro">讀 Kittel《固態物理導論》翻譯本時的<b>對照地圖</b>：每章給「<b>三層概念對應（高中 → 大學普物 → 固態物理）</b>」＋「<b>專有名詞 × 範例 速查</b>」。把機器翻譯的課文翻成人話、搭好概念橋。想看完整推導與考題，點每章末的「單元學科」連結。</p>
<div class="note">📖 <b>怎麼配</b>：先用本頁的概念橋看懂這章「在幹嘛、對到你會的什麼」→ 讀 <a href="../Kittel_翻譯.html">完整翻譯</a> 課文 → 卡在推導就跳 <a href="../../單元教學/index.html">單元學科</a> → 最後 <a href="../../考古題/詳解/index.html">逐題詳解</a> 練手。</div>
__CARDS__
<hr style="border:none;border-top:1px solid #ccc;margin:2.5em 0;">
<p style="color:#888;font-size:0.85em;">由 <code>考古題/詳解/_build_html.py</code> 的 <code>build_kittel_guide()</code> 產生。編輯 <code>教材/Kittel章節導讀/chXX_*.md</code> 後重跑即更新。</p>
</body>
</html>
"""


KPROB_INDEX = r"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kittel 習題詳解 ＋ 加碼範例</title>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
         max-width: 900px; margin: 2em auto; padding: 0 1.2em 4em; line-height: 1.7; color: #222; background: #fafafa; }
  h1 { color: #1a4d7c; border-bottom: 3px solid #1a4d7c; padding-bottom: 0.3em; }
  p.intro { color: #444; }
  .card { display: block; text-decoration: none; color: inherit; background: #fff; border: 1px solid #c5d5e5;
          border-radius: 10px; padding: 0.9em 1.2em; margin: 0.8em 0; box-shadow: 0 1px 3px rgba(0,0,0,0.04);
          transition: box-shadow 0.15s, border-color 0.15s, transform 0.05s; }
  .card:hover { border-color: #1a4d7c; box-shadow: 0 3px 10px rgba(26,77,124,0.15); transform: translateY(-1px); }
  .card-title { color: #1a4d7c; font-weight: 700; font-size: 1.08em; }
  .card-sub { color: #555; font-size: 0.95em; margin-top: 0.25em; }
  .note { background: #eef5fb; border-left: 4px solid #6aa1d6; border-radius: 4px; padding: 0.6em 1em; color: #334; font-size: 0.93em; }
  .nav { font-size: 0.92em; margin: 0 0 1em; color: #555; }
  .nav a { color: #1a4d7c; text-decoration: none; } .nav a:hover { text-decoration: underline; }
</style>
</head>
<body>
<div class="nav"><a href="../index.html">← 教材直讀</a> &nbsp;·&nbsp; <a href="../Kittel章節導讀/index.html">📑 章節導讀</a> &nbsp;·&nbsp; <a href="../../單元教學/index.html">🎓 單元學科</a> &nbsp;·&nbsp; <a href="../../考古題/詳解/index.html">逐題詳解</a></div>
<h1>🧮 Kittel 習題詳解 ＋ 加碼範例</h1>
<p class="intro">每章兩部分：<b>加碼範例題目</b>（熱身）＋ <b>Kittel 課本 end-of-chapter 習題的完整逐步解答</b>。因為手上的解答手冊在轉檔時公式被刪光，這裡的解答全部從頭重算、每步展開、答案 boxed。</p>
<div class="note">📝 <b>怎麼用</b>：先讀 <a href="../Kittel章節導讀/index.html">章節導讀</a> 建概念 → 用 <a href="../../單元教學/index.html">單元學科</a> 補推導 → 回本頁把<b>加碼範例＋課本習題</b>全部算過一遍 → 上 <a href="../../考古題/詳解/index.html">逐題詳解</a> 練資格考真題。</div>
__CARDS__
<hr style="border:none;border-top:1px solid #ccc;margin:2.5em 0;">
<p style="color:#888;font-size:0.85em;">由 <code>考古題/詳解/_build_html.py</code> 的 <code>build_kittel_problems()</code> 產生。編輯 <code>教材/Kittel習題詳解/chXX_*.md</code> 後重跑即更新。</p>
</body>
</html>
"""


PREREQ_INDEX = r"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>固態物理 先備知識補帖</title>
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
         max-width: 900px; margin: 2em auto; padding: 0 1.2em 4em; line-height: 1.7; color: #222; background: #fafafa; }
  h1 { color: #1a4d7c; border-bottom: 3px solid #1a4d7c; padding-bottom: 0.3em; }
  p.intro { color: #444; }
  .card { display: block; text-decoration: none; color: inherit; background: #fff; border: 1px solid #c5d5e5;
          border-radius: 10px; padding: 0.9em 1.2em; margin: 0.8em 0; box-shadow: 0 1px 3px rgba(0,0,0,0.04);
          transition: box-shadow 0.15s, border-color 0.15s, transform 0.05s; }
  .card:hover { border-color: #1a4d7c; box-shadow: 0 3px 10px rgba(26,77,124,0.15); transform: translateY(-1px); }
  .card-title { color: #1a4d7c; font-weight: 700; font-size: 1.1em; }
  .card-sub { color: #555; font-size: 0.95em; margin-top: 0.25em; }
  .note { background: #eef5fb; border-left: 4px solid #6aa1d6; border-radius: 4px; padding: 0.6em 1em; color: #334; font-size: 0.93em; }
  .nav { font-size: 0.92em; margin: 0 0 1em; color: #555; }
  .nav a { color: #1a4d7c; text-decoration: none; } .nav a:hover { text-decoration: underline; }
</style>
</head>
<body>
<div class="nav"><a href="../index.html">← 教材直讀</a> &nbsp;·&nbsp; <a href="../Kittel章節導讀/index.html">📑 章節導讀</a> &nbsp;·&nbsp; <a href="../../單元教學/index.html">🎓 單元學科</a></div>
<h1>🧰 固態物理 — 先備知識補帖</h1>
<p class="intro">讀 <a href="../index.html">教材直讀</a>（Kittel 原文/翻譯）時，碰到「這個我沒學過」就來這裡。每個先備概念都從<b>高中起點</b>講起，配一個<b>具體範例</b>和<b>一張圖</b>，並標明「<b>用在 Kittel 哪一章 / 哪個單元</b>」，可直接跳過去。</p>
<div class="note">📖 <b>用法</b>：在教材裡卡住 → 用 <kbd>⌘F</kbd> 在這兩頁搜尋關鍵字（如「傅立葉」「波茲曼」「有效質量」）→ 看範例＋圖懂了 → 跳回教材或對應單元繼續。</div>
__CARDS__
<hr style="border:none;border-top:1px solid #ccc;margin:2.5em 0;">
<p style="color:#888;font-size:0.85em;">由 <code>考古題/詳解/_build_html.py</code> 的 <code>build_prereq()</code> 產生。圖在 <code>figs/f00_*.svg</code>。</p>
</body>
</html>
"""


if __name__ == "__main__":
    main()

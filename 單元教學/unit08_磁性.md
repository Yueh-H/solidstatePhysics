<!-- 固態物理 單元08：磁性（Magnetism） · 從高中到資格考 -->

# 固態物理 單元08 — 磁性（Magnetism）
### 從高中概念建到資格考

> **使用說明**：本篇從你高中會的「磁鐵在磁場裡會被擺正」「能量 $U=-\boldsymbol\mu\cdot\mathbf B$」「波耳模型的圓周運動」出發，一路推到台大應物所資格考的 Langevin 順磁、居里定律、Landau 能階與鐵磁居里溫度。符號點 `▸` 就地展開。專有名詞第一次出現用「中文（English）」對照。配套：[單元整理](../考古題/單元整理.html)（出題頻率）、[逐題詳解](../考古題/詳解/index.html)、[教材直讀](../教材/index.html)。
> **慣例（本篇符號）**：外磁場用 $\mathbf B$（單位 tesla），磁矩 $\boldsymbol\mu$（或單顆奈米磁體用 $m$），磁化強度（單位體積磁矩）$\mathbf M$，磁化率（magnetic susceptibility）$\chi$。波茲曼常數 $k_B$、絕對溫度 $T$、約化普朗克常數 $\hbar$、電子電荷大小 $e>0$。本篇統一用 SI；歷年題偶用 $H$ 代外場，數學上把 $H$ 當成正比於 $B$ 的外場強度看待即可（$B=\mu_0 H$，真空中差一個常數）。
>
> 📖 **本單元權威出處與教材對照（Textbook & Reference Alignment）**：
> - **Kittel 原文 8e**：Chapter 11（Diamagnetism and Paramagnetism, pp. 297–322）＆ Chapter 12（Ferromagnetism, pp. 323–352），核心公式：Ch. 11 Eq. (9) 拉莫爾抗磁、Eq. (18) 居里定律、Eq. (20) 朗之萬函數；Ch. 12 Eq. (7) 居里–外斯定律。
> - **林盛煇《固態物理導論》**：第 8 章（§8.1 磁矩來源、§8.2 朗之萬抗磁與順磁理論、§8.3 居里與居里–外斯定律、§8.4 鐵磁性與交換交互作用、§8.5 朗道能階）。
> - **Ashcroft & Mermin**：Ch. 31（Diamagnetism and Paramagnetism）、Ch. 32（Electron Interactions）、Ch. 33（Magnetic Ordering）。
> - **臺大資格考真題對照**：2013–2025 共 3 次命題（2013 Q13, 2018 Q4, 2025 Q4），第四梯隊必拿分區。

---

## 🧭 為什麼要這個單元？（在解決什麼問題、與其他章節的關係）

### 為什麼要學「磁性」？

材料放進磁場會有反應：有的被排斥（**抗磁**）、有的被吸引（**順磁**）、有的自己就帶磁（**鐵磁**）。這些來自電子的**自旋與軌道磁矩**——是電子的「另一張臉」（前面講電子的動能與能帶，這裡講它的磁矩）。第四梯隊，但居里定律與朗道能階是固定考點。

### 在解決什麼問題？

> **核心問題**：為什麼不同材料對磁場的反應相反？磁化率 $\chi$ 隨溫度怎麼變？

做法：寫下磁矩在磁場中的能量 $U=-\boldsymbol\mu\cdot\mathbf B$，做統計平均得磁化。順磁給**居里定律** $\chi\propto1/T$；自由電子在磁場中能量量子化成**朗道能階**；鐵磁用平均場得**居里溫度** $T_C$。

### 與其他章節的關係

| 相關章節 | 關係 |
|---|---|
| **05 自由電子（往前接）** | 包立順磁、朗道抗磁建在費米面附近電子上 |
| **01 晶體結構（往前接）** | 磁性離子坐在晶格上；交換作用沿晶格鍵傳遞，決定鐵磁/反鐵磁 |
| **10 實驗（往後給）** | 朗道能階的量子振盪用來**量費米面** |

> **一句話**：前面把電子當「會跑的電荷」，unit08 把它當「小磁鐵」——而朗道能階又把磁性與 unit05 的費米面綁在一起。

---

## 🎯 這個單元在考什麼（出題地位）

磁性屬於**第四梯隊**：零星出現，但**近年回溫**，2025 又考了。歷年只出現 3 次（2013、2018、2025），但每次都是「整段必背的長推導」或「白送的觀念分」，不能裸考。

| 年份 | 配分 | 題型 | 對應本篇 |
|---|---|---|---|
| **2013 Q14** | 10 pts | **Langevin 函數**長推導：$N$ 顆隨機取向磁矩，由波茲曼因子推 $M=NmL(\alpha)$ | §3 |
| **2018 Q4** | 20 pts | **Landau 能階**（本卷重頭戲）：磁場下軌道量子化 + 磁通量子化 | §4 |
| **2025 Q4(a)** | 5 pts | **鐵磁**：$T>T_C$ 時總磁矩為何？ | §5 |

典型配分從 5 分的觀念題到 20 分的長推導都有。**最常見題型**：(1) 由 Boltzmann factor 推 Langevin/Curie（需全步驟）、(2) 解釋 Landau level 並盡量定量、(3) 居里溫度上下相態的定性問答。

---

## 🧗 高中起點：你已經會的

把這幾塊地基確認好，後面每個推導都是從這裡長出來的：

- **磁矩在磁場中的能量** $U=-\boldsymbol\mu\cdot\mathbf B=-\mu B\cos\theta$（高中：磁偶極在磁場中，平行最穩、反平行最不穩）。
- **力矩會把磁針擺正**（指南針指北）——這就是順磁排列的微觀起源。
- **波茲曼因子（Boltzmann factor）** $e^{-U/k_BT}$：能量低的狀態機率大、溫度高時各狀態趨於均等（高中化學/熱學的「分子佔據高能態的比例隨溫度上升」）。
- **波耳模型的圓周運動**：電子繞圈、向心力 = 力，$mv^2/r=$ 力。Landau 能階就是把磁場下的圓周運動量子化。
- **等比級數 / 泰勒展開**：$\coth\alpha$ 的小量展開要用到 $e^{\pm\alpha}\approx1\pm\alpha+\tfrac{\alpha^2}2$。
- **單變數積分與分部積分**：Langevin 推導的核心就是一個 $\int x e^{\alpha x}dx$。

---

## 📚 主線：從高中一路推到考試級

### 1. 磁矩、能量與磁化（Magnetic Moment, Energy, Magnetization）

**你高中學過的**：一根磁針（小磁鐵）在磁場 $\mathbf B$ 裡，會被力矩擺正，指向和場平行的方向最穩。把「磁針」量化成一個向量 $\boldsymbol\mu$（磁矩），它在場中的位能就是 $U=-\boldsymbol\mu\cdot\mathbf B$。

**為什麼需要新東西**：一塊材料裡有「天文數字」那麼多顆磁矩（每個原子可能帶一顆）。我們不在乎單顆，而在乎**單位體積內所有磁矩的向量和**——這叫磁化強度（magnetization）$\mathbf M$。材料對外場的反應，就看 $\mathbf M$ 隨 $\mathbf B$ 怎麼變。

**定義（中英對照）**：
- 磁矩（magnetic moment）$\boldsymbol\mu$：描述一顆小磁體強弱與方向的向量。
- 磁化強度（magnetization）$\mathbf M$：單位體積的總磁矩，$\mathbf M=\dfrac{1}{V}\sum_i\boldsymbol\mu_i$。
- 磁化率（magnetic susceptibility）$\chi$：磁化對外場的線性響應，$M=\chi H$（弱場）。$\chi>0$ 順磁、$\chi<0$ 抗磁。

<details>
<summary><b>▸ 磁矩在場中的能量 U = -μ · B（Zeeman energy）</b></summary>

**你高中學過的**：向量內積 $\boldsymbol\mu\cdot\mathbf B=\mu B\cos\theta$，$\theta$ 是磁矩與場的夾角。指南針會擺到能量最低的方向。

**為什麼要這個**：整個順磁理論的起點。能量隨「磁矩多平行於場」而降低，這個「想平行」的傾向，被溫度的隨機擾動對抗——兩者誰贏，決定磁化大小。

**定義**：$U=-\boldsymbol\mu\cdot\mathbf B=-\mu B\cos\theta$。$\theta=0$（平行）時 $U=-\mu B$ 最低；$\theta=\pi$（反平行）時 $U=+\mu B$ 最高。

**範例 1（最接近高中）**：磁矩平行場，$\theta=0$，$U=-\mu B$，這是基態。
**範例 2（中階）**：磁矩垂直場，$\theta=90^\circ$，$U=0$。把它從垂直轉到平行，系統釋放能量 $\mu B$。
**範例 3（對到考題）**：2013 Q14 把這個 $U=-mH\cos\theta$ 丟進波茲曼因子，對所有 $\theta$ 做統計平均，就推出 Langevin 函數（見 §3）。

</details>

<details>
<summary><b>▸ 磁化率 χ（magnetic susceptibility）</b></summary>

**你高中學過的**：歐姆定律 $V=IR$ 是「響應 ∝ 驅動」。磁化率是同一個概念：弱場下磁化 ∝ 外場。

**為什麼要這個**：實驗量到的是 $\chi$（在磁強計裡量「材料在場裡被磁化多少」）。理論的任務就是算出 $\chi$，再和實驗對。

**定義**：$\displaystyle\chi=\frac{M}{H}$（SI 下無因次）。符號決定磁性類別：
- $\chi<0$（很小，約 $-10^{-5}$）：抗磁（diamagnetism）。
- $\chi>0$（小，約 $+10^{-3}$，且 $\propto 1/T$）：順磁（paramagnetism）。
- $\chi\gg0$（甚至發散）：鐵磁（ferromagnetism）。

**範例 1**：真空 $\chi=0$。
**範例 2**：順磁鹽在室溫 $\chi\sim10^{-3}$，且降溫時變大（居里定律 §3.4）。
**範例 3**：2025 Q4 用 $\chi=C/(T-T_C)$（居里–外斯定律）描述鐵磁體在 $T>T_C$ 加場時的響應（見 §5）。

</details>

> **小結**：磁性問題 = 「磁矩想被場擺正（能量 $-\mu B$）」對抗「溫度想把它打亂（$k_BT$）」，看誰贏，結果寫成 $\chi$。

---

### 2. 抗磁 vs 順磁（Diamagnetism vs Paramagnetism）：兩種相反的反應

材料對外場有兩種「天生」反應，物理起源完全不同，務必分清。在進入定量前，先把四種「磁有序」型態的自旋排列一次看清楚：

<figure style="margin:1.3em 0;text-align:center">
<svg viewBox="0 0 640 200" width="100%" style="max-width:760px;border:1px solid #ddd;border-radius:8px;background:#fff;padding:6px;box-sizing:border-box" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="magUp8a" markerWidth="8" markerHeight="8" refX="3" refY="0" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#1a4d7c"/></marker>
<marker id="magDn8a" markerWidth="8" markerHeight="8" refX="3" refY="6" orient="auto"><path d="M0,0 L3,6 L6,0 Z" fill="#c0392b"/></marker>
</defs>
<g font-family="-apple-system,sans-serif" font-size="11">
<g transform="translate(0,0)">
<text x="75" y="22" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1a4d7c">順磁 paramagnetic</text>
<g stroke="#888" stroke-width="2.2">
<line x1="25" y1="120" x2="38" y2="55" marker-end="url(#magUp8a)"/>
<line x1="62" y1="58" x2="55" y2="122" marker-end="url(#magDn8a)"/>
<line x1="85" y1="120" x2="98" y2="62" marker-end="url(#magUp8a)"/>
<line x1="128" y1="60" x2="118" y2="120" marker-end="url(#magDn8a)"/>
<line x1="38" y1="160" x2="55" y2="100" marker-end="url(#magUp8a)"/>
<line x1="105" y1="100" x2="92" y2="160" marker-end="url(#magDn8a)"/>
<line x1="130" y1="158" x2="138" y2="98" marker-end="url(#magUp8a)"/>
</g>
<text x="75" y="186" text-anchor="middle" fill="#555">方向雜亂 → 淨 M=0</text>
</g>
<g transform="translate(165,0)">
<text x="70" y="22" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#2e8b2e">鐵磁 ferromagnetic</text>
<g stroke="#1a4d7c" stroke-width="2.2">
<line x1="22" y1="120" x2="22" y2="52" marker-end="url(#magUp8a)"/>
<line x1="52" y1="120" x2="52" y2="52" marker-end="url(#magUp8a)"/>
<line x1="82" y1="120" x2="82" y2="52" marker-end="url(#magUp8a)"/>
<line x1="112" y1="120" x2="112" y2="52" marker-end="url(#magUp8a)"/>
<line x1="37" y1="162" x2="37" y2="94" marker-end="url(#magUp8a)"/>
<line x1="67" y1="162" x2="67" y2="94" marker-end="url(#magUp8a)"/>
<line x1="97" y1="162" x2="97" y2="94" marker-end="url(#magUp8a)"/>
</g>
<text x="70" y="186" text-anchor="middle" fill="#555">全部同向 → M 大</text>
</g>
<g transform="translate(330,0)">
<text x="78" y="22" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#e67e22">反鐵磁 antiferro.</text>
<g stroke-width="2.2">
<line x1="22" y1="120" x2="22" y2="52" stroke="#1a4d7c" marker-end="url(#magUp8a)"/>
<line x1="52" y1="52" x2="52" y2="120" stroke="#c0392b" marker-end="url(#magDn8a)"/>
<line x1="82" y1="120" x2="82" y2="52" stroke="#1a4d7c" marker-end="url(#magUp8a)"/>
<line x1="112" y1="52" x2="112" y2="120" stroke="#c0392b" marker-end="url(#magDn8a)"/>
<line x1="37" y1="162" x2="37" y2="94" stroke="#1a4d7c" marker-end="url(#magUp8a)"/>
<line x1="67" y1="94" x2="67" y2="162" stroke="#c0392b" marker-end="url(#magDn8a)"/>
<line x1="97" y1="162" x2="97" y2="94" stroke="#1a4d7c" marker-end="url(#magUp8a)"/>
</g>
<text x="78" y="186" text-anchor="middle" fill="#555">↑↓ 交替 → 抵消 M=0</text>
</g>
<g transform="translate(495,0)">
<text x="75" y="22" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#c0392b">亞鐵磁 ferrimag.</text>
<g stroke-width="2.2">
<line x1="22" y1="125" x2="22" y2="48" stroke="#1a4d7c" marker-end="url(#magUp8a)"/>
<line x1="52" y1="78" x2="52" y2="120" stroke="#c0392b" marker-end="url(#magDn8a)"/>
<line x1="82" y1="125" x2="82" y2="48" stroke="#1a4d7c" marker-end="url(#magUp8a)"/>
<line x1="112" y1="78" x2="112" y2="120" stroke="#c0392b" marker-end="url(#magDn8a)"/>
<line x1="37" y1="167" x2="37" y2="90" stroke="#1a4d7c" marker-end="url(#magUp8a)"/>
<line x1="67" y1="120" x2="67" y2="162" stroke="#c0392b" marker-end="url(#magDn8a)"/>
<line x1="97" y1="167" x2="97" y2="90" stroke="#1a4d7c" marker-end="url(#magUp8a)"/>
</g>
<text x="75" y="186" text-anchor="middle" fill="#555">↑大↓小 → 殘餘 M≠0</text>
</g>
</g>
</svg>
<figcaption style="font-size:0.9em;color:#555;margin-top:0.5em">四種磁有序型態。<b style="color:#888">順磁</b>：磁矩方向亂指，淨磁化為 0（加場才部分擺正）。<b style="color:#2e8b2e">鐵磁</b>：交換作用讓相鄰自旋<b>全部同向</b>，零場就有大磁化。<b style="color:#e67e22">反鐵磁</b>：相鄰自旋<b>↑↓ 交替</b>、大小相等，完全抵消、淨 M=0。<b style="color:#c0392b">亞鐵磁</b>：↑↓ 交替但<b>兩子晶格磁矩不等</b>（↑大↓小），留下殘餘磁化（如磁鐵礦 Fe₃O₄）。本篇 §3 算順磁、§5 算鐵磁。</figcaption>
</figure>

**抗磁（diamagnetism）**：來自**外場改變電子軌道**。外場一加，根據冷次定律（Lenz's law），感應出的軌道電流會**抵抗**磁場 → 產生與場**反向**的磁矩 → $\chi<0$。**每種材料都有**這個效應（連不帶磁矩的原子也有），但很弱。它**與溫度幾乎無關**（軌道半徑不太隨溫度變）。Kittel 的 Langevin 抗磁公式 $\chi=-\dfrac{N e^2}{6mc^2}\langle r^2\rangle$（CGS），重點是**負號**與正比於 $\langle r^2\rangle$。

<details>
<summary><b>📝 更多範例（點開）：朗之萬抗磁 χ = -(N e² / 6m c²)⟨r²⟩ 的完整推導與估算</b></summary>

**範例 A（從感應磁矩一步步推出公式）**：外場 $B$ 沿 $z$，依拉莫定理（Larmor theorem）電子軌道整體進動，角頻率 $\omega_L=\dfrac{eB}{2mc}$（CGS）。一顆電子繞 $z$ 軸的等效電流為「電荷 ÷ 週期」：
$$I=\frac{-e}{T}=\frac{-e\,\omega_L}{2\pi}=\frac{-e}{2\pi}\cdot\frac{eB}{2mc}=-\frac{e^2B}{4\pi mc}.$$
此電流環包住的面積投影為 $\pi\langle\rho^2\rangle$，其中 $\langle\rho^2\rangle=\langle x^2+y^2\rangle$ 是垂直 $B$ 的橫截半徑平方。感應磁矩 $\mu=\dfrac{IA}{c}=\dfrac{I\,\pi\langle\rho^2\rangle}{c}$：
$$\mu=\frac{1}{c}\Big(-\frac{e^2B}{4\pi mc}\Big)\pi\langle\rho^2\rangle=-\frac{e^2B}{4mc^2}\langle\rho^2\rangle.$$
對球對稱原子 $\langle x^2\rangle=\langle y^2\rangle=\langle z^2\rangle=\tfrac13\langle r^2\rangle$，故 $\langle\rho^2\rangle=\langle x^2+y^2\rangle=\tfrac23\langle r^2\rangle$，代入得每電子磁矩 $\mu=-\dfrac{e^2B}{6mc^2}\langle r^2\rangle$。$N$ 個原子、每個 $Z$ 顆電子，磁化 $M=N\mu$，再除以 $B$（$\chi=M/B$）得
$$\chi=-\frac{Ne^2}{6mc^2}\langle r^2\rangle\quad(\text{每原子單電子；含 }Z\text{ 顆時 }\langle r^2\rangle\to\textstyle\sum_i\langle r_i^2\rangle).$$
每一步只用了「電流＝電荷除週期」「磁矩＝電流乘面積」與球對稱平均，沒有跳步。

**範例 B（負號的物理：冷次定律自洽）**：把上式符號逐項看清楚。$\omega_L=eB/2mc>0$，電子電荷 $-e<0$ → 電流 $I<0$（與正電流環反向）→ 磁矩 $\mu\propto I<0$，即 $\mu$ 與 $B$ **反向**。所以 $\chi=\mu/B<0$。這正是冷次定律：感應的磁矩永遠**抵抗**外加磁通的變化。與順磁（永久矩順著場、$\chi>0$）方向相反，這個負號是抗磁的指紋，不可背錯。

**範例 C（數量級估算，看為何抗磁很弱）**：取 $\langle r^2\rangle\sim a_0^2=(0.5\times10^{-8}\,\mathrm{cm})^2=2.5\times10^{-17}\,\mathrm{cm}^2$，數密度 $N\sim6\times10^{22}\,\mathrm{cm^{-3}}$（CGS 高斯單位，$e=4.8\times10^{-10}\,\mathrm{esu}$、$m=9.1\times10^{-28}\,\mathrm g$、$c=3\times10^{10}\,\mathrm{cm/s}$）。先算 $\dfrac{e^2}{mc^2}=\dfrac{(4.8\times10^{-10})^2}{9.1\times10^{-28}\times(3\times10^{10})^2}\approx\dfrac{2.3\times10^{-19}}{8.2\times10^{-7}}\approx2.8\times10^{-13}\,\mathrm{cm}$（這就是經典電子半徑量級）。於是
$$|\chi|\approx\frac{N e^2\langle r^2\rangle}{6mc^2}\approx\frac{6\times10^{22}\times2.8\times10^{-13}\times2.5\times10^{-17}}{6}\approx7\times10^{-8}.$$
量級 $10^{-6}\!\sim\!10^{-8}$（CGS 體積磁化率），確實是「很小的負數」，與實測抗磁率吻合——這解釋了為何只要有永久磁矩（順磁、$\chi\sim10^{-3}$）就會把抗磁淹沒。

</details>

<figure style="margin:1.3em 0;text-align:center">
<svg viewBox="0 0 460 230" width="100%" style="max-width:540px;border:1px solid #ddd;border-radius:8px;background:#fff;padding:6px;box-sizing:border-box" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="magB8b" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2e8b2e"/></marker>
<marker id="magMu8b" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c0392b"/></marker>
<marker id="magI8b" markerWidth="8" markerHeight="8" refX="4" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#1a4d7c"/></marker>
</defs>
<g font-family="-apple-system,sans-serif" font-size="11.5">
<text x="230" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#1a4d7c">抗磁：外場感應反向磁矩（冷次定律）</text>
<g stroke="#2e8b2e" stroke-width="2.4">
<line x1="60" y1="200" x2="60" y2="55" marker-end="url(#magB8b)"/>
<line x1="92" y1="200" x2="92" y2="55" marker-end="url(#magB8b)"/>
</g>
<text x="76" y="220" text-anchor="middle" fill="#2e8b2e" font-weight="bold">外場 B ↑（往上加）</text>
<ellipse cx="250" cy="130" rx="78" ry="50" fill="none" stroke="#1a4d7c" stroke-width="2.4"/>
<path d="M250,80 a78,50 0 0,0 -55,18" fill="none" stroke="#1a4d7c" stroke-width="2.4" marker-end="url(#magI8b)"/>
<circle cx="195" cy="98" r="3" fill="#1a4d7c"/>
<text x="250" y="135" text-anchor="middle" font-size="11" fill="#1a4d7c">感應電流環 I</text>
<text x="250" y="151" text-anchor="middle" font-size="10.5" fill="#777">（電子軌道被擾動）</text>
<line x1="250" y1="128" x2="250" y2="208" stroke="#c0392b" stroke-width="2.6" marker-end="url(#magMu8b)"/>
<text x="298" y="200" font-size="12" font-weight="bold" fill="#c0392b">μ 反向（向下）</text>
<text x="360" y="70" font-size="12" font-weight="bold" fill="#c0392b">χ &lt; 0</text>
<text x="338" y="92" font-size="11" fill="#555">μ 與 B 反向</text>
<text x="338" y="112" font-size="11" fill="#555">→ 被磁場排斥</text>
<text x="338" y="138" font-size="11" fill="#555">與溫度</text>
<text x="338" y="156" font-size="11" fill="#555">幾乎無關</text>
<text x="338" y="182" font-size="10.5" fill="#777">每種材料都有</text>
</g>
</svg>
<figcaption style="font-size:0.9em;color:#555;margin-top:0.5em">抗磁的物理：外場 B 一加，依<b>冷次定律（Lenz's law）</b>電子軌道感應出一個電流環，其磁矩 μ <b style="color:#c0392b">反向</b>於 B（抵抗磁通變化）→ 材料被磁場<b>排斥</b>、χ&lt;0。因為只與軌道半徑 ⟨r²⟩ 有關、與磁矩排列無關，所以<b>幾乎不隨溫度變</b>，而且<b>每種材料都有</b>（連惰性氣體也有），只是很弱（χ≈−10⁻⁵）。</figcaption>
</figure>

**順磁（paramagnetism）**：來自材料本身**已經帶有永久磁矩**（未配對電子自旋/軌道角動量）。外場把這些磁矩**部分擺正** → 產生與場**同向**的磁矩 → $\chi>0$。它**強烈依賴溫度**（溫度越高越難擺正，$\chi\propto1/T$）。

| | 抗磁 diamagnetism | 順磁 paramagnetism |
|---|---|---|
| 微觀起源 | 外場感應的軌道電流（冷次定律） | 已存在的永久磁矩被擺正 |
| $\chi$ 符號 | 負（$<0$） | 正（$>0$） |
| 溫度依賴 | 幾乎無關 | $\chi\propto1/T$（居里） |
| 是否人人有 | 是（普遍） | 只有帶永久磁矩者 |

> **小結**：抗磁 = 場「造」出反向磁矩（負、無關溫度）；順磁 = 場把「已有」磁矩擺正（正、$\propto1/T$）。下一節把順磁定量算出來。

---

### 3. 朗之萬順磁與居里定律（Langevin Paramagnetism & Curie Law）★2013 核心長推導

> 📖 **本節核心出處與說明（Ref）**：
> - **權威教材**：Kittel 8e Ch. 11 Eq. (18)–(21) pp. 304–305 ｜ 林盛煇 §8.2 ｜ A&M Ch. 31
> - **歷年考題**：[NTU 2013 Q13（20分）](../考古題/詳解/固態_2013_詳解.html)
> - **觀念說明**：古典連續自由轉動奈米磁矩熱平衡分佈，積分求得朗之萬函數 $L(\alpha) = \coth\alpha - 1/\alpha$。高溫弱場下展開為 $\alpha/3$，導出居里定律 $\chi = C/T$。


這是 2013 Q14（10 分），也是磁性單元最該整段背的推導。

**你高中學過的**：波茲曼因子 $e^{-U/k_BT}$ 告訴你「能量為 $U$ 的狀態出現的相對機率」。能量低 → 機率大。要算「平均值」就是「各狀態 × 其機率，再加總（積分）除以總機率」。

**為什麼需要新東西**：一顆磁矩 $m$ 在場 $H$ 中，可以指向任意方向 $\theta$。能量 $U=-mH\cos\theta$ 越接近平行越低，所以平行方向機率較大。但溫度會打亂它。我們要算的是**沿場方向的平均磁矩** $\langle m_z\rangle=\langle m\cos\theta\rangle$，再乘以 $N$ 顆。

#### 3.1 模型設定

<details>
<summary><b>▸ 朗之萬參數 α = m H / k_B T（Langevin parameter）</b></summary>

**你高中學過的**：波茲曼因子裡的指數是「能量除以 $k_BT$」這個無因次比值。

**為什麼要這個**：把 $U=-mH\cos\theta$ 除以 $k_BT$，自然冒出 $\alpha\cos\theta$，其中 $\alpha\equiv mH/k_BT$。$\alpha$ 就是「磁能 vs 熱能」的比值——整個答案只由 $\alpha$ 決定。

**定義**：$\displaystyle\alpha=\frac{mH}{k_BT}$（題目用 $H$；若用 $B$ 則 $\alpha=mB/k_BT$）。$\alpha\gg1$ 場贏（飽和）；$\alpha\ll1$ 熱贏（弱磁化、居里）。

**範例 1**：強場低溫 $\alpha\to\infty$ → 磁矩全部擺正。
**範例 2**：弱場高溫 $\alpha\to0$ → 幾乎隨機，磁化趨於 0。
**範例 3**：2013 Q14 答案 $M=NmL(\alpha)$ 完全寫成 $\alpha$ 的函數。

</details>

每顆磁矩沿場方向投影 $m\cos\theta$，以波茲曼權重 $e^{-U/k_BT}=e^{\alpha\cos\theta}$ 對所有方向（立體角 $d\Omega=2\pi\sin\theta\,d\theta$）做平均。

<figure style="margin:1.3em 0;text-align:center">
<svg viewBox="0 0 660 240" width="100%" style="max-width:780px;border:1px solid #ddd;border-radius:8px;background:#fff;padding:6px;box-sizing:border-box" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="magB8c" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2e8b2e"/></marker>
<marker id="magUp8c" markerWidth="8" markerHeight="8" refX="3" refY="0" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#1a4d7c"/></marker>
</defs>
<g font-family="-apple-system,sans-serif" font-size="11">
<text x="135" y="20" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1a4d7c">磁矩在場下「部分」對齊</text>
<line x1="20" y1="210" x2="20" y2="40" stroke="#2e8b2e" stroke-width="2.4" marker-end="url(#magB8c)"/>
<text x="20" y="34" text-anchor="middle" font-size="11" font-weight="bold" fill="#2e8b2e">B</text>
<g stroke="#1a4d7c" stroke-width="2" fill="none">
<line x1="55" y1="125" x2="68" y2="68" marker-end="url(#magUp8c)"/>
<line x1="95" y1="130" x2="100" y2="70" marker-end="url(#magUp8c)"/>
<line x1="140" y1="128" x2="135" y2="72" marker-end="url(#magUp8c)"/>
<line x1="185" y1="120" x2="205" y2="72" marker-end="url(#magUp8c)"/>
<line x1="70" y1="190" x2="80" y2="132" marker-end="url(#magUp8c)"/>
<line x1="120" y1="195" x2="118" y2="135" marker-end="url(#magUp8c)"/>
<line x1="170" y1="190" x2="158" y2="135" marker-end="url(#magUp8c)"/>
<line x1="215" y1="185" x2="222" y2="128" marker-end="url(#magUp8c)"/>
</g>
<text x="130" y="225" text-anchor="middle" fill="#555">多數偏向 B（θ 小機率大），但仍散開</text>
<line x1="260" y1="40" x2="260" y2="215" stroke="#ccc" stroke-width="1"/>
<text x="475" y="20" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#c0392b">L(x)=coth x − 1/x</text>
<line x1="320" y1="200" x2="640" y2="200" stroke="#555" stroke-width="1.3"/>
<line x1="320" y1="200" x2="320" y2="45" stroke="#555" stroke-width="1.3"/>
<text x="635" y="218" text-anchor="end" fill="#555">x = μB/kT</text>
<text x="312" y="55" text-anchor="end" fill="#555">L</text>
<line x1="320" y1="70" x2="630" y2="70" stroke="#999" stroke-width="1" stroke-dasharray="4,3"/>
<text x="634" y="73" font-size="10.5" fill="#999">1（飽和）</text>
<polyline points="320,200 340,180 360,162 380,146 405,128 435,111 470,96 510,85 555,78 600,73 630,71" fill="none" stroke="#c0392b" stroke-width="2.4"/>
<line x1="320" y1="200" x2="430" y2="115" stroke="#1a4d7c" stroke-width="1.4" stroke-dasharray="5,4"/>
<text x="400" y="150" font-size="10.5" fill="#1a4d7c">小 x：L≈x/3（居里）</text>
<text x="540" y="100" font-size="10.5" fill="#c0392b">大 x：L→1（飽和）</text>
</g>
</svg>
<figcaption style="font-size:0.9em;color:#555;margin-top:0.5em">朗之萬順磁的物理與曲線。<b>左</b>：N 顆磁矩在場 B 下，能量 −μBcosθ 讓「θ 小（偏向 B）」的方向機率較大，所以磁矩<b>部分</b>對齊（不是全對齊，溫度在搗亂）。<b>右</b>：把球面平均算出來得 M=NμL(x)，x=μB/kT。小場高溫 <b style="color:#1a4d7c">L≈x/3</b>（線性、給居里定律）；大場低溫 <b style="color:#c0392b">L→1</b>（全部擺正、磁化飽和 M→Nμ）。下面 Step 1–6 就是把這條曲線一步步算出來。</figcaption>
</figure>

#### 3.2 Langevin 函數全步驟推導

### Step 1 — 寫下統計平均
沿場方向的平均磁矩 = 「$m\cos\theta$ 乘上波茲曼權重，對立體角積分」除以「權重的積分（歸一化）」：
$$\langle m_z\rangle=m\,\frac{\displaystyle\int_0^\pi \cos\theta\,e^{\alpha\cos\theta}\,2\pi\sin\theta\,d\theta}{\displaystyle\int_0^\pi e^{\alpha\cos\theta}\,2\pi\sin\theta\,d\theta}.$$
分子是「投影 × 權重」加總，分母是「權重」加總（把機率歸一化）。**這一步是整題的靈魂，務必寫對。**

### Step 2 — 換元 $x=\cos\theta$
令 $x=\cos\theta$，則 $dx=-\sin\theta\,d\theta$；$\theta:0\to\pi$ 對應 $x:1\to-1$。$2\pi$ 上下消掉，得一維積分：
$$\boxed{\langle m_z\rangle=m\,\frac{\displaystyle\int_{-1}^{1}x\,e^{\alpha x}\,dx}{\displaystyle\int_{-1}^{1}e^{\alpha x}\,dx}.}$$

### Step 3 — 算分母
$$\int_{-1}^1 e^{\alpha x}dx=\Big[\frac{e^{\alpha x}}{\alpha}\Big]_{-1}^1=\frac{e^\alpha-e^{-\alpha}}{\alpha}=\boxed{\frac{2\sinh\alpha}{\alpha}}.$$
用到雙曲函數定義 $\sinh\alpha=\tfrac12(e^\alpha-e^{-\alpha})$。

### Step 4 — 算分子（分部積分）
用 $\displaystyle\int x e^{\alpha x}dx=\frac{x e^{\alpha x}}{\alpha}-\frac1\alpha\int e^{\alpha x}dx=\frac{x e^{\alpha x}}{\alpha}-\frac{e^{\alpha x}}{\alpha^2}$，代上下限 $-1\to1$：
$$\int_{-1}^1 x e^{\alpha x}dx=\Big[\frac{x e^{\alpha x}}{\alpha}-\frac{e^{\alpha x}}{\alpha^2}\Big]_{-1}^{1}=\frac{e^\alpha+e^{-\alpha}}{\alpha}-\frac{e^\alpha-e^{-\alpha}}{\alpha^2}=\boxed{\frac{2\cosh\alpha}{\alpha}-\frac{2\sinh\alpha}{\alpha^2}}.$$
用到 $\cosh\alpha=\tfrac12(e^\alpha+e^{-\alpha})$。

### Step 5 — 相除得 Langevin 函數
$$\langle m_z\rangle=m\,\frac{\dfrac{2\cosh\alpha}{\alpha}-\dfrac{2\sinh\alpha}{\alpha^2}}{\dfrac{2\sinh\alpha}{\alpha}}=m\Big(\frac{\cosh\alpha}{\sinh\alpha}-\frac1\alpha\Big)=m\Big(\coth\alpha-\frac1\alpha\Big).$$
分子分母各約掉一個 $2/\alpha$，剩下 $\cosh/\sinh=\coth$ 與 $1/\alpha$。定義**朗之萬函數（Langevin function）**：
$$\boxed{L(\alpha)=\coth\alpha-\frac1\alpha.}$$

### Step 6 — 總磁化（N 顆）
$N$ 顆獨立磁矩，總磁化就是 $N$ 倍：
$$\boxed{M(H)=N\langle m_z\rangle=Nm\,L(\alpha),\qquad L(\alpha)=\coth\alpha-\frac1\alpha,\quad \alpha=\frac{mH}{k_BT}.}\quad\blacksquare$$

<details>
<summary><b>📝 更多範例（點開）：Langevin 積分與展開逐步再練</b></summary>

**範例 A（分母 $\int_{-1}^1 e^{\alpha x}dx$ 從頭算）**：被積函數 $e^{\alpha x}$ 的原函數是 $\dfrac{e^{\alpha x}}{\alpha}$（因為 $\dfrac{d}{dx}\dfrac{e^{\alpha x}}{\alpha}=e^{\alpha x}$）。代上下限：
$$\int_{-1}^1 e^{\alpha x}dx=\frac{e^{\alpha\cdot 1}}{\alpha}-\frac{e^{\alpha\cdot(-1)}}{\alpha}=\frac{e^{\alpha}-e^{-\alpha}}{\alpha}.$$
再用雙曲正弦定義 $\sinh\alpha=\dfrac{e^\alpha-e^{-\alpha}}{2}$，即 $e^\alpha-e^{-\alpha}=2\sinh\alpha$，所以分母 $=\dfrac{2\sinh\alpha}{\alpha}$。沒有任何省略。

**範例 B（分子分部積分，標出 $u,dv$）**：對 $\displaystyle\int_{-1}^1 x\,e^{\alpha x}dx$，取 $u=x$（則 $du=dx$）、$dv=e^{\alpha x}dx$（則 $v=\dfrac{e^{\alpha x}}{\alpha}$）。分部積分 $\int u\,dv=uv-\int v\,du$：
$$\int x\,e^{\alpha x}dx=x\cdot\frac{e^{\alpha x}}{\alpha}-\int\frac{e^{\alpha x}}{\alpha}dx=\frac{x e^{\alpha x}}{\alpha}-\frac{e^{\alpha x}}{\alpha^2}.$$
代 $x=1$：$\dfrac{e^\alpha}{\alpha}-\dfrac{e^\alpha}{\alpha^2}$；代 $x=-1$：$\dfrac{-e^{-\alpha}}{\alpha}-\dfrac{e^{-\alpha}}{\alpha^2}$。相減（上限減下限）：
$$\Big(\frac{e^\alpha}{\alpha}-\frac{e^\alpha}{\alpha^2}\Big)-\Big(\frac{-e^{-\alpha}}{\alpha}-\frac{e^{-\alpha}}{\alpha^2}\Big)=\frac{e^\alpha+e^{-\alpha}}{\alpha}-\frac{e^\alpha-e^{-\alpha}}{\alpha^2}=\frac{2\cosh\alpha}{\alpha}-\frac{2\sinh\alpha}{\alpha^2}.$$
用了 $e^\alpha+e^{-\alpha}=2\cosh\alpha$、$e^\alpha-e^{-\alpha}=2\sinh\alpha$。

**範例 C（相除約分得 $L(\alpha)$）**：把範例 B 除以範例 A：
$$\frac{\dfrac{2\cosh\alpha}{\alpha}-\dfrac{2\sinh\alpha}{\alpha^2}}{\dfrac{2\sinh\alpha}{\alpha}}=\frac{2\cosh\alpha/\alpha}{2\sinh\alpha/\alpha}-\frac{2\sinh\alpha/\alpha^2}{2\sinh\alpha/\alpha}=\frac{\cosh\alpha}{\sinh\alpha}-\frac{1}{\alpha}=\coth\alpha-\frac1\alpha.$$
第一項分子分母同除 $2/\alpha$ 得 $\cosh/\sinh=\coth$；第二項 $\dfrac{2\sinh\alpha/\alpha^2}{2\sinh\alpha/\alpha}=\dfrac{1/\alpha^2}{1/\alpha}=\dfrac1\alpha$。乘上前面的 $m$ 就得 $\langle m_z\rangle=mL(\alpha)$。

**範例 D（$\coth$ 小量展開的來源）**：要驗證弱場 $L\approx\alpha/3$，須先有 $\coth\alpha$ 在原點的展開。用 $\sinh\alpha=\alpha+\dfrac{\alpha^3}{6}+\cdots$、$\cosh\alpha=1+\dfrac{\alpha^2}{2}+\cdots$：
$$\coth\alpha=\frac{\cosh\alpha}{\sinh\alpha}=\frac{1+\alpha^2/2}{\alpha\,(1+\alpha^2/6)}=\frac1\alpha\Big(1+\frac{\alpha^2}{2}\Big)\Big(1-\frac{\alpha^2}{6}+\cdots\Big).$$
其中 $\dfrac{1}{1+\alpha^2/6}\approx1-\dfrac{\alpha^2}{6}$（幾何級數一階）。展開括號保留到 $\alpha^2$：$\big(1+\tfrac{\alpha^2}{2}\big)\big(1-\tfrac{\alpha^2}{6}\big)\approx1+\tfrac{\alpha^2}{2}-\tfrac{\alpha^2}{6}=1+\tfrac{\alpha^2}{3}$。故 $\coth\alpha\approx\dfrac1\alpha+\dfrac\alpha3$，於是 $L=\coth\alpha-\dfrac1\alpha\approx\dfrac\alpha3$。這就是下一節居里定律的關鍵一步。

</details>

<details>
<summary><b>▸ 朗之萬函數 L(α) = coth α - 1/α（Langevin function）</b></summary>

**你高中學過的**：$\coth\alpha=\cosh\alpha/\sinh\alpha$，是雙曲餘切；在 $\alpha$ 大時趨近 1。

**為什麼要這個**：它把「磁矩被擺正的程度」濃縮成一條曲線：$\alpha$ 小（高溫弱場）時 $L\approx\alpha/3$ 線性上升；$\alpha$ 大（低溫強場）時 $L\to1$ 飽和。經典（連續取向）順磁的萬用磁化曲線。

**定義**：$L(\alpha)=\coth\alpha-\dfrac1\alpha$。奇函數，$0\le L(\alpha)<1$，$L(0)=0$，$L(\infty)=1$。

**範例 1**：$\alpha=0$（無場或無限高溫）→ $L=0$ → $M=0$（完全隨機）。
**範例 2**：$\alpha\to\infty$ → $L\to1$ → $M\to Nm$（全部擺正、飽和）。
**範例 3**：2013 Q14 的最終答案；其弱場展開 $L\approx\alpha/3$ 直接給出居里定律（下節）。

</details>

![朗之萬函數 $L(\alpha)=\coth\alpha-1/\alpha$：小場 $\approx\alpha/3$（居里）、大場飽和趨於 1](../figs/f08_langevin.svg)

#### 3.3 兩個極限（檢查物理）

**強場 / 低溫 $\alpha\gg1$**：$\coth\alpha\to1$，$1/\alpha\to0$，故 $L\to1$：
$$M\to Nm\quad(\text{飽和磁化，全部磁矩擺正}).$$

**弱場 / 高溫 $\alpha\ll1$**：用泰勒展開 $\coth\alpha\approx\dfrac1\alpha+\dfrac\alpha3-\cdots$（這是 $\coth$ 在原點的標準展開），故
$$L(\alpha)\approx\Big(\frac1\alpha+\frac\alpha3\Big)-\frac1\alpha=\frac\alpha3.$$

#### 3.4 居里定律（Curie Law）

把弱場結果代回 $M=NmL(\alpha)\approx Nm\cdot\dfrac\alpha3$，再代 $\alpha=mH/k_BT$：

### Step 1 — 代入展開
$$M\approx Nm\cdot\frac13\cdot\frac{mH}{k_BT}=\frac{Nm^2H}{3k_BT}.$$

### Step 2 — 讀出磁化率
由 $M=\chi H$ 比對：
$$\boxed{\chi=\frac{Nm^2}{3k_BT}=\frac{C}{T},\qquad C=\frac{Nm^2}{3k_B}.}$$

這就是**居里定律（Curie law）** $\chi=C/T$，$C$ 是**居里常數（Curie constant）**。

<details>
<summary><b>📝 更多範例（點開）：居里常數、有效磁矩與居里–外斯數值練習</b></summary>

**範例 A（由 $1/\chi$–$T$ 斜率反推每顆磁矩 $m$）**：把居里定律倒過來 $\dfrac1\chi=\dfrac{T}{C}$，這是過原點、斜率 $\dfrac1C$ 的直線。設實驗量到斜率 $s=\dfrac1C=2.0\,\mathrm{K}^{-1}$（任意單位），且 $N=6.0\times10^{27}\,\mathrm{m^{-3}}$。由 $C=\dfrac{Nm^2}{3k_B}$ 解 $m$：
$$m^2=\frac{3k_BC}{N}=\frac{3k_B}{N s}=\frac{3\times1.38\times10^{-23}}{6.0\times10^{27}\times2.0}=\frac{4.14\times10^{-23}}{1.2\times10^{28}}=3.45\times10^{-51}.$$
$$m=\sqrt{3.45\times10^{-51}}\approx5.9\times10^{-26}\,\mathrm{J/T}.$$
與波耳磁子 $\mu_B=9.27\times10^{-24}\,\mathrm{J/T}$ 相比，$m/\mu_B\approx6.4\times10^{-3}$——示範整個「斜率 → $C$ → $m$」的代數鏈，每一步都把單位帶著走。

**範例 B（量子版居里常數，自旋 $S=\tfrac12$、$g=2$）**：量子順磁把經典 $m^2$ 換成 $g^2\mu_B^2 S(S+1)$。代 $S=\tfrac12$：$S(S+1)=\tfrac12\cdot\tfrac32=\tfrac34$，$g^2=4$，故 $g^2S(S+1)=4\times\tfrac34=3$。於是
$$C=\frac{N g^2\mu_B^2 S(S+1)}{3k_B}=\frac{N\cdot 3\,\mu_B^2}{3k_B}=\frac{N\mu_B^2}{k_B}.$$
有效磁矩 $p_{\text{eff}}=g\sqrt{S(S+1)}=2\sqrt{3/4}=\sqrt3\approx1.73$（以 $\mu_B$ 為單位）。這就是教科書「$S=\tfrac12$ 自旋給 $p_{\text{eff}}=1.73$」的由來，逐步代入沒有跳。

**範例 C（居里 → 居里–外斯的平移）**：有交換場時 $\chi=\dfrac{C}{T-\theta}$。設某鐵磁傾向材料 $C=0.5\,\mathrm{K}$、$\theta=300\,\mathrm K$。在 $T=600\,\mathrm K$：
$$\chi=\frac{0.5}{600-300}=\frac{0.5}{300}\approx1.67\times10^{-3}.$$
若改用純居里 $\chi=C/T=0.5/600\approx8.3\times10^{-4}$，只有一半——可見「分母從 $T$ 變成 $T-\theta$」會把磁化率放大。當 $T\to\theta^+=300^+$，分母 $\to0^+$、$\chi\to+\infty$（發散），這正是 $\theta=T_C$ 處鐵磁相變的訊號。把 $\dfrac1\chi=\dfrac{T-\theta}{C}$ 畫成 $T$ 的直線，與 $T$ 軸交點就是 $\theta$：本例截距 $=300\,\mathrm K>0$ → 鐵磁傾向。

</details>

<details>
<summary><b>▸ 居里定律 χ = C/T（Curie law）</b></summary>

**你高中學過的**：反比關係 $y=C/x$（雙曲線）。這裡 $x=T$、$y=\chi$。

**為什麼要這個**：它是順磁的**實驗指紋**——量 $\chi$ 對 $1/T$ 作圖得一條過原點的直線，斜率 = 居里常數 $C$，由 $C$ 反推每顆磁矩大小 $m$。考試常要你「由斜率求有效磁矩」。

**定義**：$\chi=\dfrac CT$，$C=\dfrac{Nm^2}{3k_B}$（經典）。量子版（自旋 $S$、$g$ 因子）為 $C=\dfrac{Ng^2\mu_B^2S(S+1)}{3k_B}$，把經典的 $m^2$ 換成 $g^2\mu_B^2S(S+1)$。

**範例 1**：固定材料，溫度加倍 → $\chi$ 減半。
**範例 2**：$1/T$ 作圖斜率 = $C$ → 由 $C=Nm^2/3k_B$ 解出 $m$。
**範例 3**：鐵磁體在 $T>T_C$ 時，居里定律修正為居里–外斯 $\chi=C/(T-T_C)$（§5），$T\to T_C^+$ 時發散。

</details>

![居里定律 $\chi=C/T$：$\chi$ 對 $T$ 為反比雙曲線，$1/\chi$ 對 $T$ 為過原點直線](../figs/f08_curie.svg)

居里定律的「實驗指紋」最好用 $1/\chi$ 對 $T$ 來看——它是一條直線；交換作用一加進去（鐵磁／反鐵磁傾向），直線只是平移，截距告訴你交換場的正負：

<figure style="margin:1.3em 0;text-align:center">
<svg viewBox="0 0 480 250" width="100%" style="max-width:560px;border:1px solid #ddd;border-radius:8px;background:#fff;padding:6px;box-sizing:border-box" xmlns="http://www.w3.org/2000/svg">
<g font-family="-apple-system,sans-serif" font-size="11">
<text x="240" y="20" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1a4d7c">1/χ 對 T：居里 vs 居里–外斯</text>
<line x1="60" y1="210" x2="455" y2="210" stroke="#555" stroke-width="1.3"/>
<line x1="160" y1="225" x2="160" y2="40" stroke="#555" stroke-width="1.3"/>
<text x="450" y="228" text-anchor="end" fill="#555">T</text>
<text x="152" y="50" text-anchor="end" fill="#555">1/χ</text>
<text x="160" y="225" text-anchor="middle" fill="#777">0</text>
<polyline points="160,210 430,70" fill="none" stroke="#1a4d7c" stroke-width="2.2"/>
<text x="392" y="68" font-size="11" fill="#1a4d7c" font-weight="bold">居里 χ=C/T</text>
<text x="372" y="84" font-size="10" fill="#1a4d7c">（過原點，θ=0）</text>
<polyline points="230,210 455,93" fill="none" stroke="#c0392b" stroke-width="2.2"/>
<line x1="230" y1="210" x2="160" y2="246" stroke="#c0392b" stroke-width="1.4" stroke-dasharray="5,4"/>
<text x="345" y="135" font-size="11" fill="#c0392b" font-weight="bold">鐵磁 χ=C/(T−θ)</text>
<text x="345" y="151" font-size="10" fill="#c0392b">θ&gt;0（截距在正 T）</text>
<polyline points="90,210 320,40" fill="none" stroke="#e67e22" stroke-width="2.2"/>
<text x="60" y="170" font-size="11" fill="#e67e22" font-weight="bold">反鐵磁</text>
<text x="55" y="186" font-size="10" fill="#e67e22">χ=C/(T+|θ|)</text>
<circle cx="230" cy="210" r="3.5" fill="#c0392b"/>
<text x="230" y="226" text-anchor="middle" font-size="11" fill="#c0392b">θ=T_C</text>
<circle cx="90" cy="210" r="3.5" fill="#e67e22"/>
<text x="92" y="226" text-anchor="middle" font-size="10" fill="#e67e22">−|θ|</text>
</g>
</svg>
<figcaption style="font-size:0.9em;color:#555;margin-top:0.5em">把 χ 倒過來畫 1/χ 對 T 就是直線，斜率 = 1/C。<b style="color:#1a4d7c">純順磁（居里）</b>直線<b>過原點</b>（θ=0）。有鐵磁傾向時變成<b style="color:#c0392b">居里–外斯 χ=C/(T−θ)</b>，直線右移、與 T 軸交在<b>正</b> θ=T_C（趨近 T_C⁺ 時 1/χ→0、χ 發散）。反鐵磁傾向則 θ&lt;0，直線左移、截距落在<b style="color:#e67e22">負 T</b>。看截距正負就能判交換作用是「想平行（鐵磁）」還是「想反平行（反鐵磁）」。</figcaption>
</figure>

> **小結**：Langevin = 把 $U=-mH\cos\theta$ 丟進波茲曼因子做球面平均 → $M=NmL(\alpha)$；弱場展開 $L\approx\alpha/3$ → 居里定律 $\chi=C/T$。**強場飽和、弱場 $\propto1/T$** 兩個極限要能秒答。

---

### 4. 朗道能階（Landau Level）★2018 重頭戲（20 分）

> 📖 **本節核心出處與說明（Ref）**：
> - **權威教材**：Kittel 8e Ch. 11 pp. 317–319 ｜ 林盛煇 §8.5
> - **歷年考題**：[NTU 2018 Q4（20分）](../考古題/詳解/固態_2018_詳解.html)
> - **觀念說明**：外加磁場打破連續能帶，使垂直面動能諧振子量子化為朗道能階 $E_n = (n+\frac{1}{2})\hbar\omega_c$；軌道磁通量子化條件 $\Phi = (n+\gamma)\frac{h}{e}$ 奠定金屬量子振盪之基礎。


2018 Q4 要你「定性並盡量定量」解釋：磁場 $\mathbf B$ 下費米面上 Landau level 的存在，提示用「軌道與所含磁通量子化」。

**你高中學過的**：帶電粒子在磁場中受勞侖茲力（Lorentz force）做**圓周運動**——這就是波耳模型裡「向心力 = 力」的同一招。$mv^2/r=evB$。

**為什麼需要新東西**：自由電子在無場時，垂直平面的能量 $\dfrac{\hbar^2(k_x^2+k_y^2)}{2m}$ 是**連續**的。加上磁場後，圓周運動被量子化 → 連續的橫向能量**塌縮成離散、等間距、高度簡併**的能階，這就是 Landau levels。

#### 4.1 定性圖像

加上 $\mathbf B=B\hat z$ 後：
1. 勞侖茲力使電子在 $xy$ 平面繞**迴旋圓**（cyclotron orbit），角頻率為迴旋頻率（cyclotron frequency）$\omega_c=eB/m$；沿 $z$ 仍自由。
2. 圓周運動量子化 → 橫向能量變成**離散等間距**的 Landau levels，間距 $\hbar\omega_c$。
3. 原本均勻散布在 $k_xk_y$ 平面的態，**塌縮**到一條條離散能級上 → 每個 level **高度簡併**（簡併度 = 穿過樣品的磁通量子數，見 §4.4）。
4. 在費米面上：3D 時態凝聚成沿 $k_z$ 的同心 **Landau 管（Landau tubes）**；$B$ 增大時管子脹大、依序掃過費米面 → 物理量對 $1/B$ 週期振盪（de Haas–van Alphen 效應）。

<details>
<summary><b>▸ 迴旋頻率 ω_c = e B / m（cyclotron frequency）</b></summary>

**你高中學過的**：圓周運動「向心力 = 力」$mv^2/r=evB$（勞侖茲力提供向心力）。

**為什麼要這個**：它是 Landau 能階的能量間距 $\hbar\omega_c$ 的核心。場越強，間距越大、能級越稀疏。

**定義**：由 $mv^2/r=evB$ 得 $r=mv/eB$，角頻率 $\omega_c=v/r=eB/m$（與速度無關，只看 $B$ 與質量）。

**範例 1**：$B=1\,\mathrm T$、自由電子質量 → $\omega_c=eB/m\approx1.76\times10^{11}\,\mathrm{rad/s}$，$\hbar\omega_c\approx0.116\,\mathrm{meV}$。
**範例 2**：$B$ 加倍 → $\omega_c$ 加倍 → Landau 間距加倍。
**範例 3**：2018 Q4 的能譜 $E_n=(n+\tfrac12)\hbar\omega_c$ 完全由 $\omega_c$ 定間距。

</details>

<figure style="margin:1.3em 0;text-align:center">
<svg viewBox="0 0 500 270" width="100%" style="max-width:600px;border:1px solid #ddd;border-radius:8px;background:#fff;padding:6px;box-sizing:border-box" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="magSp8e" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#1a4d7c"/></marker>
<marker id="magSp8e2" markerWidth="9" markerHeight="9" refX="2" refY="3" orient="auto"><path d="M6,0 L0,3 L6,6 Z" fill="#1a4d7c"/></marker>
</defs>
<g font-family="-apple-system,sans-serif" font-size="11">
<text x="120" y="20" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#888">無場 B=0</text>
<line x1="40" y1="235" x2="40" y2="45" stroke="#555" stroke-width="1.3"/>
<text x="32" y="52" text-anchor="end" fill="#555">E</text>
<polyline points="40,235 60,225 90,205 130,178 175,146 205,118 205,235" fill="#dfe8f0" stroke="#888" stroke-width="1.8"/>
<text x="120" y="252" text-anchor="middle" fill="#777">連續能量（拋物線 DOS）</text>
<line x1="250" y1="140" x2="300" y2="140" stroke="#2e8b2e" stroke-width="2" marker-end="url(#magSp8e)"/>
<text x="275" y="130" text-anchor="middle" font-size="11" fill="#2e8b2e">加 B</text>
<text x="420" y="20" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1a4d7c">有場 B≠0：朗道能階</text>
<line x1="330" y1="235" x2="330" y2="45" stroke="#555" stroke-width="1.3"/>
<text x="322" y="52" text-anchor="end" fill="#555">E</text>
<g stroke="#1a4d7c" stroke-width="2.4">
<line x1="345" y1="210" x2="490" y2="210"/>
<line x1="345" y1="172" x2="490" y2="172"/>
<line x1="345" y1="134" x2="490" y2="134"/>
<line x1="345" y1="96" x2="490" y2="96"/>
<line x1="345" y1="58" x2="490" y2="58"/>
</g>
<g fill="#1a4d7c" font-size="10.5">
<text x="495" y="213" text-anchor="start">n=0</text>
</g>
<g font-size="10.5" fill="#1a4d7c"><text x="495" y="175">n=1</text><text x="495" y="137">n=2</text><text x="495" y="99">n=3</text></g>
<line x1="360" y1="210" x2="360" y2="172" stroke="#c0392b" stroke-width="1.4" marker-start="url(#magSp8e2)" marker-end="url(#magSp8e)"/>
<text x="368" y="195" font-size="11" fill="#c0392b">ħωᴄ</text>
<text x="408" y="232" text-anchor="middle" fill="#1a4d7c">E_n=(n+½)ħωᴄ</text>
<text x="408" y="248" text-anchor="middle" font-size="10.5" fill="#777">離散、等間距、高度簡併</text>
</g>
</svg>
<figcaption style="font-size:0.9em;color:#555;margin-top:0.5em">朗道能階的核心圖像。<b>左</b>：無場時橫向動能 ℏ²(kₓ²+k_y²)/2m 是<b>連續</b>的。<b>右</b>：加上 B 後迴旋運動被量子化，連續能量<b>塌縮</b>成一條條<b style="color:#1a4d7c">離散、等間距</b>的能級 E_n=(n+½)ħωᴄ，間距固定為 <b style="color:#c0392b">ħωᴄ</b>（ωᴄ=eB/m）。每條能級<b>高度簡併</b>（容量 ∝ B，見 §4.4），B 越大間距越寬、能級越少。</figcaption>
</figure>

#### 4.2 定量推導 ①：解薛丁格方程（Landau gauge）

### Step 1 — Hamiltonian
電荷 $-e$，磁場用最小耦合（minimal coupling）$\mathbf p\to\mathbf p+e\mathbf A$：
$$H=\frac{1}{2m}\big(\mathbf p+e\mathbf A\big)^2,\qquad \mathbf B=B\hat z=\nabla\times\mathbf A.$$

### Step 2 — 選規範（Landau gauge）
取 $\mathbf A=(0,\,Bx,\,0)$，驗證 $\nabla\times\mathbf A=B\hat z$ ✓。代入：
$$H=\frac{1}{2m}\Big[p_x^2+(p_y+eBx)^2+p_z^2\Big].$$

### Step 3 — 分離變數
$p_y,p_z$ 都與 $H$ 對易 → 取 $\psi=e^{i(k_yy+k_zz)}\phi(x)$，把 $p_y\to\hbar k_y$、$p_z\to\hbar k_z$：
$$H\phi=\Big[\frac{p_x^2}{2m}+\frac{1}{2m}(\hbar k_y+eBx)^2+\frac{\hbar^2k_z^2}{2m}\Big]\phi.$$

### Step 4 — 認出諧振子
把中間項配方：
$$\frac{1}{2m}(eB)^2\Big(x+\frac{\hbar k_y}{eB}\Big)^2=\frac12 m\omega_c^2\,(x-x_0)^2,\qquad \omega_c=\frac{eB}{m},\ \ x_0=-\frac{\hbar k_y}{eB}.$$
這是**中心在 $x_0$、頻率 $\omega_c$ 的 1D 諧振子**（外加沿 $z$ 的自由動能）。

### Step 5 — 寫能譜
量子諧振子能譜 $(n+\tfrac12)\hbar\omega$，加上 $z$ 方向自由動能：
$$\boxed{E_{n,k_z}=\Big(n+\tfrac12\Big)\hbar\omega_c+\frac{\hbar^2k_z^2}{2m},\qquad n=0,1,2,\dots}$$
2D（或固定 $k_z$）時即 $E_n=(n+\tfrac12)\hbar\omega_c$。能量**不依賴 $k_y$** → 巨大簡併。

<details>
<summary><b>📝 更多範例（點開）：Landau gauge 配方、規範驗證與能量數值</b></summary>

**範例 A（驗證 $\mathbf A=(0,Bx,0)$ 給出 $\mathbf B=B\hat z$）**：旋度 $\nabla\times\mathbf A$ 的 $z$ 分量是 $\partial_x A_y-\partial_y A_x$。代 $A_x=0$、$A_y=Bx$、$A_z=0$：
$$(\nabla\times\mathbf A)_z=\frac{\partial(Bx)}{\partial x}-\frac{\partial(0)}{\partial y}=B-0=B.$$
$x,y$ 分量：$(\nabla\times\mathbf A)_x=\partial_y A_z-\partial_z A_y=0-0=0$，$(\nabla\times\mathbf A)_y=\partial_z A_x-\partial_x A_z=0-0=0$。故 $\nabla\times\mathbf A=B\hat z$ ✓，這個規範合法。

**範例 B（中間項配方成諧振子，標出每一步）**：分離變數後中間項是 $\dfrac{1}{2m}(\hbar k_y+eBx)^2$。把 $eB$ 提出括號：$\hbar k_y+eBx=eB\Big(x+\dfrac{\hbar k_y}{eB}\Big)$，所以
$$\frac{1}{2m}(\hbar k_y+eBx)^2=\frac{(eB)^2}{2m}\Big(x+\frac{\hbar k_y}{eB}\Big)^2.$$
要寫成標準諧振子 $\tfrac12 m\omega_c^2(x-x_0)^2$，比較係數：$\dfrac12 m\omega_c^2=\dfrac{(eB)^2}{2m}\Rightarrow\omega_c^2=\dfrac{(eB)^2}{m^2}\Rightarrow\omega_c=\dfrac{eB}{m}$，而中心 $x_0=-\dfrac{\hbar k_y}{eB}$。於是橫向哈密頓量就是「質量 $m$、頻率 $\omega_c$、中心 $x_0$」的 1D 諧振子，能譜 $(n+\tfrac12)\hbar\omega_c$ 直接套用——每個係數都對照清楚，沒有硬背。

**範例 C（能階間距與基態能的數值）**：自由電子 $m=9.1\times10^{-31}\,\mathrm{kg}$、$B=2\,\mathrm T$。先算 $\omega_c=\dfrac{eB}{m}=\dfrac{1.6\times10^{-19}\times2}{9.1\times10^{-31}}=3.52\times10^{11}\,\mathrm{rad/s}$。能階間距
$$\hbar\omega_c=1.055\times10^{-34}\times3.52\times10^{11}=3.71\times10^{-23}\,\mathrm J=\frac{3.71\times10^{-23}}{1.6\times10^{-19}}\,\mathrm{eV}\approx2.32\times10^{-4}\,\mathrm{eV}.$$
基態（$n=0$、$k_z=0$）能量 $E_0=\tfrac12\hbar\omega_c\approx1.16\times10^{-4}\,\mathrm{eV}$。與熱能比：$k_BT$ 在 $T=300\,\mathrm K$ 約 $0.026\,\mathrm{eV}$，遠大於 $\hbar\omega_c$ → 室溫下能階被熱抹平，**要看 Landau 量子化必須低溫強場**（這也是 de Haas–van Alphen 實驗的條件）。

</details>

![朗道能階 $E_n=(n+\tfrac12)\hbar\omega_c$：離散等間距能級，間距 $\hbar\omega_c$](../figs/f08_landau.svg)

#### 4.3 定量推導 ②：軌道磁通量子化（題目提示的路）

<details>
<summary><b>▸ 磁通量子 Φ_0 = h/e（flux quantum）</b></summary>

**你高中學過的**：磁通 $\Phi=B\times($面積$)$（穿過一個圈的磁場線總量）。舊量子論：軌道要「裝得下整數個波」（波耳–索末菲 $\oint p\,dq=(n+\gamma)h$）。

**為什麼要這個**：把軌道量子化條件翻譯成「軌道包住的磁通必須是 $\Phi_0$ 的整數倍」，是 2018 題目提示的核心。

**定義**：正常金屬的磁通量子 $\Phi_0=\dfrac he$。（注意：超導的磁通量子是 $h/2e$，因 Cooper 對帶 $2e$，見單元09。）

**範例 1**：$B=1\,\mathrm T$、面積 $1\,\mu\mathrm m^2$ → $\Phi=10^{-12}\,\mathrm{Wb}$，約 $\Phi/\Phi_0\approx242$ 個磁通量子。
**範例 2**：軌道半徑 $r_n$ 滿足 $B\pi r_n^2=(n+\gamma)\Phi_0$。
**範例 3**：2018 Q4 Part C 的結論 $\Phi=(n+\gamma)\Phi_0$。

</details>

### Step 1 — 波耳–索末菲量子化
對閉合迴旋軌道，正則動量（canonical momentum）$\mathbf p=m\mathbf v-e\mathbf A$（$q=-e$）的環積分量子化：
$$\oint \mathbf p\cdot d\mathbf r=(n+\gamma)h.$$

### Step 2 — 拆成兩段
$$\oint \mathbf p\cdot d\mathbf r=\underbrace{\oint m\mathbf v\cdot d\mathbf r}_{\text{動力學項}}-e\underbrace{\oint\mathbf A\cdot d\mathbf r}_{=\,\Phi}.$$
其中 $\oint\mathbf A\cdot d\mathbf r=\int(\nabla\times\mathbf A)\cdot d\mathbf S=\int\mathbf B\cdot d\mathbf S=\Phi$（軌道包住的磁通，用斯托克斯定理（Stokes' theorem））。

### Step 3 — 動力學項
圓軌道 $\oint m\mathbf v\cdot d\mathbf r=mv\cdot(2\pi r)$；由力平衡 $mv=eBr$，且 $\Phi=B\pi r^2$：
$$\oint m\mathbf v\cdot d\mathbf r=(eBr)(2\pi r)=2eB\pi r^2=2e\Phi.$$

### Step 4 — 合併 → 磁通量子化
$$\oint\mathbf p\cdot d\mathbf r=2e\Phi-e\Phi=e\Phi=(n+\gamma)h\;\Rightarrow\;\boxed{\Phi=(n+\gamma)\frac{h}{e}=(n+\gamma)\,\Phi_0.}$$
這正是提示說的「軌道所含磁通量子化」（是 $h/e$，非超導的 $h/2e$）。

### Step 5 — 由 $\Phi$ 回推能量
$\Phi=B\pi r_n^2=(n+\gamma)\tfrac he$ → $r_n^2=(n+\gamma)\dfrac{2\hbar}{eB}$（用 $h=2\pi\hbar$）。能量
$$E=\tfrac12mv^2=\tfrac12m\Big(\tfrac{eBr_n}{m}\Big)^2=\frac{e^2B^2r_n^2}{2m}=\frac{e^2B^2}{2m}(n+\gamma)\frac{2\hbar}{eB}=(n+\gamma)\hbar\omega_c.$$
取 WKB 的 $\gamma=\tfrac12$（Maslov 指標）：
$$\boxed{E_n=\Big(n+\tfrac12\Big)\hbar\omega_c.}\quad(\text{與薛丁格解完全一致})$$

> **兩條獨立路（薛丁格／半古典磁通量子化）給同一答案，互相驗證。**

<details>
<summary><b>📝 更多範例（點開）：磁通量子化的環積分逐項展開</b></summary>

**範例 A（動力學項 $\oint m\mathbf v\cdot d\mathbf r$ 從力平衡算出）**：圓軌道上 $\mathbf v$ 與 $d\mathbf r$ 同向、$|\mathbf v|=v$ 為定值，故 $\oint m\mathbf v\cdot d\mathbf r=mv\oint dr=mv\cdot(2\pi r)$（周長）。再用勞侖茲力提供向心力 $\dfrac{mv^2}{r}=evB\Rightarrow mv=eBr$。代入：
$$\oint m\mathbf v\cdot d\mathbf r=(eBr)(2\pi r)=2\pi eB r^2.$$
而軌道包住的磁通 $\Phi=B\cdot(\pi r^2)$，即 $\pi r^2=\Phi/B$，所以 $2\pi eB r^2=2eB\cdot\pi r^2=2eB\cdot\dfrac{\Phi}{B}=2e\Phi$。每一步替換都寫出來。

**範例 B（規範項與合併）**：規範項用斯托克斯定理 $\oint\mathbf A\cdot d\mathbf r=\displaystyle\int(\nabla\times\mathbf A)\cdot d\mathbf S=\int\mathbf B\cdot d\mathbf S=\Phi$。正則動量 $\mathbf p=m\mathbf v-e\mathbf A$，所以
$$\oint\mathbf p\cdot d\mathbf r=\oint m\mathbf v\cdot d\mathbf r-e\oint\mathbf A\cdot d\mathbf r=2e\Phi-e\Phi=e\Phi.$$
代波耳–索末菲 $\oint\mathbf p\cdot d\mathbf r=(n+\gamma)h$：$e\Phi=(n+\gamma)h\Rightarrow\Phi=(n+\gamma)\dfrac he=(n+\gamma)\Phi_0$。注意這裡因子 $2e\Phi-e\Phi=e\Phi$ 留下一個 $e$（不是 $2e$），所以是 $h/e$ 不是 $h/2e$——正常金屬與超導差在這裡。

**範例 C（由 $\Phi$ 回推能量 $E_n=(n+\tfrac12)\hbar\omega_c$）**：由 $\Phi=B\pi r_n^2=(n+\gamma)\dfrac he$ 解半徑平方：$r_n^2=\dfrac{(n+\gamma)h}{e B\pi}=\dfrac{(n+\gamma)\cdot2\pi\hbar}{eB\pi}=(n+\gamma)\dfrac{2\hbar}{eB}$（用 $h=2\pi\hbar$）。動能
$$E=\tfrac12 mv^2=\tfrac12 m\Big(\frac{eBr_n}{m}\Big)^2=\frac{e^2B^2 r_n^2}{2m}=\frac{e^2B^2}{2m}(n+\gamma)\frac{2\hbar}{eB}.$$
約分：$\dfrac{e^2B^2}{2m}\cdot\dfrac{2\hbar}{eB}=\dfrac{eB\hbar}{m}=\hbar\omega_c$（因 $\omega_c=eB/m$）。故 $E=(n+\gamma)\hbar\omega_c$，取 $\gamma=\tfrac12$ 得 $E_n=(n+\tfrac12)\hbar\omega_c$，與薛丁格解完全吻合。

</details>

#### 4.4 簡併度（每個 Landau level 裝幾個態）

### Step 1 — 軌道中心離散
2D 面積 $A=L_xL_y$。軌道中心 $x_0=-\hbar k_y/eB$，$k_y=2\pi n_y/L_y$ 離散，$x_0$ 須落在 $[0,L_x]$。相鄰 $x_0$ 間距 $\Delta x_0=\dfrac{\hbar}{eB}\dfrac{2\pi}{L_y}$。

### Step 2 — 數可容納態
$$D=\frac{L_x}{\Delta x_0}=\frac{L_xL_y\,eB}{2\pi\hbar}=\boxed{\frac{eB\,A}{h}=\frac{\Phi_{\text{tot}}}{\Phi_0}.}$$
**每個 Landau level 的簡併度 = 樣品裡塞進幾個磁通量子。** $B$ 越大，每個 level 容量越大、level 數越少。

<details>
<summary><b>📝 更多範例（點開）：Landau 簡併度的計數與數值</b></summary>

**範例 A（從 $k_y$ 間距推到 $D=eBA/h$）**：週期邊界條件下 $k_y=\dfrac{2\pi n_y}{L_y}$（$n_y$ 整數），相鄰 $k_y$ 間距 $\Delta k_y=\dfrac{2\pi}{L_y}$。中心 $x_0=-\dfrac{\hbar k_y}{eB}$，故相鄰中心間距
$$\Delta x_0=\frac{\hbar}{eB}\Delta k_y=\frac{\hbar}{eB}\cdot\frac{2\pi}{L_y}=\frac{2\pi\hbar}{eBL_y}=\frac{h}{eBL_y}.$$
能塞進 $[0,L_x]$ 的中心數 $D=\dfrac{L_x}{\Delta x_0}=\dfrac{L_x\cdot eBL_y}{h}=\dfrac{eB(L_xL_y)}{h}=\dfrac{eBA}{h}$。每一步把 $\hbar$ 換 $h=2\pi\hbar$ 都寫明。

**範例 B（簡併度 = 磁通量子數）**：總磁通 $\Phi_{\text{tot}}=B\cdot A$，磁通量子 $\Phi_0=\dfrac he$。兩者相除：
$$\frac{\Phi_{\text{tot}}}{\Phi_0}=\frac{BA}{h/e}=\frac{eBA}{h}=D.$$
完全等於範例 A 的 $D$。所以「每條 Landau level 能裝的態數」＝「樣品被穿過的磁通量子個數」，這是一句話記法。

**範例 C（數值：$B=1\,\mathrm T$、$A=1\,\mathrm{cm^2}$）**：$A=10^{-4}\,\mathrm{m^2}$。
$$D=\frac{eBA}{h}=\frac{1.6\times10^{-19}\times1\times10^{-4}}{6.63\times10^{-34}}=\frac{1.6\times10^{-23}}{6.63\times10^{-34}}\approx2.4\times10^{10}.$$
單位面積簡併度 $\dfrac{D}{A}=\dfrac{eB}{h}=\dfrac{1.6\times10^{-19}\times1}{6.63\times10^{-34}}\approx2.4\times10^{14}\,\mathrm{m^{-2}}$。$B$ 加倍則 $D$ 加倍——每條 level 容量 $\propto B$，而填滿固定電子數所需的 level 數則 $\propto1/B$，這正是 de Haas–van Alphen 振盪週期 $\propto1/B$ 的根源。

</details>

> **小結**：磁場把橫向自由度變成諧振子 → $E_n=(n+\tfrac12)\hbar\omega_c$，間距 $\hbar\omega_c$，簡併度 $eBA/h$。這些 level 在費米面上凝聚成 Landau 管，掃過費米面 → de Haas–van Alphen 對 $1/B$ 週期振盪（可量費米面截面）。

---

### 5. 鐵磁性與居里溫度（Ferromagnetism & Curie Temperature）★2025

> 📖 **本節核心出處與說明（Ref）**：
> - **權威教材**：Kittel 8e Ch. 12 Eq. (1)–(7) pp. 323–326 ｜ 林盛煇 §8.3 ｜ A&M Ch. 33
> - **歷年考題**：[NTU 2025 Q4（15分）](../考古題/詳解/固態_2025_詳解.html)
> - **觀念說明**：分子場理論揭示自發對稱破缺，高於居里溫度 $T > T_C$ 自發磁化嚴格為零，系統退化為順磁相並遵循居里–外斯定律 $\chi = \frac{C}{T-T_C}$。


2025 Q4(a)：鐵磁體在 $T\to0$ 有磁化 $\mathbf M$、體積 $V$、居里溫度 $T_C$，問 **$T>T_C$ 的總磁矩是多少**？

**你高中學過的**：磁鐵（鐵、鎳）有「自發磁化」——不用外場也帶磁性。加熱到夠高（居里溫度 $T_C$）就**失去磁性**（高中常識：把磁鐵燒紅就不磁了）。

**為什麼需要新東西**：順磁靠外場才有磁化；鐵磁**零場就有**。原因是相鄰自旋之間有強烈的**交換交互作用（exchange interaction）**，傾向讓自旋互相平行。用外斯（Weiss）的**平均場（mean field）**近似，把這個交互作用模型化成一個內部「交換場（exchange field）」$B_E=\lambda M$。

#### 5.1 外斯平均場圖像

<details>
<summary><b>▸ 居里溫度 T_C（Curie temperature）</b></summary>

**你高中學過的**：相變溫度（如冰在 $0^\circ$C 融化）。$T_C$ 是「鐵磁 ↔ 順磁」的相變溫度。

**為什麼要這個**：它分開兩個相——$T<T_C$ 有自發磁化（鐵磁序）、$T>T_C$ 自發磁化消失（順磁、無序）。考題的關鍵分界。

**定義**：自發磁化消失的溫度。平均場下 $k_BT_C\propto$ 交換強度。$T>T_C$ 時 $\chi=C/(T-T_C)$（居里–外斯定律，$T\to T_C^+$ 發散）。

**範例 1**：鐵 $T_C\approx1043\,\mathrm K$、鎳 $T_C\approx627\,\mathrm K$。
**範例 2**：把鐵磁體加熱到 $T>T_C$ → 自發磁化 = 0 → 失去永久磁性。
**範例 3**：2025 Q4(a)：問 $T>T_C$ 總磁矩 → 自發磁化已消失 → 零場總磁矩 = 0。

</details>

平均場下的自發磁化（自旋 $S=\tfrac12$）滿足自洽方程
$$M=M_s\tanh\!\Big(\frac{T_C}{T}\frac{M}{M_s}\Big),$$
這是「左邊一條斜率為 1 的直線 = 右邊 $\tanh$ 曲線」的圖解。$\tanh$ 在原點斜率 = $T_C/T$：
- $T<T_C$（斜率 $>1$）→ 除了 $M=0$ 還有一個**非零交點** → 存在自發磁化 $M\neq0$（鐵磁）。
- $T>T_C$（斜率 $<1$）→ **只有 $M=0$** 一個交點 → 零場磁化消失（順磁）。
- $T=T_C$ → 曲線在原點與直線相切，是相變臨界點。

<details>
<summary><b>📝 更多範例（點開）：自洽方程的臨界溫度、臨界指數與居里–外斯</b></summary>

**範例 A（從自洽方程定出 $T_C$）**：令 $m\equiv\dfrac{M}{M_s}$，自洽方程寫成 $m=\tanh\!\Big(\dfrac{T_C}{T}m\Big)$。要找非零解何時冒出，看小 $m$ 行為，用 $\tanh u\approx u-\dfrac{u^3}{3}$（$u=\dfrac{T_C}{T}m$）：
$$m\approx\frac{T_C}{T}m-\frac13\Big(\frac{T_C}{T}\Big)^3 m^3.$$
$m\ne0$ 時兩邊除 $m$：$1\approx\dfrac{T_C}{T}-\dfrac13\Big(\dfrac{T_C}{T}\Big)^3 m^2$。當 $m\to0^+$，第二項趨於 0，得臨界條件 $\dfrac{T_C}{T}=1$，即非零解恰在 $T=T_C$ 以下才存在。這就是「原點斜率 $T_C/T$ 是否大於 1」判據的代數版。

**範例 B（臨界指數 $\beta=\tfrac12$）**：續範例 A，在 $T$ 略小於 $T_C$ 解 $m$。由 $1=\dfrac{T_C}{T}-\dfrac13\Big(\dfrac{T_C}{T}\Big)^3 m^2$ 解出
$$m^2=\frac{3\big(\frac{T_C}{T}-1\big)}{\big(\frac{T_C}{T}\big)^3}.$$
令 $t=\dfrac{T_C-T}{T_C}$（約化溫度），則 $\dfrac{T_C}{T}-1=\dfrac{T_C-T}{T}\approx t$（$T\approx T_C$），且分母 $\big(\tfrac{T_C}{T}\big)^3\approx1$。故 $m^2\approx3t$，即
$$M\propto m\propto\sqrt{t}=\Big(\frac{T_C-T}{T_C}\Big)^{1/2}.$$
指數 $\beta=\tfrac12$——平均場理論的標誌性臨界指數，解釋了 $M(T)$ 曲線在 $T_C$ 附近以「平方根」垂直切下歸零。

**範例 C（$T>T_C$ 加場 → 居里–外斯發散）**：高溫小磁化時用線性化 $\tanh u\approx u$。加外場 $B$ 後，總有效場 $=B+\lambda M$（$\lambda$ 為外斯係數，$k_BT_C\propto\lambda$）。順磁線性響應 $M=\dfrac{C}{T}(B+\lambda M)$，把含 $M$ 的項移到左邊：
$$M-\frac{C\lambda}{T}M=\frac{C}{T}B\;\Rightarrow\;M\Big(1-\frac{C\lambda}{T}\Big)=\frac{C}{T}B\;\Rightarrow\;M=\frac{C\,B}{T-C\lambda}.$$
辨識 $C\lambda\equiv T_C$，得 $\chi=\dfrac{M}{B}=\dfrac{C}{T-T_C}$（居里–外斯）。當 $T\to T_C^+$，分母 $\to0$、$\chi\to\infty$——磁化率發散正是鐵磁相變的訊號。把 §3.4 純居里的「自由場」換成「有效場 $B+\lambda M$」，分母就從 $T$ 平移成 $T-T_C$。

</details>

把這個自洽解隨溫度畫出來，就是自發磁化 $M(T)$ 的曲線：從 $T=0$ 的飽和值，一路降到 $T_C$ 歸零：

<figure style="margin:1.3em 0;text-align:center">
<svg viewBox="0 0 470 250" width="100%" style="max-width:560px;border:1px solid #ddd;border-radius:8px;background:#fff;padding:6px;box-sizing:border-box" xmlns="http://www.w3.org/2000/svg">
<g font-family="-apple-system,sans-serif" font-size="11">
<text x="235" y="20" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1a4d7c">自發磁化 M 隨溫度下降到 T_C 歸零</text>
<line x1="55" y1="205" x2="440" y2="205" stroke="#555" stroke-width="1.3"/>
<line x1="55" y1="220" x2="55" y2="40" stroke="#555" stroke-width="1.3"/>
<text x="435" y="223" text-anchor="end" fill="#555">T</text>
<text x="47" y="50" text-anchor="end" fill="#555">M</text>
<line x1="55" y1="60" x2="350" y2="60" stroke="#999" stroke-width="1" stroke-dasharray="4,3"/>
<text x="50" y="63" text-anchor="end" font-size="10.5" fill="#999">M_s</text>
<polyline points="55,60 90,60 130,61 170,64 210,69 250,78 285,92 315,116 338,150 352,184 358,205" fill="none" stroke="#c0392b" stroke-width="2.6"/>
<line x1="358" y1="205" x2="358" y2="60" stroke="#888" stroke-width="1" stroke-dasharray="4,3"/>
<text x="358" y="222" text-anchor="middle" font-size="11" fill="#1a4d7c" font-weight="bold">T_C</text>
<line x1="358" y1="205" x2="430" y2="205" stroke="#2e8b2e" stroke-width="2.6"/>
<text x="150" y="120" font-size="11.5" fill="#c0392b" font-weight="bold">鐵磁（M≠0）</text>
<text x="150" y="138" font-size="10.5" fill="#777">T&lt;T_C 自發磁化</text>
<text x="395" y="185" text-anchor="middle" font-size="11.5" fill="#2e8b2e" font-weight="bold">順磁</text>
<text x="395" y="200" text-anchor="middle" font-size="10.5" fill="#2e8b2e">M=0</text>
</g>
</svg>
<figcaption style="font-size:0.9em;color:#555;margin-top:0.5em">鐵磁體的自發磁化 M(T)。<b style="color:#c0392b">T&lt;T_C</b>：交換場壓過熱擾動，零場就有磁化；T=0 時達飽和 M_s（全部自旋同向）。升溫時熱擾動逐漸打亂自旋，M 平滑下降，在 <b style="color:#1a4d7c">T_C</b>（居里溫度）<b>連續降到 0</b>（二級相變）。<b style="color:#2e8b2e">T&gt;T_C</b>：自發磁化完全消失、進入順磁相（M=0，零場無磁性）。這正是「把磁鐵燒紅就不磁了」的曲線，也是 2025 Q4(a) 的答案來源。</figcaption>
</figure>

#### 5.2 回答 2025 Q4(a)

### Step 1 — 判斷相
$T>T_C$ → 鐵磁序被熱擾動破壞 → 轉為**順磁相**，自發磁化 $M_s(T>T_C)=0$。

### Step 2 — 算零場總磁矩
零場下總磁矩 = 自發磁化 × 體積：
$$\boxed{\text{總磁矩}=M_s\,V=0\times V=0.}$$
（若再外加磁場，則出現居里–外斯響應 $\chi=C/(T-T_C)$，磁化不再是零，但**自發**部分仍為 0。）

#### 5.3 磁滯迴線與磁區（補充：鐵磁的兩張招牌圖）

鐵磁在 $T<T_C$ 加場、退場時，磁化不會「原路折返」——它走出一條**磁滯迴線（hysteresis loop）**，這是永久磁鐵與磁性記憶體的物理：

<figure style="margin:1.3em 0;text-align:center">
<svg viewBox="0 0 440 320" width="100%" style="max-width:480px;border:1px solid #ddd;border-radius:8px;background:#fff;padding:6px;box-sizing:border-box" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="magHy8g" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c0392b"/></marker>
</defs>
<g font-family="-apple-system,sans-serif" font-size="11">
<text x="220" y="20" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1a4d7c">鐵磁磁滯迴線 M–H</text>
<line x1="40" y1="170" x2="420" y2="170" stroke="#555" stroke-width="1.2"/>
<line x1="220" y1="40" x2="220" y2="305" stroke="#555" stroke-width="1.2"/>
<text x="414" y="188" text-anchor="end" fill="#555">H</text>
<text x="232" y="50" fill="#555">M</text>
<path d="M65,290 C120,288 150,275 175,245 C200,215 210,150 270,105 C330,62 395,58 410,57" fill="none" stroke="#c0392b" stroke-width="2.4" marker-end="url(#magHy8g)"/>
<path d="M410,57 C360,58 320,62 280,80 C235,100 232,150 215,175 C175,235 110,250 65,290" fill="none" stroke="#1a4d7c" stroke-width="2.4"/>
<line x1="220" y1="80" x2="410" y2="80" stroke="#999" stroke-width="0.9" stroke-dasharray="4,3"/>
<text x="408" y="74" text-anchor="end" font-size="10.5" fill="#888">飽和 M_s</text>
<circle cx="220" cy="100" r="3.5" fill="#2e8b2e"/>
<text x="226" y="98" font-size="11" fill="#2e8b2e" font-weight="bold">M_r 殘磁</text>
<text x="226" y="112" font-size="9.5" fill="#777">(H=0 仍有磁)</text>
<circle cx="278" cy="170" r="3.5" fill="#e67e22"/>
<text x="284" y="186" font-size="11" fill="#e67e22" font-weight="bold">H_c 矯頑場</text>
<text x="284" y="199" font-size="9.5" fill="#777">(把 M 歸零所需反向場)</text>
<text x="100" y="300" font-size="10.5" fill="#c0392b">↗ 加場初始磁化</text>
<text x="300" y="50" font-size="10.5" fill="#1a4d7c">退場走另一條路</text>
</g>
</svg>
<figcaption style="font-size:0.9em;color:#555;margin-top:0.5em">鐵磁磁滯迴線。沿 H 加大，M 升到<b>飽和 M_s</b>（全部磁區轉向場）。把場降回 0，M 不歸零、留下<b style="color:#2e8b2e">殘磁 M_r（remanence）</b>——這就是「永久磁鐵」。要把 M 歸零必須加反向場到<b style="color:#e67e22">矯頑場 H_c（coercivity）</b>。迴線圍出的面積 = 一圈損耗的能量。H_c 大（硬磁）→ 永久磁鐵/記憶體；H_c 小（軟磁）→ 變壓器鐵芯。</figcaption>
</figure>

<details>
<summary><b>📝 更多範例（點開）：磁滯損耗能量與矯頑場的定量</b></summary>

**範例 A（一圈磁滯損耗 = 迴線面積）**：外場對單位體積材料做的功密度是 $dw=H\,dB=\mu_0 H\,dM$（弱磁時 $B\approx\mu_0(H+M)\approx\mu_0 M$）。繞磁滯迴線一圈，淨功
$$W_{\text{loss}}=\oint \mu_0 H\,dM=\mu_0\times(\text{M–H 迴線圍出的面積}).$$
因為「加場路徑」與「退場路徑」不同（迴線不閉合成零面積），$\oint H\,dM\ne0$，這部分功變成熱。每繞一圈就損耗一次 → 變壓器鐵芯在交流頻率 $f$ 下每秒損耗 $P=f\,W_{\text{loss}}$。軟磁（迴線瘦）面積小、損耗小，正適合鐵芯。

**範例 B（矯頑場做的反向功，矩形迴線近似）**：把迴線理想化成矩形：$M$ 在 $\pm M_s$ 之間跳，水平寬 $2H_c$、垂直高 $2M_s$。面積 $=(2H_c)(2M_s)=4H_cM_s$，故
$$W_{\text{loss}}=\mu_0\cdot 4H_c M_s.$$
代數值：硬磁 $\mu_0 H_c=0.1\,\mathrm T$、$\mu_0 M_s=1\,\mathrm T$，單位體積每圈損耗 $W=4\times\dfrac{(0.1)(1)}{\mu_0}=\dfrac{0.4}{4\pi\times10^{-7}}\approx3.2\times10^{5}\,\mathrm{J/m^3}$。可見 $H_c$ 越大、每圈損耗越大——這就是「硬磁適合永久磁鐵/記憶（抗去磁），軟磁適合鐵芯（低損耗）」的定量根據。

**範例 C（矯頑場與各向異性能的尺度）**：單疇粒子的反轉須克服磁各向異性能 $E_a=K_u\sin^2\theta$（$K_u$ 各向異性常數）。施加反向場 $H$，能量密度 $E=K_u\sin^2\theta-\mu_0 M_s H\cos\theta$。對 $\theta$ 求極值並令位障消失，可得理想矯頑場（Stoner–Wohlfarth）
$$\mu_0 H_c=\frac{2K_u}{M_s}.$$
代 $K_u=5\times10^5\,\mathrm{J/m^3}$、$M_s=1.4\times10^6\,\mathrm{A/m}$：$\mu_0 H_c=\dfrac{2\times5\times10^5}{1.4\times10^6}\approx0.71\,\mathrm T$。實測常因疇壁成核而小於此「理想上限」（Brown 佯謬），但量級對：$K_u$ 大的材料（如 Nd–Fe–B）矯頑場大、是強永久磁鐵。

</details>

未加場時鐵磁體常常「整體不顯磁性」，原因是它分成許多方向不同的**磁區（magnetic domain）**，彼此抵消：

<figure style="margin:1.3em 0;text-align:center">
<svg viewBox="0 0 560 210" width="100%" style="max-width:680px;border:1px solid #ddd;border-radius:8px;background:#fff;padding:6px;box-sizing:border-box" xmlns="http://www.w3.org/2000/svg">
<defs>
<marker id="magDoU8h" markerWidth="8" markerHeight="8" refX="3" refY="0" orient="auto"><path d="M0,6 L3,0 L6,6 Z" fill="#1a4d7c"/></marker>
<marker id="magDoR8h" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#1a4d7c"/></marker>
<marker id="magDoB8h" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#2e8b2e"/></marker>
</defs>
<g font-family="-apple-system,sans-serif" font-size="11">
<g transform="translate(0,0)">
<text x="120" y="20" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#1a4d7c">未磁化：多磁區抵消</text>
<rect x="35" y="35" width="170" height="150" fill="none" stroke="#1a4d7c" stroke-width="1.6"/>
<line x1="120" y1="35" x2="120" y2="185" stroke="#aaa" stroke-width="1"/>
<line x1="35" y1="110" x2="205" y2="110" stroke="#aaa" stroke-width="1"/>
<g stroke="#1a4d7c" stroke-width="2.2">
<line x1="77" y1="100" x2="77" y2="48" marker-end="url(#magDoU8h)"/>
<line x1="163" y1="48" x2="163" y2="100" marker-end="url(#magDoU8h)"/>
<line x1="48" y1="148" x2="105" y2="148" marker-end="url(#magDoR8h)"/>
<line x1="190" y1="172" x2="135" y2="172" marker-end="url(#magDoR8h)"/>
</g>
<text x="120" y="205" text-anchor="middle" fill="#555">各區方向不同 → 淨 M≈0</text>
</g>
<text x="290" y="115" text-anchor="middle" font-size="20" fill="#2e8b2e">→</text>
<text x="290" y="135" text-anchor="middle" font-size="10" fill="#2e8b2e">加場</text>
<g transform="translate(335,0)">
<text x="120" y="20" text-anchor="middle" font-size="12.5" font-weight="bold" fill="#2e8b2e">加場後：疇壁移動、磁區轉向</text>
<rect x="35" y="35" width="170" height="150" fill="#e8f3e8" stroke="#2e8b2e" stroke-width="1.6"/>
<g stroke="#2e8b2e" stroke-width="2.2">
<line x1="60" y1="100" x2="60" y2="48" marker-end="url(#magDoB8h)"/>
<line x1="100" y1="100" x2="100" y2="48" marker-end="url(#magDoB8h)"/>
<line x1="140" y1="100" x2="140" y2="48" marker-end="url(#magDoB8h)"/>
<line x1="180" y1="100" x2="180" y2="48" marker-end="url(#magDoB8h)"/>
<line x1="60" y1="172" x2="60" y2="120" marker-end="url(#magDoB8h)"/>
<line x1="100" y1="172" x2="100" y2="120" marker-end="url(#magDoB8h)"/>
<line x1="140" y1="172" x2="140" y2="120" marker-end="url(#magDoB8h)"/>
<line x1="180" y1="172" x2="180" y2="120" marker-end="url(#magDoB8h)"/>
</g>
<text x="120" y="205" text-anchor="middle" fill="#555">同向磁區長大 → M 飽和</text>
</g>
</g>
</svg>
<figcaption style="font-size:0.9em;color:#555;margin-top:0.5em">磁區與疇壁。<b>左</b>：鐵磁體即使 T&lt;T_C 有自發磁化，也常自發分成多個方向不同的<b>磁區（domain）</b>（為了降低退磁場能量），彼此抵消、整塊<b>對外不顯磁</b>（淨 M≈0，所以新鐵釘不黏東西）。<b>右</b>：加外場時，<b>疇壁（domain wall）移動</b>、與場同向的磁區長大、其他磁區轉向，直到整塊同向、M 飽和——這就是磁滯迴線「初始磁化」那一段的微觀機制。</figcaption>
</figure>

> **小結**：$T>T_C$ 自發磁化消失 → 零場總磁矩 = 0。鐵磁 = 順磁 + 交換場（讓 $\chi$ 在 $T_C$ 發散）。記住三條相態：$T<T_C$ 鐵磁、$T=T_C$ 臨界、$T>T_C$ 順磁（居里–外斯）。

---

## 🔑 必背公式速查（考前最後看）

| 公式與物理主題 | $\boxed{\ }$ 數學形式 | 物理說明與何時用 | 權威出處（Ref） |
|---|---|---|---|
| 磁偶極外場位能 | $U=-\boldsymbol\mu\cdot\mathbf B=-\mu B\cos\theta$ | 磁性統計物理推導基石，代入波茲曼分佈因子 $e^{-U/k_B T}$ | Kittel 8e Ch. 11 Eq. (19) p. 305 ｜ 林盛煇 §8.2 ｜ 2013 Q13 |
| 朗之萬順磁磁化強度 | $M = N m L(\alpha),\quad L(\alpha)=\coth\alpha-\frac{1}{\alpha},\ \alpha=\frac{mB}{k_B T}$ | 經典自由轉動奈米磁矩在均勻磁場下的熱平衡磁化強度 | Kittel 8e Ch. 11 Eq. (20) p. 305 ｜ 林盛煇 §8.2 ｜ 2013 Q13 (20分) |
| 朗之萬函數高溫極限 | $L(\alpha) \approx \frac{\alpha}{3} \quad (\alpha\ll 1)$ | 弱場高溫展開還原出居里定律 | Kittel 8e Ch. 11 Eq. (21) p. 305 ｜ 林盛煇 §8.2 ｜ 2013 Q13 |
| 順磁居里定律 | $\chi = \frac{M}{B} = \frac{C}{T},\quad C=\frac{N m^2}{3k_B}$ | 順磁磁化率與溫度成反比，$1/T$ 作圖求微觀磁矩 $m$ | Kittel 8e Ch. 11 Eq. (18) p. 304 ｜ 林盛煇 §8.3 ｜ 2013 Q13 |
| 磁化率正負號定義 | $\chi < 0 \ (\text{抗磁}),\quad \chi > 0 \ (\text{順磁與鐵磁})$ | 磁化率反映材料感應磁化與外加磁場同向或反向 | Kittel 8e Ch. 11 Eq. (2) p. 298 ｜ 林盛煇 §8.1 ｜ 2013, 2025 |
| 二維朗道能階（Landau Levels） | $E_n = \left(n+\frac{1}{2}\right)\hbar\omega_c + \frac{\hbar^2 k_z^2}{2m},\quad \omega_c=\frac{eB}{m}$ | 均勻磁場使電子垂直面動能諧振子量子化 | Kittel 8e Ch. 11 p. 317 ｜ 林盛煇 §8.5 ｜ 2018 Q4 (20分) |
| 朗道軌道磁通量子化 | $\Phi = \oint \mathbf A\cdot d\boldsymbol\ell = \left(n+\gamma\right)\Phi_0,\quad \Phi_0=\frac{h}{e}$ | 正常電子在磁場下閉合軌道包圍的磁通量量子化 | Kittel 8e Ch. 11 p. 318 ｜ 林盛煇 §8.5 ｜ 2018 Q4 (20分) |
| 朗道能階簡併度 | $D = \frac{e B A}{h} = \frac{\Phi_{\text{tot}}}{\Phi_0}$ | 每個朗道能階容納的電子態數正比於總磁通量 | Kittel 8e Ch. 11 p. 318 ｜ 林盛煇 §8.5 ｜ 2018 Q4 |
| 居里–外斯定律 | $\chi = \frac{C}{T-T_C} \quad (T > T_C)$ | 鐵磁體在居里溫度以上順磁相的磁化率，當 $T>T_C$ 自發磁化強度為 0 | Kittel 8e Ch. 12 Eq. (7) p. 325 ｜ 林盛煇 §8.3 ｜ 2025 Q4 (15分) |

---

## 📚 本單元權威參考文獻與出處對照（References）

1. **Charles Kittel, *Introduction to Solid State Physics***, 8th Edition, John Wiley & Sons, 2005.
   - **Chapter 11: Diamagnetism and Paramagnetism** (pp. 297–322)
     - Langevin diamagnetism equation: pp. 299–301, Eq. (9)
     - Quantum theory of diamagnetism of mononuclear systems: pp. 301–303
     - Paramagnetism & Curie's law: pp. 303–305, Eq. (18)
     - Classical Langevin theory of paramagnetism: p. 305, Eq. (20)–(21)
     - Quantum theory of paramagnetism (Brillouin function): pp. 305–309
     - Landau levels & magnetic orbital quantization: pp. 317–319
   - **Chapter 12: Ferromagnetism and Antiferromagnetism** (pp. 323–352)
     - Ferromagnetic order & Curie-Weiss law: pp. 323–326, Eq. (1)–(7)
     - Heisenberg exchange interaction & Weiss molecular field: pp. 326–328
     - Ferromagnetic domains & hysteresis: pp. 338–344
2. **林盛煇,《固態物理導論》**, 新文京開發出版.
   - **第 8 章：磁性物理** (pp. 321–370)
     - §8.1 物質磁性起源與原子磁矩
     - §8.2 朗之萬抗磁性與順磁性理論
     - §8.3 居里定律與居里–外斯分子場理論
     - §8.4 鐵磁性、反鐵磁性與自旋交換作用
     - §8.5 強磁場下的朗道能階量子化
3. **Neil W. Ashcroft & N. David Mermin, *Solid State Physics***, Saunders College Publishing, 1976.
   - **Chapter 31: Diamagnetism and Paramagnetism** (pp. 643–670)
   - **Chapter 32: Electron Interactions and Magnetic Structure** (pp. 671–694)
   - **Chapter 33: Magnetic Ordering** (pp. 695–724)
4. **國立臺灣大學應用物理學研究所博士班資格考試題**：
   - 2025 Q4 (15分): 鐵磁材料高於居里溫度（$T>T_C$）自發磁矩嚴格為零之物理推導
   - 2018 Q4 (20分): 外磁場下費米面之朗道能階量子化與軌道磁通量子化證明
   - 2013 Q13 (20分): 奈米磁顆粒外場位能、波茲曼因子積分與朗之萬函數 $L(lpha)=\cothlpha - 1/lpha$ 完整推導

---

## 📝 歷年考題實戰

- **[2013 Q14](../考古題/詳解/固態_2013_詳解.html)**（10 pts）★長推導：$N$ 顆隨機取向奈米磁體在外場 $H$，由波茲曼因子推 $M(H)=NmL(\alpha)$、$L(\alpha)=\coth\alpha-1/\alpha$。對應本篇 §3，含分部積分全步驟與居里定律極限。
- **[2013 Q13](../考古題/詳解/固態_2013_詳解.html)**（3 pts）：磁性儲存的物理極限（超順磁極限 $K_uV$ vs $k_BT$）。屬本單元延伸觀念。
- **[2018 Q4](../考古題/詳解/固態_2018_詳解.html)**（20 pts）★本卷重頭戲：磁場下費米面上 Landau level 的存在，定性 + 盡量定量（薛丁格解 + 軌道磁通量子化兩條路）。對應本篇 §4。
- **[2025 Q4(a)](../考古題/詳解/固態_2025_詳解.html)**（5 pts）：鐵磁體在 $T>T_C$ 的總磁矩（自發磁化消失 → 0）。對應本篇 §5。

---

## ✅ 自我檢核 ＋ 常見陷阱

**你應該能默寫/回答：**
1. 寫出 $U=-\mu B\cos\theta$，並把它丟進波茲曼因子寫出 $\langle m_z\rangle$ 的積分式（§3 Step 1）。
2. 換元 $x=\cos\theta$ 後，獨立算出分母 $2\sinh\alpha/\alpha$、分子（分部積分），相除得 $L(\alpha)=\coth\alpha-1/\alpha$。
3. 由 $L\approx\alpha/3$ 推出居里定律 $\chi=Nm^2/3k_BT=C/T$。
4. 說出抗磁（$\chi<0$、感應、無關溫度）與順磁（$\chi>0$、永久矩、$\propto1/T$）的物理區別。
5. 寫出 Landau 能階 $E_n=(n+\tfrac12)\hbar\omega_c$、$\omega_c=eB/m$，並用薛丁格解 + 磁通量子化兩條路導出。
6. 說出 Landau level 簡併度 $eBA/h=\Phi_{\text{tot}}/\Phi_0$ 的物理意義。
7. 回答 $T>T_C$ 時鐵磁體零場總磁矩 = 0，並寫出居里–外斯 $\chi=C/(T-T_C)$。

**常見陷阱：**
- **Langevin 分母不要忘**（陷阱）：$\langle m_z\rangle$ 要除以歸一化積分（partition function），不是只算分子。
- **正常金屬磁通量子是 $h/e$，不是 $h/2e$**（陷阱）：$h/2e$ 是**超導**（superconductivity）的，因 Cooper 對帶 $2e$。Landau 量子化用 $h/e$。
- **抗磁 ≠ 沒磁矩**（陷阱）：抗磁是「外場感應出反向矩」，連惰性氣體都有；別與「沒有永久磁矩」混淆。
- **$T>T_C$ 不是沒有磁性，而是沒有「自發」磁化**（陷阱）：加場仍有居里–外斯順磁響應，只是零場總磁矩為 0。
- **$\alpha$ 用 $B$ 還是 $H$**（陷阱）：題目寫 $\alpha=mH/k_BT$ 時把 $H$ 當外場強度；本篇必背欄用 $B$。兩者真空中差 $\mu_0$，數學步驟相同。

---

## 🔭 信心評估 ＋ 下一步

**信心評估**：磁性是第四梯隊（出題零星但近年回溫），但每種題型都「可背滿分」——Langevin（2013）、Landau（2018）、鐵磁 $T_C$（2025）三套各自獨立、推導固定，把 §3/§4/§5 三段練到能默寫即可穩拿分。

**下一步**：磁性常與超導同段出現（2013、2025 都是磁性 + 超導合題）。接著看 unit09 超導（Meissner 效應、type I/II、磁通渦旋 $\Phi_0=h/2e$），正好和本篇 Landau 的 $\Phi_0=h/e$ 對照記憶。Landau 能階的薛丁格解與簡併度也用到 unit05（自由電子費米氣體）的 DOS 概念，可回頭對照「無場 2D DOS = 常數」與 Landau level 的態數守恆。

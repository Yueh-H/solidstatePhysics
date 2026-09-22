# 固態物理「單元學科完整版」教學 — 共用寫作規格（給每個單元作者）

你要寫一份**固態物理（Solid State Physics）某單元的完整教學 markdown**，給「只有高中數學 + 單變數微積分 + 基本矩陣/向量」程度的學習者，從**高中概念**一路推到**台大應物所博士班資格考**等級。仿照本 repo 的 QFT「符號就地展開」tutorial 方法。

> 對象考試：NTU 應用物理所博士班資格考「固態物理導論」，範圍依 **C. Kittel,《Introduction to Solid State Physics》**。目標 **2027 年初資格考**。

---

## 0. 鐵則（務必遵守）

1. **繁體中文（台灣用語）**。嚴禁簡體字。物理量、單位、人名用原文。
2. **專有名詞中英對照**：每個技術名詞**第一次出現**寫成「中文（English）」，例如：原胞（primitive cell）、布拉菲晶格（Bravais lattice）、倒晶格（reciprocal lattice）、色散關係（dispersion relation）、能態密度（density of states, DOS）、有效質量（effective mass）。之後可只用中文或只用英文符號。**主要概念的小標題也用中英對照。**
3. **從高中起建**：每個新符號/概念都先有「### 你高中學過的」錨點（單變數微分、畢氏定理、向量內積/外積、單位矩陣、波 $y=A\sin(kx-\omega t)$、等比級數、$T=\tfrac12mv^2$、波耳模型…），再接到新東西。**即使概念看似簡單也要保留這個錨點**。
4. **符號就地展開**：每個新符號用 `<details><summary><b>▸ $符號$（中文（English））</b></summary>` 收合區塊，內含「你高中學過的 → 為什麼要這個 → 定義 → 範例1/2/3」。**範例剛好 3 個**（範例1 最接近高中、範例2 中階、範例3 對到歷年考題的實際用法）。
5. **推導不跳步**：關鍵證明/計算用 `### Step 1 / Step 2 / …`，一步一個動作，每步結尾把中間結果**粗體或 $\boxed{}$**，下一步從那個結果接續。禁止「易證」「顯然」「整理得」。
6. **錨定歷年考題**：每個單元最後要有「📝 歷年考題實戰」段，把該單元的歷年真考題列出，連到既有逐題詳解（見下方各單元的 anchor 清單與連結格式）。
7. **數學用 MathJax**：行內 `$...$`、獨立式 `$$...$$`。寫完自我檢查 `$` 與 `$$` 成對。

---

## 1. 每個單元 markdown 的固定骨架

````markdown
<!-- 固態物理 單元XX：<中文名>（<English>） · 從高中到資格考 -->

# 固態物理 單元XX — <中文名>（<English name>）
### 從高中概念建到資格考

> **使用說明**：本篇從你高中會的東西出發，一路接到 Kittel 等級。符號點 `▸` 就地展開。專有名詞第一次出現用「中文（English）」對照。配套：[單元整理](../考古題/單元整理.html)（出題頻率）、[逐題詳解](../考古題/詳解/index.html)、[教材直讀](../教材/index.html)。
> **慣例（本篇符號）**：<列出本單元會用到的主要符號慣例，例如晶格向量 $\mathbf a_i$、倒晶格 $\mathbf b_i$ 且 $\mathbf a_i\cdot\mathbf b_j=2\pi\delta_{ij}$、$\hbar$、$k_B$…>

---

## 🎯 這個單元在考什麼（出題地位）
<用一段＋小表說明：近年出題頻率（梯隊）、典型配分、最常見題型。資料取自 ../考古題/單元整理.md 對應單元。>

## 🧗 高中起點：你已經會的
<條列這個單元會「接上去」的高中/普物概念（3–6 點），每點一句話，讓讀者知道地基在哪。>

---

## 📚 主線：從高中一路推到考試級
<這是主體。依「概念鏈」分節 ### 1. / ### 2. / …，每節：>
### 1. <概念中文（English）>
**你高中學過的** … → **為什麼需要新東西** … → **定義（中英對照）** … → 接著該符號的 `<details>` 就地展開（範例1/2/3）。
<關鍵推導（如填充率、結構因子消光、色散關係、Bloch 定理、DOS、有效質量…）用 ### Step 1/2/… 全步驟展開。>
> **小結**：<一句話留存重點>

### 2. …
（依此類推，把該單元「必考的推導與圖像」全部建出來）

---

## 🔑 必背公式速查（考前最後看）
<把該單元「必背」公式用 $\boxed{}$ 或表格列出，每條附一句「何時用」。資料對齊 ../考古題/單元整理.md 的「必背」。>

## 📝 歷年考題實戰
<列該單元歷年真考題，每題：一句題意 + 連到既有詳解。連結格式：[2024 Q2](../考古題/詳解/固態_2024_詳解.html)。>

## ✅ 自我檢核 ＋ 常見陷阱
<5–8 條「你應該能默寫/回答」的檢核點；再列 2–4 個常見陷阱（中英對照）。>

## 🔭 信心評估 ＋ 下一步
<一句信心評估；指到相鄰單元（[[unitYY]] 風格可用純文字）。>
````

---

## 2. 專有名詞中英對照（請統一用詞，第一次出現都對照一次）

晶格（lattice）、基元/基底（basis）、布拉菲晶格（Bravais lattice）、原胞（primitive cell）、慣用晶胞（conventional cell）、維格納–賽茲原胞（Wigner–Seitz cell）、填充率（packing fraction / filling factor）、密勒指標（Miller indices）、倒晶格（reciprocal lattice）、布里淵區（Brillouin zone, BZ）、布拉格定律（Bragg law）、勞厄條件（Laue condition）、結構因子（structure factor）、消光規則（systematic absence / extinction rule）、原子形狀因子（atomic form factor）、凡得瓦力（van der Waals interaction）、離子鍵（ionic bond）、共價鍵（covalent bond）、金屬鍵（metallic bond）、馬德隆常數（Madelung constant）、藍納–瓊斯位能（Lennard–Jones potential）、內聚能（cohesive energy）、聲子（phonon）、色散關係（dispersion relation）、聲學支/光學支（acoustic / optical branch）、群速度（group velocity）、德拜模型（Debye model）、愛因斯坦模型（Einstein model）、杜隆–珀蒂定律（Dulong–Petit law）、簡正模（normal mode）、自由電子費米氣體（free electron Fermi gas）、費米能（Fermi energy）、費米面/球（Fermi surface / sphere）、能態密度（density of states, DOS）、索末菲展開（Sommerfeld expansion）、德魯德模型（Drude model）、遷移率（mobility）、維德曼–夫蘭茲定律（Wiedemann–Franz law）、勞侖茲數（Lorenz number）、能帶（energy band）、能隙（energy gap）、布洛赫定理（Bloch theorem）、近自由電子（nearly free electron, NFE）、克勒尼希–潘尼模型（Kronig–Penney model）、晶體動量（crystal momentum）、有效質量（effective mass）、緊束縛（tight-binding）、電洞（hole）、施主/受主（donor / acceptor）、本質/外質半導體（intrinsic / extrinsic semiconductor）、直接/間接能隙（direct / indirect gap）、pn 接面（pn junction）、內建電位（built-in voltage）、霍爾效應（Hall effect）、順磁/抗磁（paramagnetism / diamagnetism）、居里定律（Curie law）、朗之萬函數（Langevin function）、朗道能階（Landau level）、鐵磁性（ferromagnetism）、居里溫度（Curie temperature）、邁斯納效應（Meissner effect）、第一/第二類超導體（type I / type II superconductor）、磁通渦旋（flux vortex）。

---

## 3. 各單元的範圍、Kittel 章節、必背、anchor 考題（作者只負責自己那一個）

> 每位作者：**先讀** `../考古題/單元整理.md` 找到你單元那一節（核心考點＋歷年題＋必背）；**再讀** 你的 anchor 詳解檔（`../考古題/詳解/固態_<年>_詳解.md`）確認題目與既有解法不衝突；Kittel 內容你多半已熟，必要時 grep `../教材/Kittel_原文.md` 對符號。**錨點連結一律指向 .html。**

| 單元 | 檔名 | 中文（English） | Kittel | 深度 | anchor 詳解（連 .html） |
|---|---|---|---|---|---|
| 01 | `unit01_晶體結構.md` | 晶體結構（Crystal Structure） | Ch1 | 深 | 2025,2024,2023,2022,2021,2020,2016,2015,2014,2013 |
| 02 | `unit02_倒晶格與繞射.md` | 倒晶格與繞射（Reciprocal Lattice & Diffraction） | Ch2 | 深 | 2025,2023,2022,2021,2018,2016,2015,2014,2013 |
| 03 | `unit03_晶體鍵結.md` | 晶體鍵結（Crystal Binding） | Ch3 | 中 | 2024,2023,2020,2019,2016,2015,2014,2013 |
| 04 | `unit04_聲子與晶格振動.md` | 聲子／晶格振動（Phonons / Lattice Vibrations） | Ch4–5 | 深 | 2024,2023,2022,2021,2020,2019,2018,2016,2014,2013 |
| 05 | `unit05_自由電子費米氣體.md` | 自由電子費米氣體（Free Electron Fermi Gas） | Ch6 | 深 | 2025,2023,2022,2021,2020,2017,2016,2015,2014,2013 |
| 06 | `unit06_能帶與Bloch電子.md` | 能帶理論／Bloch 電子（Energy Bands / Bloch Electrons） | Ch7 | 深 | 2025,2024,2021,2020,2019,2018,2017,2016,2015,2014,2013 |
| 07 | `unit07_半導體.md` | 半導體（Semiconductors） | Ch8 | 中 | 2023,2022,2021,2017,2016,2013 |
| 08 | `unit08_磁性.md` | 磁性（Magnetism） | Ch11–12 | 中 | 2025,2018,2013 |
| 09 | `unit09_超導.md` | 超導（Superconductivity） | Ch10 | 中短 | 2025,2013 |
| 10 | `unit10_實驗與進階.md` | 實驗技術／進階主題（Experimental Techniques / Advanced） | 跨章 | 中短 | 2022,2018,2013 |

### 各單元「必背」重點（摘自單元整理，作者請展開成完整推導）
- **01**：sc/bcc/fcc/diamond/hcp 填充率（0.52/0.68/0.74/0.34/0.74）推導；hcp 理想 $c/a=\sqrt{8/3}\approx1.633$；$[hkl]\perp(hkl)$（立方）與 $d_{hkl}=a/\sqrt{h^2+k^2+l^2}$；basis 判準（位移 $\boldsymbol\delta$ 是否為晶格半向量）。
- **02**：各晶格結構因子與消光（bcc：$h+k+l$ 奇消失；fcc：$hkl$ 須全奇或全偶；diamond 額外條件）；$2d\sin\theta=n\lambda$；Ewald 球與 $\Delta\mathbf k=\mathbf G$；三種探針（X 光/中子/電子）強度差異來源；由 $\mathbf a_i$ 建 $\mathbf b_i$。
- **03**：藍納–瓊斯 $U=4\varepsilon[(\sigma/r)^{12}-(\sigma/r)^6]$、fcc 平衡距離與內聚能、惰性氣體沸點差異；1D 離子鏈馬德隆常數 $=2\ln2$；離子內聚能＝馬德隆＋排斥。
- **04**：單原子鏈 $\omega=2\sqrt{C/M}\,|\sin(Ka/2)|$；雙原子鏈聲學/光學能隙；德拜 $T^3$（低溫）與杜隆–珀蒂（高溫）；$\omega>\omega_{\max}\Rightarrow K$ 複數（衰減波）。
- **05**：DOS $g(E)\propto E^{1/2}$（3D）、常數（2D）、$E^{-1/2}$（1D）；$C_{el}=\gamma T$；$E_F=(\hbar^2/2m)(3\pi^2n)^{2/3}$；$\sigma=ne^2\tau/m$；維德曼–夫蘭茲 $K/\sigma T=\pi^2k_B^2/3e^2$。
- **06**：Bloch $\psi_k(\mathbf r)=u_k(\mathbf r)e^{i\mathbf k\cdot\mathbf r}$ 與兩種證法（平移算符對易／Kittel 法）；NFE 在 BZ 邊界開能隙 $=2|U_G|$；Kronig–Penney 超越方程；$1/m^*=(1/\hbar^2)d^2E/dk^2$（band 頂為負）；tight-binding $E(k)=-\alpha-2\gamma\cos(ka)$。
- **07**：本質載子 $n_i\propto T^{3/2}e^{-E_g/2k_BT}$；內建電位；霍爾效應測載子型別/濃度；直接/間接吸收（是否需聲子）；由 Bloch 運動方程推有效質量。
- **08**：朗之萬 $L(\alpha)=\coth\alpha-1/\alpha$ 與 $M=NmL(\alpha)$；居里定律 $\chi=C/T$；朗道能階 $E_n=(n+\tfrac12)\hbar\omega_c$；$T>T_C$ 自發磁化消失。
- **09**：邁斯納效應；第一/第二類；下/上臨界場 $H_{c1}/H_{c2}$ 與渦旋態；BCS 配對概念（定性）。
- **10**：STM/AFM/MFM 原理與量測（tunneling barrier height）；X 光反射率多層膜每第三峰消失（數學）；石墨烯 Dirac point 線性色散 ⇒ 無質量；蛋白質結晶 X 光定形狀；量 DOS 的實驗。

---

## 4. 交付

- 只輸出**一個檔**：你負責的 `unitXX_*.md`，寫到 `solidstatePhysics/單元教學/` 底下（用 Write）。
- **不要**自己建 HTML（主控會用既有 `_build_html.py` 統一產生）。
- 完成後回報：檔名、行數、涵蓋了哪些 anchor 考題、`$`/`$$` 是否成對。
- 目標長度：深度單元 ~500–900 行，中等 ~350–550 行，中短 ~250–400 行。寧可詳盡，不要跳步。

# 🎓 固態物理導論 — 單元學科完整版 ＆ 全公式速查大全（含出處 Ref）

> 本目錄為 **NTU 應用物理所博士班資格考「固態物理導論」** 備考全系列教材。  
> 依 **C. Kittel《Introduction to Solid State Physics》8th ed.** 核心範圍精編 10 大單元，教學採「高中概念起建 $\to$ 符號就地展開 $\to$ 資格考真題推導」，推導絕不跳步。全書數值與公式皆經程式驗證。  
> **配套資源**：[📊 資格考單元整理](../考古題/單元整理.md) ｜ [✍️ 歷年逐題詳解](../考古題/詳解/index.html) ｜ [📖 教材直讀](../教材/index.html) ｜ [🧭 備考導讀](../考古題/導讀.md) ｜ [🖥️ 本機互動教學版（含公式快查與 Ref）](index.html)

---

## 🗺️ 十大單元全景導覽 ＆ 教材對照

| 單元 | 主題（中文 / 英文） | Kittel 8e 章節 | 核心考點與推導 | 考試梯隊 | 完整講義 |
|:---:|:---|:---:|:---|:---:|:---:|
| **01** | [晶體結構（Crystal Structure）](unit01_晶體結構.md) | **Ch. 1** (p.1–28) | 原胞、Bravais 晶格、密勒指標、各晶型填充率、HCP $c/a$ 軸比 | **第一梯隊** | [📖 unit01_晶體結構.md](unit01_晶體結構.md) |
| **02** | [倒晶格與繞射（Reciprocal Lattice & Diffraction）](unit02_倒晶格與繞射.md) | **Ch. 2** (p.29–52) | 倒晶格向量 $\mathbf b_i$、Bragg 與 Laue 等價性、幾何結構因子 $S_{\mathbf G}$、消光規則 | **第一梯隊** | [📖 unit02_倒晶格與繞射.md](unit02_倒晶格與繞射.md) |
| **03** | [晶體鍵結（Crystal Binding）](unit03_晶體鍵結.md) | **Ch. 3** (p.53–84) | Lennard-Jones 12-6 位能、內聚能、Madelung 常數、離子鍵與共價鍵 | **第二梯隊** | [📖 unit03_晶體鍵結.md](unit03_晶體鍵結.md) |
| **04** | [聲子與晶格振動（Phonons / Vibrations）](unit04_聲子與晶格振動.md) | **Ch. 4–5** (p.85–130) | 單/雙原子鏈色散關係、聲學支與光學支、Debye $T^3$ 定律、Dulong-Petit、衰減波 | **第一梯隊** | [📖 unit04_聲子與晶格振動.md](unit04_聲子與晶格振動.md) |
| **05** | [自由電子費米氣體（Free Electron Fermi Gas）](unit05_自由電子費米氣體.md) | **Ch. 6** (p.131–160) | 費米能量 $E_F$、1D/2D/3D 能態密度 DOS、電子熱容 $\gamma T$、Wiedemann-Franz 定律 | **第二梯隊** | [📖 unit05_自由電子費米氣體.md](unit05_自由電子費米氣體.md) |
| **06** | [能帶理論與 Bloch 電子（Energy Bands）](unit06_能帶與Bloch電子.md) | **Ch. 7** (p.161–196) | Bloch 定理、NFE 邊界能隙 $2|U_G|$、Kronig-Penney、有效質量張量、緊束縛模型 | **第一梯隊** | [📖 unit06_能帶與Bloch電子.md](unit06_能帶與Bloch電子.md) |
| **07** | [半導體物理（Semiconductors）](unit07_半導體.md) | **Ch. 8** (p.197–230) | 載子濃度 $n_i$、質量作用定律、本質費米能階、pn 接面內建電位、Hall 效應 | **第三梯隊** | [📖 unit07_半導體.md](unit07_半導體.md) |
| **08** | [磁性（Magnetism）](unit08_磁性.md) | **Ch. 11–12** (p.297–352) | 朗之萬抗磁與順磁、Curie 定律、Curie-Weiss 定律、Landau 能階量子化 | **第四梯隊** | [📖 unit08_磁性.md](unit08_磁性.md) |
| **09** | [超導現象（Superconductivity）](unit09_超導.md) | **Ch. 10** (p.259–296) | 邁斯納效應、倫敦方程、第一類與第二類超導體、磁通量子 $\Phi_0$、BCS 能隙 | **第四梯隊** | [📖 unit09_超導.md](unit09_超導.md) |
| **10** | [實驗技術與進階（Experimental & Advanced）](unit10_實驗與進階.md) | **Ch. 1, 9, 18** 跨章 | STM 穿隧電流、X 光反射率多層膜消光、石墨烯 Dirac 錐線性色散、魔角雙層 | **第四梯隊** | [📖 unit10_實驗與進階.md](unit10_實驗與進階.md) |

---

## 🧮 固態物理全單元核心公式速查大全（Master Formula Sheet ＆ Ref）

以下依 10 大單元彙整資格考**默寫推導必備**的核心公式、符號定義、使用情境與**權威文獻出處（Ref）**：

---

### 單元 01：晶體結構（Crystal Structure）

#### 1. 晶格向量與平移週期性
實空間布拉菲晶格由基底向量 $\mathbf a_1, \mathbf a_2, \mathbf a_3$ 整數線性組合而成：
$$
\mathbf R = n_1 \mathbf a_1 + n_2 \mathbf a_2 + n_3 \mathbf a_3, \quad n_1, n_2, n_3 \in \mathbb Z
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 1, p. 4
> - **林盛煇《固態物理導論》**：§1.2 晶體之平移對稱性
> - **歷年考題**：[NTU 2013 Q1](../考古題/詳解/固態_2013_詳解.html), [2014 Q1](../考古題/詳解/固態_2014_詳解.html), [2024 Q1](../考古題/詳解/固態_2024_詳解.html)

#### 2. 原胞體積（Primitive Cell Volume）
三基底向量構成之平行六面體純量三重積：
$$
V_p = |\mathbf a_1 \cdot (\mathbf a_2 \times \mathbf a_3)|
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 1, p. 7
> - **歷年考題**：[NTU 2024 Q1（35分）](../考古題/詳解/固態_2024_詳解.html)

#### 3. 立方晶系密勒指標與晶面間距
在正交立方晶系中，晶向向量垂直於同指標晶面：$[hkl] \perp (hkl)$。相鄰兩 $(hkl)$ 晶面間距為：
$$
d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 1, Eq. (16), p. 13
> - **林盛煇《固態物理導論》**：§1.4 晶面指數與面間距
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html), [2014](../考古題/詳解/固態_2014_詳解.html)

#### 4. 各大常見晶體結構充填率（Packing Fraction, PF）
定義：$\text{PF} = \dfrac{N_{\text{atom}} \times \frac{4}{3}\pi r^3}{V_{\text{cell}}}$
- **簡單立方（SC）**：最近鄰接觸 $a = 2r$，$N=1$
  $$
  \text{PF}_{\text{SC}} = \frac{1 \times \frac{4}{3}\pi r^3}{(2r)^3} = \frac{\pi}{6} \approx 0.524
  $$
- **體心立方（BCC）**：體對角線接觸 $4r = \sqrt{3}a$，$N=2$
  $$
  \text{PF}_{\text{BCC}} = \frac{2 \times \frac{4}{3}\pi r^3}{\left(\frac{4r}{\sqrt{3}}\right)^3} = \frac{\sqrt{3}\pi}{8} \approx 0.680
  $$
- **面心立方（FCC）**：面對角線接觸 $4r = \sqrt{2}a$，$N=4$
  $$
  \text{PF}_{\text{FCC}} = \frac{4 \times \frac{4}{3}\pi r^3}{\left(\frac{4r}{\sqrt{2}}\right)^3} = \frac{\sqrt{2}\pi}{6} \approx 0.740
  $$
- **鑽石結構（Diamond）**：FCC 帶兩原子基底，體對角線 $1/4$ 處相切 $8r = \sqrt{3}a$，$N=8$
  $$
  \text{PF}_{\text{Diamond}} = \frac{8 \times \frac{4}{3}\pi r^3}{\left(\frac{8r}{\sqrt{3}}\right)^3} = \frac{\sqrt{3}\pi}{16} \approx 0.340
  $$
- **六方最密堆積（HCP）**：配位數 12，理想軸比條件下充填率等同 FCC：
  $$
  \text{PF}_{\text{HCP}} = \frac{\pi}{3\sqrt{2}} \approx 0.740
  $$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 1, Table 2, p. 11
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html), [2015](../考古題/詳解/固態_2015_詳解.html), [2020](../考古題/詳解/固態_2020_詳解.html), [2021](../考古題/詳解/固態_2021_詳解.html), [2023](../考古題/詳解/固態_2023_詳解.html), [2024](../考古題/詳解/固態_2024_詳解.html)

#### 5. HCP 理想軸比推導結果
正四面體幾何關係（底邊 $a$，高 $c/2$）：
$$
\frac{c}{a} = \sqrt{\frac{8}{3}} \approx 1.633
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 1, p. 15
> - **歷年考題**：[NTU 2015](../考古題/詳解/固態_2015_詳解.html), [2021](../考古題/詳解/固態_2021_詳解.html), [2024](../考古題/詳解/固態_2024_詳解.html)

#### 6. 基元判準（縮格定理）
基元位移 $\boldsymbol\delta$ 若滿足 $2\boldsymbol\delta \in L$ 且具有反演對稱，可判定是否能縮減為較小之單原子布拉菲晶格。
> **Ref 出處**：
> - **Kittel 8e**：Chapter 1, p. 16
> - **歷年考題**：[NTU 2023 Q1](../考古題/詳解/固態_2023_詳解.html), [2025 Q1（40分）](../考古題/詳解/固態_2025_詳解.html)

---

### 單元 02：倒晶格與繞射（Reciprocal Lattice & Diffraction）

#### 1. 倒晶格基底向量定義
$$
\mathbf b_1 = 2\pi \frac{\mathbf a_2 \times \mathbf a_3}{\mathbf a_1 \cdot (\mathbf a_2 \times \mathbf a_3)}, \quad \mathbf b_2 = 2\pi \frac{\mathbf a_3 \times \mathbf a_1}{\mathbf a_1 \cdot (\mathbf a_2 \times \mathbf a_3)}, \quad \mathbf b_3 = 2\pi \frac{\mathbf a_1 \times \mathbf a_2}{\mathbf a_1 \cdot (\mathbf a_2 \times \mathbf a_3)}
$$
正交與標度關係：
$$
\mathbf a_i \cdot \mathbf b_j = 2\pi \delta_{ij}
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 2, Eq. (13), p. 34
> - **林盛煇《固態物理導論》**：§2.2 倒晶格之定義與性質
> - **歷年考題**：[NTU 2015](../考古題/詳解/固態_2015_詳解.html), [2016](../考古題/詳解/固態_2016_詳解.html), [2022](../考古題/詳解/固態_2022_詳解.html), [2024](../考古題/詳解/固態_2024_詳解.html), [2025](../考古題/詳解/固態_2025_詳解.html)

#### 2. 倒晶格向量與晶面法向量
$$
\mathbf G_{hkl} = h \mathbf b_1 + k \mathbf b_2 + l \mathbf b_3, \quad |\mathbf G_{hkl}| = \frac{2\pi}{d_{hkl}}
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 2, Eq. (16), p. 35

#### 3. 布拉格定律（Bragg's Law）與勞厄條件（Laue Condition）
- **實空間布拉格定律**：
  $$
  2d\sin\theta = n\lambda
  $$
- **倒空間勞厄條件**（彈性散射波矢變化等於倒晶格向量）：
  $$
  \Delta \mathbf k = \mathbf k' - \mathbf k = \mathbf G
  $$
- **彈性散射條件**（$|\mathbf k'| = |\mathbf k|$）：
  $$
  2\mathbf k \cdot \mathbf G = |\mathbf G|^2
  $$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 2, Eq. (1), (18)–(25), p. 30, 36–37
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html), [2014](../考古題/詳解/固態_2014_詳解.html), [2016](../考古題/詳解/固態_2016_詳解.html), [2018](../考古題/詳解/固態_2018_詳解.html), [2023](../考古題/詳解/固態_2023_詳解.html)

#### 4. 幾何結構因子（Structure Factor）
原胞內 $p$ 個原子位置為 $\mathbf r_j$：
$$
S_{\mathbf G} = \sum_{j=1}^p f_j e^{-i \mathbf G \cdot \mathbf r_j}
$$
繞射線強度正比於 $|S_{\mathbf G}|^2$。
> **Ref 出處**：
> - **Kittel 8e**：Chapter 2, Eq. (39), p. 42
> - **林盛煇《固態物理導論》**：§2.4 幾何結構因子

#### 5. 資格考必背四大晶格消光規則（Extinction Rules）
- **BCC（慣用胞 2 原子：$(0,0,0)$ 與 $(\frac{1}{2},\frac{1}{2},\frac{1}{2})$）**：
  $$
  S_{\mathbf G} = f \left(1 + e^{-i\pi(h+k+l)}\right) \implies \begin{cases} 2f & h+k+l \text{ 為偶數（允許反射）} \\ 0 & h+k+l \text{ 為奇數（系統性消光）} \end{cases}
  $$
- **FCC（慣用胞 4 原子）**：
  $$
  S_{\mathbf G} = f \left(1 + e^{-i\pi(h+k)} + e^{-i\pi(k+l)} + e^{-i\pi(l+h)}\right) \implies \begin{cases} 4f & h, k, l \text{ 全奇或全偶（允許）} \\ 0 & h, k, l \text{ 奇偶混雜（消光）} \end{cases}
  $$
- **鑽石結構（Diamond，FCC + 基元移位 $(\frac{1}{4},\frac{1}{4},\frac{1}{4})$）**：
  $$
  S_{\text{dia}} = S_{\text{FCC}} \times \left(1 + e^{-i\frac{\pi}{2}(h+k+l)}\right)
  $$
  - $h,k,l$ 奇偶混雜 $\implies S=0$
  - 全奇數 $\implies |S|^2 = 32 f^2$
  - 全偶數且 $h+k+l = 4n$ $\implies |S|^2 = 64 f^2$
  - 全偶數且 $h+k+l = 4n+2$ $\implies S=0$（例如 (200), (222) 消光）
> **Ref 出處**：
> - **Kittel 8e**：Chapter 2, Eq. (42)–(44), p. 43–45
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html), [2014](../考古題/詳解/固態_2014_詳解.html), [2016](../考古題/詳解/固態_2016_詳解.html), [2018](../考古題/詳解/固態_2018_詳解.html), [2021](../考古題/詳解/固態_2021_詳解.html)

---

### 單元 03：晶體鍵結（Crystal Binding）

#### 1. 藍納–瓊斯（Lennard-Jones）12-6 位能
描述凡得瓦晶體（惰性氣體晶體）的原子間交互作用：
$$
U(r) = 4\varepsilon \left[ \left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^6 \right]
$$
- $r^{-12}$ 項：泡利不相容原理引起的近距離短程排斥
- $r^{-6}$ 項：電偶極起伏引起的誘導偶極–誘導偶極凡得瓦吸引能
> **Ref 出處**：
> - **Kittel 8e**：Chapter 3, Eq. (2), p. 55
> - **林盛煇《固態物理導論》**：§3.2 凡得瓦晶體與 Lennard-Jones 位能
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html), [2014](../考古題/詳解/固態_2014_詳解.html), [2015](../考古題/詳解/固態_2015_詳解.html), [2016](../考古題/詳解/固態_2016_詳解.html)

#### 2. FCC 惰性氣體晶體平衡間距與總內聚能
令最近鄰間距為 $R$，晶格和 $A_{12} = \sum_{j} p_{ij}^{-12} \approx 12.13$，$A_6 = \sum_{j} p_{ij}^{-6} \approx 14.45$：
$$
U_{\text{tot}}(R) = 2N\varepsilon \left[ A_{12}\left(\frac{\sigma}{R}\right)^{12} - A_6\left(\frac{\sigma}{R}\right)^6 \right]
$$
由 $\frac{dU_{\text{tot}}}{dR} = 0$ 求得：
- 平衡間距：
  $$
  R_0 = \left(\frac{2 A_{12}}{A_6}\right)^{1/6} \sigma \approx 1.09 \sigma
  $$
- 每莫耳平衡內聚能：
  $$
  U_{\text{tot}}(R_0) = -2N\varepsilon \cdot \frac{A_6^2}{4 A_{12}} = -N\varepsilon \frac{A_6^2}{2A_{12}} \approx -8.61 N\varepsilon
  $$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 3, Eq. (8)–(12), Table 4, p. 58–60
> - **歷年考題**：[NTU 2014](../考古題/詳解/固態_2014_詳解.html), [2016](../考古題/詳解/固態_2016_詳解.html)

#### 3. 離子晶體位能與馬德隆常數（Madelung Constant）
每對離子交互作用位能（含長程庫侖吸引與短程 Born 排斥）：
$$
U_{ij} = \pm \frac{e^2}{4\pi\varepsilon_0 r_{ij}} + \frac{B}{r_{ij}^n} \implies U_{\text{tot}} = N \left( -\frac{\alpha e^2}{4\pi\varepsilon_0 R} + \frac{z B}{R^n} \right)
$$
- **1D 離子鏈馬德隆常數推導**：
  $$
  \alpha_{\text{1D}} = 2 \left( 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots \right) = 2\ln 2 \approx 1.386
  $$
- **3D 氯化鈉（NaCl）結構馬德隆常數**：
  $$
  \alpha_{\text{NaCl}} \approx 1.7476
  $$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 3, Eq. (20)–(23), Table 7, p. 64–65
> - **歷年考題**：[NTU 2020](../考古題/詳解/固態_2020_詳解.html), [2023 Q1](../考古題/詳解/固態_2023_詳解.html), [2024 Q2](../考古題/詳解/固態_2024_詳解.html)

---

### 單元 04：聲子與晶格振動（Phonons / Lattice Vibrations）

#### 1. 一維單原子鏈色散關係（Dispersion Relation）
晶格常數 $a$，原子質量 $M$，等效彈簧常數 $C$：
$$
\omega(K) = 2\sqrt{\frac{C}{M}} \left|\sin\left(\frac{Ka}{2}\right)\right|
$$
- 最高截止角頻率（BZ 邊界 $K=\pm\pi/a$）：
  $$
  \omega_{\max} = 2\sqrt{\frac{C}{M}}
  $$
- 長聲學波聲速（$K \to 0$）：
  $$
  v_s = \lim_{K\to 0}\frac{\omega}{K} = a\sqrt{\frac{C}{M}}
  $$
- 群速度（能量傳遞速度）：
  $$
  v_g = \frac{d\omega}{dK} = a\sqrt{\frac{C}{M}}\cos\left(\frac{Ka}{2}\right)
  $$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 4, Eq. (9)–(16), p. 89–92
> - **林盛煇《固態物理導論》**：§4.2 一維單原子晶格振動
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html), [2019](../考古題/詳解/固態_2019_詳解.html), [2021](../考古題/詳解/固態_2021_詳解.html), [2023](../考古題/詳解/固態_2023_詳解.html), [2024](../考古題/詳解/固態_2024_詳解.html)

#### 2. 一維雙原子鏈（質量 $M_1 > M_2$，間距 $a$）
$$
\omega^2 = C\left(\frac{1}{M_1} + \frac{1}{M_2}\right) \pm C\sqrt{\left(\frac{1}{M_1} + \frac{1}{M_2}\right)^2 - \frac{4\sin^2(Ka/2)}{M_1 M_2}}
$$
- **聲學支（Acoustic Branch，取 $-$ 號）**：$K\to 0$ 時 $\omega \to 0$
- **光學支（Optical Branch，取 $+$ 號）**：$K\to 0$ 時 $\omega = \sqrt{2C\left(\frac{1}{M_1}+\frac{1}{M_2}\right)}$
- **BZ 邊界能隙（Phonon Band Gap）**：
  $$
  \Delta \omega = \omega_{\text{op}}(BZ) - \omega_{\text{ac}}(BZ) = \sqrt{\frac{2C}{M_2}} - \sqrt{\frac{2C}{M_1}}
  $$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 4, Eq. (20)–(27), p. 94–97
> - **歷年考題**：[NTU 2018](../考古題/詳解/固態_2018_詳解.html), [2020](../考古題/詳解/固態_2020_詳解.html)

#### 3. 衰減波（Evanescent Wave）
當驅動頻率 $\omega > \omega_{\max}$，波矢轉為複數 $K = \frac{\pi}{a} + i\kappa$：
$$
u_n \propto e^{i(Kn - \omega t)} = e^{-\kappa a n} e^{i(\pi n - \omega t)}
$$
振幅隨空間呈指數衰減，無能量淨傳輸。
> **Ref 出處**：
> - **Kittel 8e**：Chapter 4, Problem 1, p. 104
> - **歷年考題**：[NTU 2021](../考古題/詳解/固態_2021_詳解.html), [2024](../考古題/詳解/固態_2024_詳解.html)

#### 4. 德拜比熱模型（Debye Model）
- **德拜截止頻率 $\omega_D$ 與德拜溫度 $\Theta_D$**：
  $$
  \omega_D = v_s \left(6\pi^2 \frac{N}{V}\right)^{1/3}, \quad \Theta_D = \frac{\hbar\omega_D}{k_B}
  $$
- **3D 聲子態密度（DOS，包含 3 個偏振支）**：
  $$
  D(\omega) = \frac{3V \omega^2}{2\pi^2 v_s^3} = \frac{9N}{\omega_D^3} \omega^2 \quad (\omega \le \omega_D)
  $$
- **低溫德拜 $T^3$ 定律（$T \ll \Theta_D$）**：
  $$
  C_v \approx \frac{12\pi^4}{5} N k_B \left(\frac{T}{\Theta_D}\right)^3 \propto T^3
  $$
- **高溫杜隆–珀蒂極限（$T \gg \Theta_D$）**：
  $$
  C_v \to 3N k_B
  $$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 5, Eq. (15)–(28), p. 110–116
> - **林盛煇《固態物理導論》**：§5.3 德拜晶格熱容理論
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html), [2014](../考古題/詳解/固態_2014_詳解.html), [2015](../考古題/詳解/固態_2015_詳解.html), [2016](../考古題/詳解/固態_2016_詳解.html)

---

### 單元 05：自由電子費米氣體（Free Electron Fermi Gas）

#### 1. 費米–狄拉克分布（Fermi-Dirac Distribution）
$$
f(E) = \frac{1}{e^{(E-\mu)/k_BT} + 1}
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 6, Eq. (5), p. 135
> - **歷年考題**：[NTU 2016](../考古題/詳解/固態_2016_詳解.html)

#### 2. 費米面基本量（3D 自由電子氣）
- 費米波向量：
  $$
  k_F = (3\pi^2 n)^{1/3}, \quad n = \frac{N}{V}
  $$
- 費米能量與費米溫度：
  $$
  E_F = \frac{\hbar^2 k_F^2}{2m} = \frac{\hbar^2}{2m}(3\pi^2 n)^{2/3}, \quad T_F = \frac{E_F}{k_B}
  $$
- 費米速度：
  $$
  v_F = \frac{\hbar k_F}{m} = \sqrt{\frac{2E_F}{m}}
  $$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 6, Eq. (17)–(23), p. 138–139
> - **林盛煇《固態物理導論》**：§6.3 費米面與費米能
> - **歷年考題**：[NTU 2016](../考古題/詳解/固態_2016_詳解.html), [2017](../考古題/詳解/固態_2017_詳解.html), [2022](../考古題/詳解/固態_2022_詳解.html)

#### 3. 1D / 2D / 3D 能態密度（DOS）對照表
- **3D**：
  $$
  g_{\text{3D}}(E) = \frac{V}{2\pi^2} \left(\frac{2m}{\hbar^2}\right)^{3/2} \sqrt{E} = \frac{3N}{2E_F}\left(\frac{E}{E_F}\right)^{1/2} \propto E^{1/2}
  $$
- **2D**：
  $$
  g_{\text{2D}}(E) = \frac{A m}{\pi \hbar^2} = \text{常數（與 } E \text{ 無關）}
  $$
- **1D**：
  $$
  g_{\text{1D}}(E) = \frac{L}{\pi} \sqrt{\frac{2m}{\hbar^2}} E^{-1/2} \propto E^{-1/2}
  $$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 6, Eq. (20)–(21), p. 139
> - **歷年考題**：[NTU 2016（2D DOS）](../考古題/詳解/固態_2016_詳解.html), [2023（1D DOS）](../考古題/詳解/固態_2023_詳解.html), [2024](../考古題/詳解/固態_2024_詳解.html), [2025（2D DOS）](../考古題/詳解/固態_2025_詳解.html)

#### 4. 0K 總能量與電子低溫熱容
- **3D 總基態動能**：
  $$
  U_0 = \int_0^{E_F} E g(E) dE = \frac{3}{5} N E_F
  $$
- **電子熱容（索末菲展開 $T \ll T_F$）**：
  $$
  C_{el} = \frac{\pi^2}{3} k_B^2 g(E_F) T = \frac{\pi^2}{2} N k_B \left(\frac{T}{T_F}\right) = \gamma T
  $$
- **低溫金屬總熱容（電子＋聲子）**：
  $$
  C = C_{el} + C_{ph} = \gamma T + A T^3 \implies \frac{C}{T} = \gamma + A T^2
  $$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 6, Eq. (23), (37)–(43), p. 139, 143–145
> - **歷年考題**：[NTU 2014](../考古題/詳解/固態_2014_詳解.html), [2015](../考古題/詳解/固態_2015_詳解.html), [2016](../考古題/詳解/固態_2016_詳解.html), [2020](../考古題/詳解/固態_2020_詳解.html), [2021](../考古題/詳解/固態_2021_詳解.html)

#### 5. 輸運性質與維德曼–夫蘭茲定律（Wiedemann-Franz Law）
- **德魯德電導率與遷移率**：
  $$
  \sigma = \frac{n e^2 \tau}{m}, \quad \mu = \frac{e\tau}{m}
  $$
- **電子熱導率**：
  $$
  K = \frac{1}{3} C_{el} v_F l = \frac{\pi^2 n k_B^2 \tau T}{3m}
  $$
- **維德曼–夫蘭茲定律與勞侖茲數（Lorenz Number）**：
  $$
  \frac{K}{\sigma T} = \frac{\pi^2 k_B^2}{3e^2} = L \approx 2.443 \times 10^{-8} \, \text{W}\cdot\Omega/\text{K}^2
  $$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 6, Eq. (46)–(54), p. 151–154
> - **歷年考題**：[NTU 2014（30分）](../考古題/詳解/固態_2014_詳解.html), [2015（20分）](../考古題/詳解/固態_2015_詳解.html)

---

### 單元 06：能帶理論與 Bloch 電子（Energy Bands & Bloch Electrons）

#### 1. 布洛赫定理（Bloch's Theorem）
在週期位能 $U(\mathbf r + \mathbf R) = U(\mathbf r)$ 中，單電子波函數滿足：
$$
\psi_{\mathbf k}(\mathbf r) = u_{\mathbf k}(\mathbf r) e^{i\mathbf k \cdot \mathbf r}, \quad u_{\mathbf k}(\mathbf r + \mathbf R) = u_{\mathbf k}(\mathbf r)
$$
或平移算符形式：$T_{\mathbf R}\psi_{\mathbf k}(\mathbf r) = \psi_{\mathbf k}(\mathbf r + \mathbf R) = e^{i\mathbf k \cdot \mathbf R} \psi_{\mathbf k}(\mathbf r)$。
> **Ref 出處**：
> - **Kittel 8e**：Chapter 7, Eq. (5)–(7), p. 167
> - **林盛煇《固態物理導論》**：§7.2 布洛赫定理與其證明
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html), [2014](../考古題/詳解/固態_2014_詳解.html), [2015](../考古題/詳解/固態_2015_詳解.html), [2016](../考古題/詳解/固態_2016_詳解.html), [2025](../考古題/詳解/固態_2025_詳解.html)

#### 2. 近自由電子模型（Nearly Free Electron, NFE）能隙
在第一布里淵區邊界 $k = \pm \frac{1}{2}G$，電子形成駐波：
$$
\psi_+ \propto \cos\left(\frac{Gx}{2}\right), \quad \psi_- \propto \sin\left(\frac{Gx}{2}\right)
$$
位能 $U(x) = 2 U_G \cos(Gx)$ 導致能階分裂，打開能隙：
$$
E_+ - E_- = \Delta E_g = 2 |U_G|
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 7, Eq. (24)–(27), p. 165
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html), [2014](../考古題/詳解/固態_2014_詳解.html), [2018](../考古題/詳解/固態_2018_詳解.html), [2020](../考古題/詳解/固態_2020_詳解.html), [2021](../考古題/詳解/固態_2021_詳解.html)

#### 3. 克勒尼希–潘尼模型（Kronig-Penney Model）超越方程
對於週期性 Delta 勢位障陣列（位障強度 $P = \frac{m V_0 b a}{\hbar^2}$）：
$$
P \frac{\sin(Ka)}{Ka} + \cos(Ka) = \cos(ka)
$$
若左式絕對值大於 1，無實數解 $Ka$，對應**禁帶（Forbidden Energy Gap）**。
> **Ref 出處**：
> - **Kittel 8e**：Chapter 7, Eq. (21b), p. 169–171
> - **歷年考題**：[NTU 2014](../考古題/詳解/固態_2014_詳解.html), [2015](../考古題/詳解/固態_2015_詳解.html), [2016](../考古題/詳解/固態_2016_詳解.html)

#### 4. 有效質量張量（Effective Mass Tensor）
$$
\left(\frac{1}{m^*}\right)_{ij} = \frac{1}{\hbar^2} \frac{\partial^2 E(\mathbf k)}{\partial k_i \partial k_j}
$$
- 在能帶頂部（曲率向下 $\frac{\partial^2 E}{\partial k^2} < 0$），有效質量為**負**，常改以帶正電之「電洞（hole）」描述。
> **Ref 出處**：
> - **Kittel 8e**：Chapter 7, Eq. (37)–(40), p. 176–178
> - **歷年考題**：[NTU 2016](../考古題/詳解/固態_2016_詳解.html), [2017](../考古題/詳解/固態_2017_詳解.html), [2021](../考古題/詳解/固態_2021_詳解.html)

#### 5. 緊束縛模型（Tight-Binding Model）
一維單鏈原子軌域 $s$ 能帶（晶格常數 $a$，重疊積分 $\gamma$）：
$$
E(k) = -\alpha - 2\gamma \cos(ka)
$$
- 帶寬（Bandwidth）：$W = 4\gamma$
- 帶底有效質量（$k \to 0$）：$m^* = \frac{\hbar^2}{2\gamma a^2}$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 9, p. 232–234
> - **講義.md**：§能帶理論之緊束縛近似
> - **歷年考題**：[NTU 2025 Q2](../考古題/詳解/固態_2025_詳解.html)

---

### 單元 07：半導體（Semiconductors）

#### 1. 平衡載子濃度與本質載子濃度
- **傳導帶電子濃度**：
  $$
  n = N_c e^{-(E_c - \mu)/k_BT}, \quad N_c = 2\left(\frac{m_e^* k_BT}{2\pi \hbar^2}\right)^{3/2}
  $$
- **價帶電洞濃度**：
  $$
  p = N_v e^{-(\mu - E_v)/k_BT}, \quad N_v = 2\left(\frac{m_h^* k_BT}{2\pi \hbar^2}\right)^{3/2}
  $$
- **質量作用定律（Mass Action Law）**：
  $$
  np = n_i^2 = N_c N_v e^{-E_g/k_BT}
  $$
- **本質載子濃度**：
  $$
  n_i = \sqrt{N_c N_v} e^{-E_g / 2k_BT} \propto T^{3/2} e^{-E_g / 2k_BT}
  $$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 8, Eq. (29)–(43), p. 206–209
> - **林盛煇《固態物理導論》**：§8.2 半導體之平衡載子濃度
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html), [2016](../考古題/詳解/固態_2016_詳解.html), [2022](../考古題/詳解/固態_2022_詳解.html)

#### 2. 本質化學勢（Fermi Level）
$$
\mu_{\text{int}} = \frac{E_c + E_v}{2} + \frac{3}{4} k_B T \ln\left(\frac{m_h^*}{m_e^*}\right)
$$
當 $T \to 0$ 時，$\mu$ 恰好坐落在禁帶正中央。
> **Ref 出處**：
> - **Kittel 8e**：Chapter 8, Eq. (44), p. 209
> - **歷年考題**：[NTU 2022 Q2](../考古題/詳解/固態_2022_詳解.html)

#### 3. 施主／受主類氫模型束縛能
$$
E_d = \frac{m^*}{m_0 \epsilon_r^2} E_H = \frac{13.6 \, \text{eV}}{\epsilon_r^2} \left(\frac{m^*}{m_0}\right)
$$
因介電常數 $\epsilon_r \sim 12$ 且有效質量 $m^* \sim 0.1 m_0$，$E_d \sim 10\text{--}50\,\text{meV}$，室溫即可全數熱電離。
> **Ref 出處**：
> - **Kittel 8e**：Chapter 8, Eq. (48)–(50), p. 212
> - **歷年考題**：[NTU 2016 Q3](../考古題/詳解/固態_2016_詳解.html)

#### 4. pn 接面內建電位（Built-in Voltage）
$$
V_{bi} = \frac{k_B T}{e} \ln\left(\frac{N_A N_D}{n_i^2}\right)
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 17, p. 488 / Sze《Physics of Semiconductor Devices》Ch. 2
> - **歷年考題**：[NTU 2022 Q2（40分）](../考古題/詳解/固態_2022_詳解.html)

#### 5. 霍爾效應（Hall Effect）
$$
R_H = \frac{E_y}{j_x B_z} = \begin{cases} -\frac{1}{n e} & (\text{電子傳導}) \\ +\frac{1}{p e} & (\text{電洞傳導}) \end{cases}
$$
雙載子共存時：
$$
R_H = \frac{p \mu_h^2 - n \mu_e^2}{e (p \mu_h + n \mu_e)^2}
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 6, Eq. (56), p. 154 ＆ Chapter 8, Eq. (52), p. 214
> - **歷年考題**：[NTU 2016](../考古題/詳解/固態_2016_詳解.html)

---

### 單元 08：磁性（Magnetism）

#### 1. 朗之萬抗磁性（Larmor Diamagnetism）
封閉電子殼層在外加磁場下的抗磁磁化率（拉摩進動）：
$$
\chi_{\text{dia}} = -\frac{N \mu_0 Z e^2}{6m} \langle r^2 \rangle
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 11, Eq. (9), p. 300
> - **林盛煇《固態物理導論》**：§11.2 抗磁性與拉摩定理
> - **歷年考題**：[NTU 2013 Q4](../考古題/詳解/固態_2013_詳解.html)

#### 2. 順磁性居里定律（Curie's Law）
獨立磁矩在弱場高溫極限下（$\mu B \ll k_BT$）：
$$
M = \chi H = \frac{C}{T} H, \quad C = \frac{N \mu_0 \mu^2}{3 k_B}
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 11, Eq. (13)–(15), p. 303
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html), [2025](../考古題/詳解/固態_2025_詳解.html)

#### 3. 經典朗之萬順磁函數（Langevin Function）
$$
M = N m L(\alpha), \quad L(\alpha) = \coth\alpha - \frac{1}{\alpha}, \quad \alpha = \frac{m B}{k_B T}
$$
- 當 $\alpha \ll 1$ 時：$L(\alpha) \approx \frac{\alpha}{3} \implies \chi = \frac{N \mu_0 m^2}{3 k_B T}$（還原居里定律）
- 當 $\alpha \gg 1$ 時：$L(\alpha) \to 1 \implies M \to Nm$（達到飽和磁化量）
> **Ref 出處**：
> - **Kittel 8e**：Chapter 11, Eq. (17)–(23), p. 304–305
> - **歷年考題**：[NTU 2013 Q4（20分）](../考古題/詳解/固態_2013_詳解.html)

#### 4. 居里–外斯定律（Curie-Weiss Law）
在鐵磁性物質中，分子場效應使得順磁磁化率在居里溫度 $T_C$ 以上呈現：
$$
\chi = \frac{C}{T - T_C}
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 12, Eq. (8), p. 325
> - **歷年考題**：[NTU 2025 Q3](../考古題/詳解/固態_2025_詳解.html)

#### 5. 朗道能階（Landau Levels）
2D 電子氣在垂直磁場 $B$ 下的軌域量子化：
$$
E_n = \left(n + \frac{1}{2}\right) \hbar\omega_c, \quad \omega_c = \frac{e B}{m^*}
$$
每個朗道能階之軌域簡併度（每單位面積，單電子磁通量子 $\Phi_0 = h/e$）：
$$
D = \frac{e B}{h} = \frac{B}{\Phi_0}
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 9, p. 254–256 ＆ Chapter 11
> - **歷年考題**：[NTU 2018 Q3（20分）](../考古題/詳解/固態_2018_詳解.html)

---

### 單元 09：超導現象（Superconductivity）

#### 1. 邁斯納效應與倫敦穿透深度（London Penetration Depth）
- **倫敦第二方程**：
  $$
  \nabla \times \mathbf J_s = -\frac{n_s e^2}{m} \mathbf B
  $$
- **磁場穿透衰減**：
  $$
  \nabla^2 \mathbf B = \frac{1}{\lambda_L^2} \mathbf B, \quad \lambda_L = \sqrt{\frac{m}{\mu_0 n_s e^2}}
  $$
  磁場在超導體表面呈指數衰減：$B(x) = B(0) e^{-x/\lambda_L}$。
> **Ref 出處**：
> - **Kittel 8e**：Chapter 10, Eq. (14)–(19), p. 269–271
> - **林盛煇《固態物理導論》**：§10.3 倫敦理論與邁斯納效應
> - **歷年考題**：[NTU 2013 Q5](../考古題/詳解/固態_2013_詳解.html)

#### 2. 熱力學臨界磁場與凝聚能
$$
H_c(T) = H_c(0) \left[ 1 - \left(\frac{T}{T_c}\right)^2 \right]
$$
超導凝聚能密度：
$$
\Delta f = f_n - f_s = \frac{1}{2}\mu_0 H_c^2
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 10, Eq. (3)–(4), p. 263
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html)

#### 3. 第一類 vs 第二類超導體判定（Ginzburg-Landau 參數）
定義 $\kappa = \lambda / \xi$（$\xi$ 為相干長度）：
- **第一類超導體（Type-I）**：$\kappa < \frac{1}{\sqrt{2}}$，表面能為正，無混合態，直接在 $H_c$ 發生一階相變。
- **第二類超導體（Type-II）**：$\kappa > \frac{1}{\sqrt{2}}$，表面能為負，在下臨界場 $H_{c1}$ 與上臨界場 $H_{c2}$ 之間形成**磁通渦旋態（Vortex State / Shubnikov Phase）**。
> **Ref 出處**：
> - **Kittel 8e**：Chapter 10, p. 278–282
> - **歷年考題**：[NTU 2025 Q4](../考古題/詳解/固態_2025_詳解.html)

#### 4. 磁通量子（Magnetic Flux Quantum）
超導波函數單值性要求磁通量子化（Cooper 對電荷 $q=2e$）：
$$
\Phi_0 = \frac{h}{2e} \approx 2.0678 \times 10^{-15} \, \text{Wb} \, (\text{T}\cdot\text{m}^2)
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 10, Eq. (36), p. 283
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html), [2025](../考古題/詳解/固態_2025_詳解.html)

#### 5. BCS 零溫能隙
$$
\Delta(0) \approx 1.764 \, k_B T_c \implies E_g = 2\Delta(0) \approx 3.528 \, k_B T_c
$$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 10, Eq. (40), Table 3, p. 273
> - **歷年考題**：[NTU 2013](../考古題/詳解/固態_2013_詳解.html)

---

### 單元 10：實驗技術與進階主題（Experimental Techniques & Advanced）

#### 1. 掃描穿隧顯微鏡（STM）穿隧電流
穿隧電流對探針與樣品表面間距 $d$ 呈超敏感指數衰減：
$$
I \propto e^{-2\kappa d}, \quad \kappa = \frac{\sqrt{2m\phi}}{\hbar} \approx 0.512 \sqrt{\phi(\text{eV})} \,\, \text{Å}^{-1}
$$
若功函數 $\phi \sim 4\,\text{eV}$，$\kappa \approx 1\,\text{Å}^{-1}$，探針每拉開 $1\,\text{Å}$ 電流衰減約一個數量級（$e^{-2} \approx 0.135$）。
> **Ref 出處**：
> - **Kittel 8e**：Chapter 1, p. 20 (STM 介紹)
> - **講義.md**：§固態物理實驗技術
> - **歷年考題**：[NTU 2013 Q3](../考古題/詳解/固態_2013_詳解.html), [2018](../考古題/詳解/固態_2018_詳解.html)

#### 2. X 光反射率多層膜消光條件
週期 $D = D_1 + D_2$ 之超晶格多層膜，繞射階數 $m$ 之結構因子為零的條件：
$$
F_m \propto \frac{\sin(m\pi D_1 / D)}{m} = 0 \implies m \frac{D_1}{D} = \text{整數}
$$
若 $D_1 = D/3$，則每逢第 3、6、9... 階 Bragg 峰消失。
> **Ref 出處**：
> - **歷年考題**：[NTU 2013 Q3（20分）](../考古題/詳解/固態_2013_詳解.html)

#### 3. 石墨烯（Graphene）無質量 Dirac 費米子
在布里淵區頂點 $K, K'$ 附近，能量隨波矢呈嚴格線性色散：
$$
E(\mathbf q) = \pm \hbar v_F |\mathbf q|, \quad v_F \approx 10^6 \, \text{m/s}
$$
- 2D 能態密度正比於能量絕對值（4重簡併：2 自旋 $\times$ 2 谷）：
  $$
  g(E) = \frac{2}{\pi \hbar^2 v_F^2} |E|
  $$
> **Ref 出處**：
> - **Kittel 8e**：Chapter 18 (Nanostructures)
> - **Castro Neto et al.**：*The electronic properties of graphene*, Rev. Mod. Phys. 81, 109 (2009)
> - **歷年考題**：[NTU 2018 Q4](../考古題/詳解/固態_2018_詳解.html), [2023 Q1](../考古題/詳解/固態_2023_詳解.html)

#### 4. 魔角雙層石墨烯（Twisted Bilayer Graphene）
旋轉角度 $\theta \approx 1.08^\circ \approx 1.1^\circ$ 時，莫爾晶格造成能帶極度平坦（平帶，Flat Bands），電子群速度 $v_g \to 0$，強關聯效應誘導非常規超導與莫特絕緣體。
> **Ref 出處**：
> - **Bistritzer & MacDonald**：*Moiré bands in twisted double-layer graphene*, PNAS 108, 12233 (2011)
> - **Cao et al.**：*Unconventional superconductivity in magic-angle graphene superlattices*, Nature 556, 43 (2018)

---

## 📚 權威參考書目與出處索引（Authoritative References）

1. **[Kittel 8e]** Charles Kittel, *Introduction to Solid State Physics*, 8th Edition, John Wiley & Sons, 2005. ISBN: 978-0471415268.（本備考庫第一權威真相源）
2. **[Kittel 譯本]** 邱雅萍、林盛煇等譯,《固態物理學導論》第八版, 滄海圖書.（專有名詞繁體中文對照基準）
3. **[林盛煇]** 林盛煇,《固態物理導論》講義與教材, 國立臺灣大學應用物理學研究所.
4. **[Ashcroft-Mermin]** Neil W. Ashcroft and N. David Mermin, *Solid State Physics*, Saunders College, 1976.（能帶與輸運深層證明依據）
5. **[NTU 考古題]** 國立臺灣大學應用物理學研究所博士班資格考試題（2013–2025 年共 13 卷全詳解）.
6. **[質檢證明]** 本庫專屬質檢報告 [`_質檢報告_主表.md`](../_質檢報告_主表.md)（經 Python 獨立程式數值重算，33 檔全數通過核對）.

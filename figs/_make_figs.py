#!/usr/bin/env python3
"""產生固態物理共用圖庫（SVG，向量、座標軸用英文/數學避免中文字型問題）。
被 單元教學/ 與 教材/Kittel章節導讀/ 兩層引用。重跑即重新產生所有圖。
輸出到本資料夾 figs/ 下的 f<NN>_<name>.svg。"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrow, Polygon, Arc

HERE = os.path.dirname(os.path.abspath(__file__))
plt.rcParams.update({
    "figure.figsize": (4.2, 3.0), "font.size": 9, "axes.linewidth": 0.8,
    "mathtext.fontset": "cm", "savefig.bbox": "tight", "svg.fonttype": "none",
})

def save(fig, name):
    fig.savefig(os.path.join(HERE, name), format="svg")
    plt.close(fig)
    print("wrote", name)

# ---------- 單元 1：晶體結構 ----------
def f01_lattice_basis():
    fig, ax = plt.subplots()
    for i in range(5):
        for j in range(4):
            ax.plot(i, j, 'o', color='#1a4d7c', ms=5)
            ax.plot(i+0.35, j+0.2, 's', color='#c0392b', ms=4)
    ax.annotate("", xy=(1,0), xytext=(0,0), arrowprops=dict(arrowstyle="->", color='green', lw=1.6))
    ax.annotate("", xy=(0,1), xytext=(0,0), arrowprops=dict(arrowstyle="->", color='green', lw=1.6))
    ax.text(0.5,-0.28,r"$\mathbf{a}_1$",color='green'); ax.text(-0.42,0.5,r"$\mathbf{a}_2$",color='green')
    ax.add_patch(Rectangle((0,0),1,1,fill=True,fc='#1a4d7c',alpha=0.08,ec='#1a4d7c',ls='--'))
    ax.text(2.4,3.4,"lattice (●) × basis (●+■)",fontsize=8)
    ax.set_xlim(-0.6,4.6); ax.set_ylim(-0.6,3.8); ax.set_aspect('equal'); ax.axis('off')
    ax.set_title("2D lattice + primitive cell + basis")
    save(fig,"f01_lattice_basis.svg")

def f01_packing_bar():
    fig, ax = plt.subplots()
    names=['sc','diamond','bcc','fcc/hcp']; vals=[0.524,0.340,0.680,0.740]
    cols=['#7fb3d5','#e59866','#5dade2','#2874a6']
    b=ax.bar(names,vals,color=cols,width=0.6)
    for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2,v+0.01,f"{v:.3f}",ha='center',fontsize=8)
    ax.set_ylabel("packing fraction"); ax.set_ylim(0,0.85)
    ax.set_title("Atomic packing fraction"); ax.grid(axis='y',alpha=0.3)
    save(fig,"f01_packing_bar.svg")

def f01_miller():
    fig, ax = plt.subplots()
    ax.add_patch(Rectangle((0,0),1,1,fill=False,ec='gray'))
    # (110)-like plane trace in 2D cube face: line through (1,0)-(0,1)
    ax.plot([1,0],[0,1],color='#c0392b',lw=2)
    ax.plot([0,1,1,0,0],[0,0,1,1,0],color='gray')
    ax.annotate("",xy=(0.5,0.5),xytext=(0.15,0.15),arrowprops=dict(arrowstyle="->",color='#1a4d7c',lw=1.6))
    ax.text(0.52,0.5,r"$\mathbf{G}\perp$plane",color='#1a4d7c',fontsize=8)
    ax.text(0.55,0.05,"(110)",color='#c0392b'); ax.text(-0.18,-0.12,"O")
    ax.text(1.05,0,"a"); ax.text(0,1.05,"a")
    ax.set_xlim(-0.25,1.3); ax.set_ylim(-0.25,1.3); ax.set_aspect('equal'); ax.axis('off')
    ax.set_title(r"Miller plane: $d_{hkl}=a/\sqrt{h^2+k^2+l^2}$",fontsize=9)
    save(fig,"f01_miller.svg")

# ---------- 單元 2：倒晶格與繞射 ----------
def f02_bragg():
    fig, ax = plt.subplots()
    for y in (0,1):
        ax.axhline(y,color='gray',lw=0.8)
        for x in np.arange(0.2,3,0.4): ax.plot(x,y,'o',color='#1a4d7c',ms=4)
    ax.annotate("",xy=(1.2,1),xytext=(0.2,1.8),arrowprops=dict(arrowstyle="->",color='#c0392b',lw=1.5))
    ax.annotate("",xy=(2.2,1.8),xytext=(1.2,1),arrowprops=dict(arrowstyle="->",color='#c0392b',lw=1.5))
    ax.annotate("",xy=(1.2,0),xytext=(0.6,0.9),arrowprops=dict(arrowstyle="->",color='#2874a6',lw=1.2))
    ax.annotate("",xy=(1.8,0.9),xytext=(1.2,0),arrowprops=dict(arrowstyle="->",color='#2874a6',lw=1.2))
    ax.text(0.75,1.45,r"$\theta$"); ax.text(1.25,0.45,"d",color='black')
    ax.annotate("",xy=(1.2,1),xytext=(1.2,0),arrowprops=dict(arrowstyle="<->",color='black',lw=0.8))
    ax.set_xlim(0,3); ax.set_ylim(-0.2,2); ax.set_aspect('equal'); ax.axis('off')
    ax.set_title(r"Bragg: $2d\sin\theta=n\lambda$")
    save(fig,"f02_bragg.svg")

def f02_bz_square():
    fig, ax = plt.subplots()
    for i in range(-2,3):
        for j in range(-2,3): ax.plot(i,j,'o',color='#1a4d7c',ms=4)
    ax.add_patch(Rectangle((-0.5,-0.5),1,1,fill=True,fc='#f39c12',alpha=0.25,ec='#e67e22',lw=1.5))
    ax.text(0,-0.05,"1st BZ",ha='center',fontsize=8,color='#b9770e')
    ax.annotate("",xy=(1,0),xytext=(0,0),arrowprops=dict(arrowstyle="->",color='green',lw=1.4))
    ax.annotate("",xy=(0,1),xytext=(0,0),arrowprops=dict(arrowstyle="->",color='green',lw=1.4))
    ax.text(0.5,0.08,r"$\mathbf{b}_1$",color='green'); ax.text(0.06,0.5,r"$\mathbf{b}_2$",color='green')
    ax.set_xlim(-2.4,2.4); ax.set_ylim(-2.4,2.4); ax.set_aspect('equal'); ax.axis('off')
    ax.set_title("Reciprocal lattice + 1st Brillouin zone")
    save(fig,"f02_bz_square.svg")

def f02_diffraction_peaks():
    fig, ax = plt.subplots(figsize=(4.6,2.6))
    # sum of squares for allowed reflections
    sc=[1,2,3,4,5,6,8]; bcc=[2,4,6,8,10,12]; fcc=[3,4,8,11,12,16]
    for s in sc: ax.vlines(s,0,1,color='#7fb3d5',lw=2)
    for s in bcc: ax.vlines(s+0.08,0,2,color='#2874a6',lw=2)
    for s in fcc: ax.vlines(s+0.16,0,3,color='#c0392b',lw=2)
    ax.text(8.5,1,"sc",color='#7fb3d5'); ax.text(8.5,2,"bcc",color='#2874a6'); ax.text(8.5,3,"fcc",color='#c0392b')
    ax.set_xlabel(r"$h^2+k^2+l^2$"); ax.set_yticks([])
    ax.set_title("Allowed reflections (extinction rules)")
    ax.set_xlim(0,10)
    save(fig,"f02_diffraction_peaks.svg")

# ---------- 單元 3：晶體鍵結 ----------
def f03_lennard_jones():
    fig, ax = plt.subplots()
    r=np.linspace(0.9,2.6,400); U=4*((1/r)**12-(1/r)**6)
    ax.plot(r,U,color='#1a4d7c',lw=2)
    ax.axhline(0,color='gray',lw=0.6); r0=2**(1/6)
    ax.plot(r0,-1,'o',color='#c0392b'); ax.axvline(r0,color='#c0392b',ls=':',lw=0.8)
    ax.text(r0+0.02,-0.5,r"$r_0=2^{1/6}\sigma$",color='#c0392b',fontsize=8)
    ax.text(1.6,-0.95,r"$-\varepsilon$",color='#c0392b')
    ax.set_xlabel(r"$r/\sigma$"); ax.set_ylabel(r"$U/\varepsilon$"); ax.set_ylim(-1.3,2)
    ax.set_title(r"Lennard–Jones $U=4\varepsilon[(\sigma/r)^{12}-(\sigma/r)^6]$",fontsize=8.5)
    ax.grid(alpha=0.3)
    save(fig,"f03_lennard_jones.svg")

def f03_madelung_chain():
    fig, ax = plt.subplots(figsize=(4.8,1.8))
    for i in range(-3,4):
        c='#c0392b' if i%2==0 else '#2874a6'; s='+' if i%2==0 else '$-$'
        ax.plot(i,0,'o',color=c,ms=16)
        ax.text(i,0,s,ha='center',va='center',color='white',fontsize=11)
    ax.annotate("",xy=(1,0.3),xytext=(0,0.3),arrowprops=dict(arrowstyle="<->",color='black',lw=0.8))
    ax.text(0.5,0.4,"R",ha='center')
    ax.text(0,-0.6,r"$\alpha=2\ln 2\approx1.386$",ha='center',fontsize=9)
    ax.set_xlim(-3.6,3.6); ax.set_ylim(-0.8,0.7); ax.axis('off')
    ax.set_title("1D ionic chain (Madelung)")
    save(fig,"f03_madelung_chain.svg")

# ---------- 單元 4：聲子 ----------
def f04_mono_dispersion():
    fig, ax = plt.subplots()
    K=np.linspace(-np.pi,np.pi,400); w=2*np.abs(np.sin(K/2))
    ax.plot(K,w,color='#1a4d7c',lw=2)
    ax.plot(K,np.abs(K),color='#c0392b',ls='--',lw=1,label='long-wave (sound)')
    ax.axhline(2,color='gray',ls=':',lw=0.8); ax.text(-3,2.05,r"$\omega_{max}=2\sqrt{C/M}$",fontsize=8)
    ax.set_xlabel(r"$Ka$"); ax.set_ylabel(r"$\omega\,/\sqrt{C/M}$")
    ax.set_xticks([-np.pi,0,np.pi]); ax.set_xticklabels([r"$-\pi/a$","0",r"$\pi/a$"])
    ax.set_title("Monatomic chain dispersion"); ax.legend(fontsize=7); ax.grid(alpha=0.3); ax.set_ylim(0,2.3)
    save(fig,"f04_mono_dispersion.svg")

def f04_diatomic_dispersion():
    fig, ax = plt.subplots()
    K=np.linspace(-np.pi,np.pi,400); M1,M2,C=2.0,1.0,1.0
    s=np.sin(K/2)**2
    root=np.sqrt((1/M1+1/M2)**2-4*s/(M1*M2))
    wo=np.sqrt(C*((1/M1+1/M2)+root)); wa=np.sqrt(C*((1/M1+1/M2)-root))
    ax.plot(K,wo,color='#c0392b',lw=2,label='optical'); ax.plot(K,wa,color='#1a4d7c',lw=2,label='acoustic')
    ax.set_xlabel(r"$Ka$"); ax.set_ylabel(r"$\omega$")
    ax.set_xticks([-np.pi,0,np.pi]); ax.set_xticklabels([r"$-\pi/a$","0",r"$\pi/a$"])
    ax.set_title("Diatomic chain: acoustic + optical (gap)"); ax.legend(fontsize=7); ax.grid(alpha=0.3)
    save(fig,"f04_diatomic_dispersion.svg")

def f04_debye_heat():
    fig, ax = plt.subplots()
    x=np.linspace(0.04,2.0,200)
    def cv(t):
        u=np.linspace(1e-3,1/t,400); integ=np.trapz(u**4*np.exp(u)/(np.exp(u)-1)**2,u)
        return 9*t**3*integ
    C=np.array([cv(t) for t in x])
    ax.plot(x,C,color='#1a4d7c',lw=2)
    ax.axhline(3,color='gray',ls=':',lw=0.8); ax.text(1.3,2.7,"Dulong–Petit 3R",fontsize=8)
    ax.plot(x[x<0.3],234*x[x<0.3]**3,color='#c0392b',ls='--',lw=1)
    ax.text(0.32,0.2,r"$\propto T^3$",color='#c0392b',fontsize=9)
    ax.set_xlabel(r"$T/\theta_D$"); ax.set_ylabel(r"$C_V$ (units of R)")
    ax.set_title("Debye heat capacity"); ax.grid(alpha=0.3); ax.set_ylim(0,3.3)
    save(fig,"f04_debye_heat.svg")

# ---------- 單元 5：自由電子 ----------
def f05_fermi_sphere():
    fig, ax = plt.subplots()
    ax.add_patch(Circle((0,0),1,fc='#aed6f1',ec='#1a4d7c',lw=1.5))
    for _ in range(0): pass
    ax.annotate("",xy=(0.71,0.71),xytext=(0,0),arrowprops=dict(arrowstyle="->",color='#c0392b',lw=1.5))
    ax.text(0.3,0.45,r"$k_F$",color='#c0392b')
    ax.text(0,-1.35,"filled states",ha='center',fontsize=8,color='#1a4d7c')
    ax.set_xlabel(r"$k_x$"); ax.set_ylabel(r"$k_y$")
    ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.5,1.5); ax.set_aspect('equal')
    ax.set_title(r"Fermi sphere ($T=0$)")
    save(fig,"f05_fermi_sphere.svg")

def f05_dos_dims():
    fig, ax = plt.subplots()
    E=np.linspace(0.02,3,300)
    ax.plot(E,np.sqrt(E),color='#1a4d7c',lw=2,label=r"3D $\propto E^{1/2}$")
    ax.plot(E,np.ones_like(E),color='#27ae60',lw=2,label="2D = const")
    ax.plot(E,1/np.sqrt(E),color='#c0392b',lw=2,label=r"1D $\propto E^{-1/2}$")
    ax.set_xlabel(r"$E$"); ax.set_ylabel(r"$g(E)$"); ax.set_ylim(0,3)
    ax.set_title("Density of states (1D/2D/3D)"); ax.legend(fontsize=7); ax.grid(alpha=0.3)
    save(fig,"f05_dos_dims.svg")

def f05_fermi_dirac():
    fig, ax = plt.subplots()
    E=np.linspace(-3,3,400)
    for T,c,lab in [(0.01,'#1a4d7c','T=0'),(0.3,'#2874a6','low T'),(0.8,'#c0392b','high T')]:
        ax.plot(E,1/(np.exp(E/T)+1),color=c,lw=2,label=lab)
    ax.axvline(0,color='gray',ls=':',lw=0.8); ax.text(0.05,0.9,r"$\mu=E_F$",fontsize=8)
    ax.set_xlabel(r"$E-E_F$"); ax.set_ylabel(r"$f(E)$")
    ax.set_title("Fermi–Dirac distribution"); ax.legend(fontsize=7); ax.grid(alpha=0.3)
    save(fig,"f05_fermi_dirac.svg")

# ---------- 單元 6：能帶 ----------
def f06_nfe_gap():
    fig, ax = plt.subplots()
    k=np.linspace(-np.pi,np.pi,400)
    ax.plot(k,k**2/2,color='gray',ls='--',lw=1,label='free electron')
    # opened band edges (schematic) near +-pi
    kk=np.linspace(-np.pi,np.pi,400)
    lower=kk**2/2; lower[np.abs(kk)>np.pi-1e-9]=np.nan
    ax.axvline(np.pi,color='#e67e22',ls=':',lw=0.8); ax.axvline(-np.pi,color='#e67e22',ls=':',lw=0.8)
    Eg=1.2; e=(np.pi**2/2)
    ax.plot([np.pi],[e-Eg/2],'o',color='#c0392b'); ax.plot([np.pi],[e+Eg/2],'o',color='#c0392b')
    ax.annotate("",xy=(np.pi,e+Eg/2),xytext=(np.pi,e-Eg/2),arrowprops=dict(arrowstyle="<->",color='#c0392b',lw=1.2))
    ax.text(np.pi-1.1,e,r"gap $=2|U_G|$",color='#c0392b',fontsize=8)
    ax.set_xticks([-np.pi,0,np.pi]); ax.set_xticklabels([r"$-\pi/a$","0",r"$\pi/a$"])
    ax.set_xlabel(r"$k$"); ax.set_ylabel(r"$E$"); ax.set_title("NFE gap at zone boundary")
    ax.legend(fontsize=7); ax.grid(alpha=0.3)
    save(fig,"f06_nfe_gap.svg")

def f06_tight_binding():
    fig, ax = plt.subplots()
    k=np.linspace(-np.pi,np.pi,400); E=-1-2*np.cos(k)
    ax.plot(k,E,color='#1a4d7c',lw=2)
    ax.text(-1.5,-2.7,r"$E(k)=-\alpha-2\gamma\cos ka$",fontsize=8.5)
    ax.text(0,-3.1,"bottom: $m^*>0$",fontsize=7,ha='center',color='#2874a6')
    ax.text(np.pi-0.2,1.1,"top: $m^*<0$",fontsize=7,ha='right',color='#c0392b')
    ax.annotate("bandwidth\n$4\\gamma$",xy=(0,1.2),xytext=(1.4,0),fontsize=7)
    ax.set_xticks([-np.pi,0,np.pi]); ax.set_xticklabels([r"$-\pi/a$","0",r"$\pi/a$"])
    ax.set_xlabel(r"$k$"); ax.set_ylabel(r"$E$"); ax.set_title("Tight-binding band"); ax.grid(alpha=0.3)
    save(fig,"f06_tight_binding.svg")

def f06_kronig_penney():
    fig, ax = plt.subplots()
    Ka=np.linspace(0.01,4*np.pi,800); P=3
    f=P*np.sin(Ka)/Ka+np.cos(Ka)
    ax.plot(Ka,f,color='#1a4d7c',lw=1.5)
    ax.axhline(1,color='#c0392b',ls='--',lw=0.8); ax.axhline(-1,color='#c0392b',ls='--',lw=0.8)
    ax.fill_between(Ka,-1,1,where=(np.abs(f)<=1),color='#aed6f1',alpha=0.5)
    ax.text(9,1.4,"allowed |f|≤1 (bands)",fontsize=7,color='#1a4d7c')
    ax.set_xlabel(r"$Ka$"); ax.set_ylabel(r"$P\,\frac{\sin Ka}{Ka}+\cos Ka$",fontsize=8)
    ax.set_ylim(-2.5,2.5); ax.set_title("Kronig–Penney bands/gaps"); ax.grid(alpha=0.3)
    save(fig,"f06_kronig_penney.svg")

# ---------- 單元 7：半導體 ----------
def f07_pn_junction():
    fig, ax = plt.subplots()
    x=np.linspace(-2,2,400)
    bend=0.6*(1/(1+np.exp(-3*x)))
    Ec=1.2-1.2*bend+0.0; Ev=0.0-1.2*bend
    # shift so p-side high, n-side low
    Ec=1.1- bend; Ev=0.1-bend
    ax.plot(x,Ec,color='#1a4d7c',lw=2); ax.plot(x,Ev,color='#c0392b',lw=2)
    ax.axhline(0.6-0.5,color='green',ls='--',lw=1); ax.text(1.2,0.13,r"$E_F$",color='green',fontsize=8)
    ax.text(-1.9,1.15,"$E_c$",color='#1a4d7c'); ax.text(-1.9,0.15,"$E_v$",color='#c0392b')
    ax.text(-1.5,-0.5,"p",fontsize=11); ax.text(1.5,-0.9,"n",fontsize=11)
    ax.annotate(r"$eV_{bi}$",xy=(0,1.0),xytext=(0.2,0.7),fontsize=8)
    ax.set_xlabel("position"); ax.set_ylabel("energy"); ax.set_yticks([])
    ax.set_title("pn junction band bending")
    save(fig,"f07_pn_junction.svg")

def f07_direct_indirect():
    fig,(a1,a2)=plt.subplots(1,2,figsize=(5,2.6),sharey=True)
    k=np.linspace(-1.5,1.5,200)
    for ax,title,shift in [(a1,"direct",0),(a2,"indirect",0.9)]:
        ax.plot(k,k**2,color='#1a4d7c',lw=2)
        ax.plot(k,-0.5-0.6*(k-shift)**2,color='#c0392b',lw=2)
        if shift==0:
            ax.annotate("",xy=(0,0),xytext=(0,-0.5),arrowprops=dict(arrowstyle="->",color='green',lw=1.5))
        else:
            ax.annotate("",xy=(shift,-0.5),xytext=(0,0),arrowprops=dict(arrowstyle="->",color='green',lw=1.5))
            ax.text(0.2,-0.1,"+phonon",fontsize=6,color='green')
        ax.set_title(title,fontsize=9); ax.set_xticks([]); ax.set_xlabel("k")
    a1.set_ylabel("E"); a1.set_yticks([])
    plt.suptitle("Direct vs indirect gap",fontsize=9)
    save(fig,"f07_direct_indirect.svg")

def f07_carrier_T():
    fig, ax = plt.subplots()
    invT=np.linspace(0.5,8,200)
    n=np.piecewise(invT,[invT<2,(invT>=2)&(invT<5),invT>=5],
                   [lambda t:18-1.2*t, lambda t:15.6, lambda t:15.6+1.0*(t-5)])
    n=18-1.2*invT
    ax.plot(invT,18-1.0*invT,color='#c0392b',lw=2,label='intrinsic')
    ax.hlines(15.6,2,5,color='#1a4d7c',lw=2,label='extrinsic (saturation)')
    ax.plot(np.linspace(5,8,50),15.6-1.0*(np.linspace(5,8,50)-5),color='#27ae60',lw=2,label='freeze-out')
    ax.plot(np.linspace(0.5,2,50),18-1.0*np.linspace(0.5,2,50),color='#c0392b',lw=2)
    ax.set_xlabel(r"$1/T$"); ax.set_ylabel(r"$\ln n$")
    ax.set_title("Carrier concentration vs 1/T"); ax.legend(fontsize=7); ax.grid(alpha=0.3)
    save(fig,"f07_carrier_T.svg")

# ---------- 單元 8：磁性 ----------
def f08_langevin():
    fig, ax = plt.subplots()
    a=np.linspace(0.01,8,300); L=1/np.tanh(a)-1/a
    ax.plot(a,L,color='#1a4d7c',lw=2)
    ax.plot(a,a/3,color='#c0392b',ls='--',lw=1); ax.text(0.6,0.5,r"$\approx\alpha/3$ (Curie)",color='#c0392b',fontsize=8)
    ax.axhline(1,color='gray',ls=':',lw=0.8); ax.text(5,0.92,"saturation",fontsize=8)
    ax.set_xlabel(r"$\alpha=mB/k_BT$"); ax.set_ylabel(r"$L(\alpha)=\coth\alpha-1/\alpha$",fontsize=8)
    ax.set_title("Langevin function"); ax.grid(alpha=0.3); ax.set_ylim(0,1.1)
    save(fig,"f08_langevin.svg")

def f08_curie():
    fig, ax = plt.subplots()
    T=np.linspace(0.5,6,200)
    ax.plot(T,1/T,color='#1a4d7c',lw=2,label=r"$\chi=C/T$")
    ax.set_xlabel(r"$T$"); ax.set_ylabel(r"$\chi$",color='#1a4d7c')
    ax2=ax.twinx(); ax2.plot(T,T,color='#c0392b',lw=2,ls='--',label=r"$1/\chi=T/C$")
    ax2.set_ylabel(r"$1/\chi$",color='#c0392b')
    ax.set_title("Curie law"); ax.grid(alpha=0.3)
    save(fig,"f08_curie.svg")

def f08_landau():
    fig, ax = plt.subplots()
    for n in range(6):
        ax.hlines((n+0.5),0,1,color='#1a4d7c',lw=2)
        ax.text(1.05,(n+0.5)-0.1,f"n={n}",fontsize=7)
    ax.annotate("",xy=(0.5,1.5),xytext=(0.5,0.5),arrowprops=dict(arrowstyle="<->",color='#c0392b',lw=1.2))
    ax.text(0.55,1.0,r"$\hbar\omega_c$",color='#c0392b')
    ax.set_xlim(0,1.5); ax.set_ylim(0,6); ax.set_xticks([])
    ax.set_ylabel(r"$E/\hbar\omega_c$"); ax.set_title(r"Landau levels $E_n=(n+\frac{1}{2})\hbar\omega_c$",fontsize=8.5)
    save(fig,"f08_landau.svg")

# ---------- 單元 9：超導 ----------
def f09_typeI_II():
    fig,(a1,a2)=plt.subplots(1,2,figsize=(5,2.6),sharey=True)
    H=np.linspace(0,2,200)
    M1=np.where(H<1,H,0)
    a1.plot(H,M1,color='#1a4d7c',lw=2); a1.axvline(1,color='gray',ls=':'); a1.text(1.02,0.1,r"$H_c$",fontsize=8)
    a1.set_title("type I",fontsize=9)
    M2=np.where(H<0.6,H,np.where(H<1.6,0.6*(1.6-H)/1.0,0))
    a2.plot(H,M2,color='#c0392b',lw=2); a2.axvline(0.6,color='gray',ls=':'); a2.axvline(1.6,color='gray',ls=':')
    a2.text(0.4,0.62,r"$H_{c1}$",fontsize=7); a2.text(1.45,0.1,r"$H_{c2}$",fontsize=7)
    a2.text(0.9,0.3,"vortex\nstate",fontsize=6,ha='center')
    a2.set_title("type II",fontsize=9)
    for a in (a1,a2): a.set_xlabel("H"); a.set_xticks([])
    a1.set_ylabel(r"$-M$"); a1.set_yticks([])
    plt.suptitle("Magnetization vs field",fontsize=9)
    save(fig,"f09_typeI_II.svg")

def f09_meissner():
    fig, ax = plt.subplots()
    ax.add_patch(Circle((0,0),0.8,fc='#aed6f1',ec='#1a4d7c',lw=1.5))
    ax.text(0,0,"SC",ha='center',va='center',fontsize=9)
    for y in np.linspace(-1.4,1.4,8):
        if abs(y)<0.85:
            x=np.linspace(-1.6,1.6,100); yy=y*(1+0.5*np.exp(-(x/0.6)**2)*np.sign(y))
            ax.plot(x,yy,color='#c0392b',lw=1)
        else:
            ax.plot([-1.6,1.6],[y,y],color='#c0392b',lw=1)
    ax.text(-1.5,1.6,"B expelled (Meissner)",fontsize=8,color='#c0392b')
    ax.set_xlim(-1.7,1.7); ax.set_ylim(-1.7,1.8); ax.set_aspect('equal'); ax.axis('off')
    save(fig,"f09_meissner.svg")

# ---------- 單元 10：費米面與進階 ----------
def f10_fermi_surface():
    fig, ax = plt.subplots()
    ax.add_patch(Rectangle((-1,-1),2,2,fill=False,ec='#e67e22',lw=1.5))
    ax.add_patch(Circle((0,0),1.13,fill=False,ec='#1a4d7c',lw=2))
    ax.text(0,0,"1st zone",ha='center',fontsize=7)
    ax.text(0.8,0.95,"into\n2nd zone",fontsize=6,color='#1a4d7c')
    ax.set_xlim(-1.6,1.6); ax.set_ylim(-1.6,1.6); ax.set_aspect('equal'); ax.axis('off')
    ax.set_title("Free-electron Fermi circle vs BZ")
    save(fig,"f10_fermi_surface.svg")

def f10_stm_tunnel():
    fig, ax = plt.subplots()
    d=np.linspace(0,4,200); I=np.exp(-2*d)
    ax.semilogy(d,I,color='#1a4d7c',lw=2)
    ax.set_xlabel(r"tip distance $d$ ($\mathrm{\AA}$)"); ax.set_ylabel(r"$I\propto e^{-2\kappa d}$")
    ax.text(1.3,0.25,r"$\kappa\approx1\,\mathrm{\AA}^{-1}$"+"\n+1 Ang: I x 1/7.4",fontsize=8)
    ax.set_title("STM tunneling current"); ax.grid(alpha=0.3,which='both')
    save(fig,"f10_stm_tunnel.svg")

def f10_dirac_cone():
    fig, ax = plt.subplots()
    k=np.linspace(-1,1,200)
    ax.plot(k,np.abs(k),color='#1a4d7c',lw=2); ax.plot(k,-np.abs(k),color='#c0392b',lw=2)
    ax.text(0.1,0.6,r"$E=\hbar v_F|k|$",fontsize=9)
    ax.plot(0,0,'o',color='black',ms=4); ax.text(0.05,-0.25,"Dirac point",fontsize=7)
    ax.set_xlabel(r"$k$"); ax.set_ylabel(r"$E$"); ax.set_title("Graphene linear dispersion (massless)")
    ax.grid(alpha=0.3)
    save(fig,"f10_dirac_cone.svg")

# ---------- 先備知識（prerequisites）f00_* ----------
def f00_dotcross():
    fig,(a1,a2)=plt.subplots(1,2,figsize=(5,2.5))
    a1.annotate("",xy=(1.4,0),xytext=(0,0),arrowprops=dict(arrowstyle="->",color='#1a4d7c',lw=2))
    a1.annotate("",xy=(0.9,0.9),xytext=(0,0),arrowprops=dict(arrowstyle="->",color='#c0392b',lw=2))
    a1.plot([0.9,0.9],[0,0.9],color='gray',ls=':')
    a1.text(1.2,-0.18,r"$\mathbf{a}$",color='#1a4d7c'); a1.text(0.7,0.95,r"$\mathbf{b}$",color='#c0392b')
    a1.text(0.2,0.12,r"$\theta$"); a1.set_title(r"dot: $\mathbf{a}\cdot\mathbf{b}=ab\cos\theta$",fontsize=9)
    a1.set_xlim(-0.3,1.7); a1.set_ylim(-0.3,1.2); a1.set_aspect('equal'); a1.axis('off')
    a2.annotate("",xy=(1.3,0),xytext=(0,0),arrowprops=dict(arrowstyle="->",color='#1a4d7c',lw=2))
    a2.annotate("",xy=(0.4,1.1),xytext=(0,0),arrowprops=dict(arrowstyle="->",color='#c0392b',lw=2))
    a2.annotate("",xy=(0,0.001),xytext=(0,0),arrowprops=dict(arrowstyle="->",color='green',lw=2))
    a2.plot(0.1,0.05,'o',color='green'); a2.text(0.13,0.12,r"$\mathbf{a}\times\mathbf{b}$ (out)",color='green',fontsize=7)
    a2.set_title(r"cross: $|\mathbf{a}\times\mathbf{b}|=ab\sin\theta$",fontsize=9)
    a2.set_xlim(-0.3,1.6); a2.set_ylim(-0.3,1.3); a2.set_aspect('equal'); a2.axis('off')
    save(fig,"f00_dotcross.svg")

def f00_euler():
    fig, ax = plt.subplots()
    th=np.linspace(0,2*np.pi,200); ax.plot(np.cos(th),np.sin(th),color='gray',lw=1)
    a=1.0; ax.annotate("",xy=(np.cos(a),np.sin(a)),xytext=(0,0),arrowprops=dict(arrowstyle="->",color='#1a4d7c',lw=2))
    ax.plot([np.cos(a),np.cos(a)],[0,np.sin(a)],color='#c0392b',ls=':')
    ax.plot([0,np.cos(a)],[0,0],color='#27ae60',ls=':')
    ax.text(np.cos(a)+0.03,np.sin(a),r"$e^{i\theta}$",color='#1a4d7c')
    ax.text(0.3,-0.12,r"$\cos\theta$",color='#27ae60',fontsize=8); ax.text(np.cos(a)+0.02,0.3,r"$\sin\theta$",color='#c0392b',fontsize=8)
    ax.set_xlabel("Re"); ax.set_ylabel("Im"); ax.set_aspect('equal')
    ax.set_title(r"Euler: $e^{i\theta}=\cos\theta+i\sin\theta$"); ax.grid(alpha=0.3)
    ax.set_xlim(-1.3,1.3); ax.set_ylim(-1.3,1.3)
    save(fig,"f00_euler.svg")

def f00_fourier():
    fig, ax = plt.subplots()
    x=np.linspace(0,2*np.pi,400)
    sq=np.sign(np.sin(x))
    ax.plot(x,sq,color='gray',lw=1.5,label='square wave')
    for n,c in [(1,'#aed6f1'),(3,'#5dade2'),(9,'#1a4d7c')]:
        s=sum(np.sin(k*x)*4/(np.pi*k) for k in range(1,2*n,2))
        ax.plot(x,s,color=c,lw=1.2,label=f"{ (n+1)//1 } terms" if False else f"sum {len(range(1,2*n,2))} terms")
    ax.set_title("Fourier: periodic = sum of sines"); ax.legend(fontsize=6.5)
    ax.set_xlabel("x"); ax.set_xticks([0,np.pi,2*np.pi]); ax.set_xticklabels(["0",r"$\pi$",r"$2\pi$"]); ax.grid(alpha=0.3)
    save(fig,"f00_fourier.svg")

def f00_geometric():
    fig, ax = plt.subplots()
    n=np.arange(1,9); terms=0.5**n; partial=np.cumsum(terms)
    ax.bar(n,terms,color='#aed6f1',label='term $(1/2)^n$')
    ax.plot(n,partial,'o-',color='#c0392b',label='partial sum')
    ax.axhline(1,color='gray',ls=':'); ax.text(5.5,1.02,"limit = 1",fontsize=8)
    ax.set_xlabel("n"); ax.set_title(r"Geometric series $\sum r^n=\frac{1}{1-r}$",fontsize=9)
    ax.legend(fontsize=7); ax.grid(alpha=0.3)
    save(fig,"f00_geometric.svg")

def f00_sho():
    fig, ax = plt.subplots()
    x=np.linspace(-2,2,200); ax.plot(x,x**2,color='#1a4d7c',lw=2)
    for n in range(4):
        E=0.5+n; xr=np.sqrt(E); ax.hlines(E,-xr,xr,color='#c0392b',lw=1.2)
        ax.text(xr+0.05,E-0.1,f"n={n}",fontsize=7)
    ax.text(-1.9,3.5,r"$V=\frac{1}{2} kx^2$",fontsize=9)
    ax.text(0,-0.5,r"$E_n=(n+\frac{1}{2})\hbar\omega$",ha='center',fontsize=8,color='#c0392b')
    ax.set_xlabel("x"); ax.set_ylabel("E"); ax.set_title("Harmonic oscillator (phonon building block)",fontsize=8.5)
    ax.set_ylim(-0.8,4); ax.grid(alpha=0.3)
    save(fig,"f00_sho.svg")

def f00_boltzmann():
    fig, ax = plt.subplots()
    E=np.linspace(0,4,200)
    for T,c in [(0.5,'#1a4d7c'),(1.0,'#2874a6'),(2.0,'#c0392b')]:
        ax.plot(E,np.exp(-E/T),color=c,lw=2,label=f"kT={T}")
    ax.set_xlabel("E (energy of state)"); ax.set_ylabel(r"$\propto e^{-E/k_BT}$")
    ax.set_title("Boltzmann factor: occupation vs energy"); ax.legend(fontsize=7); ax.grid(alpha=0.3)
    save(fig,"f00_boltzmann.svg")

def f00_particlebox():
    fig, ax = plt.subplots()
    ax.axvline(0,color='black',lw=2); ax.axvline(1,color='black',lw=2)
    x=np.linspace(0,1,200)
    for n in range(1,4):
        E=n**2; ax.hlines(E,0,1,color='gray',ls=':',lw=0.8)
        ax.plot(x,E+1.6*np.sin(n*np.pi*x),color='#1a4d7c',lw=1.3)
        ax.text(1.03,E,f"$E_{n}\\propto{n}^2$",fontsize=7)
    ax.set_xlabel("x / L"); ax.set_ylabel("E"); ax.set_title(r"Particle in a box: $E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}$",fontsize=8.5)
    ax.set_xlim(-0.1,1.4); ax.set_yticks([])
    save(fig,"f00_particlebox.svg")

def f00_coulomb():
    fig, ax = plt.subplots()
    r=np.linspace(0.25,4,200); ax.plot(r,-1/r,color='#1a4d7c',lw=2)
    ax.axhline(0,color='gray',lw=0.6)
    ax.set_xlabel("r"); ax.set_ylabel(r"$U=-\frac{q^2}{4\pi\varepsilon_0 r}$",fontsize=9)
    ax.set_title("Coulomb potential (ionic binding)"); ax.grid(alpha=0.3); ax.set_ylim(-4,0.5)
    save(fig,"f00_coulomb.svg")

def f00_taylor():
    fig, ax = plt.subplots()
    x=np.linspace(-2,2,200)
    ax.plot(x,np.sin(x),color='#1a4d7c',lw=2,label=r"$\sin x$")
    ax.plot(x,x,color='#c0392b',ls='--',lw=1.5,label=r"$x$ (small-angle)")
    ax.plot(x,x-x**3/6,color='#27ae60',ls=':',lw=1.5,label=r"$x-x^3/6$")
    ax.set_title("Taylor / small-angle approximation"); ax.legend(fontsize=7)
    ax.set_xlabel("x"); ax.grid(alpha=0.3); ax.set_ylim(-2,2)
    save(fig,"f00_taylor.svg")

def f00_wave():
    fig, ax = plt.subplots(figsize=(4.6,2.4))
    x=np.linspace(0,4*np.pi,400); ax.plot(x,np.sin(x),color='#1a4d7c',lw=2)
    ax.annotate("",xy=(2*np.pi,1.2),xytext=(0,1.2),arrowprops=dict(arrowstyle="<->",color='#c0392b'))
    ax.text(np.pi,1.3,r"$\lambda=2\pi/k$",color='#c0392b',ha='center',fontsize=8)
    ax.set_title(r"Wave $y=A\sin(kx-\omega t)$"); ax.set_xlabel("x"); ax.set_yticks([])
    ax.set_ylim(-1.5,1.7)
    save(fig,"f00_wave.svg")

def main():
    for name,fn in list(globals().items()):
        if name.startswith("f") and name[1:3].isdigit() and callable(fn):
            fn()
    print("DONE")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Genera las figuras vectoriales (PDF) del paper teórico.
Ejecutar:  python generar_figuras.py
Las figuras se guardan en ./figuras/
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

AZUL = "#144682"
NARANJA = "#E08A00"
VERDE = "#2E7D32"
GRIS = "#5A5A5A"

os.makedirs("figuras", exist_ok=True)
plt.rcParams.update({
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": GRIS,
    "axes.labelcolor": "#222222",
    "figure.figsize": (5.6, 3.6),
})

def guardar(nombre):
    plt.tight_layout()
    plt.savefig(f"figuras/{nombre}.pdf", bbox_inches="tight")
    plt.close()

# 1 -- Demanda y demanda inversa --------------------------------------------
Q = np.linspace(0, 120, 200)
p_inv = 60 - 0.5 * Q
plt.plot(Q, p_inv, color=AZUL, lw=2)
plt.title("Demanda inversa: $p = 60 - \\frac{1}{2}Q$")
plt.xlabel("Cantidad $Q$"); plt.ylabel("Precio $p$")
plt.xlim(0, 120); plt.ylim(0, 65)
plt.fill_between(Q, p_inv, alpha=0.06, color=AZUL)
guardar("demanda_inversa")

# 2 -- Equilibrio de mercado ------------------------------------------------
Q = np.linspace(0, 120, 200)
dem = 60 - 0.5 * Q          # demanda inversa
ofe = 10 + Q / 3            # oferta inversa  (Qs = -30 + 3p)
plt.plot(Q, dem, color=AZUL, lw=2, label="Demanda")
plt.plot(Q, ofe, color=NARANJA, lw=2, label="Oferta")
plt.plot(60, 30, "o", color="black", zorder=5)
plt.vlines(60, 0, 30, ls="--", color=GRIS, lw=1)
plt.hlines(30, 0, 60, ls="--", color=GRIS, lw=1)
plt.annotate("$(q^*=60,\\ p^*=30)$", (60, 30), xytext=(66, 36), color="black")
plt.title("Equilibrio de mercado")
plt.xlabel("Cantidad $Q$"); plt.ylabel("Precio $p$")
plt.xlim(0, 120); plt.ylim(0, 65); plt.legend()
guardar("equilibrio")

# 3 -- Excedentes del consumidor y del productor ----------------------------
Q = np.linspace(0, 60, 200)
dem = 60 - 0.5 * Q
ofe = 10 + Q / 3
plt.plot(np.linspace(0,120,200), 60-0.5*np.linspace(0,120,200), color=AZUL, lw=2, label="Demanda")
plt.plot(np.linspace(0,120,200), 10+np.linspace(0,120,200)/3, color=NARANJA, lw=2, label="Oferta")
plt.fill_between(Q, dem, 30, color=AZUL, alpha=0.18)
plt.fill_between(Q, 30, ofe, color=NARANJA, alpha=0.18)
plt.text(15, 40, "EC", color=AZUL, fontsize=13, fontweight="bold")
plt.text(15, 22, "EP", color=NARANJA, fontsize=13, fontweight="bold")
plt.plot(60, 30, "o", color="black", zorder=5)
plt.hlines(30, 0, 60, ls="--", color=GRIS, lw=1)
plt.title("Excedente del consumidor (EC) y del productor (EP)")
plt.xlabel("Cantidad $Q$"); plt.ylabel("Precio $p$")
plt.xlim(0, 120); plt.ylim(0, 65); plt.legend()
guardar("excedentes")

# 4 -- Costo medio en U y costo marginal ------------------------------------
q = np.linspace(1, 30, 200)
CMe = 50 / q + 10 + 0.5 * q
CMg = 10 + q
plt.plot(q, CMe, color=AZUL, lw=2, label="Costo medio $C_{me}$")
plt.plot(q, CMg, color=NARANJA, lw=2, label="Costo marginal $C_{mg}$")
plt.plot(10, 20, "o", color="black", zorder=5)
plt.annotate("mínimo de $C_{me}$\n($C_{mg}=C_{me}$)", (10, 20), xytext=(13, 11), color="black")
plt.title("El costo marginal corta al medio en su mínimo")
plt.xlabel("Cantidad $q$"); plt.ylabel("Costo por unidad")
plt.xlim(0, 30); plt.ylim(0, 45); plt.legend()
guardar("costos_U")

# 5 -- Beneficio (parábola) con máximo --------------------------------------
q = np.linspace(0, 100, 200)
Pi = -0.5 * q**2 + 50 * q - 50
plt.plot(q, Pi, color=AZUL, lw=2)
plt.axhline(0, color=GRIS, lw=0.8)
plt.plot(50, 1200, "o", color="black", zorder=5)
plt.vlines(50, 0, 1200, ls="--", color=GRIS, lw=1)
plt.annotate("máximo: $q^*=50,\\ \\Pi=1200$", (50, 1200), xytext=(20, 1280), color="black")
plt.title("Beneficio: $\\Pi(q) = -\\frac{1}{2}q^2 + 50q - 50$")
plt.xlabel("Cantidad $q$"); plt.ylabel("Beneficio $\\Pi$")
plt.xlim(0, 100); plt.ylim(-100, 1450)
guardar("beneficio")

# 6 -- Elasticidad e ingreso total ------------------------------------------
p = np.linspace(0, 20, 200)
I = 200 * p - 10 * p**2
plt.plot(p, I, color=AZUL, lw=2)
plt.axvline(10, ls="--", color=GRIS, lw=1)
plt.plot(10, 1000, "o", color="black", zorder=5)
plt.fill_between(p[p <= 10], I[p <= 10], color=VERDE, alpha=0.12)
plt.fill_between(p[p >= 10], I[p >= 10], color=NARANJA, alpha=0.12)
plt.text(3.5, 300, "inelástico\n$|\\varepsilon|<1$", color=VERDE, ha="center")
plt.text(15.5, 300, "elástico\n$|\\varepsilon|>1$", color=NARANJA, ha="center")
plt.annotate("ingreso máximo\n($\\varepsilon=-1$)", (10, 1000), xytext=(11, 1080), color="black")
plt.title("Ingreso total y elasticidad")
plt.xlabel("Precio $p$"); plt.ylabel("Ingreso total $I=p\\,Q$")
plt.xlim(0, 20); plt.ylim(0, 1200)
guardar("elasticidad_ingreso")

# 7 -- Curvas de reacción de Cournot ----------------------------------------
q2 = np.linspace(0, 90, 200)
r1 = (90 - q2) / 2          # mejor respuesta de la empresa 1: q1 = (90 - q2)/2
q1 = np.linspace(0, 90, 200)
r2 = (90 - q1) / 2          # mejor respuesta de la empresa 2
plt.plot((90 - q2) / 2, q2, color=AZUL, lw=2, label="Reacción empresa 1")
plt.plot(q1, (90 - q1) / 2, color=NARANJA, lw=2, label="Reacción empresa 2")
plt.plot(30, 30, "o", color="black", zorder=5)
plt.annotate("Equilibrio de Nash\n$(30,\\ 30)$", (30, 30), xytext=(38, 40), color="black")
plt.title("Duopolio de Cournot: curvas de reacción")
plt.xlabel("$q_1$"); plt.ylabel("$q_2$")
plt.xlim(0, 90); plt.ylim(0, 90); plt.legend()
guardar("cournot")

# 8 -- Perfil del VAN -------------------------------------------------------
flujos = np.array([-1000, 400, 400, 400, 400])
tasas = np.linspace(0, 0.40, 200)
van = [np.sum(flujos / (1 + r) ** np.arange(len(flujos))) for r in tasas]
plt.plot(tasas * 100, van, color=AZUL, lw=2)
plt.axhline(0, color=GRIS, lw=0.8)
plt.axvline(21.86, ls="--", color=NARANJA, lw=1.2)
plt.annotate("TIR $\\approx 21.9\\%$", (21.86, 0), xytext=(24, 120), color=NARANJA)
plt.plot(10, np.sum(flujos / 1.1 ** np.arange(len(flujos))), "o", color="black", zorder=5)
plt.annotate("VAN$(10\\%)\\approx 268$", (10, 268), xytext=(2, 360), color="black")
plt.title("Perfil del VAN")
plt.xlabel("Tasa de descuento (\\%)"); plt.ylabel("VAN")
plt.xlim(0, 40)
guardar("van_perfil")

print("Figuras generadas en ./figuras/")

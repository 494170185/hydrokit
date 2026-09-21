# Formulas & References

## IDF 暴雨强度公式

我国常用形式（《室外排水设计标准》GB 50014）：

```
i = A * (1 + C * lg T) / (t + b)^n    [mm/min]
```

## SCS 单位线

```
q_p = 0.208 * A * Q / t_p    [m³/s per mm]
t_p = 0.6 * t_c + 0.5 * D    [hr]
```

`0.208 = 2.08 / (254 * 60 / 100)` 换算自英制。^1

## SCS-CN 径流深

```
Q = (P - Ia)² / (P - Ia + S), P > Ia
S = 25400 / CN - 254         [mm]
Ia = λ * S, λ = 0.2
```

## Horton 下渗

```
f(t) = f_c + (f_0 - f_c) * exp(-k t)
F(t) = f_c·t + (f_0 - f_c)/k * (1 - exp(-k t))
```

## Muskingum

```
S = K * (x · I + (1 - x) · O)
O_2 = C_0 I_2 + C_1 I_1 + C_2 O_1
C_0 = (Δt/2 - Kx) / (K - Kx + Δt/2)
C_1 = (Δt/2 + Kx) / (K - Kx + Δt/2)
C_2 = (K - Kx - Δt/2) / (K - Kx + Δt/2)
```

## Manning

```
V = (1/n) * R^(2/3) * √S
Q = A * V
矩形: A = b·y, R = b·y / (b + 2y)
梯形: A = (b + z·y)·y, R = A / (b + 2y√(1+z²))
```

## Penman-Monteith FAO-56

```
ET_0 = [0.408·Δ·(Rn - G) + γ · (900/(T+273)) · u2 · (es - ea)]
       / [Δ + γ·(1 + 0.34 u2)]    [mm/day]
```

## Hargreaves-Samani

```
ET_0 = 0.0023 · (T_mean + 17.8) · √(T_max − T_min) · R_a · 0.408
```

## P-III 设计值

```
X_p = mean * (1 + Cv * K_p)
K_p 用 Wilson-Hilferty: K_p = (2/Cs)*(1 + Cs*t/6 − Cs²/36)³ − (2/Cs)(1 − Cs²/24)³
```

---

^1 Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). *Applied Hydrology*.

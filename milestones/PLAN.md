# hydrokit · milestone 规划（供 git history 生成）

> 12 个 milestone，8 周开发节奏（2026-08-04 → 2026-09-24）。每个 milestone 是一次有意义的推进、对应一个版本号。

## M1 · v0.1.0 · 项目骨架与工具（08-04 ~ 08-06，commits 4）
- README/pyproject/.gitignore
- hydrokit/__init__.py/__main__.py
- hydrokit/core/{errors,logging,ids,time,utils}.py
- tests/core

## M2 · v0.2.0 · 单位与量纲（08-07 ~ 08-11，commits 4）
- hydrokit/units/{length,area,volume,flow,time,convert}.py
- 流域面积/流量/水深换算
- tests/units

## M3 · v0.3.0 · 统计与频率分析（08-12 ~ 08-16，commits 4）
- hydrokit/stats/{frequency,p3,gumbel,normal,fit}.py
- P-III 型频率曲线 / Gumbel / Normal
- 频率计算 / 适线
- tests/stats

## M4 · v0.4.0 · 设计暴雨（08-17 ~ 08-21，commits 4）
- hydrokit/precip/{design_storm,idf,temporal,spatial,areal_reduction}.py
- 暴雨强度公式 / 芝加哥雨型 / 时空分配
- tests/precip

## M5 · v0.5.0 · 下渗与土壤水（08-22 ~ 08-26，commits 4）
- hydrokit/infiltration/{horton,philip,green_ampt,curve_number,soil_moisture}.py
- Horton / Philip / Green-Ampt / CN 曲线
- tests/infiltration

## M6 · v0.6.0 · 单位线（08-27 ~ 08-31，commits 4）
- hydrokit/uh/{unit_hydrograph,clark,snyder,scs,convolution}.py
- Clark / Snyder / SCS UH 推求
- tests/uh

## M7 · v0.7.0 · 产流计算（09-01 ~ 09-05，commits 4）
- hydrokit/runoff/{simple,scs_cn,xinanjiang,gr4j}.py
- 径流系数法 / SCS-CN / 新安江 / GR4J
- tests/runoff

## M8 · v0.8.0 · 洪水演算（09-06 ~ 09-10，commits 4）
- hydrokit/routing/{muskingum,muskingum_cunge,lag,kinematic}.py
- Muskingum 及其变体
- tests/routing

## M9 · v0.9.0 · 明渠水力学（09-11 ~ 09-15，commits 4）
- hydrokit/channel/{manning,normal_depth,critical_depth,backwater,hydraulic_jump}.py
- Manning / 正常水深 / 临界水深 / 回水曲线 / 水跃
- tests/channel

## M10 · v1.0.0 · 蒸发与水量平衡（09-16 ~ 09-20，commits 4）
- hydrokit/evap/{penman,priestley_taylor,hargreaves,pan}.py
- hydrokit/balance/{water_balance,bucket,abstractions}.py
- Penman-Monteith / Priestley-Taylor / Hargreaves / 蒸发皿折算
- tests/evap tests/balance

## M11 · v1.0.1 · IO 与序列（09-21 ~ 09-23，commits 3）
- hydrokit/io/{csv,excel,json,timeseries,resample}.py
- 时序读写/插值/重采样
- tests/io

## M12 · v1.0.2 · CLI / CI / 发布（09-24，commits 3）
- hydrokit/cli/{main,storm,runoff,routing,channel}.py
- .github/workflows/tests.yml
- docs/{architecture,formulas,api,contributing}.md
- scripts/{bootstrap,check,package}.py
- LICENSE

合计：46 commits、≥150 代码文件、约 200+ tests

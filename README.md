# hydrokit

工程水文计算工具库：设计暴雨 → 产流 → 单位线 → 汇流/河道演算 → 水力要素 → 蒸发与水量平衡。纯标准库、零运行时依赖，可离线构建。

## 覆盖内容

| 模块 | 内容 |
|---|---|
| `units` | 长度/面积/体积/流量/时间换算（含亩、km² 面雨量→体积） |
| `stats` | 频率分析（Weibull 适线、P-III、Gumbel、正态分位数） |
| `precip` | 暴雨强度公式 IDF、芝加哥雨型、时程分配、点面折减（ARF/泰森） |
| `infiltration` | Horton、Philip、Green-Ampt、SCS 曲线数 CN、前期土壤湿度 AMC |
| `uh` | Clark / Snyder / SCS 单位线、卷积预报、S 曲线 |
| `runoff` | 径流系数法、SCS-CN 产流、新安江蓄水容量曲线、GR4J |
| `routing` | Muskingum、Muskingum-Cunge、滞后演算、运动波 |
| `channel` | Manning 正常水深、临界水深、回水曲线、水跃 |
| `evap` | Penman-Monteith、Priestley-Taylor、Hargreaves、蒸发皿折算 |
| `balance` | 水量平衡、土壤蓄水桶、损失分割 |
| `io` | 时序 CSV/JSON 读写、重采样、插值 |

## 快速开始

```bash
python -m hydrokit --version
python -m hydrokit storm --idf-file idf.json --T 50 --duration 120
python -m hydrokit runoff --cn 78 --p 120
```

## 开发

```bash
python -m pytest
python -m ruff check hydrokit tests
python scripts/check.py
```

公式与出处见 `docs/formulas.md`。

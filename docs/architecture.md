# hydrokit Architecture

```
precip (IDF / 芝加哥 / 分配)
    ↓ 时段降雨
infiltration (Horton / Philip / Green-Ampt / CN / AMC)
    ↓ 净雨
uh (SCS / Clark / Snyder)
    ↓ 直接径流
routing (Muskingum / Cunge / 运动波 / 滞后)
    ↓ 出口断面
channel (Manning / 正常水深 / 临界 / 水跃 / 回水)
    ↓ 水力要素
evap (PM / PT / Hargreaves / pan) ← 与 balance 组成闭合
balance (bucket / phi-index / 闭合校验)
```

## 关键决策

- **无 NumPy 依赖**：核心计算全部走 `list[float]` + `math`，小型水库也能跑
- **不可变 dataclass**：TimeSeries 与 UnitHydrograph 都是值对象
- **调用链分层**：precip → infiltration → uh → routing → channel 单向依赖
- **显式单位切换**：`units/convert.py` 是唯一改动单位的地方，其他函数都假定 SI

## 未实现（有界扩展位）

- HEC-HMS 完整导入（留 io/hess 接口）
- Muskingum 非线性变体（v 与 w 因子法）
- 湿润区新安江三层水源（当前为单一层，位于 runoff/xinanjiang.py）

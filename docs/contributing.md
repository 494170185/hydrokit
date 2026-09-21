# Contributing

## 环境

```
python -m venv .venv && .venv\\Scripts\\activate
pip install -e .[dev] pytest ruff
```

## 开发约束

1. 新增计算模块必须带测试用例（正常 + 边界 + 病态输入）
2. `ruff check hydrokit tests` 必须 0 错
3. 提交信息用 conventional commits
4. 新公式请在 `docs/formulas.md` 登记

## 扩展点

- `precip/`：其他空间分配方法
- `uh/`：Clark 带面积曲线的完整实现
- `routing/`：HEC-RAS 1D 简化版
- `io/`：GRIB / NetCDF 读取（需引入新依赖，先议再加）

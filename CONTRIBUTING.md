# Contributing

1. M9A 专属行为放入 `automas_script_maafw_pack_m9a`。
2. 通用 MaaFW 行为应提交到 `automas-maafw` 仓库。
3. 改动依赖约束时同步更新 `automas-m9a` meta-package 版本。
4. 提交使用 Conventional Commits，例如 `fix(m9a): ...`。

本地构建：

```powershell
uv sync --all-packages --group dev
uv run python scripts/build_all.py
```


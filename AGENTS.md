# Agent Instructions

本仓库维护 AUTO-MAS 的 M9A 专属 MaaFW project pack 与聚合安装包。

- M9A 业务、迁移和资源声明属于 `automas-script-maafw-pack-m9a`。
- `automas-m9a` 只负责依赖聚合，不包含运行时代码或插件 entry point。
- 通用 MaaFW 运行能力必须依赖 `automas-maafw` 仓库发布的包，不在本仓库复制实现。
- 修改 pack 行为时补充测试并同步提升 pack 与 meta-package 的最低依赖。
- 提交前运行测试和 `python scripts/build_all.py`。
- 不提交构建产物、虚拟环境或 Python 缓存。


# AUTO-MAS M9A Plugins

AUTO-MAS 的 M9A 专属 MaaFW project pack 与一键安装聚合包。

## Packages

- `automas-script-maafw-pack-m9a`：注册 M9A project pack。
- `automas-m9a`：安装 M9A 所需全部 MaaFW 插件的 meta-package。

通用 MaaFW 运行栈由独立的 `automas-maafw` 仓库维护和发布。

## Development

```powershell
uv sync --all-packages --group dev
```


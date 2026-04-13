# 📺 视频资源配置中心

## 📋 项目简介

本项目是一个集中管理 TVBox 和视频应用（KVideo、MoonTV 等）配置文件的仓库，提供多种视频资源接口的统一管理和自动更新功能。

## 📁 目录结构

```
files/
├── README.md                          # 项目说明文档
├── .github/workflows/                 # GitHub Actions 自动化工作流
│   ├── update_base58.yml             # Base58 编码自动更新
│   └── update_kvideo_config.yml      # KVideo 配置自动转换
├── video/                            # 视频配置文件目录
│   ├── config_kvideo.json            # KVideo 资源配置（新格式）
│   ├── config_moontv.json            # MoonTV 原始配置
│   ├── config_moontv_base58.json     # Base58 编码配置
│   └── tvbox.json                    # TVBox 多仓接口配置
└── x/                                # 其他文件目录
```

## 🔧 配置文件说明

### 1. config_moontv.json
MoonTV 应用的原始配置文件，包含以下特点：
- 采用 `api_site` 对象格式，包含多个 API 源
- 每个源包含 `name`（名称）、`api`（接口地址）、`detail`（详情页地址）
- 支持普通资源（normal）和高级资源（premium）两种分组
- 包含缓存时间配置（`cache_time`）

### 2. config_kvideo.json
KVideo 应用的新格式资源配置，由 `config_moontv.json` 自动转换生成：
- 采用数组格式，每个资源为独立对象
- 字段包括：`id`、`name`、`baseUrl`、`group`、`priority`、`enabled`
- 自动按资源类型分组并设置优先级
- **高级资源（premium）**：默认启用
- **普通资源（normal）**：包含常规影视资源

### 3. config_moontv_base58.json
由 `config_moontv.json` 经过 Base58 编码生成的配置文件：
- 用于特定应用的加密配置需求
- 由 GitHub Actions 自动生成和更新

### 4. tvbox.json
TVBox 应用的多仓接口配置：
- 包含多个公开的 TVBox 配置源 URL
- 支持多种线路和配置选项
- 包含小盒子、肥猫、饭太硬、摸鱼等多个知名配置源

## 🤖 自动化工作流

### update_base58.yml
**触发条件**：
- `config_moontv.json` 文件被推送时
- 手动触发（workflow_dispatch）

**功能**：
- 使用 Python 的 base58 库对配置文件进行编码
- 自动生成 `config_moontv_base58.json`
- 自动提交并推送到仓库

### update_kvideo_config.yml
**触发条件**：
- `config_moontv.json` 文件被推送时
- 手动触发（workflow_dispatch）

**功能**：
- 将 `config_moontv.json` 转换为 KVideo 新格式
- 自动识别资源类型（normal/premium）
- 自动设置优先级顺序
- 生成 `config_kvideo.json` 并提交

## 📊 资源分组说明

### 普通资源（normal）
- 常规影视资源网站
- 例如：1080资源、360资源、卧龙资源、量子资源等
- 优先级从 1 开始递增

### 高级资源（premium）
- 成人内容资源网站
- 默认启用状态（`enabled: true`）
- 优先级独立于普通资源

## 🚀 使用方法

### 更新配置
1. 编辑 `video/config_moontv.json` 文件
2. 提交更改到仓库
3. GitHub Actions 将自动运行：
   - 生成新的 `config_kvideo.json`
   - 生成新的 `config_moontv_base58.json`

### 手动触发
1. 进入仓库的 Actions 页面
2. 选择对应的工作流
3. 点击 "Run workflow" 手动执行

### 使用配置
- **MoonTV 用户**：使用 `config_moontv.json` 或 `config_moontv_base58.json`
- **KVideo 用户**：使用 `config_kvideo.json`
- **TVBox 用户**：使用 `tvbox.json` 中的多仓配置

## ⚠️ 注意事项

1. **内容提示**：本项目包含部分成人内容资源接口，请谨慎使用
2. **接口可用性**：由于资源接口可能随时变化，不保证所有接口长期有效
3. **版权声明**：本项目仅供学习和技术研究使用
4. **合法使用**：请遵守当地法律法规，合法使用相关资源

## 🔄 配置格式示例

### MoonTV 格式（原始）
```json
{
  "cache_time": 9200,
  "api_site": {
    "api_1": {
      "name": "TV-1080资源",
      "api": "https://api.1080zyku.com/inc/api_mac10.php",
      "detail": "https://api.1080zyku.com"
    }
  }
}
```

### KVideo 格式（转换后）
```json
[
  {
    "id": "source_1",
    "name": "TV-1080资源",
    "baseUrl": "https://api.1080zyku.com/inc/api_mac10.php",
    "group": "normal",
    "priority": 1
  }
]
```

## 📝 资源命名规范

- **TV-** 前缀：普通影视资源
- 命名格式：`类型-资源名称`

## 🛠️ 技术支持

如遇到配置问题或接口失效，可以：
1. 检查网络连通性
2. 确认 API 接口是否仍然可用
3. 提交 Issue 反馈问题
4. 提交 Pull Request 更新配置

## 📄 许可证

本项目仅供学习和技术研究使用。请遵守当地法律法规。

---

**最后更新时间**：2026年4月13日

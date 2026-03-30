# 🧰 多功能工具箱 (Android App Demo)

一个基于 Flet 框架开发的跨平台多功能工具箱应用，支持移动端和 PC 端响应式布局。

## 📁 项目结构

```
android-app-demo/
├── src/                          # 源代码目录
│   ├── components/               # 公共组件
│   │   ├── __init__.py
│   │   ├── bottom_nav.py        # 底部导航栏（旧版）
│   │   ├── unified_nav.py       # 统一导航栏（响应式）
│   │   └── dialogs.py           # 对话框组件
│   ├── features/                 # 功能模块（按页面组织）
│   │   ├── base_page.py         # 页面基类
│   │   ├── home/                # 主页功能模块
│   │   │   ├── __init__.py
│   │   │   ├── home.py          # 首页（工具列表）
│   │   │   ├── counter.py       # 计数器
│   │   │   ├── calculator.py    # 计算器
│   │   │   ├── converter.py     # 单位转换
│   │   │   └── settings.py      # 设置
│   │   └── mine/                # 个人中心模块
│   │       ├── __init__.py
│   │       └── mine.py          # 我的页面
│   ├── utils/                    # 工具模块
│   │   ├── __init__.py
│   │   └── responsive.py        # 响应式配置
│   ├── config.py                 # 全局配置
│   └── routes.py                 # 路由管理
├── main.py                       # 应用入口
├── requirements.txt              # Python 依赖
├── flet.yaml                     # Flet 打包配置
└── README.md                     # 项目文档
```

## ✨ 主要特性

- 📱 **响应式布局**：自动适配手机、平板、PC 端
- 🎨 **Material Design**：现代化的 UI 设计
- 🔄 **路由系统**：完整的页面导航和历史记录管理
- 🛠️ **工具集合**：
  - 计数器
  - 计算器
  - 单位转换
  - 设置页面
- 👤 **个人中心**：用户信息和功能菜单

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Flet 0.80.5

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行应用

```bash
python main.py
```

## 📱 响应式说明

| 设备类型 | 屏幕宽度 | 导航方式 | 网格列数 |
|---------|---------|---------|---------|
| 移动端 | < 600px | 底部导航栏 | 1 列 |
| 平板端 | 600-1200px | 底部导航栏 | 2 列 |
| PC 端 | ≥ 1200px | 侧边导航栏 | 3 列 |

## 🏗️ 架构设计

### 核心组件

1. **Router** (`routes.py`)
   - 路由管理
   - 导航历史
   - 响应式布局切换

2. **UnifiedNavigationBar** (`components/unified_nav.py`)
   - 统一的导航接口
   - 自动适配移动端/PC 端

3. **ResponsiveConfig** (`utils/responsive.py`)
   - 设备类型检测
   - 响应式参数配置

4. **BasePage** (`features/base_page.py`)
   - 所有页面的基类
   - 提供响应式容器方法

### 页面模块

- **Home 模块** (`features/home/`)
  - 主页工具列表
  - 各工具子页面

- **Mine 模块** (`features/mine/`)
  - 个人中心页面

## 🔧 开发指南

### 添加新页面

1. 在 `features/home/` 或 `features/mine/` 下创建新页面文件
2. 继承 `BasePage` 类
3. 实现 `build()` 方法
4. 在 `routes.py` 中注册路由

### 示例代码

```python
from src.features.base_page import BasePage

class NewPage(BasePage):
    def build(self):
        return ft.Column([
            ft.AppBar(title=ft.Text("新页面")),
            ft.Text("内容")
        ])
```

## 📦 打包发布

### Android APK

```bash
flet build apk
```

### iOS IPA

```bash
flet build ipa
```

### Web 应用

```bash
flet build web
```

## 📝 更新日志

### v1.0.0
- ✅ 初始版本发布
- ✅ 响应式布局支持
- ✅ 基础工具功能
- ✅ 路由系统完善

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 👥 作者

Your Name

---

**Happy Coding! 🎉**

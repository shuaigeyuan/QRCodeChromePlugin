# 网页二维码 Chrome 扩展

一个优雅的 Chrome 扩展，可以为当前浏览的网页生成带有网站图标的二维码。

## 功能特点

- 自动生成当前网页的二维码
- 在二维码中央优雅地嵌入网站图标
- 显示网站名称
- 精美的苹果风格界面设计
- 流畅的动画效果
- 支持复制链接和保存二维码图片
- 支持浅色/深色模式自动切换

## 项目结构

extension/
├── manifest.json        # 扩展配置文件
├── popup.html          # 弹出窗口 HTML
├── popup.js            # 弹出窗口逻辑
├── styles.css          # 样式文件
├── qrcode.min.js       # QR 码生成库
└── icons/              # 图标文件
    ├── icon16.png
    ├── icon48.png
    └── icon128.png

## 安装说明

1. 下载或克隆本项目到本地
2. 打开 Chrome 浏览器，进入扩展管理页面 (chrome://extensions/)
3. 开启右上角的"开发者模式"
4. 点击"加载已解压的扩展程序"
5. 选择本项目的目录

## 使用方法

1. 点击浏览器工具栏中的扩展图标
2. 扩展会自动生成当前页面的二维码
3. 可以点击二维码进行保存
4. 可以点击链接进行复制

## 技术栈

- HTML5
- CSS3 (Flexbox, Grid, 动画)
- JavaScript (ES6+)
- Chrome Extension API
- qrcode.js 库

## 开发相关

### 本地开发

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/web-qrcode.git
```

2. 安装依赖：
```bash
cd web-qrcode
npm install
```

3. 在 Chrome 扩展管理页面加载项目目录

### 构建发布

```bash
npm run build
```

构建后的文件将生成在 `dist` 目录中

## 浏览器兼容性

- Chrome 88+
- Edge 88+ (基于 Chromium)

## 注意事项

- 扩展需要 `activeTab` 权限来
# 心形弹窗提示程序 💖

一个浪漫的心形弹窗提示程序，弹窗会组成爱心形状并持续显示动画效果。

## ✨ 功能特点

- 💖 弹窗自动组成爱心形状
- 🎨 随机文字和粉色系背景色
- ✨ 平滑的移动动画效果
- 🎯 从中心向外发射弹窗
- 🛑 左下角停止按钮

## 🚀 使用方法

### 直接运行Python脚本

```bash
python demo.py
```

### 打包为Windows exe

详细步骤请查看：[GitHub打包步骤.md](GitHub打包步骤.md)

快速步骤：
1. 将项目上传到GitHub
2. 在Actions页面触发打包
3. 下载打包好的exe文件

## 📋 系统要求

- Python 3.7+
- tkinter（Python标准库）

## 📁 文件说明

- `demo.py` - 主程序文件
- `.github/workflows/build-windows.yml` - GitHub Actions自动打包配置
- `GitHub打包步骤.md` - 详细的GitHub打包教程

## 🎮 操作说明

1. 运行程序后，弹窗会从随机位置出现
2. 弹窗平滑移动到爱心形状的位置
3. 所有爱心弹窗显示完毕后，从中心开始向外发射弹窗
4. 发射的弹窗会逐渐缩小并在3秒后消失
5. 点击左下角的"停止"按钮可退出程序

## 📝 注意事项

- 程序会持续运行，直到点击停止按钮
- 建议在Windows电脑上测试运行
- 打包exe需要使用GitHub Actions或在Windows系统上操作


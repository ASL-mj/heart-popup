# GitHub Actions 打包 Windows exe - 详细步骤

## 准备工作

确保你有：
- ✅ GitHub账号（如果没有，访问 https://github.com 免费注册）
- ✅ 项目文件：`demo.py` 和 `.github/workflows/build-windows.yml`

---

## 步骤一：创建GitHub仓库

1. **登录GitHub**
   - 访问 https://github.com
   - 登录你的账号

2. **创建新仓库**
   - 点击右上角的 "+" 号，选择 "New repository"
   - 或直接访问：https://github.com/new

3. **填写仓库信息**
   - Repository name: `heart-popup`（或其他你喜欢的名字）
   - Description: `心形弹窗提示程序`（可选）
   - ✅ 选择 Public（公开）或 Private（私有）都可以
   - ❌ **不要**勾选 "Add a README file"（我们已有文件）
   - ❌ **不要**勾选 "Add .gitignore"
   - ❌ **不要**勾选 "Choose a license"

4. **点击 "Create repository" 创建仓库**

---

## 步骤二：上传文件到GitHub

### 方法一：使用Git命令行（推荐，适合开发者）

```bash
# 1. 进入项目目录
cd 心形弹窗提示

# 2. 初始化Git仓库（如果还没有）
git init

# 3. 添加所有文件
git add .

# 4. 提交
git commit -m "初始提交：心形弹窗提示程序"

# 5. 连接到GitHub仓库（替换YOUR_USERNAME和YOUR_REPO）
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# 6. 推送到GitHub
git branch -M main
git push -u origin main
```

### 方法二：使用GitHub网页上传（最简单，适合新手）

1. **在仓库页面点击 "uploading an existing file"**
   - 或直接访问：`https://github.com/YOUR_USERNAME/YOUR_REPO/upload`

2. **拖拽或选择文件上传**
   - 上传 `demo.py`
   - 上传 `.github/workflows/build-windows.yml`（确保路径正确！）

3. **重要：创建正确的文件夹结构**
   - 如果 `.github` 文件夹不存在，先创建它
   - 点击 "Add file" → "Create new file"
   - 文件名输入：`.github/workflows/build-windows.yml`
   - 粘贴配置文件内容

4. **提交文件**
   - 在页面底部填写 Commit message: `初始提交`
   - 点击 "Commit changes"

---

## 步骤三：触发GitHub Actions打包

### 方法一：自动触发（推送代码后）

如果你用Git命令行推送了代码，GitHub Actions会自动运行。

### 方法二：手动触发（推荐）

1. **进入Actions页面**
   - 在你的GitHub仓库页面
   - 点击顶部的 "Actions" 标签

2. **选择workflow**
   - 在左侧选择 "Build Windows EXE"

3. **手动触发**
   - 点击右上角的 "Run workflow"
   - 在弹出框中选择分支（通常是 `main` 或 `master`）
   - 点击绿色的 "Run workflow" 按钮

4. **等待打包完成**
   - 你会看到一个运行中的任务
   - 点击任务查看详细进度
   - 通常需要 2-5 分钟

---

## 步骤四：下载打包好的exe文件

1. **等待打包完成**
   - 在Actions页面，等待任务状态变为绿色的 ✓
   - 如果失败了（红色❌），点击查看错误信息

2. **下载exe文件**
   - 打包完成后，在任务页面底部找到 "Artifacts" 区域
   - 点击 "心形弹窗提示-Windows" 下载
   - 这会下载一个 `.zip` 文件

3. **解压使用**
   - 解压下载的zip文件
   - 里面就是 `心形弹窗提示.exe`
   - 可以直接在Windows电脑上运行！

---

## 常见问题

### Q1: Actions页面显示 "No workflows found"
**解决：** 检查 `.github/workflows/build-windows.yml` 文件是否正确上传

### Q2: 打包失败，显示找不到文件
**解决：** 确保 `demo.py` 在仓库根目录，不在子文件夹中

### Q3: 如何更新代码后重新打包？
**解决：** 更新 `demo.py` 后，推送到GitHub，Actions会自动重新打包

### Q4: 可以自动打包吗？
**解决：** 是的，每次推送代码到main/master分支会自动打包

### Q5: 打包需要多长时间？
**解决：** 通常 2-5 分钟，取决于GitHub服务器负载

---

## 快速检查清单

- [ ] GitHub账号已注册
- [ ] 创建了新的仓库
- [ ] 上传了 `demo.py`
- [ ] 上传了 `.github/workflows/build-windows.yml`
- [ ] 在Actions页面手动触发了workflow
- [ ] 打包成功（绿色✓）
- [ ] 下载了exe文件

---

## 需要帮助？

如果遇到问题：
1. 检查文件路径是否正确
2. 查看Actions页面的错误信息
3. 确保所有文件都已上传到GitHub

祝你打包顺利！🎉


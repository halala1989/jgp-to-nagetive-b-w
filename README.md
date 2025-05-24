# JPG 转黑白负片项目

## 项目简介
本项目包含两个主要脚本，用于从指定网站下载图片并将下载的 JPG 图片转换为黑白负片。

### `download_images.py`
该脚本用于从目标网站的帖子列表页面下载帖子及回帖中的图片。它使用 `requests` 库发送 HTTP 请求，`BeautifulSoup` 库解析 HTML 页面，并将图片保存在“图片”文件夹中。

### `image_processor.py`
该脚本用于将 `.jpg` 图片转换为黑白负片。它使用 `Pillow` 库进行图像处理，并引入 `tqdm` 库在终端显示处理进度。

## 使用方法
### 环境准备
确保你已经安装了以下 Python 库：
- `requests`
- `beautifulsoup4`
- `Pillow`
- `tqdm`

你可以使用以下命令安装这些依赖：
```bash
pip install requests beautifulsoup4 Pillow tqdm
```

### 下载图片
1. 打开 `download_images.py` 文件，将 `post_list_url` 变量替换为目标网站的帖子列表页面 URL。
2. 运行脚本：
```bash
python download_images.py
```
图片将被下载到“图片”文件夹中。

### 转换图片为黑白负片
1. 确保需要处理的 `.jpg` 图片与 `image_processor.py` 脚本在同一目录或其子目录下。
2. 运行脚本：
```bash
python image_processor.py
```
处理过程中会在终端显示进度条。

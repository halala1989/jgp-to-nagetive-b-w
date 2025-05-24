import requests
from bs4 import BeautifulSoup
import os
import re

def download_image(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"下载成功: {save_path}")
    except Exception as e:
        print(f"下载失败 {url}: {e}")

def get_images_from_post(post_url, post_folder):
    try:
        response = requests.get(post_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找所有图片标签
        img_tags = soup.find_all('img')
        
        for img in img_tags:
            img_url = img.get('src')
            if img_url:
                # 处理相对链接
                if not img_url.startswith('http'):
                    base_url = '/'.join(post_url.split('/')[:3])
                    img_url = f"{base_url}{img_url}"
                
                # 生成保存路径
                img_name = os.path.basename(img_url)
                img_name = re.sub(r'[<>:"/\\|?*]', '_', img_name)  # 替换非法文件名字符
                save_path = os.path.join(post_folder, img_name)
                
                download_image(img_url, save_path)
    except Exception as e:
        print(f"处理帖子 {post_url} 时出错: {e}")

def main():
    # 替换为目标网站的帖子列表页面 URL
    post_list_url = "https://example.com/posts"
    try:
        response = requests.get(post_list_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 假设帖子链接在 <a> 标签中，且有特定的类名
        post_links = soup.find_all('a', class_='post-link')
        
        # 创建主图片文件夹
        images_folder = "图片"
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)
        
        for link in post_links:
            post_url = link.get('href')
            if post_url:
                # 处理相对链接
                if not post_url.startswith('http'):
                    base_url = '/'.join(post_list_url.split('/')[:3])
                    post_url = f"{base_url}{post_url}"
                
                # 创建帖子文件夹
                post_name = link.text.strip()
                post_name = re.sub(r'[<>:"/\\|?*]', '_', post_name)  # 替换非法文件名字符
                post_folder = os.path.join(images_folder, post_name)
                if not os.path.exists(post_folder):
                    os.makedirs(post_folder)
                
                get_images_from_post(post_url, post_folder)
    
    except Exception as e:
        print(f"获取帖子列表时出错: {e}")

if __name__ == "__main__":
    main()
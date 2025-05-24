from PIL import Image
import os
from tqdm import tqdm

def convert_to_bw_and_invert(image_path):
    try:
        # 打开图片
        img = Image.open(image_path)
        
        # 转换为黑白图片
        bw_img = img.convert('L')
        
        # 转换为反色
        inverted_img = Image.new('L', bw_img.size)
        for x in range(bw_img.width):
            for y in range(bw_img.height):
                pixel = bw_img.getpixel((x, y))
                inverted_pixel = 255 - pixel
                inverted_img.putpixel((x, y), inverted_pixel)
        
        # 保存修改后的图片
        inverted_img.save(image_path)
        print(f"处理完成: {image_path}")
    except Exception as e:
        print(f"处理 {image_path} 时出错: {e}")

def main():
    jpg_files = []
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 遍历目录下所有 .jpg 文件
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.lower().endswith('.jpg'):
                file_path = os.path.join(root, file)
                jpg_files.append(file_path)
        for file_path in tqdm(jpg_files, desc='处理图片进度'):
                convert_to_bw_and_invert(file_path)

if __name__ == "__main__":
    main()
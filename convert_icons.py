import os
from PIL import Image, ImageDraw

def convert_svg_to_png(svg_file, png_file, size):
    # 创建一个纯色背景的图片
    img = Image.new('RGBA', (size, size), (45, 45, 45, 255))
    
    # 在背景上绘制二维码图案
    draw = ImageDraw.Draw(img)
    
    # 计算缩放比例
    scale = size / 128
    
    # 绘制白色方块
    patterns = [
        (34, 34, 58, 58),
        (70, 34, 94, 58),
        (34, 70, 58, 94),
        (70, 70, 78, 78),
        (86, 70, 94, 78),
        (70, 86, 94, 94)
    ]
    
    for x1, y1, x2, y2 in patterns:
        scaled_coords = [int(c * scale) for c in (x1, y1, x2, y2)]
        draw.rectangle(scaled_coords, fill='white')
    
    # 保存图片
    img.save(png_file, 'PNG')

# 创建 icons 目录（如果不存在）
if not os.path.exists('icons'):
    os.makedirs('icons')

# 需要生成的尺寸
sizes = [16, 48, 128]

try:
    for size in sizes:
        output_file = f'icons/icon{size}.png'
        convert_svg_to_png('icons/icon.svg', output_file, size)
        print(f'Successfully created {output_file}')
except Exception as e:
    print(f'Error converting icons: {str(e)}')
else:
    print('All icons were successfully converted!') 
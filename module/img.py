'''
画像に関するモジュール
'''
from PIL import Image

def compress_image(input_path, output_path, quality=85):
    '''
    画像をロード、圧縮して保存する
    Args:
        input_path: 圧縮する画像のパス
        output_path: 圧縮後の画像のパス
        quality: 圧縮品質(0-100)
    Returns:
        None
    '''
    try:
        img = Image.open(input_path)#ほとんどの画像ファイル形式をロード可能
        print(f'Image loaded successfully:{input_path}')
        img.save(output_path, optimize=True, quality=quality)
        print(f'quality:{quality}, Image saved successfully:{output_path}')
    except Exception as e:
        print(f'Error: {e}')
    except FileNotFoundError:
        print(f'File not found: {input_path}')

def main():
    print('img.main')

if __name__ == '__main__':
    main()
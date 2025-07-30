import module.webcam as webcam

def main():
    result_list = webcam.detect_available_cameras(3)
    print(f'オープン可能カメラID:{result_list}')
    #カメラ画像を表示
    #webcam.show_camera_stream(result_list[0])


if __name__ == '__main__':
    main()



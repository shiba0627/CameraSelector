import webcam

def main():
    consecutive_failures = 0#失敗カウント用
    max_consecutive_failures = 3#この回数連続で失敗したら終了
    result_list = []
    for i in range(999):
        if webcam.try_to_open_camera(i):
            result_list.append(i)
            consecutive_failures = 0
        else:
            consecutive_failures += 1
        if consecutive_failures >= max_consecutive_failures:
            break

    print(f'オープン可能カメラID:{result_list}')
    #カメラ画像を表示
    webcam.show_camera_stream(result_list[0])


if __name__ == '__main__':
    main()



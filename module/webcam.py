'''
WEBカメラに関するモジュール
'''
#__all__ = ['try_to_open_camera', 'show_camera_stream']
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
CAM_ID = 2
def try_to_open_camera(camera_id:int) -> bool:
    """
    指定されたカメラIDがオープン可能かどうかを確認する

    Args:
        camera_id (int): 使用するカメラのID

    Returns:
        bool: カメラが正常にオープンできた場合は True、失敗した場合は False
    """
    cap = cv2.VideoCapture(camera_id)
    ret, frame = cap.read()
    cap.release()
    if ret == True:
        return True
    return False

def show_camera_stream(cam_id:int):
    '''
    webカメラから取得した画像を表示
    Args:
        cam_id: カメラのID
    Returns:
        None

    'q'で終了
    '''
    cap = cv2.VideoCapture(cam_id)
    while(cap.isOpened()):#キャプチャがオープンしているなら
        ret, frame = cap.read()
        if ret == True:#フレームがあるなら
            cv2.imshow(f'ID:{cam_id}', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):#'q'が押されたら
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

def detect_available_cameras(max_consecutive_failures = 3) -> list[int]:
    '''
    使用可能なカメラのIDを検出
    
    Args:
        max_consecutive_failures: 探索終了条件：連続で失敗した回数
    Returns:
        list[int]: 使用可能なカメラのIDリスト
    '''
    consecutive_failures = 0#失敗カウント用
    result_list = []
    for i in range(999):
        if try_to_open_camera(i):
            result_list.append(i)
            consecutive_failures = 0
        else:
            consecutive_failures += 1
        if consecutive_failures >= max_consecutive_failures:
            break
    return result_list

def main():
    pass

if __name__ == '__main__':
    main()

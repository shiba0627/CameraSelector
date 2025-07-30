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

def main():
    pass

if __name__ == '__main__':
    main()

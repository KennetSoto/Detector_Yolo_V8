import cv2

#teste vara verificar se a câmera está funcionando e qual o índice dela
def check_cameras():
    index = 0
    available_cameras = []
    while index < 10:  
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            available_cameras.append(index)
            cap.release()
        index += 1
    return available_cameras

available_cameras = check_cameras()
print("Câmeras disponíveis:", available_cameras)









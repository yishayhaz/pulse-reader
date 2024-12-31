import cv2
import numpy as np

def read_video(input_video_path):
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        raise Exception("Path {} is not a valid video file".format(input_video_path))
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    data = []

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret:
            cv2.imshow("frame", frame)
            cv2.waitKey(1)
        else:
            break

        # calculate the avarage color of the frame
        avg_color_per_row = np.average(frame, axis=0)

        # calculate the avarage color of the frame
        avg_color = np.average(avg_color_per_row, axis=0)

        # print the avarage color of the frame
        data.append(avg_color.tolist())

    cap.release()
    cv2.destroyAllWindows()

    return data, fps
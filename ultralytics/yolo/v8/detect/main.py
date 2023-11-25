import cv2
import numpy as np

data = {
'004': {'areas': [[[0.3536458333333333, 0.9694444444444444], [0.296875, 0.4425925925925926], [0.5197916666666667, 0.4074074074074074], [0.9604166666666667, 0.7138888888888889]], [[0.9630208333333333, 0.7092592592592593], [0.5203125, 0.4046296296296296], [0.6203125, 0.39166666666666666], [0.9989583333333333, 0.587037037037037]]]},
}

def coord(image_name):
    image_path = f'{image_name}.jpg'
    video = cv2.VideoCapture(image_path)
    if image_name in data:
        areas = data[image_name]['areas']

        all_points = np.array([[int(x * video.get(3)), int(y * video.get(4))] for area in areas for x, y in area])
        x, y, w, h = cv2.boundingRect(all_points)

        bottom_left = (x, y + h)
        top_right = (x + w, y)
        print(bottom_left)
        return bottom_left, top_right
    else:
        print(f"Данные для изображения '{image_name}' не найдены в переменной data.")

import cv2
import numpy as np

data = {
'1': {'areas': [[[0.29140625, 0.4673611111111111], [0.4234375, 0.4270833333333333], [0.65234375, 0.6027777777777777], [0.33984375, 0.8263888888888888]], [[0.4234375, 0.4270833333333333], [0.50625, 0.3909722222222222], [0.769140625, 0.5055555555555555], [0.65234375, 0.6027777777777777]]]},
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

import cv2
import numpy as np

# Захват видеопотока
video_capture = cv2.VideoCapture('videos/3.mp4')  # путь к видеофайлу

# Фоновый субтрактивный объект
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=25, detectShadows=False)

# Комбинирование Собеля с Лапласианом
def combined_edge_detection(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Оператор Собеля с ядром 3
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobel_x, sobel_y)

    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    combined = cv2.addWeighted(sobel_combined, 0.5, laplacian, 0.5, 0)
    _, thresholded = cv2.threshold(combined, 100, 255, cv2.THRESH_BINARY)   # с параметром thresh можно поиграться
    return np.uint8(thresholded)

while True:
    ret, frame = video_capture.read()           # ret: Bool удачно обработан кадр или нет, frame - сам кадр
    if not ret:
        print("No frame detected")              # Лучше кинуть Exception, но пусть будет так
        break

    # Вычетание фона
    fgmask = fgbg.apply(frame)

    # Медианное размытие
    fgmask = cv2.medianBlur(fgmask, 5)

    # Применение комбинированного детектора краев
    edges = combined_edge_detection(frame)

    # Комбинируем результат с маской
    combined_mask = cv2.bitwise_and(edges, fgmask)

    # Нахождение контуров
    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Рисуем контуры
    for contour in contours:
        if 50 < cv2.contourArea(contour) < 1000:        # Фильтруем слишком маленькие и большие объекты
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Отображение результатов
    cv2.imshow('Frame with Contours', frame)
    cv2.imshow('Foreground Mask', fgmask)
    cv2.imshow('Combined Edges', edges)

    # Выход из окна по нажатию кнопки 'Q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
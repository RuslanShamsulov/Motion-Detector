# Motion Detection Script
.py скрипт представляет собой простой скрипт для обнаружения движущихся объектов на статическом/динамическом фоне. Основная задача скрипта — выделение контуров движущихся объектов с использованием методов компьютерного зрения и фильтрации.

## Описание проекта
Скрипт использует следующие инструменты:

OpenCV — библиотека для обработки изображений и видео, используемая для вычитания фона, фильтрации и работы с изображениями.
NumPy — библиотека для работы с многомерными массивами и матрицами, которая обеспечивает эффективные числовые операции.

## Установка и запуск проекта
# Шаг 1: Клонирование репозитория
```
 git clone https://github.com/RuslanShamsulov/Motion-Detector.git 
 cd motion-detection
```
# Шаг 2: Создание виртуального окружения
Рекомендуется создать виртуальное окружение, чтобы изолировать зависимости проекта:

На Windows:
```
 python -m venv venv 
 .\venv\Scripts\activate
```

На macOS/Linux:
```
 python3 -m venv venv 
 source venv/bin/activate
```

# Шаг 3: Установка зависимостей
Установите необходимые библиотеки, указанные в файле requirements.txt:
` pip install -r requirements.txt `


# Шаг 4: Запуск скрипта
` python motion_detection.py `

По умолчанию скрипт будет использовать тестовые видео, которые находятся в папке /videos. При желании добавьте в эту папку свои видео и измените путь в следущей строке:
` video_capture = cv2.VideoCapture('Video_path')  # путь к видеофайлу `

# Шаг 5: Пример работы
![Frame with Contours 2024-09-10 15-08-33](https://github.com/user-attachments/assets/1174f291-9ac2-4829-95cc-a84b5012ba9b)
![Frame with Contours 2024-09-10 15-08-57](https://github.com/user-attachments/assets/5d4b4651-2390-4dfd-b5cd-f8088d7b4395)
![Frame with Contours 2024-09-10 15-07-49](https://github.com/user-attachments/assets/b06d1ca2-c4ae-41db-acff-420416a4cf89)




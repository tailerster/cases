{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np #Библиотека, необходимая для удобного представления многомерных массивов\n",
    "from PIL import Image # Библиотека для работы с растровой графикой\n",
    "from requests import get # Библиотека для составления HTTP протоколов\n",
    "from bokeh.plotting import figure, show, output_notebook #Bokeh - Библиотека для визуализации данных\n",
    "from bokeh.layouts import layout\n",
    "from bokeh.palettes import gray"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "def image_dither(path, black='#000000', white='#ffffff'):\n",
    "    image_rgb = read_image(path) #Читаем файл в Red Green Blue\n",
    "    image_gray = grayscale(image_rgb) #Переделываем цвета в оттенки серого\n",
    "    image_bw = floyd_steinberg(image_gray) #Алгоритм Флойд-Стойнберг\n",
    "\n",
    "    show(layout([[ #Отоброжаем изображения на экране\n",
    "        plot(image_gray, palette=gray(256)),\n",
    "        plot(image_bw, palette=[black, white])        \n",
    "    ]]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "def read_image(path, size=400): # Считываем картинку и преобразуем его в удобном виде, для представления на экране \n",
    "    \n",
    "    image = Image.open(path)\n",
    "    \n",
    "    width, height = image.size # Кортеж [x, y]\n",
    "    width, height = size, int(size * height / width)\n",
    "    image = image.resize((width, height), Image.ANTIALIAS)\n",
    "    \n",
    "    data = image.getdata()\n",
    "    assert data.bands in [3, 4], 'RGB or RGBA image is required'\n",
    "    \n",
    "    raw = np.array(data, dtype=np.uint8) #Представляем массив в привычном математическом виде unsigned [0, 255]\n",
    "    return raw.reshape(height, width, data.bands)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "def grayscale(image):#Преобразование в оттенки серого цвета\n",
    "    height, width, _ = image.shape #Считываем изменённое под удобный формат изображение в RGB формате\n",
    "    \n",
    "    image = np.array(image, dtype=np.float32) / 255 #Вещественные числа и считываем ошибки после запятой для преобразования в серую палитру\n",
    "    image = image[:, :, 0] * .21 + image[:, :, 1] * .72 + image[:, :, 2] * .07 #Срез [255, 255, 255]\n",
    "    \n",
    "    return image.reshape(height, width)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "def floyd_steinberg(image):#Алгоритм Флойда-Стойнберга\n",
    "    image = image.copy()\n",
    "    distribution = np.array([7, 3, 5, 1], dtype=float) / 16 #Список значений для передачи части ошибки в другие пиксели\n",
    "    u = np.array([0, 1, 1, 1]) \n",
    "    v = np.array([1, -1, 0, 1])\n",
    "    \n",
    "    for y in range(image.shape[0] - 1): #Округляем в цикле до черной точки или белой (>128), (<128)\n",
    "        for x in range(image.shape[1] - 1):\n",
    "            value = np.round(image[y, x]) #Округляем x и y у пикселя\n",
    "            error = image[y, x] - value #Получение ошибки тонирования (артефакт)\n",
    "            image[y, x] = value #Передаём пикселю округлённые значения\n",
    "            image[y + u, x + v] += error * distribution #Передаём часть ошибки вправо и вниз\n",
    "            \n",
    "    image[:, -1] = 1 \n",
    "    image[-1, :] = 1\n",
    "\n",
    "    return image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "def plot(image, palette):\n",
    "    y, x = image.shape #Получаем размеры изображения\n",
    "\n",
    "    plot = figure(x_range=(0, x), y_range=(0, y), plot_width=x, plot_height=y) #Создаём поле фигуры с размерами изображения холста\n",
    "    plot.axis.visible = False #Делает фигуру видимой\n",
    "    plot.toolbar_location = None #Убирает toolbar\n",
    "    plot.min_border = 0\n",
    "    plot.image([np.flipud(image)], x=0, y=0, dw=x, dh=y, palette=palette) #Отрисовывает картинку на layout\n",
    "    \n",
    "    return plot"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Запуск программы"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "image_dither('cute.jpg', white='#ffffff')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "image_dither('pasha_the_cat.jpg', white='#ffebcd')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "image_dither('pasha_cute.jpg', white='#f0f0ff')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

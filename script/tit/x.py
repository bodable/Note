import os
import PIL
import numpy
import matplotlib

matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import time

from matplotlib.animation import FuncAnimation

# 是否需要进行图片更新
need_update = True

def get_screen_image():
    # 截取手机当前图片
    os.system('adb shell screencap -p /sdcard/screen.png')
    # 拉取到PC端
    os.system('adb pull /sdcard/screen.png')
    # 将图像转成数组返回
    return numpy.array(PIL.Image.open('screen.png'))



def update_screen(frame):
    global need_update
    if need_update:
        time.sleep(1)
        axes_image.set_array(get_screen_image())
        # 已刷新，设置为false
        need_update = False
    return axes_image,

def click(x,y):
	os.system("adb shell input tap 1768 918 ")


figure = plt.figure()

def main():
	axes_image = plt.imshow(get_screen_image(), animated=True)
	ani = FuncAnimation(figure, update_screen,interval=50, blit=True)
	plt.show()
	return True

main()



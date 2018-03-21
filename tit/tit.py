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


def jump_to_next(point1, point2):
    x1, y1 = point1;
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    # 计算按压指令和按压时长
    os.system("adb shell input touchscreen swipe 320 410 320 410 %d" % (distance * 1.35))


def on_clack(event, coor=[]):
    global need_update
    coor.append((event.xdata, event.ydata))
    if len(coor) == 2:
        # 执行跳步指令
        jump_to_next(coor.pop(), coor.pop())
    # 进行图片刷新
    need_update = True


def update_screen(frame):
    global need_update
    if need_update:
        time.sleep(2)
        axes_image.set_array(get_screen_image())
        # 已刷新，设置为false
        need_update = False
    return axes_image,


figure = plt.figure()
axes_image = plt.imshow(get_screen_image(), animated=True)
figure.canvas.mpl_connect('button_press_event', on_clack)
# 定时更新
ani = FuncAnimation(figure, update_screen, interval=50, blit=True)
plt.show()

# encoding: utf-8
# 终端显示器（瞎做的
# Made by Enderman114514

from typing import Union

_CHAR: str = '\u2584'

def clear():
    """
    清除终端
    :return: None
    """
    print("\033[2J", flush=False)

def setCursor(show: bool = False):
    """
    显示/隐藏光标
    :param show: 是否显示光标
    :return: None
    """
    print(f"\033[?25{'h' if show else 'l'}", flush=False)

class Color:
    """
    颜色类
    """
    _red: int = 0
    _green: int = 0
    _blue: int = 0

    def __init__(self, r: int, g: Union[int, None] = None, b: Union[int, None] = None):
        """
        初始化
        :param r: 颜色值（如0xffffff）或红色量
        :param g: 绿色量
        :param b: 蓝色量
        """
        if g is None and b is None: # 若只有1个参数
            r = min(max(0x000000, r), 0xffffff)
            self.r = r // 256 // 256
            self.g = r // 256 % 256
            self.b = r % 256
        elif b is None:             # 若有2个参数
            raise TypeError("__init__() missing 1 required positional argument: 'b'")
        else:                       # 若有3个参数
            self.r = min(max(0, r), 255)
            self.g = min(max(0, g), 255)
            self.b = min(max(0, b), 255)

    def __str__(self):
        """
        返回颜色的终端表达形式
        :return: 颜色的终端表达形式
        """
        return f"{self.r};{self.g};{self.b}"

    def __repr__(self):
        """
        返回颜色的repr形式
        :return: 颜色的repr形式
        """
        return f"Color({self.r}, {self.g}, {self.b})"

    def __int__(self):
        """
        转为颜色值
        :return: 颜色值
        """
        return self.r * 256 * 256 + self.g * 256 + self.b

CLEAR:           int = 0   # 棍母
BLACK_16:        int = 30  # 黑色（16色模式）
RED_16:          int = 31  # 红色（16色模式）
GREEN_16:        int = 32  # 绿色（16色模式）
YELLOW_16:       int = 33  # 黄色（16色模式）
BLUE_16:         int = 34  # 蓝色（16色模式）
PURPLE_16:       int = 35  # 紫色（16色模式）
CYAN_16:         int = 36  # 青色（16色模式）
WHITE_16:        int = 37  # 白色（16色模式）
DARK_16:         int = 90  # 深灰色（16色模式）
LIGHT_RED_16:    int = 91  # 浅红色（16色模式）
LIGHT_GREEN_16:  int = 92  # 浅绿色（16色模式）
LIGHT_YELLOW_16: int = 93  # 浅黄色（16色模式）
LIGHT_BLUE_16:   int = 94  # 浅蓝色（16色模式）
LIGHT_PURPLE_16: int = 95  # 浅紫色（16色模式）
LIGHT_CYAN_16:   int = 96  # 浅青色（16色模式）
LIGHT_16:        int = 97  # 浅灰色（16色模式）
BLACK:         Color = Color(0  , 0  , 0  )  # 黑色
RED:           Color = Color(255, 0  , 0  )  # 红色
GREEN:         Color = Color(0  , 255, 0  )  # 绿色
YELLOW:        Color = Color(255, 255, 0  )  # 黄色
BLUE:          Color = Color(0  , 0  , 255)  # 蓝色
PURPLE:        Color = Color(255, 0  , 255)  # 紫色
CYAN:          Color = Color(0  , 255, 255)  # 青色
WHITE:         Color = Color(255, 255, 255)  # 白色
DARK:          Color = Color(85 , 85 , 85 )  # 深灰色
LIGHT_RED:     Color = Color(255, 128, 128)  # 浅红色
LIGHT_GREEN:   Color = Color(128, 255, 128)  # 浅绿色
LIGHT_YELLOW:  Color = Color(255, 255, 128)  # 浅黄色
LIGHT_BLUE:    Color = Color(128, 128, 255)  # 浅蓝色
LIGHT_PURPLE:  Color = Color(255, 128, 255)  # 浅紫色
LIGHT_CYAN:    Color = Color(128, 255, 255)  # 浅青色
LIGHT:         Color = Color(170, 170, 170)  # 浅灰色


def putText(content: object, x: int, y: int, fore: Color, back: Color):
    """
    打印彩色文字
    :param content: 请输入文本
    :param x:       打印的x坐标
    :param y:       打印的y坐标
    :param fore:    文字颜色
    :param back:    背景颜色
    :return:        None
    """
    print(f"\033[{y + 1};{x + 1}H\033[38;2;{fore}m\033[48;2;{back}m{content.__str__()}\033[0m",
          end="", flush=False)


class _PairPixels_16:
    """
    像素对
    为兼容而保留（部分终端不支持真彩色）
    """
    pixel1: int = BLACK_16
    pixel2: int = BLACK_16

    def __init__(self, p1, p2):
        """
        初始化
        :param p1: 上方像素的颜色
        :param p2: 下方像素的颜色
        """
        self.pixel1 = p1
        self.pixel2 = p2

    def draw(self, x: int, y: int):
        """
        绘制像素对
        :param x: 绘制的x坐标
        :param y: 绘制的y坐标
        :return:  None
        """
        self.pixel1 += 10
        print(f"\033[{y + 1};{x + 1}H\033[{self.pixel2};{self.pixel1}m{_CHAR}\033[0m", end="", flush=False)

    @staticmethod
    def draw2Pixels(x: int, y: int, pixel1: int, pixel2: int):
        """
        绘制像素对
        :param x:      绘制的x坐标
        :param y:      绘制的y坐标
        :param pixel1: 上方像素的颜色
        :param pixel2: 下方像素的颜色
        :return:       None
        """
        pixel1 += 10
        print(f"\033[{y + 1};{x + 1}H\033[{pixel2};{pixel1}m{_CHAR}\033[0m", end="", flush=False)


class Frame:
    """
    帧对象（其实就是一张图片
    """
    __pixels: list[list[Color]]
    def __init__(self, rows: int, cols: int, pixels: Union[list[list[Color]], Color] = BLACK):
        """
        初始化
        :param rows:   行数
        :param cols:   列数
        :param pixels: 像素列表
        """
        if isinstance(pixels, Color):
            self.__pixels = [[pixels for _ in range(cols)] for _ in range(rows)]
        if isinstance(pixels, list):
            self.__pixels = pixels

    @staticmethod
    def _drawPixel(x: int, y: int, p1: Color, p2: Color):
        """
        绘制一对像素
        :param x:  绘制的x坐标
        :param y:  绘制的y坐标
        :param p1: 上方像素的颜色
        :param p2: 下方像素的颜色
        :return:   None
        """
        print(
            f"\033[{y + 1};{x + 1}H\033[38;2;{p2}m\033[48;2;{p1}m{_CHAR}\033[0m",
            end="", flush=False
        )

    def setPixel(self, x: int, y: int, color: Union[int, Color]):
        """
        设置帧中的像素
        :param x:     像素的x坐标
        :param y:     像素的y坐标
        :param color: 像素的颜色
        :return:      None
        """
        self.__pixels[y][x] = color

    def draw(self, sx: int, sy: int):
        """
        绘制帧
        :param sx: 帧左上角的x坐标
        :param sy: 帧左上角的y坐标
        :return:   None
        """
        rows: int = len(self.__pixels)
        cols: int = len(self.__pixels[0])
        for y in range(0, rows, 2):
            row1: list[Color] = self.__pixels[y]
            row2: list[Color] = self.__pixels[y + 1] if y + 1 < rows else [BLACK] * cols
            for x in range(0, cols, 1):
                pixel1: Color = row1[x]
                pixel2: Color = row2[x]
                Frame._drawPixel(x + sx, y // 2 + sy, pixel1, pixel2)

    def drawPixel(self, x: int, y: int, sx: int, sy: int):
        """
        绘制帧中的单个像素
        :param x:  绘制的x坐标
        :param y:  绘制的y坐标
        :param sx: 像素在帧中的x坐标
        :param sy: 像素在帧中的y坐标
        :return:   None
        """
        if y % 2 == 0:
            row1: list[Color] = self.__pixels[y - 1]
            row2: list[Color] = self.__pixels[y]
        else:
            row1: list[Color] = self.__pixels[y]
            row2: list[Color] = self.__pixels[y + 1]
        Frame._drawPixel(x + sx, y // 2 + sy, row1[x], row2[x])

    @staticmethod
    def convertImage(path: str, scale: tuple[float, float] = (0.0, 0.0)) -> "Frame":
        """
        将一张图片转为帧（需要PIL与Numpy）
        :param path:  图片位置
        :param scale: 缩放比例
        :return:      该图片的帧
        """
        try:
            from PIL import Image
            import numpy as np

            image: Image = Image.open(path).convert("RGB")
            width, height = image.size

            if scale[0] < 0.000001:   scale = (1 / 80, scale[1])
            if scale[1] < 0.000001:   scale = (scale[0], 1 / 80)
            n_width, n_height = round(scale[0] * width), round(scale[1] * height)

            image = image.resize((n_width, n_height))
            pixels = np.asarray(image)
            frame = Frame(n_height, n_width)
            for y in range(n_height):
                for x in range(n_width):
                    frame.setPixel(x, y, Color(*pixels[y, x]))
            return frame
        except ImportError as e:
            raise ImportError(f"{e}\n\tPlease install Pillow & Numpy to use `printImage()`.")


if __name__ == '__main__':
    # 测试项
    _16_COLOR_TEST   = 1
    _RGB_COLOR_TEST  = 1
    _HEX_COLOR_TEST  = 1
    _COLOR_TEXT_TEST = 1
    _IMAGE_SHOW_TEST = 1

    clear()
    setCursor(False)

    # 16色测试
    if _16_COLOR_TEST:
        _PairPixels_16.draw2Pixels(0, 0, BLACK_16, DARK_16)
        _PairPixels_16.draw2Pixels(1, 0, RED_16, LIGHT_RED_16)
        _PairPixels_16.draw2Pixels(2, 0, GREEN_16, LIGHT_GREEN_16)
        _PairPixels_16.draw2Pixels(3, 0, YELLOW_16, LIGHT_YELLOW_16)
        _PairPixels_16.draw2Pixels(4, 0, BLUE_16, LIGHT_BLUE_16)
        _PairPixels_16.draw2Pixels(5, 0, PURPLE_16, LIGHT_PURPLE_16)
        _PairPixels_16.draw2Pixels(6, 0, CYAN_16, LIGHT_CYAN_16)
        _PairPixels_16.draw2Pixels(7, 0, WHITE_16, LIGHT_16)
        input(); clear()

    # 真彩色设置
    if _RGB_COLOR_TEST:
        _colors: Frame = Frame(512, 768)
        _red: int = 0
        _green: int = 0
        _blue: int = 0
        _light: int = 0
        for _x in range(768):
            for _y in range(512):
                _colors.setPixel(_x, _y, Color(_red, _green, _blue))
                if _y < 256:
                    if _x <= 256:
                        _red = int(max(0, 256 - _x) * (255 - _light) / 255 + _light)
                        _green = int(min(_x, 255) * (255 - _light) / 255 + _light)
                        _blue = _light
                    if 256 < _x <= 512:
                        _red = _light
                        _green = int(max(0, 512 - _x) * (255 - _light) / 255 + _light)
                        _blue = int(min(_x - 256, 255) * (255 - _light) / 255 + _light)
                    if _x > 512:
                        _red = int(min(_x - 512, 255) * (255 - _light) / 255 + _light)
                        _green = _light
                        _blue = int(max(0, 768 - _x) * (255 - _light) / 255 + _light)
                    _light = 255 - _y
                else:
                    if _x <= 256:
                        _red = int(max(0, 256 - _x) * (_light / 255))
                        _green = int(min(_x, 255) * (_light / 255))
                        _blue = 0
                    if 256 < _x <= 512:
                        _red = 0
                        _green = int(max(0, 512 - _x) * (_light / 255))
                        _blue = int(min(_x - 256, 255) * (_light / 255))
                    if _x > 512:
                        _red = int(min(_x - 512, 255) * (_light / 255))
                        _green = 0
                        _blue = int(max(0, 768 - _x) * (_light / 255))
                    _light = 511 - _y
        _colors.draw(0, 0)
        input(); clear()

    # 16进制颜色
    if _HEX_COLOR_TEST:
        _c1: Color = Color(0x5bbcf4)  #5bbcf4
        _c2: Color = Color(0x7bd4ff)  #7bd4ff
        _c3: Color = Color(0x43a7e1)  #43a7e1
        _paint: Frame = Frame(8, 8, [
            [_c1, _c1, _c1, _c1, _c1, _c1, _c1, _c1],
            [_c1, _c2, _c2, _c2, _c2, _c2, _c2, _c1],
            [_c1, _c2, _c3, _c2, _c2, _c3, _c2, _c1],
            [_c1, _c2, _c3, _c2, _c2, _c3, _c2, _c1],
            [_c1, _c2, _c3, _c2, _c2, _c3, _c2, _c1],
            [_c1, _c2, _c2, _c2, _c2, _c2, _c2, _c1],
            [_c1, _c2, _c2, _c2, _c2, _c2, _c2, _c1],
            [_c1, _c1, _c1, _c1, _c1, _c1, _c1, _c1],
        ])
        _paint.draw(0, 0)
        input(); clear()

    # 彩色文本测试
    if _COLOR_TEXT_TEST:
        putText("Colormatic Text", 0, 0, Color(0x114514), Color(0x19, 198, 0x10))
        input(); clear()

    # 图像显示
    if _IMAGE_SHOW_TEST:
        _img: Frame = Frame.convertImage("./sanlian.png", (1, 1))
        _img.draw(0, 0)
        input(); clear()

        _img: Frame = Frame.convertImage("./青秀一中.jpg", (3 / 4, 3 / 4))
        _img.draw(0, 0)
        input(); clear()

        _img: Frame = Frame.convertImage("./swell.png", (1 / 2, 1 / 2))
        _img.draw(0, 0)
        input(); clear()

setCursor(True)
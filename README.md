## 介绍&emsp;Introduction

这个程序可以在终端打印图片和彩色文字，灵感来源于（忘了是谁）制作的在终端运行的Minecraft。

This program can print images and colored text in the terminal. 
I have inspired by a youtuber who made the Minecraft in terminal.

> 注：这个程序一开始只是Enderman114514为了在终端播放*Bad Apple*然后在同学们面前装13所作的 **οωο**\
> Note: I made it just to play _Bad Apple_ in terminal and show off to my classmate at first

---

## 安装&emsp;Installation

将`displayer.py`直接放入`<Python路径>/Lib/site-packages`或项目根目录中即可，或者在导入该程序前添加下面的代码。

Put `displayer.py` into `<PythonPath>/Lib/site-packages` or the project root directories directly, or add the following scripts before importing the program.

```python
import sys
sys.path.append("<displayer.py路径|The path of displayer.py>")
```

若需要完整功能，还须安装`PIL`与`Numpy`库。

You also need to install the `PIL` and the `Numpy` libraries.

```shell
pip install pillow==9.4.0
pip install numpy==2.0.2
```

---

## 使用方法&emsp;Usage

这个程序非常地简单（~~简单到你可以自己手搓一个~~），主要通过`Frame`类打印图片，`putText`方法打印彩色文字。

This program is so simple ~~that you can make it by yourself~~. The main usages are printing images by class `Frame`
and printing colored text by method `putText`.

### 方法表 Method Table

| 类/方法&emsp;Class/Method                                                 | 描述&emsp;Description                                           |
|------------------------------------------------------------------------|---------------------------------------------------------------|
| `clear()`                                                              | 清除终端&emsp;Clear the terminal                                  |
| `setCursor(show: bool)`                                                | 设置光标显示模式&emsp;Set display mode of the cursor                  |
| `putText(content: object, x: int, y: int, fore: Color, back: Color)`   | 打印彩色文字&emsp;Print colored text                                |
| `Color(r: int, g: Union[int, None], b: Union[int, None])`              | 颜色&emsp;Color                                                 |
| `Frame(rows: int, cols: int, pixels: Union[list[list[Color]], Color])` | 帧（图片）&emsp;Frame(Image)                                       |
| `Frame.setPixel(x: int, y: int, color: Union[int, Color])`             | 设置帧中的像素&emsp;Set pixels in the frame                          | 
| `Frame.draw(sx: int, sy: int)`                                         | 绘制帧&emsp;Draw the whole frame                                 |
| `Frame.drawPixel(x: int, y: int, sx: int, sy: int)`                    | 绘制帧中的单个像素&emsp;Draw a pixel in the frame                      |
| `Frame.convertImage(path: str, scale: tuple[float, float]) -> Frame`   | 将一张图片转为帧（静态方法）&emsp;Convert an image to frame (Static method) |

*注：方法的参数说明可以去看源文件；`_PairPixels_16`类已废弃；`Frame.convertImage`需要`PIL`库与`Numpy`库。*

*Note: You can view the source file to get the descriptions of parameters; Class `_PairPixels_16` is obsolete; `Frame.convertImage` require the `PIL` and the `Numpy` libraries.*

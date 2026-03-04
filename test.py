import numpy as np
from PIL import Image

img = Image.open('Lena.png')  # 加载图像
img_array = np.array(img)  # 将图像转换为Numpy数组
print(img_array.shape)  # 输出图像的形状 (高度, 宽度, 通道数)
red_meow_arr = img_array[:, :, 0]  # 提取红色通道
red_meow = Image.fromarray(red_meow_arr)  # 将红色通道数组转换回图像
red_meow.save('new_Lena.png')  # 保存红色通道图像
print(red_meow_arr.shape)  # 输出红色通道图像的形状 (高度, 宽度)

cropped_img_arr = img_array[100:400, 325:-100, :]  # 截取左上角100x100的区域，并保留所有通道
cropped_img = Image.fromarray(cropped_img_arr)  # 将截取的区域转换回图像
cropped_img.save('cropped_Lena.png')  # 保存截取的图像
print(cropped_img_arr.shape)  # 输出截取的图像的形状 (300, 475, 3)

squashed_img_arr = img_array[::2, :, :]  
squashed_img = Image.fromarray(squashed_img_arr)  # 将截取的区域转换回图像
squashed_img.save('squashed_Lena.png')
print(squashed_img_arr.shape)  # 输出压缩后的图像的形状 (256, 512, 3)

reversed_img_arr = img_array[:, ::-1, :]  
reversed_img = Image.fromarray(reversed_img_arr)  # 将反转后的数组转换回图像
reversed_img.save('reversed_Lena.png')  # 保存反转后的图像
print(reversed_img_arr.shape)  # 输出反转后的图像的形状 (512, 512, 3)
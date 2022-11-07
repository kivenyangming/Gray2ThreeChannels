在常规的监控相机中红外探测器送出来的是16位的单通道图像,因为要送显才被转化成8位单通道。看见8位的单通道，我不免想起了灰度图（8位单通道图像），查阅
资料文献有如下结论：

1. 红外图象 是获取物体红外光的强度，而成的图象
2. 灰度图象 是获取物体可见光的强度
3. 对于数据格式，是一样的，都是单通道图象
    在查看监控的红外图像与自己转换的灰度图可以发现它们大体相同。

## 图像转换
由于红外图象是获取物体红外光的强度，而成的图象，灰度图象是获取物体可见光的强度。他们都是单通道的灰度图，那么我们在无法采集那么多的
红外图像时，我们可以将已有的三通道图像进行转化为单通道的灰度图，保持灰度图图像内容再扩充到三通道，那么这样我们就可以有了大量的“红外状态下的图像”

在这里我们采用opencv进行图像的读取与转化为灰度图,这样我们就有了初步的灰度图，
```commandline
src = cv2.imread("rgb.jpg")
gray_src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
```
但是我们在训练的时候往往是需要将数据集放在一起进行训练的，数据集的内的图像格式也是需要保持一致，那么我们就需要将灰度图的单通道扩充到三通道，
在这个里面扩充后还不能影响到图像的内容。在这里我们借助 numpy 将opencv转化为单通道图像扩充到三通道状态,后面再存储到本地。
```commandline
ThreeChannels = np.stack((gray_src,) * 3, axis=-1)
```
## 批量操作
在实际应用中我们往往是需要进行批量操作：对三通道图像转灰度图，然后对灰度图扩充到三通道状态。转换完了之后目标的位置并没有得改变，那么可以对之前的标签文件
一样是可以重复利用的，后续我们就需要对图像和标签文件进行重命名处理（在这里我们主要进行图像转换的操作，不进行重命名处理，关于这方面的代码大家自行google）

```commandline
def Gray2ThreeChannels(RgbImgDir, SaveImgDir):
    img_names = os.listdir(RgbImgDir)
    for img_name in tqdm(img_names):
        if img_name.lower().endswith(
                ('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
            image_path = os.path.join(RgbImgDir, img_name)
            src = cv2.imread(image_path)
            ThreeChannelsImg = gray2ThreeChannels(src)
            if not os.path.exists(SaveImgDir):
                os.makedirs(SaveImgDir)
            SaveImgPath = SaveImgDir + img_name
            cv2.imwrite(SaveImgPath, ThreeChannelsImg)
```

## 运行
git clone https://github.com/kivenyangming/Gray2ThreeChannels.git
cd Gray2ThreeChannls
vim main.py
----Line27: RgbImgDir = "./RgbImg/"  your RGBPath
----Line28:SaveImgDir = "./SaveThreeChannels/"  your SavePath

python main.py
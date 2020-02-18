#### 1. 依赖库
* numpy
* pandas
* torch
* torchvision
* matplotlib
* fastai

#### 2.机器配置
项目使用阿里云的 PAI-DSW服务，该服务配置32G 内存，M40显卡。

#### 3.训练时间

##### pytorch
每个 epoch耗时：
自定义模型    3分钟
预训练VGG_16  5分钟

##### fastai
每个 epoch耗时：
* resnet50，batchsize=64，size=224
  freeze 2.5min
  unfreeze 3.5min
* resnet50，batchsize=128，size=112
  freeze 1.7min
* resnet152，batchsize=32，size=224
  freeze 6min
  unfreeze 6min

#### 4.App 安装

安装网址：https://www.pgyer.com/OeG6?sign=&auSign=&code=
若图片不能显示，请查看 app安装.pdf
扫描二维码，使用浏览器打开网址
![436229c960a12cce67d328738c96c885](README.resources/IMG_C517A60EF8E9-1_1.jpeg)

在下面的页面输入密码 huangzhenxin2020
![e3d3ee962c87092de67125c87b0b07d2](README.resources/IMG_BE36EB3DFDAB-1.jpeg)


点击安装，安装完成后点击页面上的"未受信任的企业级开发者"的解决办法，根据提示信任证书。
![66e9ee9bd39dfddc73816b08f7e9fc6a](README.resources/IMG_597ECBA5425A-1.jpeg)

完成后运行 App。

this repo is for dl code for papers i have read.

## FAQ

0. the structure are divided into three different folders include "模型篇"， "数据集篇"， "训练篇"

1. 所有py文件都是先用ipynb进行简单的测试，然后用ipynb-py-convert生成的（ipynb调试更加方便）

2. 训练集篇是从模型篇中拷贝模型文件，再从数据集篇拷贝Dataset文件，然后放入训练篇下，希望这样的文件划分能产生一定的代码复用性

3. jupyter-lab是一个好东西，如果有更多的extension，建立起vscode那样的生态就好了

4. tensorboard启动方法：
```bash
tensorboard --logdir=<path-to-runs> --host=0.0.0.0
```
注意：tensorboard的结果不会马上渲染到页面，需要等待一会才能看到过程

5. 如何在cuda上训练：需要先将模型移到cuda上，然后将输入x和y移到cuda上
```
# for model
model.cuda() / model.to('cuda')
# tensor x, y
x = x.cuda() # 注意直接x.cuda()是不行的，需要将x.cuda()的值赋给x，对于模型可以直接cuda()
y = y.cuda() 
```
6. 关于torch和RTX3090,cudnn问题，见torch官网/get-started/locally

7. 深度学习果然还是炼丹
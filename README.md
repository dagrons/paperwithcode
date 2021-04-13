this repo is for dl code for papers i have read.

## FAQ

0. the structure are divided into three different folders include "模型篇"， "数据集篇"， "训练篇"

1. 所有py文件都是先用ipynb进行简单的测试，然后用ipynb-py-convert生成的（ipynb调试更加方便）

2. 训练集篇是从模型篇中拷贝模型文件，再从数据集篇拷贝Dataset文件，然后放入训练篇下，希望这样的文件划分能产生一定的代码复用性，包括generate_dataset.py, model.py, train.py以及scripts文件夹，其中scripts文件夹包括对数据集的划分和基本处理的代码文件

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

8. 在部署时，也要注意，state_dict保存时是save的是cuda版本，加载时也要是cuda版本，并且输入也要是cuda

9. jupyter-lab markdown下无法paste，需要改emacs键位到default

10. 在jupyter-lab中使用git
首先
```bash
pip3 install jupyterlab-git==0.30.0b1
```
然后在jupyter-lab中enable extension，然后install jupyterlab-git插件，注意前后端版本号要一致，不然无法显示git panel

11. 在jupyter中调试
```
import pdb; pdb.set_trace()
```

12. 远程文件互传，WinSCP，真的好用

13. 如果tensorx为唯一元素[x]或[[x]], 可以通过tensorx.item()取出x为python基本类型(int, float等)
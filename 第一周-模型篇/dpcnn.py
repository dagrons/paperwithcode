# %%
import torch
import torch.nn as nn
from torchsummary import summary

# %%
"""
参数解释：
1. output_channels决定了filter的个数，每个filter会产生一个channel
2. kernel_size决定了filter的形状
3. 如果要使input和ouput的大小一致，则kernel_size为奇数，且padding=kernel_size/2(下取整)，例如：kernel_size=3时，padding=kernel_size/2=1
4. conv3的目的是为了让identity的channels和x的channels保持一致
5. conv layer不对输入的图像大小做假设
6. nn.Sequential接受一个list of layers，返回他们串联的结果
7. nn.MaxPool1d(kernel_size=3, stride=2, padding=1), stride=2，则图像大小H和W应该为偶数，stride=2会造成图像缩小一半
8. nn.AvgPool1d(kernel_size=2, stride=1)会造成图像H-1,W-1

模型来源：https://ai.tencent.com/ailab/media/publications/ACL3-Brady.pdf
"""

# %%
class BasicBlock(nn.Module):
    # 256 => 256
    def __init__(self, in_channels, out_channels):
        super().__init__()
        
        self.relu = nn.ReLU()
        self.conv1 = nn.Conv1d(in_channels=in_channels, out_channels=out_channels, kernel_size=3, padding=1) 
        self.conv2 = nn.Conv1d(in_channels=out_channels, out_channels=out_channels, kernel_size=3, padding=1)
        self.conv3 = nn.Conv1d(in_channels=in_channels, out_channels=out_channels, kernel_size=1)
    
    def forward(self, x):
        identity = x
        
        out = self.relu(x)
        out = self.conv1(out)
        out = self.relu(out)
        out = self.conv2(out)
        
        if out.shape != identity.shape:
            identity = self.conv3(identity)
        
        return nn.ReLU()(out + identity)
    
class DPCNN(nn.Module):
    def __init__(self, in_channels):
        super().__init__()
        
        self.first_block = BasicBlock(in_channels, 256)
        self.repeat_blocks = self._generate_repeated_block(7)
        self.avg_pool = nn.AvgPool1d(kernel_size=2, stride=1)
        self.linear = nn.Linear(256, 9)
        
        # Kaiming He initialization
        for m in self.modules():
            if isinstance(m, nn.Conv1d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
        
    @staticmethod
    def _generate_repeated_block(num):
        layers = []
        for i in range(num):
            repeat_block = nn.Sequential(
                nn.MaxPool1d(kernel_size=3, stride=2, padding=1),
                BasicBlock(in_channels=256, out_channels=256)
            )
            layers.append(repeat_block)
            
        return nn.Sequential(*layers)
    
    def forward(self, x):
        out = self.first_block(x)
        out = self.repeat_blocks(out)
        out = self.avg_pool(out)
        out = out.view(out.shape[0], -1) # padding
        out = self.linear(out)
        
        return out


# %%
"""
summary解释：

1. channels数不变，但输入经过每一层Basic block变小
"""
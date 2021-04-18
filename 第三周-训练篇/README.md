## 参数选择
模型的训练一般要训练多个epoch，每个epoch都会吃完全部数据，一般EPOCHS选择10-20比较合适

## 模型保存
1. 保存整个module，一般不推荐，不利于部署
```python
torch.save(model, path)
```
2. 只保存参数，一般部署用
```python
torch.save(model.state_dict(), path)
model.load_state_dict(torch.load(path))
```
3. 断点训练
```python
checkpoint = {
    'model': model.state_dict(),
    'optimizer': optimizer.state_dict(),
    'epoch': epoch
}

# save checkpoints
torch.save(checkpoint, '[task_name]%[model_name]%[epoch].checkpoint')

# load checkpoint
checkpoint = torch.load('[task_name]%[model_name]%[epoch].checkpoint')
model.load_state_dict(checkpoint['model'])
optimizer.load_state_dict(checkpoint['optimizer'])

start_epoch = checkpoint['epoch'] + 1
for ep in range(start_epoch, EPOCHS):
    ... # resume training
```

4. 模型命名规则：[task_name]%[model_name]%[epoch].pth or [task_name]%[model_name]%best.pth

5. 在训练时，采用3/5的数据进行训练，在最终部署时，使用全部数据

6. 验证集和测试集的区别：验证集就是模拟考试，让我们有机会调参，测试集是期末考，考完后就没有调参的必要了，当我们使用训练集和验证集跳完参数后，选择认为最优的那组参数，在训练集和验证集总集上进行训练，然后提交模型


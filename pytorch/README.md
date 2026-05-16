
- 使用 torch.cuda 单命令测试

```bash

# 测试1：检查CUDA是否可用
python -c "import torch; print('CUDA可用:', torch.cuda.is_available()); print('GPU数量:', torch.cuda.device_count()); print('GPU名称:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None')"

# 测试2：执行简单计算
python -c "import torch; a=torch.randn(1000,1000).cuda(); b=torch.randn(1000,1000).cuda(); c=torch.mm(a,b); print('计算完成，结果形状:', c.shape)"

# 测试3：显存分配测试
python -c "import torch; x=torch.zeros(1000,1000,1000).cuda(); print('显存分配成功，大小:', x.element_size() * x.nelement() / 1e6, 'MB'); del x; torch.cuda.empty_cache()"

```

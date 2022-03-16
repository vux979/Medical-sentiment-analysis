主要代码点进通过colab创建的文件`colab_整体运行（已更改）.ipynb`[colab](https://colab.research.google.com/github/vux979/Medical-sentiment-analysis/blob/main/colab_整体运行（已更改）.ipynb)即可登陆colab运行，此代码使用bert作为特征提取器，而后使用textCNN来拟合数据。

baseline，使用的是`《动手学深度学习》(PyTorch版)`的[10.8 文本情感分类：使用卷积神经网络（textCNN）](https://tangshusen.me/Dive-into-DL-PyTorch/#/chapter10_natural-language-processing/10.8_sentiment-analysis-cnn)     

# 环境配置
> requirements
>> requirements_baseline.txt      
>> - baseline的环境     
>> requirements_bert.txt
>> - bert的环境

# 数据集创建
colab中修改了数据集创建的代码，更改了内存占用过高的问题，原始代码data文件夹下的`数据集创建.ipynb`中未做更改，请参考后进行更改，colab中少了一些注释，请参考原始文件

data文件夹下的`数据集创建.py`已做更改

# 权重
weight文件夹中包含训练好的权重

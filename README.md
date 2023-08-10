# Me

## 简介：
近日在两位好友的帮助和ChatGPT的通力合作下，我利用过去几年的微信聊天记录微调（ptuning）清华的开源大模型ChatGLM2-6B，训练了一个“自己”，受_Doctor Who_里面一个角色的启发，我将这个娱乐项目命名为Me（吾）。

## 步骤：
1. 首先需要获取微信聊天记录，由于腾讯的限制，我们无法直接破解MicroMsg.db数据库文件，因此只能曲线救国。比较简单的方法是先将过去所有的聊天记录都存到同一台iPhone或者iPad上，下面分情况讨论：①如果聊天记录保存在不同的手机或平板上，那么可以直接通过设备间迁移功能将其聚拢在一台iOS设备上；②如果在电脑上也有聊天记录，那么需要用微信桌面版将这些记录迁移到手机上；③还有一种最复杂的情况，那就是在其他电脑或移动硬盘上也有聊天记录。这时需打开桌面版微信，依次点击左下角→设置→文件管理，查看微信文件的默认保存位置，把其他电脑或移动硬盘的聊天记录复制到这个路径。如果你一直用同一个微信号，那么不同位置的聊天记录的文件夹名都是一样的。你从其他位置复制同名文件夹过来，这些文件夹就会自动重命名为xxx(1)、xxx(2)等。我们先按②中的方式完成一次迁移，然后我们将xxx重命名为任意名称，然后将xxx(1)改名为xxx，再按照②中的方式完成一次迁移，最后按照相同方式处理xxx(2)。这一轮操作之后，我们过去所有的聊天记录就都汇总在同一台iOS设备上了。
2. 接下来，我们要利用[WechatExporter](https://github.com/BlueMatthew/WechatExporter)将整个iOS设备备份到电脑上。具体方法详见WechatExporter仓库。提醒一点，如果聊天记录较多，我们可以只导出需要纳入训练集的那部分，要征求微信好友或群友的同意。建议选择自己发言比较多的群，和内容不敏感且可体现自己性格的一对一聊天。
3. 导出txt文件之后，我们需要清洗数据，具体方法请参考我上传的Python文件，主要目的是去掉表情包和一些敏感关键词。同时我们需要将txt文件保存成json文件，作为训练集、验证集和测试集。训练集、验证集和测试集所需的数据量也是不一致的，在数据量不是特别大的情况下，一般遵循6:2:2的划分比例。
4. 接下来下载[ChatGLM2-6B模型](https://huggingface.co/THUDM/chatglm2-6b/tree/main)和[微调相关文件](https://github.com/THUDM/ChatGLM2-6B/tree/main)。
5. 如果自己的电脑有显存大于等于8G的GPU，那么可以在本地训练和推理，否则需要租用服务器，我用的是[AutoDL](https://www.autodl.com/home)，感觉还是不错的，相对物美价廉，具体用法见AutoDL官网。另外，如果没用过Linux的话，可以提前了解一下常用的命令。
6. 我们准备开始用自己的数据进行ptuning，需要修改train.sh文件：根据自己的文件名、输入输出key和路径修改train_file、validation_file、prompt_column、response_column、model_name_or_path，其他参数酌情修改。PRE_SEQ_LEN和LR分别是soft prompt长度和训练的学习率，可以进行调节以取得最佳的效果。在默认配置quantization_bit=4、per_device_train_batch_size=1、gradient_accumulation_steps=16下，INT4的模型参数被冻结，一次训练迭代会以1的批处理大小进行16次累加的前后向传播，等效为16的总批处理大小，此时最低只需6.7G显存。若想在同等批处理大小下提升训练效率，可在二者乘积不变的情况下，加大per_device_train_batch_size的值，但也会带来更多的显存消耗，请酌情调整。
7. 在Linux环境中，首先需要下载依赖：
   `pip install -r requirements.txt`
   `pip install transformers==4.27.1`
   `pip install rouge_chinese nltk jieba datasets`
8. 运行bash train.sh开始训练。
9. 训练结束后我们运行bash web_demo.sh测试效果。运行之前需要改一下web_demo.py的`demo.queue().launch()`，改为`share=True`，这样就可以用浏览器测试了。

## 注意事项：
1. 可以将train.sh中的save_steps设置得小一些，如设为200，意味着每200次迭代记录一个checkpoint。如果打断了训练过程，下一次还可以从某一个checkpoint继续进行（在train.sh中加一行`--ptuning_checkpoint /root/autodl-tmp/chatglm/ChatGLM2-6B/ptuning/output/chatglm-6b-pt-96-2e-2/checkpoint-2000 \`，当然这里的路径要改成你的实际路径）。同时，微调结束后的推理也要依赖这些checkpoint。
2. 我们可以根据前几轮的loss下降情况做出大致判断，如果学习率不合适可以及时调整，这也体现出save_steps小一些的好处。
3. 第一轮微调结束后，我们可以以最后的checkpoint为基础进行第二次微调（如有必要）。

## Me项目的个人总结：
我ptuning两次之后的loss仍然在3.6左右，下降并不好，但测试过程中的某些回答还是可以体现出个性。下面放几张测试图：




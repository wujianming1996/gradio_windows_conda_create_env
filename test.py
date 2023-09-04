import os
text = "当前环境：\n"
commond = "conda env list"
process = os.popen(commond)
for outputs in process:
    text += outputs
    print(text)
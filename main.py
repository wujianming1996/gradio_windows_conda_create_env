from gradio import *
import subprocess
import time

with Blocks() as demo:
    HTML('<H1>Python 环境创建工具</H1>')
    textbox = Textbox(label='环境名称')
    python_vision = Textbox(label='Python 版本')
    with Row():
        button = Button('创建',variant='primary')
        clear = Button('清除')
    
    with Tab(label='显示'):
        code_disply = Code(label='已有环境')
    with Tab(label='创建'):
        code_create = Code(label='创建进度')
    def repeat(name,python_vision):
        time.sleep(0.005)
        text = "创建环境名称：" + name + "\n" + "创建的Python 版本："  + python_vision + "\n"
        commond = f"conda create -n {name} python={python_vision}"
        process = subprocess.run(commond,input="y\n",stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True,shell=True)
        for output in process.stdout:
            text += output
            yield text
    
    button.click(repeat,[textbox,python_vision],code_create)


if __name__ == '__main__':
    demo.queue(concurrency_count=5,max_size=20).launch(server_port=52012)
    
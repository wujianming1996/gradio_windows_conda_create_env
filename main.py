from gradio import *
import subprocess
import time
import os

with Blocks(title='Python 机器学习环境创建工具') as demo:
    HTML('<H1>Python 机器学习环境创建工具</H1>')
    textbox = Textbox(label='环境名称')
    python_vision = Textbox(label='Python 版本')
    Ml_vision = Radio(['JupyterLab + Pytorch环境','JupyterLab + Tensorflow环境'],label='初始环境',info='',value='')
    with Row():
        button = Button('创建',variant='primary')
        display_env_button = Button('刷新环境')
        Clear = Button('清除')
    with Tab(label='显示') as tab:
        code_disply = Code(label='已有环境')  
    with Tab(label='创建'):
        code_create = Code(label='创建进度')
        
    def create_env(name,python_vision,Ml_vision):
        #print(len(name),len(python_vision))
        if len(name) >0 and len(python_vision) >0:
            time.sleep(0.005)
            text = "创建环境名称：" + name + "\n" + "创建的Python 版本："  + python_vision + "\n"
            commond = f"conda create -n {name} python={python_vision}"
            process = subprocess.run(commond,input="y\n",stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True,shell=True)
            for output in process.stdout:
                text += output
                yield text
            if Ml_vision =='JupyterLab + Pytorch环境':
                commond =f"""conda activate {name}\n
                conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia\n
                pip install jupyter lab\n"""
                process = subprocess.run(commond,input="y\n",stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True,shell=True)
                for output in process.stdout:
                    text += output
                    yield text


        else:
            time.sleep(0.005)
            return "\n请输入环境名称和Python版本"

    def disply_env():
        text = "当前环境：\n"
        commond = "conda env list"
        process = os.popen(commond)
        for outputs in process:
            text += outputs
            yield text
    def reset_state():
        return "", "","","","",

    Clear.click(reset_state,outputs=[code_disply,code_create,textbox,python_vision],show_progress=True)
    display_env_button.click(disply_env,None,code_disply)
    button.click(create_env,[textbox,python_vision,Ml_vision],code_create)
    


if __name__ == '__main__':
    demo.queue(concurrency_count=5,max_size=20).launch(server_port=52012)
    
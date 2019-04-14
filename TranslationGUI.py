from appJar import gui
import translation_general
import json

d1 = {}

with open('languages.json', 'r') as f:
        d1=json.load(f)
        # key values 互换
        d2 = {value:key for key, value in d1.items()}
iconlocation = './media/icon.ico'
def press(button):
    if button == '翻译':
        app.setLabel('提示','正在翻译，请稍后')
        goallan = d2[app.getOptionBox('选择目标语言：')]
        goaltext=translation_general.translateBD(app.getTextArea('origintext'),goallan)
        app.setLabel('提示','翻译成功！')
        
        app.clearTextArea('译文')
        app.setTextArea('译文',goaltext)
    elif button == '清空':
        app.clearAllTextAreas()
    return 1
with gui('百度中英文翻译') as app:
    # app = gui('百度中英文翻译')
    app.addLabel('百度中英文翻译',row=0,column=0,colspan=3)
    app.setTitle('百度中英文翻译')
    app.setIcon(iconlocation)
    app.setSize(600,600)
    app.setLocation("CENTER")
    app.addLabel("l2","要翻译的内容：",row=1,column=0,colspan=3)
    # app.setLabelBg('l2')
    app.addTextArea("origintext",colspan=3)
    # app.setFocus("orgintext")
    row=app.getRow()

    app.addLabelOptionBox('选择目标语言：',d2.keys(),row,0)
    app.addIconButton("翻译",press,'check-alt',row,1)

    # app.addIconButton("翻译",press,'check-alt',row,0)
    app.addIconButton("清空",press,'trash-empty',row,2)

    # app.addButton()
    # app.addButton()
    app.addTextArea("译文",colspan=3)
    app.addLabel('提示','当前状态：正常，请输入要翻译的内容')
    # app.hideTitleBar()
    app.go() 
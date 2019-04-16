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
        app.setLabel('提示', '正在翻译，请稍后')
        goallan = d2[app.getOptionBox('选择目标语言：')]
        goaltext=translation_general.translateBD(app.getTextArea('origintext'),goallan)
        app.setLabel('提示','翻译成功！')
        
        app.clearTextArea('译文')
        app.setTextArea('译文', goaltext)
    elif button == '清空':
        app.clearAllTextAreas()
        app.setLabel('提示','已清空！')

    elif button == '复制':
        app.topLevel.clipboard_clear()  # 清空剪切板
        app.topLevel.clipboard_append(app.getTextArea("译文"))
        app.setLabel('提示','复制成功！')
    return 1
with gui('百度中英文翻译') as app:
    # app = gui('百度中英文翻译')
    col_num = 4
    app.addLabel('Daltan翻译',row=0,column=0,colspan=col_num)
    app.setLabelBg('Daltan翻译','green')
    app.setTitle('Daltan翻译')
    app.setIcon(iconlocation)
    app.setSize(600,600)
    app.setLocation("CENTER")
    app.addLabel("l2","要翻译的内容：",row=1,column=0,colspan=col_num)
    # app.setLabelBg('l2')
    app.addTextArea("origintext",colspan=col_num)
    # app.setFocus("orgintext")
    row=app.getRow()

    app.addLabelOptionBox('选择目标语言：',d2.keys(),row,0)
    app.addIconButton("翻译",press,'check-alt',row,1)
    app.addIconButton("复制",press,'files',row, 2)
    # app.addIconButton("翻译",press,'check-alt',row,0)
    app.addIconButton("清空",press,'trash-empty',row,3)

    # app.addButton()
    # app.addButton()
    app.addTextArea("译文",colspan=col_num)
    app.addLabel('提示','当前状态：正常，请输入要翻译的内容')
    # app.hideTitleBar()
    app.go() 

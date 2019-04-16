from appJar import gui
import translation_general
import json


def press(button):  # 控制所有的按钮
    if button == '翻译':
        app.setLabel('提示', '正在翻译，请稍后')
        goallan = d2[app.getOptionBox('选择目标语言：')]
        goaltext = translation_general.translateBD(
            app.getTextArea('origintext'), goallan)
        app.setLabel('提示', '翻译成功！')
        app.clearTextArea('译文')
        app.setTextArea('译文', goaltext)
    elif button == '清空':
        app.clearAllTextAreas()
        app.setLabel('提示', '已清空！')
    elif button == '复制':
        app.topLevel.clipboard_clear()  # 清空剪切板
        app.topLevel.clipboard_append(app.getTextArea("译文"))
        app.infoBox('复制成功', '内容已复制到剪贴板', parent=None)
        app.setLabel('提示', '复制成功！')
    if button == '确定':
        app.changeLanguage(app.getRadioButton('lan'))
    return 1


def tbfunc(press_content):  # 控制控制栏按钮
    if press_content == 'CHECK-ALT':
        press('翻译')
    if press_content == 'FILES':
        press('复制')
    if press_content == 'TRASH-EMPTY':
        press('清空')
    if press_content == 'WEB':
        launch('选择语言')
    if press_content == 'ABOUT':
        app.infoBox('关于', 'Daltan翻译 v1.0 2019', parent=None)
    if press_content == 'OFF':
        app.stop()


def launch(win):  # 控制子窗口
    app.showSubWindow(win)


with gui('百度中英文翻译') as app:
    d1 = {}
    with open('languages.json', 'r') as f:
        d1 = json.load(f)
        d2 = {value: key for key, value in d1.items()}
    # app = gui('百度中英文翻译')
    iconlocation = './media/icon.ico'
    # 窗口1
    app.startSubWindow("选择语言", modal=True)
    app.setSize(300, 300)
    app.addLabel("label_chooselan", "选择语言")
    app.addRadioButton("lan", "中文")
    app.addRadioButton("lan", "English")
    app.addRadioButton("lan", "Francais")
    app.addRadioButton("lan", "日本语")
    app.addRadioButton("lan", "韩语")
    app.addButton("确定", press)
    app.app
    app.setIcon(iconlocation)
    app.stopSubWindow()
    # 窗口1结束
    tools = [
        'CHECK-ALT',
        'FILES',
        'TRASH-EMPTY',
        'WEB',
        'ABOUT',
        'OFF'
    ]
    col_num = 4
    app.addLabel('标题', 'Daltan翻译', row=0, column=0, colspan=col_num)
    app.setLabelBg('标题', 'green')
    app.setTitle('Daltan翻译')
    app.setIcon(iconlocation)
    app.setSize(600, 600)
    app.setRadioButtonChangeFunction("lan", press)
    app.addToolbar(tools, tbfunc, findIcon=True)
    app.addLabel("l2", "要翻译的内容：", row=1, column=0, colspan=col_num)
    app.addTextArea("origintext", colspan=col_num)
    row = app.getRow()
    app.addLabelOptionBox('选择目标语言：', d2.keys(), row, 0)
    app.addIconButton("翻译", press, 'check-alt', row, 1)
    app.addIconButton("复制", press, 'files', row, 2)
    app.addIconButton("清空", press, 'trash-empty', row, 3)
    app.addTextArea("译文", colspan=col_num)
    app.addLabel('提示', '当前状态：正常，请输入要翻译的内容')
    app.go()

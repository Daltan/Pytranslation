from appJar import gui 

def launch(win):
    app.showSubWindow(win)

app=gui()

# these go in the main window
app.addButtons(["one", "two"], launch)

# this is a pop-up
app.startSubWindow("one", modal=True)
app.addLabel("l1", "SubWindow One")
app.stopSubWindow()

# this is another pop-up
app.startSubWindow("two")
app.addLabel("l2", "SubWindow Two")
app.stopSubWindow()

app.go()
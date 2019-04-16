from appJar import gui
app=gui("Language Demo")

app.addLabel("l1", "default text")
app.addLabel("l2", "default text")
app.addLabel("l3", "default text")

# as long as the language file has the same name as the button
# the button can call .changeLanguage directly
app.addButtons(["English", "Francais", "한글"], app.changeLanguage)

app.go()
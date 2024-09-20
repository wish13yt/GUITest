from guizero import App, Text, PushButton
def change_message():
    message.value = "Hello Button!"
app = App(title="GUITest")
text = Text(app, text="GUI World!")
button = PushButton(app, text="Press me!", command=change_message)
message = Text(app, text="Please press the button above!")
app.display()
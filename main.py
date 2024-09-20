from guizero import App, Text, PushButton, TextBox
def say_hello():
  message.value = "Hello"
def change_message():
    message.value = "Hello Button!"
app = App(title="GUITest")
text = Text(app, text="GUI World!")
button = PushButton(app, text="Press me!", command=change_message)
message = Text(app, text="Please press the button above!")
name = TextBox(app)
button = PushButton(app, text="Submit input!", command=say_hello)
change = Text(app, text="Input 'Hello World' in the text box above.")
app.display()
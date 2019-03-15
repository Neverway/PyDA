# code for text:
#   line 1 = Type of text (t = general text, i = interaction, c = character line)
#   line 2 = Text id
#   line 3 = Event (e = error, o = other, d = debug)
#   line 4 = Line
fail_safe = {
    0: "You should never see this message... oh"
}
text1 = {
    1: "Text 1 test successful"
}
text2 = {
    1: "Text 2 test successful!"
}
text3 = {
    2: "Text 3 line 1/2 loaded.",
    1: "Text 3 line 2/2 loaded. Text 3 test successful!"
}
text4 = {
    3: "Text 4 line 1/3 loaded.",
    2: "Text 4 line 2/3 loaded.",
    1: "Text 4 line 3/3 loaded. Text 4 test successful!"
}
text5 = {
    9: "Hello, this is only the alpha so don't expect much.",
    8: "Hopefully more stuff will be added in soon.",
    7: "...",
    6: "So yeah, you can press f4 to enter full screen and f1 to exit.",
    5: "Esc will quit the game. Understandable if you want to.",
    4: "The arrow keys are for movement...",
    3: "and z is to open the chat bar...",
    2: "which you already know since you are reading this.",
    1: "...",
}

# Fight
bt_intro = {
    1: "(atk_enm) draws near!"
}
# def delay_txt():
#    global text_surface
#    text = render_text
#    t = 0
#    while True:
#        t += 1
#        shown_text = text[0:t]
#        time.sleep(.25)
#        if t >= 6:
#            break
#   text_surface = font.render(shown_text, True, (255, 255, 255))

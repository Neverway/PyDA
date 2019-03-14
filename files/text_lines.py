# code for text:
#   line 1 = Type of text (t = general text, i = interaction, c = character line)
#   line 2 = Text id
#   line 3 = Event (e = error, o = other, d = debug)
#   line 4 = Line
fail_safe = {
    0: "Text test failed successfully!"
}
text1 = {
    1: "This is a text line. In a text box. (1)"
}
text2 = {
    1: "Text 2 test successful!"
}
text3 = {
    2: "Text 5 first line.",
    1: "Text 5 second line. Text 5 test successful!"
}
text4 = {
    1: "Text 4 test successful!"
}
text5 = {
    2: "Text 5 first line.",
    1: "Text 5 second line. Text 5 test successful!"
}
text6 = {
    3: "Text 6 line 1/3 loaded.",
    2: "Text 6 line 2/3 loaded.",
    1: "Text 6 line 3/3 loaded. Text 6 test successful!"
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

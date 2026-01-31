import pyray as pr

pr.init_window(800, 600, "teste")

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    pr.draw_rectangle(100, 100, 200, 80, pr.BLUE)
    pr.draw_text("Botão", 140, 130, 20, pr.BLACK)

    pr.end_drawing()

pr.close_window()

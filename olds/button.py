import pyray as pr


pr.set_config_flags(pr.FLAG_MSAA_4X_HINT)
pr.init_window(800, 600, 'Botão com hover')

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    # geometria do botão
    x, y, w, h = 100, 100, 100, 32
    rect_border = (x, y, w, h)
    rect_inner_border = (x+1, y+1, w-2, h-2)
    rect_fill = (x+2, y+2, w-4, h-4)

    radius = 0.2
    segments = 6
    # inset = 1

    # input
    mouse = pr.get_mouse_position()
    hover = pr.check_collision_point_rec(mouse, rect_border)

    # cores dinâmicas
    if hover:
        border = (180, 180, 180, 255)
        inner_border = (210, 210, 250, 255)
        fill = (200, 200, 240, 255)
    else:
        border = (180, 180, 180, 255)
        inner_border = (240, 240, 240, 255)
        fill = (225, 225, 225, 255)

    # borda
    pr.draw_rectangle_rounded(rect_border, radius, segments, border)
    # borda interna
    pr.draw_rectangle_rounded(rect_inner_border, radius, segments, inner_border)
    # fundo
    pr.draw_rectangle_rounded(rect_fill, radius, segments, fill)
    # texto
    pr.draw_text('Botão', x+35, y+10, 12, pr.BLACK)

    pr.end_drawing()

pr.close_window()

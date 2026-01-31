import pyray as pr

pr.set_config_flags(pr.FLAG_MSAA_4X_HINT)
pr.init_window(800, 600, 'Botão com hover/click')

last_click_time = 0.0
DOUBLE_CLICK_TIME = 0.3

last_mouse = pr.get_mouse_position()

exit_app = False
while not pr.window_should_close() and not exit_app:
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    # geometria do botão
    x, y, w, h = 100, 100, 100, 32
    rect_border = (x, y, w, h)
    rect_inner_border = (x+1, y+1, w-2, h-2)
    rect_fill = (x+2, y+2, w-4, h-4)

    radius = 0.3
    segments = 6

    # input
    mouse = pr.get_mouse_position()
    mouse_delta = (mouse.x - last_mouse.x, mouse.y - last_mouse.y)
    last_mouse = mouse

    hover = pr.check_collision_point_rec(mouse, rect_border)
    pressed = hover and pr.is_mouse_button_down(pr.MOUSE_LEFT_BUTTON)
    clicked = hover and pr.is_mouse_button_pressed(pr.MOUSE_LEFT_BUTTON)
    released = hover and pr.is_mouse_button_released(pr.MOUSE_LEFT_BUTTON)
    dragging = pressed and (mouse_delta != (0, 0))

    right_clicked  = hover and pr.is_mouse_button_pressed(pr.MOUSE_RIGHT_BUTTON)
    middle_clicked = hover and pr.is_mouse_button_pressed(pr.MOUSE_MIDDLE_BUTTON)
    wheel = pr.get_mouse_wheel_move()

    # cores dinâmicas
    if pressed:
        border = (140, 140, 140, 255)
        inner_border = (180, 180, 220, 255)
        fill = (170, 170, 210, 255)
    elif hover:
        border = (180, 180, 180, 255)
        inner_border = (210, 210, 250, 255)
        fill = (200, 200, 240, 255)
    else:
        border = (180, 180, 180, 255)
        inner_border = (240, 240, 240, 255)
        fill = (225, 225, 225, 255)

    # ação do botão
    current_time = pr.get_time()
    double_clicked = False

    if clicked:
        if current_time - last_click_time < DOUBLE_CLICK_TIME:
            double_clicked = True
        last_click_time = current_time
    
    if clicked:
        print("Botão clicado")
    
    if right_clicked:
        print("Click direito")
        # pr.close_window()
        exit_app = True

    if middle_clicked:
        print("Click rodinha")

    if double_clicked:
        print("Double click")
        
    if released:
        print("Released")
    
    if wheel != 0:
        print("Scroll:", wheel)
        if wheel > 0:
            print('Scroll para cima')
        elif wheel < 0:
            print('Scroll para baixo')
    
    if dragging:
        print("Drag delta:", mouse_delta)
    
    if mouse_delta != (0, 0):
        print("Mouse moveu para:", mouse, "delta:", mouse_delta)

    # desenho
    pr.draw_rectangle_rounded(rect_border, radius, segments, border)
    pr.draw_rectangle_rounded(rect_inner_border, radius, segments, inner_border)
    pr.draw_rectangle_rounded(rect_fill, radius, segments, fill)
    pr.draw_text('Botão', x+35, y+10, 12, pr.BLACK)

    pr.end_drawing()

pr.close_window()

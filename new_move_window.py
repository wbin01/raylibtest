import pyray as pr

pr.set_config_flags(pr.FLAG_WINDOW_UNDECORATED)
pr.set_config_flags(pr.FLAG_MSAA_4X_HINT)
pr.init_window(800, 600, "Janela Drag Cross-Platform")
pr.set_target_fps(60)

DRAG_HEIGHT = 32
dragging = False
offset_x = 0
offset_y = 0

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    mouse = pr.get_mouse_position()
    left_pressed = pr.is_mouse_button_pressed(pr.MOUSE_LEFT_BUTTON)
    left_down = pr.is_mouse_button_down(pr.MOUSE_LEFT_BUTTON)
    win_pos = pr.get_window_position()

    # Detecta início do drag
    if left_pressed and mouse.y <= DRAG_HEIGHT:
        dragging = True
        # Calcula offset entre posição do mouse e canto superior da janela
        offset_x = mouse.x
        offset_y = mouse.y

    # Para drag quando solta o botão
    if not left_down:
        dragging = False

    # Aplica movimento da janela
    # if dragging:
    #     new_x = int(pr.get_mouse_x() - offset_x + win_pos.x)
    #     new_y = int(pr.get_mouse_y() - offset_y + win_pos.y)
    #     pr.set_window_position(new_x, new_y)
    
    if dragging:
        delta_x = pr.get_mouse_delta().x
        delta_y = pr.get_mouse_delta().y

        new_x = int(win_pos.x + delta_x)
        new_y = int(win_pos.y + delta_y)

        pr.set_window_position(new_x, new_y)


    # --- UI mínima ---
    pr.draw_rectangle(0, 0, 800, DRAG_HEIGHT, (100, 100, 240, 255))
    pr.draw_text("Arraste aqui", 10, 8, 20, pr.WHITE)

    pr.end_drawing()

pr.close_window()

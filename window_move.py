import pyray as pr

pr.set_config_flags(pr.FLAG_MSAA_4X_HINT)
pr.set_config_flags(pr.FLAG_WINDOW_HIGHDPI)
pr.set_config_flags(pr.FLAG_WINDOW_UNDECORATED)

pr.init_window(400, 300, "Drag Window")
pr.set_target_fps(60)

dragging = False
drag_offset = (0, 0)

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    # Window size
    W = pr.get_screen_width()
    H = pr.get_screen_height()

    pr.draw_text("Minha janela custom", 30, 20, 20, pr.BLACK)

    # Header 
    title_rect = (W // 2 - 50, 0, 100, 32)
    mouse = pr.get_mouse_position()
    hover = pr.check_collision_point_rec(mouse, title_rect)

    # Header pressed vars
    if hover and pr.is_mouse_button_pressed(pr.MOUSE_LEFT_BUTTON):
        dragging = True
        drag_offset = mouse

    # Header released vars
    if pr.is_mouse_button_released(pr.MOUSE_LEFT_BUTTON):
        dragging = False
        pr.set_mouse_cursor(pr.MOUSE_CURSOR_ARROW)

    # Header Drag
    if dragging:
        pr.set_mouse_cursor(pr.MOUSE_CURSOR_RESIZE_ALL)

        delta = pr.get_mouse_delta()
        win_pos = pr.get_window_position()
        pr.set_window_position(
            int(win_pos.x + delta.x), int(win_pos.y + delta.y))
        
        # Snaping
        # if int(win_pos.x + delta.x) < 20:
        #     pr.set_window_position(0, int(win_pos.y))
    
    # Draw Header
    pr.draw_rectangle(W // 2 - 50 , 2, 100, 20, (0, 0, 0, 100,))
    pr.draw_text("Drag me", (W // 2 - 50) + 20, 5, 12, pr.BLACK)

    pr.end_drawing()

pr.close_window()

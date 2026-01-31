import pyray as pr

pr.set_config_flags(pr.FLAG_MSAA_4X_HINT)
pr.set_config_flags(pr.FLAG_WINDOW_HIGHDPI)
pr.set_config_flags(pr.FLAG_WINDOW_UNDECORATED)

pr.init_window(400, 300, "Drag Window")
pr.set_target_fps(60)

dragging = False
drag_offset = (0, 0)

def win_drag_area():
    global dragging
    global drag_offset

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
    
    # Draw Header
    pr.draw_rectangle(W // 2 - 50 , 2, 100, 20, (0, 0, 0, 100,))
    pr.draw_text("Drag me", (W // 2 - 50) + 20, 5, 12, pr.BLACK)


BORDER = 10
resizing = False
resize_dir = None

MIN_W = 200
MIN_H = 150

def win_resize():
    global BORDER
    global resizing
    global resize_dir
    global MIN_W
    global MIN_H

    W = pr.get_screen_width()
    H = pr.get_screen_height()
    mouse = pr.get_mouse_position()
    delta = pr.get_mouse_delta()
    win_pos = pr.get_window_position()

    # zonas de resize
    zones = {
        "top":            (BORDER, 0, W-2*BORDER, BORDER),
        "bottom":         (BORDER, H-BORDER, W-2*BORDER, BORDER),
        "left":           (0, BORDER, BORDER, H-2*BORDER),
        "right":          (W-BORDER, BORDER, BORDER, H-2*BORDER),

        "top_left":       (0, 0, BORDER, BORDER),
        "top_right":      (W-BORDER, 0, BORDER, BORDER),
        "bottom_left":    (0, H-BORDER, BORDER, BORDER),
        "bottom_right":   (W-BORDER, H-BORDER, BORDER, BORDER),
    }

    # detectar hover
    hover_zone = None
    for name, rect in zones.items():
        if pr.check_collision_point_rec(mouse, rect):
            hover_zone = name

            if hover_zone in ("left", "right"):
                pr.set_mouse_cursor(pr.MOUSE_CURSOR_RESIZE_EW)
            elif hover_zone in ("top", "bottom"):
                pr.set_mouse_cursor(pr.MOUSE_CURSOR_RESIZE_NS)
            elif hover_zone in ("top_left", "bottom_right"):
                pr.set_mouse_cursor(pr.MOUSE_CURSOR_RESIZE_NWSE)
            elif hover_zone in ("top_right", "bottom_left"):
                pr.set_mouse_cursor(pr.MOUSE_CURSOR_RESIZE_NESW)
            
            break

    # iniciar resize
    if hover_zone and pr.is_mouse_button_pressed(pr.MOUSE_LEFT_BUTTON):
        resizing = True
        resize_dir = hover_zone
    
    if not hover_zone and not resizing:
        pr.set_mouse_cursor(pr.MOUSE_CURSOR_DEFAULT)

    # parar resize
    if pr.is_mouse_button_released(pr.MOUSE_LEFT_BUTTON):
        resizing = False
        resize_dir = None
        pr.set_mouse_cursor(pr.MOUSE_CURSOR_DEFAULT)

    # aplicar resize
    if resizing and resize_dir:
        new_x = win_pos.x
        new_y = win_pos.y
        new_w = W
        new_h = H

        dx = int(delta.x)
        dy = int(delta.y)

        if "right" in resize_dir:
            new_w += dx
        if "bottom" in resize_dir:
            new_h += dy
        if "left" in resize_dir:
            new_x += dx
            new_w -= dx
        if "top" in resize_dir:
            new_y += dy
            new_h -= dy

        # limites mínimos
        old_w = new_w
        old_h = new_h

        new_w = max(new_w, MIN_W)
        new_h = max(new_h, MIN_H)

        if new_w == MIN_W and "left" in resize_dir:
            new_x = win_pos.x  # cancela movimento
        if new_h == MIN_H and "top" in resize_dir:
            new_y = win_pos.y

        pr.set_window_position(int(new_x), int(new_y))
        pr.set_window_size(int(new_w), int(new_h))

    # debug visual das bordas
    # for rect in zones.values():
    #     pr.draw_rectangle_lines(*rect, pr.RED)

while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)

    win_drag_area()
    pr.draw_text("Minha janela custom", 30, 20, 20, pr.BLACK)
    win_resize()

    pr.end_drawing()

pr.close_window()

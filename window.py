import pyray as pr

pr.set_config_flags(pr.FLAG_MSAA_4X_HINT)
pr.set_config_flags(pr.FLAG_WINDOW_HIGHDPI)
pr.set_config_flags(pr.FLAG_WINDOW_UNDECORATED)
pr.set_config_flags(pr.FLAG_WINDOW_TRANSPARENT)
# pr.glfw_init_hint(pr.GLFW_ANGLE_PLATFORM_TYPE, 327682)
# pr.glfw_init_hint(pr.GLFW_ANGLE_PLATFORM_TYPE_METAL, 225288)

pr.init_window(500, 400, "Custom Window")
pr.set_target_fps(60)

# print("OpenGL version:", pr.rl_get_version())
# print("GLSL version:", pr.get_shader_location)

# QT_QPA_PLATFORM=xcb python window.py
# SDL_VIDEODRIVER=x11 python window.py
# if Wayland:
#     usa fake (desenha retângulo)
# if X11:
#     usa ARGB real
# if Windows:
#     usa DWM
# if macOS:
#     usa NSWindow

while not pr.window_should_close():
    # https://www.reddit.com/r/raylib/comments/191o1xz/transparent_overlay_window_help/
    # BLEND_MULTIPLIED BLEND_ALPHA_PREMULTIPLY
    # pr.begin_blend_mode(pr.BLEND_ALPHA_PREMULTIPLY)

    pr.clear_background(pr.BLANK)
    pr.begin_drawing()

    # tamanho da janela real
    W = pr.get_screen_width()
    H = pr.get_screen_height()

    # geometria da "janela interna"
    margin = 1
    inner_margin = 1

    rect_outer = (0, 0, W, H)
    rect_inner_border = (
        margin,
        margin,
        W - margin*2,
        H - margin*2
    )
    rect_fill = (
        margin + inner_margin,
        margin + inner_margin,
        W - (margin + inner_margin)*2,
        H - (margin + inner_margin)*2
    )

    radius = 0.05
    segments = 8

    # cores
    outer_border = (0, 255, 0, 255)
    inner_border = (0, 0, 255, 255)
    fill = (240, 240, 240, 255)

    # desenha como se fosse um botão gigante
    pr.draw_rectangle_rounded(rect_outer, radius, segments, outer_border)
    pr.draw_rectangle_rounded(rect_inner_border, radius, segments, inner_border)
    pr.draw_rectangle_rounded(rect_fill, radius, segments, fill)

    pr.draw_text("Minha janela custom", 30, 20, 20, pr.BLACK)

    pr.end_blend_mode()
    pr.end_drawing()

pr.close_window()

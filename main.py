import arcade

#arcade.open_window(800,800, "Draw")

step = 30
height = 800
width = 800

my_window = arcade.open_window(height, width, "PALs 401 (10/14")


#arcade.set_background_color(arcade.color.)
arcade.set_background_color(arcade.color.GENERIC_VIRIDIAN)

# all the draw supposed to be here between start_render and finish render
arcade.start_render()
                     # 'start_y', 'end_x', 'end_y', and 'color'
arcade.draw_line(my_window.width/2, 0, my_window.width/2, my_window.height, arcade.color.AFRICAN_VIOLET)

for i in range(0, my_window.height, step):
    my_text = arcade.Text(f"i", (my_window.width/2) + 10, i)
    my_text.font_size = 24
    my_text.draw()


#drawing arc

arcade.draw_text("Arc", 200, 750, arcade.color.WHITE )
arcade.draw_arc_filled(100, 650, 90, 100, arcade.color.WHITE, 0, 180)
arcade.draw_arc_outline(300, 650, 90, 100, arcade.color.WHITE, 0, 180)

# drawing rectangle
# arguments (x_window, y_window, x_for_object, y_for object, object color)
arcade.draw_rectangle_filled(100,120, 100, 200, arcade.color.WHITE)
arcade.draw_rectangle_outline(300,120, 100, 200, arcade.color.WHITE)
arcade.draw_text("draw Rectangle", 200, 250, arcade.color.WHITE)

# drawing Circle
arcade.draw_text("draw Circle", 200,500, arcade.color.WHITE)
arcade.draw_circle_filled(100, 400, 50, arcade.color.WHITE )
arcade.draw_circle_outline(300, 400, 50, arcade.color.WHITE )

# drawing line
arcade.draw_text("Line",700, 750, arcade.color.WHITE)
arcade.draw_line(750, 650, 450, 650, arcade.color.WHITE, 5)

# drawing Triangle
arcade.draw_text("Triangle", 700,500, arcade.color.WHITE)
#arcade.draw_triangle_filled(100, 100, 300,100, 200,300, arcade.color.WHITE )
arcade.draw_triangle_filled(450, 450, 650,450, 550,500, arcade.color.WHITE)


arcade.draw_text("points", 700, 250, arcade.color.WHITE)
arcade.draw_point(750,200, arcade.color.WHITE, 10)
arcade.draw_point(700,200, arcade.color.WHITE, 10)
arcade.draw_point(750,100, arcade.color.WHITE, 10)
arcade.draw_point(700,100, arcade.color.WHITE, 10)


arcade.draw_point(800,0, arcade.color.BLACK, 40)
arcade.draw_point(800,800, arcade.color.BLACK, 40)
arcade.draw_point(0,800, arcade.color.BLACK, 40)
arcade.draw_point(0,0, arcade.color.BLACK, 40)
arcade.draw_text("Keyshawn Jeannot", 500, 150, arcade.color.KOBE)

arcade.finish_render()
arcade.run()





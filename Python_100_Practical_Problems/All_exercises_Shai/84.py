import pyglet as pg

window = pg.window.Window(800, 600, "Hello, World! Pyglet")

label = pg.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
label.draw()
# win.set_visible()
pg.app.run()


# This code results in flikery window. as the app.run keeps running.
# Having the window event on_draw makes the output stable
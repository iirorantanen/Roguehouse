import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50	
LIMIT_FPS = 20

def handle_keys():
  key = libtcod.console_wait_for_keypress(True)
  if key.vk == libtcod.KEY_ENTER and key.lalt:
    #Alt+Enter = fullscreen
    libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
  elif key.vk == libtcod.KEY_ESCAPE:
    return True

  global playerx, playery
  if libtcod.console_is_key_pressed(libtcod.KEY_UP):
    player.move(0, -1)
  elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
    player.move(0, 1)
  elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
    player.move(-1, 0)
  elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
    player.move(1, 0)

class Object:
  def __init__(self, x, y, char, color):
    self.x = x
    self.y = y
    self.char = char
    self.color = color

  def move(self, dx, dy):
    self.x += dx
    self.y += dy

  def draw(self):
    libtcod.console_set_foreground_color(con, self.color)
    libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

  def clear(self):
    libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)

#Initialization & Main Loop
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Roguehouse', False)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
libtcod.sys_set_fps(LIMIT_FPS)

player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white)
npc = Object(SCREEN_WIDTH/2-5, SCREEN_HEIGHT/2, '@', libtcod.yellow)
objects = [npc, player]

first_time = True
while not libtcod.console_is_window_closed():
  for object in objects:
    object.clear()

  if not first_time:
    exit = handle_keys()
    if exit:
      break
  first_time = False
  
  for object in objects:
    object.draw()

  libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
  libtcod.console_flush()

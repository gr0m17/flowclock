import time
import math
import displayio
from adafruit_matrixportal.matrix import Matrix

##--| User Config |-----------------------------------------
SINGULARITIES = (
    # type  location  strength
    ('freestream', None, (1, 0)),

#1, first position
   ('source', (7, 9), 1),
   ('doublet', (8, 9), 1),
   ('doublet', (9, 9), 1),
   ('doublet', (9, 10), 1),
   ('doublet', (9, 11), 1),
   ('doublet', (9, 12), 1),
   ('doublet', (9, 13), 1),
   ('doublet', (9, 14), 1),
   ('source', (9, 15), 1),
   ('doublet', (9, 16), 1),
   ('doublet', (9, 17), 1),
   ('doublet', (9, 18), 1),
   ('doublet', (9, 19), 1),
   ('doublet', (9, 20), 1),
   ('doublet', (9, 21), 1),
   ('source', (9, 22), 1),

#2, second position
   ('doublet', (13, 12), 1),
   ('doublet', (13, 11), 1),
   ('doublet', (13, 10), 1),
   ('vortex', (14, 9), 1),
   ('doublet', (15, 9), 1),
   ('doublet', (16, 9), 1),
   ('doublet', (17, 10), 1),
   ('doublet', (17, 11), 1),
  ('doublet', (17, 12), 1),
  ('doublet', (17, 13), 1),
  ('doublet', (17, 14), 1),
  ('doublet', (16, 15), 1),
  ('doublet', (16, 16), 1),
  ('doublet', (15, 17), 1),
  ('doublet', (15, 18), 1),
  ('doublet', (14, 19), 1),
  ('doublet', (14, 20), 1),
  ('doublet', (14, 21), 1),
  ('doublet', (14, 22), 1),
  ('doublet', (15, 22), 1),
  ('doublet', (16, 22), 1),
  ('doublet', (17, 22), 1),

#dots

  ('source', (19, 14), -3),
  ('source', (19, 22), -3),

#3rd position
   ('doublet', (23, 12), 1),
   ('doublet', (23, 13), 1),
   ('doublet', (23, 14), 1),
   ('doublet', (23, 15), 1),
   ('doublet', (23, 16), 1),
   ('doublet', (23, 17), 1),
   ('doublet', (23, 18), 1),
   ('doublet', (23, 19), 1),
   ('doublet', (24, 20), 1),
   ('doublet', (24, 21), 1),
   ('doublet', (25, 22), 1),
   ('doublet', (26, 22), 1),
   ('doublet', (27, 21), 1),
   ('doublet', (27, 20), 1),
   ('doublet', (24, 11), 1),
   ('doublet', (24, 10), 1),
   ('doublet', (25, 9), 1),
   ('doublet', (26, 9), 1),
   ('doublet', (27, 10), 1),
   ('doublet', (28, 11), 1),
   ('doublet', (28, 12), 1),
   ('doublet', (28, 12), 1),
   ('doublet', (28, 13), 1),
   ('doublet', (28, 14), 1),
   ('doublet', (28, 15), 1),
   ('doublet', (28, 16), 1),
   ('doublet', (28, 17), 1),
   ('doublet', (28, 18), 1),
   ('doublet', (28, 19), 1),


#4th position
   ('doublet', (30, 12), 1),
   ('doublet', (30, 13), 1),
   ('doublet', (30, 14), 1),
   ('doublet', (30, 15), 1),
   ('doublet', (30, 16), 1),
   ('doublet', (30, 17), 1),
   ('doublet', (30, 18), 1),
   ('doublet', (30, 19), 1),
   ('doublet', (31, 20), 1),
   ('doublet', (31, 21), 1),
   ('doublet', (32, 22), 1),
   ('doublet', (33, 22), 1),
   ('doublet', (34, 21), 1),
   ('doublet', (34, 20), 1),
   ('doublet', (31, 11), 1),
   ('doublet', (31, 10), 1),
   ('doublet', (32, 9), 1),
   ('doublet', (33, 9), 1),
   ('doublet', (34, 10), 1),
   ('doublet', (35, 11), 1),
   ('doublet', (35, 12), 1),
   ('doublet', (35, 12), 1),
   ('doublet', (35, 13), 1),
   ('doublet', (35, 14), 1),
   ('doublet', (35, 15), 1),
   ('doublet', (35, 16), 1),
   ('doublet', (35, 17), 1),
   ('doublet', (35, 18), 1),
   ('doublet', (35, 19), 1),







#AM

   ('doublet', (42, 15), 1),
   ('doublet', (42, 16), 1),
   ('doublet', (42, 17), 1),
   ('doublet', (42, 18), 1),
   ('doublet', (42, 19), 1),
   ('doublet', (42, 20), 1),
   ('doublet', (42, 21), 1),
   ('doublet', (43, 14), 1),
   ('doublet', (44, 14), 1),
   ('doublet', (45, 14), 1),
   ('doublet', (45, 15), 1),
   ('doublet', (45, 16), 1),
   ('doublet', (45, 17), 1),
   ('doublet', (45, 18), 1),
   ('doublet', (45, 19), 1),
   ('doublet', (45, 20), 1),
   ('doublet', (45, 21), 1),

   ('source', (43, 22), -1),
('doublet', (44, 22), 1),
   ('doublet', (45, 22), 1),


   ('doublet', (48, 14), 1),
   ('doublet', (48, 15), 1),
   ('doublet', (48, 16), 1),
   ('doublet', (48, 17), 1),
   ('doublet', (48, 18), 1),
   ('doublet', (48, 19), 1),
   ('doublet', (48, 20), 1),
   ('doublet', (48, 21), 1),
   ('doublet', (48, 22), 1),
   ('doublet', (49, 15), 1),
   ('doublet', (50, 14), 1),
   ('doublet', (51, 14), 1),
   ('doublet', (53, 14), 1),
   ('doublet', (54, 14), 1),

   ('doublet', (52, 15), 1),
   ('doublet', (52, 16), 1),
   ('doublet', (52, 17), 1),
   ('doublet', (52, 18), 1),
   ('doublet', (52, 19), 1),
   ('doublet', (52, 20), 1),
   ('doublet', (52, 21), 1),
   ('doublet', (52, 22), 1),

   ('doublet', (55, 15), 1),
   ('doublet', (55, 16), 1),
   ('doublet', (55, 17), 1),
   ('doublet', (55, 18), 1),
   ('doublet', (55, 19), 1),
   ('doublet', (55, 20), 1),
   ('doublet', (55, 21), 1),
   ('doublet', (55, 22), 1),



)
SEEDS = (
#   (x, y) starting location
    (0, 0),
    (0, 2),
    (0, 4),
    (0, 6),
    (0, 8),
    (0, 10),
    (0, 12),
    (0, 14),
    (0, 16),
    (0, 18),
    (0, 20),
    (0, 22),
    (0, 24),
    (0, 26),
    (0, 28),
    (0, 30),
    (0, 32),
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (1, 9),
    (1, 10),




)
MATRIX_WIDTH = 64
MATRIX_HEIGHT = 32
BACK_COLOR = 0x000000 # background fill
SING_COLOR = 0xADAF00 # singularities
HEAD_COLOR = 0x00FFFF # leading particles
TAIL_COLOR = 0x000A0A # trailing particles
TAIL_LENGTH = 32      # length in pixels
DELAY = 0.01          # smaller = faster
#----------------------------------------------------------

# matrix and displayio setup
matrix = Matrix(width=MATRIX_WIDTH, height=MATRIX_HEIGHT, bit_depth=6)
display = matrix.display
group = displayio.Group()
display.show(group)

bitmap = displayio.Bitmap(display.width, display.height, 4)

palette = displayio.Palette(4)
palette[0] = BACK_COLOR
palette[1] = SING_COLOR
palette[2] = HEAD_COLOR
palette[3] = TAIL_COLOR

tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
group.append(tile_grid)

# global to store streamline data
STREAMLINES = []

def compute_velocity(x, y):
    '''Compute resultant velocity induced at (x, y) from all singularities.'''
    vx = vy = 0
    for s in SINGULARITIES:
        if s[0] == 'freestream':
            vx += s[2][0]
            vy += s[2][1]
        else:
            dx = x - s[1][0]
            dy = y - s[1][1]
            r2 = dx*dx + dy*dy
            if s[0] == 'source':
                vx += s[2] * dx / r2
                vy += s[2] * dy / r2
            elif s[0] == 'vortex':
                vx -=  s[2] * dy / r2
                vy +=  s[2] * dx / r2
            elif s[0] == 'doublet':
                vx += s[2] * (dy*dy - dx*dx) / (r2*r2)
                vy -= s[2] * (2*dx*dy) / (r2*r2)
    return vx, vy

def compute_streamlines():
    '''Compute streamline for each starting point (seed) defined.'''
    for seed in SEEDS:
        streamline = []
        x, y = seed
        px = round(x)
        py = round(y)
        vx, vy = compute_velocity(x, y)
        streamline.append( ((px, py), (vx, vy)) )
        steps = 0
        while x < MATRIX_WIDTH and steps < 2 * MATRIX_WIDTH:
            nx = round(x)
            ny = round(y)
            # if we've moved to a new pixel, store the info
            if nx != px or ny != py:
                streamline.append( ((nx, ny), (vx, vy)) )
                px = nx
                py = ny
            vx, vy = compute_velocity(x, y)
            x += vx
            y += vy
            steps += 1
        # add streamline to global store
        STREAMLINES.append(streamline)

def show_singularities():
    '''Draw the singularites.'''
    for s in SINGULARITIES:
        try:
            x, y = s[1]
            bitmap[round(x), round(y)] = 1
        except:
            pass # just don't draw it

def show_streamlines():
    '''Draw the streamlines.'''
    for sl, head in enumerate(HEADS):
        try:
            streamline = STREAMLINES[sl]
            index = round(head)
            length = min(index, TAIL_LENGTH)
            # draw tail
            for data in streamline[index-length:index]:
                x, y = data[0]
                bitmap[round(x), round(y)] = 3
            # draw head
            bitmap[round(x), round(y)] = 2
        except:
            pass # just don't draw it

def animate_streamlines():
    '''Update the current location (head position) along each streamline.'''
    reset_heads = True
    for sl, head in enumerate(HEADS):
        # get associated streamline
        streamline = STREAMLINES[sl]
        # compute index
        index = round(head)
        # get velocity
        if index < len(streamline):
            vx, vy = streamline[index][1]
            reset_heads = False
        else:
            vx, vy = streamline[-1][1]
        # move head
        HEADS[sl] += math.sqrt(vx*vx + vy*vy)
    if reset_heads:
        # all streamlines have reached the end, so reset to start
        for index, _ in enumerate(HEADS):
            HEADS[index] = 0

def update_display():
    '''Update the matrix display.'''
    display.auto_refresh = False
    bitmap.fill(0)
    show_singularities()
    show_streamlines()
    display.auto_refresh = True

#==========
# MAIN
#==========
print('Computing streamlines...', end='')
compute_streamlines()
print('DONE')
HEADS = [0]*len(STREAMLINES)
print('Flowing...')
while True:
    animate_streamlines()
    update_display()
    time.sleep(DELAY)
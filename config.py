from math import *

# Экран
width = 1200
height = 800
half_width = width / 2
half_height = height / 2

# Карта
block_size = 100
text_map = ["WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W..........WW...................WW...........WWWWWW..WWWWWW......WWWW..WW..........WW...........WWWW...W",
"WWWWW..WWWWWWWWWWWWWWWWWWW..WWWWWWW..WW..WW......WW................WW..WWWWWW..WW..WWWWWWW....WW..WW..WW",
"W..WW..WW..............WWW...........WW..WWWWWWWWWWWWWW..WWWWWWWWWWWW..WW......WW..WWWWWWWWWWWW.......WW",
"W..WW..WW..WWWWWWWWWW..WWW..WWWWWWWWWWW.............WWW.................WWWWWWW..................WWWWWWW",
"W..WW..WW..WW..........WWW......WW..WWWWWWWWWWWWWW..WWWWWWWWWW..WWWWWWWWWWWWWWWWW..WWWWWWWWWW..WWW..WWWW",
"W..WW..WW..WW..WWWWWW..WWWWWWW..WW..............WW..WW..WWWW..........WW.......WW..WWWWWWWWWWW..WW..WWWW",
"W......WW..WW..........WWWWWWW..WW..WWWWWWWWWW..WW..WW....WWWWWWWWWW..WW..WWW..WW..WW.......WW..WW....WW",
"WWWWW..WW..WWWWWWWWWWWWWWWWWWW..WW..WWWWWWWWWW..WW..WWWW..WW......WW..WW..W.W..WW..WWWWWWW..WWWWWWWW..WW",
"W...............................................WW....WW..WW..WW..WW..WW..W....WW...........WWWWWW....WW",
"W..WWWWWWWWWWWWWWWWWWWWWWWWWWWWW..WWWWWWWWWWWWWWWWWW..WW..WW..WWWWWWWWWW..WWWWWWWWWWWWWWWW..WW......WWWW",
"W..W..WW.........WWWWWWWWWWWWWWWWWWWWW......................................................WWWWWW....WW",
"W..W......WW..W..WW..................WWWW..WW..WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW..WWWWWWWWWWWWWWWWWWWW..WW",
"W..WWWWWWWWW..W..WW..WWWWWWWWWWWWWW........WW..WWW..........................WW..WW.........WWWWWW.....WW",
"W.............W..WWW....WWW......WWWWWWWW..WWWWWWW..WWWWWWWWWWWWWWW..WWWWW..WW..WWWWWWWWW..........WWWWW",
"WWW..WWWWWWWWWW..WWWWW.......WW........WW...........WW..WWWWWW..WWW..W..WW..WW..WW.........WWWWWW.....WW",
"WWW..WWWWWWW..W..WWWWWWWW..WWWWWWWWWW..WWWWWWWWWWW..WW..........WWW..W..WW..WW..WW..WWWWWWWWWWWWWWWW..WW",
"W..........................WWWW........WW...........WWWWWWWW..WWWWW.....WWWWWW..WW..WWWWWWWWWWWW..WW..WW",
"W..WWWW..WWWWW..WWWWWWWWW..WWWWWWWWWW..WW..WWWWWWWWWW.........WWWWWWWWWWWW..WW..WW..WWW..WWWWWWW..WW..WW",
"W..WWWWWWWWWWWWWWWWW...................WW..WWWWWWWWWWWW..WWWWWWWWWW.........WW..WW..WWWWWW........WW..WW",
"W..WW.............WW..WWWWWWWWWWW..WWWWWW........................WW..WWWWWWWWW..WW..WWWWWWW..WWW..WW..WW",
"W..WW..WWWWWWWWW..WW..W........WW.......WWWWWWWWWWWWWWWWWWWWWWWWWWW..WW.....WW..WW............WW..WW..WW",
"W..WWWWWWWWWWWWW..WW..WWWWWWW..WWWWWWW..WW......WW......WW......WW...WWWWW..WW..WWWWWWWWWWWWWWWWWWW...WW",
"W.................WW...........WW...........WW......WW......WW..............WW........................WW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"]
block_map = set()
y_block_pos = 0
for row in text_map:
    x_block_pos = 0
    for column in list(row):
        if column == "W":
            block_map.add((x_block_pos, y_block_pos))
        x_block_pos += block_size
    y_block_pos += block_size

# Ray Casting
FOV = pi / 2
half_FOV = FOV / 2
max_depth = width // block_size
num_rays =  1200
delta_ray = FOV / (num_rays - 1)
dist = num_rays / (2 * tan(half_FOV))
coefficient = dist * block_size * 2
scale = width // num_rays
depth_coeff = 2
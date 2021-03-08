import sys
sys.path.insert(1, './base_python')
from display import *
from matrix import *

s = new_screen()
c = [ 255, 255, 255 ]

edge_matrix = []
add_edge(edge_matrix, [250, 250], [125, 125])
add_edge(edge_matrix, [125, 125], [250, 0])
add_edge(edge_matrix, [250, 0], [375, 125])
add_edge(edge_matrix, [375, 125], [250, 250])
add_edge(edge_matrix, [250, 250], [250, 0])

draw_matrix(edge_matrix, s, c)

save_ppm(s, 'binary.ppm')
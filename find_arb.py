from shortest_path import get_arb_path
from construct_matrix import get_price_matrix
import time
import numpy as np

i = 0
while True:
	print('trial number {}'.format(i))
	p_matrix = get_price_matrix()
	numpy.savetxt('output.csv',np.asarray(p_matrix),delimiter=",")
	found_arb = get_arb_path(p_matrix, 0)
	if found_arb:
		print('FOUND AN ARB!!!!!!!!')
	time.sleep(10)
	i += 1

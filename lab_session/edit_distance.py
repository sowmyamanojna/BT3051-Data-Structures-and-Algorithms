import numpy as np

def edit_distance(s, t, E):
	for i in range(1, len(s)+1):
		for j in range(1, len(t)+1):
			values = np.array([0, 0, 0])
			if s[i-1] == t[j-1]:
				values = [1, 1, 0]
			else:
				values = [1, 1, 1]
			E_vals = np.array([E[i, j-1], E[i-1, j], E[i-1, j-1]])
			E[i, j] = min(E_vals+values)
	return E


s = 'ATTATCAT'
t = 'TTATCATT'

E =-np.zeros((len(s)+1, len(t)+1))
E[0,:] = np.array(range(len(s)+1))
E[1:,0] = np.array(range(1, len(t)+1))
print (edit_distance(s, t, E))
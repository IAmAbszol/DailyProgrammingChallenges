def zig_to_zag(s, k):
	if k < 1:
		return None
	'''
		s = thisisazigzag, k = 4
		[[t_____a],
		 [_h___s],
         [__i__i_],
		 [___s__]]
		time O(n * k) <-- per element, k inqueries. 
	'''
	zigs = ['' for _ in range(k)]
	pos = 0;
	constant = 1
	for idx, i in enumerate(s):
		zigs[pos] += i
		zigs = [zig + ' ' if z_idx != idx else zig for z_idx, zig in enumerate(zigs)]
		if idx % (k - 1) == 0 and idx != 0:
			zigs[pos] += ' '
			constant *= -1
		pos += constant
	for zig in zigs:
		print(zig)

zig_to_zag('thisisazigzag', 4)
	

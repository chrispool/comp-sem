model([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14],
	[f(1,n_table_2,[d1]),
	f(1,n_chair_1,[d2]),
	f(1,n_lamp_2,[d3]),
	f(1,n_glassware_1,[d4,d5]),
	f(1,n_napkin_1,[d6,d7]),
	f(1,n_tablecloth_1,[d8,d12]),
	f(1,n_cutlery_2,[d9,d10,d11]),
	f(1,n_porcelain_1,[d13,d14]),
	f(1,a_red_1,[d3,d6,d7]),
	f(1,a_brown_1,[d2]),
	f(1,a_white_1,[d13,d14])]),
	f(2,s_near, [(d2,d1), (d1,d2)],
	f(2,s_touch,[(d8, d3), (d3,d8), (d8,d4), (d4,d8), (d5,d8), (d8,d5), (d8,d6),(d6,d8), (d8,d7),(d7,d8), (d8,d1),(d1,d8),(d8,d9),(d9,d8),(d10,d8),(d10,d8),(d11,d13),(d13,d11),(d13,d12),(d12,d13),(d8,d12), (d12,d8),(d12,d1),(d1,d12),(d14,d8),(d8,d14)],
	f(2,supports,[(d1,d8),(d1,d12),(d1,d4),(d1,d5),(d1,d6),(d1,d7),(d1,d8),(d1,d12),(d1,d9),(d1,d10),(d1,d11),(d1,d13),(d1,d14)]
	




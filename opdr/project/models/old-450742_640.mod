model([d1,d2,d3,d4,d5,n1,n2,n3,n4,n5,n6],
      [f(1,n_sky_1,[d1]),
       f(1,n_nature_3,[d2]),
       f(1,n_lane_1,[d3]),
       f(1,n_grass_1,[n1]),
       f(1,n_tree_1,[n2,n3]),
       f(1,n_bush_1,[n4,n5]),
       f(1,n_old_man_1,[d4]),
       f(1,n_old_woman_1,[d5]),
       f(1,n_staff_2,[n6]),
	   f(2,s_touches,[(d4,d5),(d5,d4),(n6,d5),(d5,n6),(d3,d4),(d3,d5),(d4,d3),(d5,d3),(d3,n1),(n1,d3)]),
	   f(2,s_supports,[(n6,d5),(d3,d4),(d3,d5)]),
	   f(2,s_part_of,[(n1,d4)]),
	   f(2,s_near,[(d5,n1),(n1,d5)])]).

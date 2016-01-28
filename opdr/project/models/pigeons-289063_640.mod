model([d1,d2,d3,n1,n2],
      	[f(1,n_pigeon_1,[d1,d2]),
       	f(1,n_railing_1,[d3]),
       	f(1,n_head_1,[n1,n2]),
       	f(1,a_grey_1,[d1,d2]),
       	f(1,a_light_brown_1,[d3]),
	f(2,s_part_of,[(n1,d1),(n2,d2)]),
	f(2,s_touches,[(d1,d3),(d2,d3)]),
	f(2,s_supports,[(d3,d1),(d3,d2)]),
	f(2,s_near,[(d1,d2)])]).
      

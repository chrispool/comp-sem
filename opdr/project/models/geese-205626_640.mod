model([d1,d2,d3,d4],
      [f(1,n_body_of_water_1,[d1]),
       f(1,n_mute_swan_1,[d2]),
       f(1,n_honker_3,[d3,d4]),
       f(1,a_white_1,[d2]),
       f(1,a_grey_1,[d1]),
       f(2,s_near,[(d2,d3),(d3,d2),(d2,d4),(d4,d2)]),
       f(2,s_supports,[(d1,d2),(d1,d3),(d1,d4)]),
       f(2,s_touches,[(d1,d2),(d2,d1),(d1,d3),(d3,d1),(d1,d4),(d4,d1)])]).
      

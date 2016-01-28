model([d1,d2,d3,d4,d5,d6],
      [f(1,n_horse_1,[d1,d2,d3]),
       f(1,n_forest_1,[d4]),
       f(1,n_grass_1,[d5]),
       f(1,n_mountain_1,[d6]),
       f(2,s_supports,[(d5,d1),(d5,d2),(d5,d3)]),
       f(2,s_near,[(d1,d2),(d2,d1)]),
       f(2,s_touches,[(d5,d1),(d1,d5),(d5,d2),(d2,d5),(d5,d3),(d3,d5)])]).

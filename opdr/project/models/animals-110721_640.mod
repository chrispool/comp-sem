model([d1,d2,d3,d4],
      [f(1,n_pheasant_1,[d1,d2]),
       f(1,n_grass_1,[d3]),
       f(1,n_hedgehog_1,[d4]),
       f(2,s_touches,[(d1,d3),(d3,d1),(d2,d3),(d3,d2),(d3,d4),(d4,d4)]),
       f(2,s_supports,[(d3,d1),(d3,d2),(d3,d4)]),
       f(2,s_near,[(d1,d3),(d3,d1),(d2,d3),(d3,d2),(d3,d4),(d4,d4)])]).
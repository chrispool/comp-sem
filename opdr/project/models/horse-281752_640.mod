model([d1,d2,d3],
      [f(1,n_horse_1,[d1]),
       f(1,n_hand_1,[d2]),
       f(1,n_carrot_1,[d3]),
       f(2,s_supports,[(d2,d3),(d1,d3)]),
       f(2,s_touches,[(d1,d3),(d3,d1),(d2,d3),(d3,d2)])]).

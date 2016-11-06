from ElevatorConstants import *
SuitBuildingInfo = (((1, 1), 
  (1, 4),
  (5, 5),
  (8, 10),
  (1,)), 
 ((1, 2), 
  (2, 5),
  (5, 5),
  (10, 11),
  (1, 1.2)), 
 ((1, 3),
  (3, 6),
  (6, 6),
  (12, 13),
  (1, 1.3, 1.6)), 
 ((2, 3), 
  (4, 7),
  (7, 7),
  (14, 15),
  (1, 1.4, 1.8)), 
 ((2, 4), 
  (5, 7),
  (8, 8),
  (16, 17),
  (1,
   1.6,
   1.8,
   2)), 
 ((3, 4),
  (6, 8),
  (9, 9),
  (17, 18),
  (1,
   1.6,
   2,
   2.4)), 
 ((3, 5),
  (6, 9),
  (10, 10),
  (18, 19),
  (1,
   1.6,
   1.8,
   2.2,
   2.4)),  
 ((4, 5), 
  (7, 10),
  (11, 11),
  (18, 19),
  (1,
   1.8,
   2.4,
   3,
   3.2)), 
 ((5, 5),
  (8, 12),
  (12, 12),
  (20, 22),
  (1.4,
   1.8,
   2.6,
   3.4,
   4)),  
 ((6, 6),
  (9, 14),
  (14, 14),
  (22, 26),
  (1.8,
   2.6,
   3.4,
   4.2,
   4.8,
   5.6)), 
 ((1, 1), 
  (5, 13), #VP Cogs 
  (13, 13),
  (100, 100),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (8, 13), #VP Skelecogs 
  (13, 13),
  (150, 150),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (5, 14), #CFO Cogs 
  (14, 14),
  (150, 150),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (8, 14), #CFO Skelecogs 
  (14, 14),
  (200, 200),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (5, 16), #CJ Cogs 
  (16, 16),
  (300, 300),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (5, 18), #CEO Waiters 
  (18, 18),
  (290, 290),
  (1,
   1,
   1,
   1,
   1),
  (1,)),
 ((1, 1),
  (1, 5),
  (5, 5),
  (33, 33),
  (1,
   1,
   1,
   1,
   1)),
 ((1, 1),
  (4, 5),
  (5, 5),
  (50, 50),
  (1,
   1,
   1,
   1,
   1)), 
 ((1, 1),
  (11, 12), #CEO Banquet 
  (18, 18),
  (220, 220),
  (1,
   1,
   1,
   1,
   1),
  (1,)))
SUIT_BLDG_INFO_FLOORS = 0
SUIT_BLDG_INFO_SUIT_LVLS = 1
SUIT_BLDG_INFO_BOSS_LVLS = 2
SUIT_BLDG_INFO_LVL_POOL = 3
SUIT_BLDG_INFO_LVL_POOL_MULTS = 4
SUIT_BLDG_INFO_REVIVES = 5
VICTORY_RUN_TIME = ElevatorData[ELEVATOR_NORMAL]['openTime'] + TOON_VICTORY_EXIT_TIME
TO_TOON_BLDG_TIME = 8
VICTORY_SEQUENCE_TIME = VICTORY_RUN_TIME + TO_TOON_BLDG_TIME
CLEAR_OUT_TOON_BLDG_TIME = 4
TO_SUIT_BLDG_TIME = 8

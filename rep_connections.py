from collections import OrderedDict

all_connections = {('sim1', 'sim1'): ['1490642434.41', 3, 5],
               ('tlx3', 'tlx3'): ['1492545925.15', 8, 5],
               ('sim1', 'pvalb'): ['1495574744.01', 8, 4],
               ('tlx3', 'pvalb'): ['1496699390.01', 8, 2],
               ('tlx3', 'sst'): ['1497653267.74', 3, 4],
               ('pvalb', 'sim1'): ['1495574744.01', 4, 8],
               ('pvalb', 'tlx3'): ['1503953399.15', 2, 8],
               ('pvalb', 'pvalb'): ['1491597493.27', 2, 6],
               ('pvalb','sst'): ['1493765516.34', 8, 3],
               ('pvalb', 'vip'): ['1487796524.54', 3, 6],
               ('sst', 'tlx3'): ['1504300627.31', 8, 2],
               ('sst', 'pvalb'): ['1493765516.34', 3, 8],
               ('sst', 'sst'): ['1493765516.34', 2, 3],
               ('sst', 'vip'): ['1494632512.34', 5, 4],
               ('vip','sst'): ['1490997794.08', 7, 8],
               ('vip', 'vip'): ['1500408589.73', 8, 1],
               ('L23pyr','L23pyr'): ['1501101571.17', 1, 5],
               ('rorb', 'rorb'): ['1502301827.80', 6, 8],
               ('ntsr1', 'ntsr1'): ['1504737622.52', 8, 2],
               ('slc17a8', 'slc17a8'): ['1495833911.11', 1, 8],
               ('human_L2', 'human_L2'): ['1504052194.49', 1, 5],
               ('human_L3', 'human_L3'): ['1503372117.27', 6, 4],
               ('human_L4', 'human_L4'): ['1497580583.99', 4, 3],
               ('human_L5', 'human_L5'): ['1503376975.16', 2, 4]}

human_connections = OrderedDict([(('human_L2', 'human_L2'), ['1504052194.49', 1, 5]),
                                 (('human_L3', 'human_L3'), ['1503372117.27', 6, 4]),
                                 (('human_L4', 'human_L4'), ['1497580583.99', 4, 3]),
                                 (('human_L5', 'human_L5'), ['1503376975.16', 2, 4]),
                                 (('human_L6', 'human_L6'), ['1512513429.49', 8, 1])])

ee_connections = OrderedDict([(('L23pyr','L23pyr'), ['1501101571.17', 1, 5]),
                              (('rorb', 'rorb'), ['1502301827.80', 6, 8]),
                              (('sim1', 'sim1'), ['1490642434.41', 3, 5]),
                              (('tlx3', 'tlx3'), ['1492545925.15', 8, 5]),
                              (('slc17a8', 'slc17a8'), ['1495833911.11', 1, 8]),
                              (('ntsr1', 'ntsr1'), ['1504737622.52', 8, 2])])
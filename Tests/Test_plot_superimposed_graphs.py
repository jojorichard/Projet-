def test_plot_superimposed_graphs():
    """
    Test function for plot_superimposed_graphs.

    This function simulates user inputs and verifies the function's behavior.

    Returns:
    None
    """
    import io
    import sys

    # Données d'échantillon pour le test
    sample_data = {
        "EmWl [nm]": [350, 350.5, 351, 351.5, 352, 352.5, 353, 353.5, 354, 354.5, 355, 355.5, 356, 356.5, 357, 357.5, 358, 358.5, 359, 359.5,
                      360, 360.5, 361, 361.5, 362, 362.5, 363, 363.5, 364, 364.5,365, 365.5, 366, 366.5, 367, 367.5, 368, 368.5, 369, 369.5,
                      370, 370.5, 371, 371.5, 372, 372.5, 373, 373.5, 374, 374.5,375, 375.5, 376, 376.5, 377, 377.5, 378, 378.5, 379, 379.5,
                      380, 380.5, 381, 381.5, 382, 382.5, 383, 383.5, 384, 384.5,385, 385.5, 386, 386.5, 387, 387.5, 388, 388.5, 389, 389.5,
                      390, 390.5, 391, 391.5, 392, 392.5, 393, 393.5, 394, 394.5,395, 395.5, 396, 396.5, 397, 397.5, 398, 398.5, 399, 399.5,
                      400, 400.5, 401, 401.5, 402, 402.5, 403, 403.5, 404, 404.5,405, 405.5, 406, 406.5, 407, 407.5, 408, 408.5, 409, 409.5,
                      410, 410.5, 411, 411.5, 412, 412.5, 413, 413.5, 414, 414.5,415, 415.5, 416, 416.5, 417, 417.5, 418, 418.5, 419, 419.5,
                      420, 420.5, 421, 421.5, 422, 422.5, 423, 423.5, 424, 424.5,425, 425.5, 426, 426.5, 427, 427.5, 428, 428.5, 429, 429.5,
                      430, 430.5, 431, 431.5, 432, 432.5, 433, 433.5, 434, 434.5,435, 435.5, 436, 436.5, 437, 437.5, 438, 438.5, 439, 439.5,
                      440, 440.5, 441, 441.5, 442, 442.5, 443, 443.5, 444, 444.5,445, 445.5, 446, 446.5, 447, 447.5, 448, 448.5, 449, 449.5,
                      450, 450.5, 451, 451.5, 452, 452.5, 453, 453.5, 454, 454.5,455, 455.5, 456, 456.5, 457, 457.5, 458, 458.5, 459, 459.5,
                      460, 460.5, 461, 461.5, 462, 462.5, 463, 463.5, 464, 464.5,465, 465.5, 466, 466.5, 467, 467.5, 468, 468.5, 469, 469.5,
                      470, 470.5, 471, 471.5, 472, 472.5, 473, 473.5, 474, 474.5,475, 475.5, 476, 476.5, 477, 477.5, 478, 478.5, 479, 479.5,
                      480, 480.5, 481, 481.5, 482, 482.5, 483, 483.5, 484, 484.5,485, 485.5, 486, 486.5, 487, 487.5, 488, 488.5, 489, 489.5,
                      490, 490.5, 491, 491.5, 492, 492.5, 493, 493.5, 494, 494.5,495, 495.5, 496, 496.5, 497, 497.5, 498, 498.5, 499, 499.5,
                      500, 500.5, 501, 501.5, 502, 502.5, 503, 503.5, 504, 504.5,505, 505.5, 506, 506.5, 507, 507.5, 508, 508.5, 509, 509.5,
                      510, 510.5, 511, 511.5, 512, 512.5, 513, 513.5, 514, 514.5,515, 515.5, 516, 516.5, 517, 517.5, 518, 518.5, 519, 519.5,
                      520, 520.5, 521, 521.5, 522, 522.5, 523, 523.5, 524, 524.5,525, 525.5, 526, 526.5, 527, 527.5, 528, 528.5, 529, 529.5,
                      530, 530.5, 531, 531.5, 532, 532.5, 533, 533.5, 534, 534.5,535, 535.5, 536, 536.5, 537, 537.5, 538, 538.5, 539, 539.5,
                      540, 540.5, 541, 541.5, 542, 542.5, 543, 543.5, 544, 544.5,545, 545.5, 546, 546.5, 547, 547.5, 548, 548.5, 549, 549.5,
                      550, 550.5, 551, 551.5, 552, 552.5, 553, 553.5, 554, 554.5,555, 555.5, 556, 556.5, 557, 557.5, 558, 558.5, 559, 559.5,
                      560, 560.5, 561, 561.5, 562, 562.5, 563, 563.5, 564, 564.5,565, 565.5, 566, 566.5, 567, 567.5, 568, 568.5, 569, 569.5,
                      570, 570.5, 571, 571.5, 572, 572.5, 573, 573.5, 574, 574.5,575, 575.5, 576, 576.5, 577, 577.5, 578, 578.5, 579, 579.5,
                      580, 580.5, 581, 581.5, 582, 582.5, 583, 583.5, 584, 584.5,585, 585.5, 586, 586.5, 587, 587.5, 588, 588.5, 589, 589.5,
                      590, 590.5, 591, 591.5, 592, 592.5, 593, 593.5, 594, 594.5,595, 595.5, 596, 596.5, 597, 597.5, 598, 598.5, 599, 599.5,
                      600],
        250: [0.77, 0.8966, 0.9829, 0.9755, 0.9746, 1.0333, 0.9876, 0.8903, 0.8318, 0.9077, 0.9706, 1.059, 1.234, 359036, 414552, 467147, 110305, 1.1035, 1.0921, 1.0275, 
              1.0471, 1.0716, 1.1447, 1.1218, 1.0933, 1.104, 1.1819, 464590, 554805, 420396, 621645, 513533, 590599, 1.332, 222435, 1.1837, 1.1303, 127106, 1.1322, 1.0672, 
              1.0912, 1.0911, 1.1558, 55154, 294387, 510977, 520473, 820337, 310093, 1.1728, 1.1569, 1.1264, 1.1625, 178606, 696884, 1.501, 1119105, 1225756, 1061397, 
              1086964, 1209320, 1.527, 1304648, 1498227, 1320353, 1283464, 17899, 941963, 1.449, 1001497, 1067241, 1359070, 1426274, 1495670, 1160378, 810475, 691041, 
              727200, 922240, 1055188, 1.525, 1657108, 1767410, 1805761, 1788595, 1649437, 1794804, 2047186, 2172099, 2167716, 1848495, 2145437, 2530402, 2601624, 2.001, 
              45475, 2955910, 2.0386, 2.0428, 2.0515, 2679056, 2.0725, 2.1533, 2.1153, 2.1245, 2.0904, 2788628, 2.0262, 2.0209, 2.0414, 2839033, 2864234, 2510314, 
              2323675, 2154568, 1838998, 1.699, 2008106, 2341936, 2321118, 2.0391, 316333, 769234, 1129729, 772156, 475214, 2.1834, 2930707, 2.0491, 2.0489, 321081, 
              1068368, 1127902, 1556332, 1444202, 1149086, 17564, 2.1673, 2.1351, 2.1491, 2.1594, 187403, 183020, 526713, 318159, 2.1274, 2807986, 2647645, 1926656, 
              1853608, 2073849, 2203510, 2285690, 2221407, 2412429, 2763427, 1.955, 2642166, 1.849, 2135940, 2193283, 2033672, 1992765, 1839729, 1962816, 2188535, 2144706, 
              1977060, 1791151, 1671352, 1684500, 1822198, 2149455, 2350702, 31413, 2505200, 2437631, 2151646, 1970121, 1829136, 1437231, 1631175, 1860913, 1976329, 
              1772158, 1.759, 2480364, 2610390, 2714850, 2681978, 2444936, 2681613, 2465024, 2110739, 1512472, 1602321, 1664047, 1526351, 1442345, 1611817, 1755722, 
              1906933, 1852878, 1670987, 1818180, 1668430, 2098321, 2390880, 2609660, 2828075, 2910254, 2767079, 2653854, 2547569, 2653854, 2138132, 2616965, 
              2770367, 2642166, 2606007, 29952, 2509948, 2.0453, 29618, 45353, 539862, 623867, 1069463, 859449, 744032, 196534, 502607, 981805, 1629380, 1647642, 
              1645085, 1550853, 2356212, 2156059, 2.862, 2.817, 2.727, 2306174, 2543948, 2243353, 2092508, 1619883, 1523825, 1408774, 1286052, 700203, 2.1289, 1859, 
              221370, 345188, 276887, 2.1343, 45598, 2.0886, 2748086, 2704257, 2546473, 2935456, 2.0709, 2.0424, 2.0541, 2753565, 2.0105, 2.1112, 2.1125, 367832, 
              524521, 773252, 318159, 2.1261, 2.1191, 209318, 729423, 1634493, 1556697, 1952255, 2784276, 2797060, 2446063, 2466516, 3.0644, 3.1781, 3.0688, 150906, 
              1887, 688544, 1171028, 1160802, 2598031, 2824847, 4.019, 4.044, 4.1788, 1099107, 1805486, 2363576, 2272996, 5.0412, 5.1198, 2080514, 1329940, 483308, 
              2849318, 1371913, 234182, 2855134, 2.844, 1951524, 2.756, 2102735, 2439488, 2036625, 1378459, 506260, 275791, 2.1392, 2950431, 2578980, 2.0433, 2665177, 
              2718867, 2730555, 2848164, 2670655, 2451875, 2734573, 2950431, 2.0805, 2.1025, 2.0358, 2.0259, 2873000, 2510314, 2098686, 1631905, 1931404, 1741844, 1553013, 
              1426639, 1396324, 1468642, 1489461, 1469737, 1553744, 1584424, 1593920, 1419335, 1425178, 1447093, 1476677, 1651629, 1725042, 1724312, 1736365, 
              1704954, 1632271, 1604878, 1566528, 1566528, 1557031, 1609260, 1473025,  1648707, 1840459, 2057413, 2138132, 2159315, 2058508, 2176482, 2313813, 
              2413159, 2637418, 2.0517, 2.184, 673540, 577847, 466082, 584786, 994223, 1750275, 2036991, 1727265, 1553410, 2.689, 2288643, 2024937, 2719994, 3.1625, 
              890157, 1679447, 3.553, 3.377, 163324, 125339, 3.084, 2788294, 2465785, 2317862, 2514362, 2126110, 1652025, 1222500, 604509, 177906, 2.0301, 2448587, 
              1564701, 1441249, 1378793, 1.523, 1392306, 1425908, 1599034, 1868948, 1889767, 1777637, 1620948, 1511376, 1179004, 1.393, 1.334, 638812, 653422, 822894, 
              830564, 775047, 1.397, 817050, 708938, 691772, 598634, 980313, 754958, 894115, 1177543, 874393, 508420, 1.309, 437563, 1.392, 373280, 480296, 438658, 760802, 
              547136, 122723, 1.127, 1.1858, 25204, 173492, 321050, 767377, 1069067, 1337885, 1065780, 718799, 578181, 460938, 44197, 1.1276, 1.0909, 1.0526, 
              0.896, 0.9219, 0.8722, 0.8583, 0.9719, 0.9987, 1.1037, 1.1497, 1.134, 42736, 1.0977, 1.1292, 1.1655, 200521, 260420, 1.1635, 39814, 1.0985, 0.9405, 0.9281, 
              0.8407, 0.8014, 0.8918, 0.9529, 0.941, 0.9048, 0.8842, 0.7939, 0.7917, 0.7779, 0.7313, 0.7484, 0.7835, 0.336],
        "Int(350)" : [183.412, 160.5854, 125.7934, 96.7918, 71.7968, 42.3403, 24.0595, 2236351, 10441, 2764217, 3.363, 634825, 342631, 390112, 369293, 2.1735, 18660, 2.1877, 2.089, 2.0551, 2.1223, 
              2.1783, 2.1315, 2.1677, 2.1859, 2.299, 2.323, 13547, 669888, 2.325, 708238, 645052, 963543, 1498988, 2.721, 2565496, 2.958, 3.0428, 2919417, 3.0021, 3.0493, 3.0604, 3.1086, 
              3.328, 1502669, 2466909, 2829595, 45326, 2782843, 4.0381, 4.0334, 3.907, 2839457, 4.177, 864256, 1868307, 1841280, 2313538, 5.0344, 867573, 1970606, 2770852, 230621, 
              865413, 1804817, 7.0228, 7.1786, 1884104, 134989, 8.909, 676675, 10.1059, 11.1855, 140224, 13.451, 14.8949, 16.4691, 18.0453, 19.6212, 21.3109, 22.4063, 23.8783, 
              25.1808, 25.9863, 26.6476, 27.4038, 27.961, 28.0413, 28.4045, 28.2258, 27.767, 27.3488, 26.2791, 25.1535, 24.2147, 23.2084, 21.959, 20.697, 19.6977, 18.6434, 
              18.1403, 17.6462, 17.1931, 16.9865, 16.878, 16.5613, 16.1582, 15.8334, 15.645, 15.6821, 15.9731, 16.1676, 16.4715, 16.7542, 16.9093, 16.9604, 16.9079, 16.9309, 
              16.9175, 17.0168, 17.1612, 16.9675, 16.9276, 17.009, 17.0338, 16.9928, 16.8967, 16.9407, 17.3441, 17.5065, 17.7989, 17.5418, 17.6731, 17.8451, 17.7793, 17.6552, 
              17.6049, 17.7238, 18.0633, 18.079, 18.3331, 18.145, 18.3922, 18.4892, 18.3327, 18.1126, 17.94, 17.7769, 17.5679, 17.3237, 17.0887, 16.8647, 16.9416, 16.9879, 
              16.9688, 16.7931, 16.933, 17.1102, 17.1578, 17.1703, 17.3462, 17.6186, 17.6356, 17.4981, 17.3388, 17.1842, 16.8083, 16.6142, 16.3256, 15.9347, 15.5936, 15.5963, 
              15.2936, 15.4263, 15.5723, 15.7542, 15.809, 15.8825, 15.7273, 15.3114, 15.0101, 14.9046, 14.7029, 14.563, 14.6096, 14.6506, 14.7687, 14.7276, 14.5538, 14.4965, 
              14.322, 13.877, 13.5319, 13.1906, 13.1021, 2802842, 2337523, 12.694, 1263345, 828341, 51105, 2607772, 2640279, 2471537, 2463136, 2754600, 2720633, 2607772, 
              1767714, 709242, 72260, 2878752, 11.0708, 2857933, 11.1129, 11.0986, 479505, 1084347, 11.196, 11.304, 120471, 11.1281, 11.1881, 11.1779, 11.1617, 11.1151, 
              11.289, 816258, 559858, 734078, 11.1496, 2928424, 2759317, 2130370, 1263284, 1120109, 983143, 652964, 876127, 125553, 10.1029, 10.1748, 10.1583, 10.1084, 
              10.0945, 2793620, 2110982, 1396202, 1542664, 724887, 345035, 279291, 9.1085, 9.1507, 2742455, 2093785, 1652572, 8.586, 1105438, 644137, 118918, 8.152, 
              8.0606, 8.033, 2151097, 1769418, 7.463, 361044, 7.1576, 7.0274, 2772709, 7.1225, 567770, 492531, 323788, 182439, 280324, 354834, 365791, 283246, 
              205085, 364331, 7.1496, 7.0109, 2782570, 2524344, 7.0513, 7.1055, 7.1613, 783264, 955658, 986703, 868000, 824536, 202528, 159429, 7.1743, 7.1197, 
              7.1533, 7.1548, 2861463, 2411484, 2225211, 1646301, 950879, 6.286, 6.0481, 269702, 825236, 1118161, 860665, 826697, 466203, 6.1445, 2706204, 1957092, 
              1381835, 2042193, 2632790, 14397, 154650, 539617, 6.326, 493596, 262762, 6.1886, 6.1327, 6.1067, 6.045, 6.0998, 2466240, 5.655, 1016592, 528628, 
              634914, 5.307, 5.455, 5.385, 710884, 633453, 5.1822, 5.1345, 5.1748, 516575, 1455614, 1316456, 1503826, 1053847, 970572, 301812, 640393, 1484468, 2172950, 
              6.0454, 1039998, 6.593, 2588262, 7.0716, 7.0703, 7.0854, 197780, 7.1635, 7.1617, 7.1895, 1281454, 1890679, 8.0192, 8.1722, 8.0861, 506076, 1234369, 
              1256283, 1967046, 9.0162, 673387, 1286629, 1838511, 1226000, 1659908, 2632182, 10.0569, 2790332, 10.1855, 1561687, 1788503, 2730098, 2589115, 
              1773893, 2918928, 439327, 670526, 11.1785, 75911, 11.0947, 11.0206, 2349880, 875762, 1204480, 10.741, 2380196, 2043442, 1016015, 624475, 10.0864, 10.049, 
              2479877, 2831240, 10.245, 10.0593, 2590911, 2704501, 2131435, 1713964, 341017, 9.0199, 2591976, 1797573, 1038233, 500962, 1043712, 1051382, 421704, 
              8.1048, 8.0699, 2731467, 7.715, 1547351, 1050255, 1360712, 1068883, 7.1443, 2518866, 2183573, 2032728, 6.651, 1296034, 1708028, 2395414, 2928302, 33756, 
              1904527, 1398667, 476430, 6.0225, 6.0174, 2897956, 6.0209, 6.224, 6.225, 141502, 6.1401, 6.0957, 2671506, 2323430, 1946135, 1173281, 370478, 5.1374, 
              5.1424, 5.1713, 5.1685, 5.266, 163751, 28976, 5.0773, 4.977, 2278840, 1695913, 2007466, 1692261, 1092899, 878500, 537730, 331367, 4.1533, 4.1678, 4.0289, 4.0357, 4.0754, 
              4.0081, 2472023, 2217448, 1858416, 1270740, 477068, 671742, 37681, 80049, 3.1713, 3.1576, 3.0471, 2671417, 2706115, 2424513, 2.898, 2660825, 2093238, 1816385, 1536243, 
              2.409, 2.391]
    }
    

    eem = pd.DataFrame(sample_data)

    # Simulate user inputs
    input_values = ["2","yes", "250", "350", "yes"]
    input_iter = iter(input_values)

    def mock_input(prompt):
        return next(input_iter)

    # Replace input with our mock_input
    original_input = __builtins__.input
    __builtins__.input = mock_input

    # Capture the output of the plot function
    original_stdout = sys.stdout
    sys.stdout = io.StringIO()

    try:
        plot_superimposed_graphs()
        # Optionally, you can check the printed output
        output = sys.stdout.getvalue()
        print(output)
    finally:
        # Restore original functions
        __builtins__.input = original_input
        sys.stdout = original_stdout    

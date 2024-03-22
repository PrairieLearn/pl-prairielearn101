# constant values used in the digital logic helper functions


# general constants
VAR_NAMES = ['x', 'y', 'z', 'w', 'u', 'v']

# video hashes
youtube_videos = {
    "e2c": "29IJIFhvuzE",
    "c2t": "oDMmsa8WxJU",
    "t2c": "8sja1RXR_Iw",
    "e2t": "i2HZ_ZZKg1M",
    "t2e": "fvPjmPx7g5k",
    "v2c": "G6rybJ7X6HU",
    "c2e": "_0KaTciimNM"
}

# equation templates

# family = [And, Or, Not]
# num_terminals = 2
equation_templates11 = [["5", "2+5", "25", "21+5"],                     # level0
                            ["(1+4)(1+5)", "14+15", "(25)'", "(2+5)'"]] # level1

# num_terminals = 3
equation_templates12 = [["5", "2+5", "25", "1+25", "225"],              # level0
                            ["13+225", "2(1+45)", "2(2+5)", "2+2+5"]]   # level1

# family = 2, 3: [Nand], [Nand, Not]
# num_terminals = 2
equation_templates31 = [["5", "2^5", "(2^5)'"],                         # level0
                            ["6^(2^5)", "(6^(2^5))'"]]                  # level1
# num_terminals = 3
equation_templates32 = [["2^(2^5)", "(2^(2^5))'"],                      # level3
                            ["2^(2^5)'", "(2^(2^5)')'"]]                # level4

# family = 4, 5: [Nor], [Nor, Not]
# num_terminals = 2
equation_templates51 = [["7", "2/5", "(2/5)'"],                         # level0
                            ["6/5", "(2/5)'"],                          # level1
                            ["6/5", "(2/5)'"]]                          # level2 theseneedhelp
                        # (6/(2/5)')' --> x + y' --> draws complicated solution
                        # x'/(y'/x')' --> xy --> VERY complicated solution especially family=4
# num_terminals = 3
equation_templates52 = [["2/(2/5)", "(2/(2/5))'"],                      # level3
                            ["2/(2/5)'", "(2/(2/5)')'"]]                # level4

equation_templates = {0: [equation_templates11, equation_templates12], 
                    1: [equation_templates31, equation_templates32], 
                    2: [equation_templates51, equation_templates52]}
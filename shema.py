def allShema():
    shema = {
                1: (
                    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
                    {
                        "A": ["EF"],
                        "F": ["CH"],
                        "I": ["DB"],
                        "J": ["I"],
                        "BF": ["JE"],
                        "E": ["CD"]
                    }
                    ),
                2: (
                    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
                    {
                        "DI": ["B"],
                        "AJ": ["F", "HD"],
                        "GB": ["FJE"],
                        "I": ["CG"],
                    }
                    ),
                3: (
                    ['A','B','C','D','E','F','G','I','J','K'],
                    {
                        "A": ["EF"],
                        "E": ["CD"], 
                        "F": ["BG"], 
                        "IB": ["J"],
                        "AG": ["K"]
                    }
                    ),
                4: ( 
                    ['K','L','M','N','O','P','R','S','T','U'],
                    {
                        "K": ["MN"],
                        "ST": ["U"], 
                        "KLM": ["N"], 
                        "R": ["S"],
                        "U": ["K"]
                    }
                    ),
                5: (
                    ['A','B','C','H','I','J','W','X','Y','Z'],
                    {
                        "A": ["Z"],
                        "BC": ["W"],   
                        "ZY": ["AB"],    
                        "IJ": ["H"],
                        "AI": ["XY"],
                    }
                ),
                6: (
                    ['A','B','C','D','E','F','G','H','I','J'],
                    {
                        "A": ["B", "D", "H"],
                        "C": ["B"],
                        "B": ["E"], 
                        "I": ["J"],
                        "H": ["G"],
                        "D": ["F"]
                    }
                ),
                7:(
                    [],
                    {
                    }
                ),
            }
    return shema
            
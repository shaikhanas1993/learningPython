import math
raw_data = [float('NaN'),56,2,float('NaN')]
for k,v in enumerate(raw_data):
    if not math.isnan(v):
        print k,v
    
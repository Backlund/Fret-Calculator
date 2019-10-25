
scale = float(input ("Scale in mm: "))
numfrets = int(input("Number of frets: "))

distance = 0

for fret in range(1, numfrets+1):
    location = scale - distance
    scaling_factor = location / 17.817
    distance = distance + scaling_factor
    print ("Distance to fret {} in mm: {}".format(fret, round(distance, 2)))


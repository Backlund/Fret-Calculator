
scale = float(input ("Scale: "))
numfrets = int(input("Number of frets: "))

distance = 0
units = "mm"
if scale < 50:
    units = "inches"

for fret in range(1, numfrets+1):
    location = scale - distance
    scaling_factor = location / 17.817
    distance += scaling_factor
    print ("Distance to fret {} in {}: {}".format(fret, units, round(distance, 3)))


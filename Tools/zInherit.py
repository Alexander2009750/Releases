import binascii
import re
import struct
import math
import os
import copy
import operator

ContentFolder = "F:\Modding Stuff\Hydro Stuff\Hydro Shortcuts\Mining\Content"

def find_sublist(sub, bigger):
    if not bigger:
        return -1
    if not sub:
        return 0
    first, rest = sub[0], sub[1:]
    pos = 0
    try:
        while True:
            pos = bigger.index(first, pos) + 1
            if not rest or bigger[pos:pos+len(rest)] == rest:
                return pos
    except ValueError:
        return -1


HeilosGUID = [
list(binascii.unhexlify("AEB01D6208A47946A53E561D2B21B017")), # BP_ParentItem StaticMesh
list(binascii.unhexlify("50134F0A7D55204EAB399A0AF0654415")), # BP_ParentPower LegsDown
list(binascii.unhexlify("4E1DD9065E1D6046822468D7AD914559")), # BP_ParentPower LegsUp
list(binascii.unhexlify("7A8C1BDFBFF5EF4295CDDF9D608439E6")), # BP_ParentPower LegsLeft
list(binascii.unhexlify("899B81E396B185458FA58F3CC5998841")) # BP_ParentPower LegsRight
]

MaxGUID = [
list(binascii.unhexlify("8D738624717D4344829E0B260558CDCA")), # BP_ParentItem StaticMesh
list(binascii.unhexlify("78E26F20A83B04479AFBB815A028A5E0")), # BP_ParentPower LegsDown
list(binascii.unhexlify("1ED2DBA1FBC69C46B221BB7BD6FC916A")), # BP_ParentPower LegsUp
list(binascii.unhexlify("873478DC327F1D4C8C69269EA9071625")), # BP_ParentPower LegsLeft
list(binascii.unhexlify("85E32DA9AE41A445AFF74300E641A555")) # BP_ParentPower LegsRight
]

for subdir, dirs, files in os.walk(ContentFolder):
	for file in files:
		if file.endswith(".uexp"):
			reading = open(os.path.join(subdir, file), 'rb')
			content = list(reading.read())
			for x in range (0, len(HeilosGUID)):
				GUIDGRAB = find_sublist(HeilosGUID[x], content)
				if GUIDGRAB > -1:
					rawr = 0
					for y in range (GUIDGRAB, GUIDGRAB+16):
						content[y-1] = MaxGUID[x][rawr]
						rawr = rawr+1
					print(file)
					reading.close()
					reading = open(os.path.join(subdir, file), 'wb')
					reading.write(bytearray(content))
			reading.close()
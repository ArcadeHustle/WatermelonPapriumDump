Canvas is 1024x12352 pixels<br>
Lines are 1024x32 pixels<br>
Tiles are 32x32 pixels <br>
32 tiles per line<br>

Tile map:<br>
0_0 - Blank Tile (skip)<br>

Character type - normal:<br>
                   0_32A   0_64AB<br>
(overhang) 0_32A   0_32B   0_96AB<br>
                   0_160A  0_128AB (overlap)<br>

Character type - zoomed:<br>
                  0_192A   0_224AB<br>
(overhang) 0_192A 0_192B   0_256AB<br>
                  0_320A   0_288AB (overlap)<br>

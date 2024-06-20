A solution for calculating gallons of paint in batches for SCADA on automated paint line. Implemented in Ignition. 
COLOR,GALLONS should equate to 
SOD,0          
P234,2          
A123,6
L890,5
G123,8
G123,1
F890,4
C789,6
P234,3
P234,4
T456,7
D234,8
S123,9
A123,4
A123,8
E567,1
Q567,3
M123,5
A123,1
A123,1
B456,2
R890,4
J234,6
EOD,0

should equate to

SOD,0          
P234,2          
A123,6
L890,5
G123,9
F890,4
C789,6
P234,7
T456,7
D234,8
S123,9
A123,12
E567,1
Q567,3
M123,5
A123,2
B456,2
R890,4
J234,6
EOD,0

Configuration Precautions for Ethernet Interface
================================================

Configuration_Precautions_for_Ethernet_Interface

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Limitations on fixed ports:  1. The first 16 ports (0 to 15) support only the 10G LAN mode.  2. The remaining 10G ports (ports 16 to 27 in 28\*10GE mode, ports 16 to 25 in 26\*10G+18\*GE mode, and ports 16 to 19 in 20\*10G+24\*GE mode) support the 10G LAN, 10G WAN, or 1G mode.  The use of hardware modules is restricted. | NE40E-M2 | NE40E-M2H |
| When an interface works in 1GE/10GE mode, the forwarding delay is long when large packets are received or sent. This is because the forwarding delay includes the delay for receiving/sending entire packets, which is calculated by dividing the interface rate into the maximum packet length. For example, if the maximum packet length is 9300 bytes, the receiving delay of a 1GE interface is 74.4 Î¼s (9300 bytes/1GE = 74.4 Î¼s). | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| It is recommended that you set the hold-down time to 500 ms for a CX68L4XFG, CX68E2NBD, or CX68E1NBB subcard. | NE40E-M2 | NE40E-M2K |
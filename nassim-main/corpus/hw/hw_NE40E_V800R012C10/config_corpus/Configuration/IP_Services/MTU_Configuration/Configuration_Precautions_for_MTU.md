Configuration Precautions for MTU
=================================

Configuration Precautions for MTU

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| IPv6 or IPv4 packets that are forcibly not fragmented are forwarded through a PW connected to a VBDIF interface. To allow the packets whose length exceeds the MTU to be sent to the CPU, run the forward-mode loopback command on the VBDIF interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
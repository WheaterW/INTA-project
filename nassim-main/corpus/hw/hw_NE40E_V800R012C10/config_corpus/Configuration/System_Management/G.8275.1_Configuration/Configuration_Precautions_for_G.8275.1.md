Configuration Precautions for G.8275.1
======================================

Configuration Precautions for G.8275.1

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| In PTP time synchronization, when the time recovery performance is +/-1 Î¼s, a maximum of 30 hops are supported. If more than 30 hops are supported, the time synchronization performance is affected. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The same protocol type must be configured at both transmit and receive ends of signals on 1PPS+TOD external time interfaces.  If the ubx or nmea parameter is configured, the device cannot obtain the clock class from an external time source. It cannot detect any clock class degrade on the upstream device or perform source switching when such degrade occurs.  After the clock tod protocol ccsa command is executed, the PPS status of TOD input and output external time signals is converted into the clock class based on the CCSA standard. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
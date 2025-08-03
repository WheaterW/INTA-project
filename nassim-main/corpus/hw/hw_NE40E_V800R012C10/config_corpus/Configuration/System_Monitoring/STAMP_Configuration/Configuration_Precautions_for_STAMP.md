Configuration Precautions for STAMP
===================================

Configuration Precautions for STAMP

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| URPF check cannot be enabled for STAMP detection based on the default next hop address. Otherwise, the STAMP function does not take effect, packet loss occurs, and the traffic path may change. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When the local device functions as the sender and connects to the TWAMP Light reflector, the loop prevention function cannot be configured on the reflector. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
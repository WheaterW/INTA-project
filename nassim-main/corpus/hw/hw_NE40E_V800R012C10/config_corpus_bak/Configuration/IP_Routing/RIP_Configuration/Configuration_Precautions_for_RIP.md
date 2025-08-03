Configuration Precautions for RIP
=================================

Configuration_Precautions_for_RIP

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| After the device is restarted, if the BFD session status of the local device or neighbor is AdminDown, the RIP status is not affected. When the BFD session is renegotiated, if BFD reports the detection status Down but the previous detection status is Up, RIP sets the neighbor status to Down. In other cases, the RIP status is not affected. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
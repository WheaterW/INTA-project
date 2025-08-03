Configuration Precautions for ATOM GPS Timing
=============================================

Configuration_Precautions_for_ATOM_GPS_Timing

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The ATOM GPS 1.0/2.0/3.0 module does not support traffic loopback. After loopback-related commands are run on the interface where the ATOM GPS 1.0/2.0 module is inserted, the ATOM GPS 1.0/2.0 module reports an ETH\_LOS alarm. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The ATOM GPS 1.0/2.0/3.0 module can only be inserted into a GE optical interface.  When a GE optical interface that has an ATOM GPS module installed is replaced with a common optical module, the ATOM GPS timing configuration on the GE optical interface is cleared.  Time synchronization is affected.  This restriction requires that the device must have GE optical interfaces. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
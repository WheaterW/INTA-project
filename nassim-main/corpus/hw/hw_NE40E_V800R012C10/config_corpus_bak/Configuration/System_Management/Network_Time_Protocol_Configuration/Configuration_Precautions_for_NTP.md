Configuration Precautions for NTP
=================================

Configuration_Precautions_for_NTP

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The NTP protocol version of the device ranges from V1 to V4. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| For security purposes, you are advised not to use the weak security algorithm provided by this feature. By default, the weak security algorithm is enabled. To disable the weak security algorithm, run the crypto weak-algorithm disable command. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| 1. The existing configuration will not be deleted when the NTP service is disabled.  2. Currently, each device can be configured with a maximum of 256 multicast servers, peers, unicast servers, 1024 NTP authentication keys, and 1024 multicast clients. A maximum of 256 multicast clients can take effect simultaneously.  3. A device running NTP supports a maximum of 256 sessions at the same time, including static and dynamic sessions. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
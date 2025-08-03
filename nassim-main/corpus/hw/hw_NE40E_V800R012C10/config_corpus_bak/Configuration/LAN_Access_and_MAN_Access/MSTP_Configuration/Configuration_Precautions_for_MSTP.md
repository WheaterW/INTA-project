Configuration Precautions for MSTP
==================================

Configuration_Precautions_for_MSTP

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| RSTP applies a single spanning tree instance to the entire switching network. It cannot solve the problem of performance deterioration caused by the increase of the network scale. Therefore, the network diameter cannot exceed 7. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| BPDU protection takes effect only on manually configured edge ports. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Loop protection and root protection cannot be configured on the same port. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When MSTP multi-instance is configured, the length of a protocol packet increases with the number of instances. MSTP sends MSTP packets in each process independently. When MSTP multi-process is configured, the number of sent MSTP packets increases. In multi-process and multi-instance scenarios, the default CPCAR value of STP cannot meet protocol requirements. You need to manually increase the CPCAR value of STP. Otherwise, protocol packets may be discarded by CAR. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| To prevent traffic looping on the access ring after the link between the UPEs fails, it is advised to configure priorities and root protection for MSTP multi-processes. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| PW interfaces do not support multi-instance computation. They use only the forwarding status of instance 0.  Loops may occur when the status of different MSTP instances on PW interfaces is inconsistent.  Configure the network properly to ensure the status of MSTP instances is consistent on PW interfaces. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
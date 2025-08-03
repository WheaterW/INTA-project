Configuration Precautions for ND
================================

Configuration Precautions for ND

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| 1. The fast ND reply function is supported only in local ND scenarios, but not in ND proxy scenarios.  2. Due to the limitation of the LocalArpv6 algorithm table specification, interfaces that exceed the specification do not support the ND fast reply function.  3. The fast ND reply function does not support VLANIF interfaces.  4. The fast ND reply function does not support VBDIF interfaces and the source address is FE80 link-local.  5. The fast ND reply function is not supported in mVRRP6 non-ipowner scenarios.  6. If the destination address is an anycast address, the fast ND reply function is not supported.  7. If the destination address is an FE80 link-local address, the fast ND reply function is not supported. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After the fast ND reply function is enabled, if a LocalArpv6 resource threshold-crossing alarm is generated on an interface board, other services may fail to be restored after the interface board or device is restarted because the number of shared table resources exceeds the threshold.  Disabling ND fast reply is recommended. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Run the "ipv6 nd na anti-attack enable" command on an interface to enable interface attack defense for NA packets.  1. This command is mutually exclusive with the ipv6 nd na glean command in the interface view. As a result, neighbor relationship generation on the backup device is affected in ND dual-sending scenarios.  2. After NA attack defense is configured, the local device discards gratuitous NA packets sent by the remote device for MAC address update, affecting neighbor update. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| NA message attack defense does not support VBDIF interfaces, VE sub-interfaces, or global VE sub-interfaces. For interfaces and boards that are not supported, NA messages are directly sent to the CPU. As a result, the CPU resources of the device may be greatly consumed in neighbor entry learning and response, affecting the processing of other services. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
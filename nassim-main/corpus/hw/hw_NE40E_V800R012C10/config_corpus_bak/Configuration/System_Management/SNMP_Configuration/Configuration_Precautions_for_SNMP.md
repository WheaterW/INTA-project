Configuration Precautions for SNMP
==================================

Configuration_Precautions_for_SNMP

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Each independent admin VS allows a maximum of three target hosts to enable the private VB function. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| SNMPv1 does not support GetBulk operations or Inform alarms. IPv6 networks do not support Inform alarms. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| If the NMS frequently accesses a device (for example, the access frequency set on the NMS is high or multiple NMSs access the device), the CPU usage may increase and the device may respond slowly to the NMS. In this case, you can reduce the access frequency of the NMS to ensure that the device can respond to the SNMP packets sent by the NMS in a timely manner. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When the number of nodes in the SNMP IP address locking list exceeds 512, the device stops processing SNMP packets. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| SNMPv3 is recommended because it is more secure than SNMPv1 and SNMPv2c. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| SNMPv1 does not support the GetBulk operation. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The port number and authentication parameters configured on the NMS must be the same as those on the device, and the SNMP version used on the NMS must be enabled on the device; otherwise, the NMS cannot manage the device. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| The default aging time of the SNMP get-next/get-bulk query cache is 5 seconds. Within the 5 seconds, the data in the cache may have been deleted or the value may have changed in the DB or APP component. However, SNMP cannot detect this situation, the data in the buffer is still returned to the NMS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
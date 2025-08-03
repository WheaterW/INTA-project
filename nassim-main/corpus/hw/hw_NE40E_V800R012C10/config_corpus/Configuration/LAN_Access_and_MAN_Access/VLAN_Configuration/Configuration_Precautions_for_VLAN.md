Configuration Precautions for VLAN
==================================

Configuration Precautions for VLAN

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| In actual applications, the trunk interface transparently transmits packets of all VLANs. Therefore, do not use the port trunk allow-pass vlan all command. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When the mapping VLAN or stacking VLAN goes Down, protocol packets sent to the outbound interface can be transparently transmitted. As a result, traffic from the remote device may be incorrectly sent to the local device and then discarded. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In a VLANIF IP FRR scenario, if the primary outbound interface is a VLANIF interface and fails, FRR cannot rapidly switch traffic to the backup outbound interface. Traffic can be restored only when routes are hard converged to the backup outbound interface. Packet loss occurs during the switchover. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| VLANs cannot support the Layer 3 function of VLANIF interfaces after the port vlan-mapping and port vlan-stacking commands are configured.  Do not configure VLANIF Layer 3 services after the port vlan-mapping and port vlan-stacking commands are configured. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
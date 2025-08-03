Configuration Precautions for ACL
=================================

Configuration_Precautions_for_ACL

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| By default, interface-based ACLs do not take effect for Layer 3 reserved multicast protocol packets.  You are advised to run the "traffic-policy match-protocol-type mc-reserved" command to configure interface-based ACL matching. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
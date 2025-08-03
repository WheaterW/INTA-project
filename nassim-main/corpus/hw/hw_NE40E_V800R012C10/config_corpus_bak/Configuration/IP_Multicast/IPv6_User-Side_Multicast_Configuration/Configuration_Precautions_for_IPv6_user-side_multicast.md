Configuration Precautions for IPv6 user-side multicast
======================================================

Configuration_Precautions_for_IPv6_user-side_multicast

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| IPv6 user-side multicast replication by interface or VLAN.  1. After user-based multicast replication and port-VLAN-based multicast replication are configured on a BRAS sub-interface, some online IPoX users are interrupted when ordering programs. The configuration takes effect only after the users order the programs again.  2. If replication based on user aggregation and then replication based on port VLAN are configured on a BRAS sub-interface, the ordered programs of an online IPoX user are interrupted. The configuration takes effect only after the user orders the programs again. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| IPv6 user-side multicast does not support IPv6 user multicast VPN. As a result, user-side multicast cannot be generated. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| User-side multicast does not support global VE interfaces. The function does not take effect after being configured. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
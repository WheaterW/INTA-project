Configuration Precautions for Mirroring
=======================================

Configuration_Precautions_for_Mirroring

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The port mirroring filtering rules delivered by the RADIUS server support only IPv4 traffic mirroring but not IPv6 traffic mirroring.  Non-Ethernet packets do not support filtering rules. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Traffic of users who go online through VE interfaces cannot be mirrored. | NE40E-M2 | NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In a low-speed APS 1+1 TDM PWE3 scenario, when inbound mirroring is configured on a public network interface, traffic fails to be mirrored. | NE40E-M2 | NE40E-M2K-B |
| The main interface's configuration about packet label removing also applies to its sub-interfaces, regardless of whether the main interface and the sub-interfaces are in the same independent VS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| After port mirroring is configured on a main interface, the configuration also takes effect for its sub-interfaces, regardless of whether the main interface and sub-interfaces are in the same independent VS. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Packets mirrored from POS or CPOS interfaces on CR5D00C4CF71 subcards carry special 8484 Ethernet frame headers, and the packet payload is the same as that of the forwarded packets. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K |
| When the mirroring function is used to mirror packets of a certain protocol, the protocol cannot be enabled on the corresponding observing port. Otherwise, a connection fails to be set up through this protocol, which may cause interface flapping.  Properly plan services. If protocol packets need to be mirrored, do not enable the protocol on the observing port. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
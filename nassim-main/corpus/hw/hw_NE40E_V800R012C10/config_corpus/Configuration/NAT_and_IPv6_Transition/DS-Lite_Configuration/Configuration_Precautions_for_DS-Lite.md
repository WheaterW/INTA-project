Configuration Precautions for DS-Lite
=====================================

Configuration Precautions for DS-Lite

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| In the DS-Lite scenario, if multiple instances are configured with the same local IP address for load balancing, ACLs must be configured to direct different traffic to different instances. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
| In a DS-Lite dynamic load balancing scenario, if a CPU in an instance recovers from a fault or a load balancing member is added to the instance, some centralized users on the original CPU are switched to the new CPU, and traffic needs to be interrupted and re-established.  When address resources are sufficient, users that are not switched to the new CPU are not affected. When address resources are insufficient and address resources are reclaimed using the idle address reclamation, traffic of centralized users that are not switched to the new CPU may be interrupted and re-established. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
| In a DS-Lite inbound-interface traffic policy scenario, when an ACL is associated with an instance, the address wildcard in the ACL rule does not support inconsecutive subnet masks (0s and 1s in a subnet mask, such as 255, 0.255, and 0). The subnet mask must be consecutive. That is, the 0s and 1s in the subnet mask must be consecutive, for example, 255, 255, 255, and 0. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
| When centralized DS-Lite providing backup for centralized DS-Lite is deployed, different NAT public addresses must be configured for the two centralized DS-Lite devices. Plan services properly. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
| In a distributed DS-Lite scenario, the prefix length configured in an instance must be the same as the prefix length in the IPv6 address pool of the BRAS to which users access. If they are inconsistent, users fail to go online. | NE40E-M2 | NE40E-M2K/NE40E-M2K-B |
Applying a Layer 2 ACL
======================

Layer 2 ACLs can be used in QoS services.

#### Context

[Table 1](#EN-US_TASK_0172364605__tab_dc_vrp_acl4_cfg_008101) describes the typical applications of Layer 2 ACLs.

**Table 1** Typical applications of Layer 2 ACLs
| Typical Application | Usage Scenario | Operation |
| --- | --- | --- |
| QoS | To process different types of traffic, users can configure a Layer 2 ACL to perform traffic policing, traffic shaping, or traffic classification on traffic that matches the ACL rules. | To find out more about the procedures for processing different types of traffic, see how to configure traffic policing, traffic shaping, and traffic behaviors. |



#### Typical Cases of Applying a Layer 2 ACL

**Cases of applying a Layer 2 ACL in QoS services**

For example, a user configures a device as follows:

* Configuring an Ethernet frame header-based ACL in firewall traffic behavior (packet filtering)
  ```
  acl number 4001
   rule permit 8021p 3 source-mac 1-1-1 ffff-ffff-ffff
   rule 10 deny 
  traffic classifier acl 
   if-match acl 4001
  traffic behavior test
   permit
  traffic policy test
   classifier acl behavior test
  interface GigabitEthernet0/2/0
   traffic-policy test inbound
  ```
  
  Matching result: Only VLAN packets with the 802.1p priority 3 in the outer VLAN tag, source MAC address 1-1-1, and source MAC address mask ffff-ffff-ffff are permitted.
* Configuring an Ethernet frame header-based ACL in common traffic behavior
  ```
  acl number 4001
   rule permit 8021p 3 source-mac 1-1-1 ffff-ffff-ffff
   rule 10 deny 
  traffic classifier acl 
   if-match acl 4001
  traffic behavior test
   remark 8021p 7
  traffic policy test
   classifier acl behavior test
  interface GigabitEthernet0/2/0
   traffic-policy test inbound
  ```
  
  Matching result: Only VLAN packets with the 802.1p priority 3 in the outer VLAN tag, source MAC address 1-1-1, and source MAC address mask ffff-ffff-ffff are permitted, and the packets' 802.1p priority is re-marked 7.
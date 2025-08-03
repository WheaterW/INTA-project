Applying an MPLS-based ACL
==========================

MPLS-based ACLs can be used in QoS services.

#### Context

[Table 1](#EN-US_TASK_0172364632__tab_dc_vrp_acl4_cfg_006901) describes the typical applications of MPLS-based ACLs.

**Table 1** Typical applications of MPLS-based ACLs
| Typical Application | Usage Scenario | Operation |
| --- | --- | --- |
| QoS services | To process different types of traffic, configure an MPLS-based ACL to perform traffic policing, traffic shaping, or traffic classification on traffic that matches the ACL rules. | For details on how to process different types of traffic, see Configuring the Traffic Policing Policy, Configuring Traffic Shaping, and Configuring Traffic Behaviors. |



#### Typical Cases of Applying an MPLS-based ACL

**Cases of applying an MPLS-based ACL in QoS services**

For example, a user configures a device as follows:

* Configuring an MPLS-based ACL in firewall traffic behavior (packet filtering)
  ```
  acl number 10001
   rule 5 permit exp 3 label 2048 ttl eq 23
   rule 10 deny 
  traffic classifier acl 
   if-match acl 10001
  traffic behavior test
   permit
  traffic policy test
   classifier acl behavior test
  interface GigabitEthernet0/2/0
   traffic-policy test inbound
  ```
  
  Matching result: Only MPLS packets with the EXP value 3, label value 2048, and TTL value 23 are permitted.
* Configuring an MPLS-based ACL in common traffic behavior
  ```
  acl number 10001
   rule 5 permit exp 3 label 2048 ttl eq 23
   rule 10 deny 
  traffic classifier acl 
   if-match acl 10001
  traffic behavior test
   remark mpls-exp 7
  traffic policy test
   classifier acl behavior test
  interface GigabitEthernet0/2/0
   traffic-policy test inbound
  ```
  
  Matching result: Only MPLS packets with the EXP value 3, label value 2048, and TTL value 23 are permitted, and the packet EXP value is re-marked 7.
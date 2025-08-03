Configuring an MPLS-based ACL
=============================

An MPLS-based ACL defines rules to filter packets.

#### Usage Scenario

An MPLS-based ACL filters packets based on the EXP, label, and TTL values of MPLS packets.

**Figure 1** Configuring an MPLS-based ACL  
![](figure/en-us_image_0000001526330480.png)

As shown in [Figure 1](#EN-US_TASK_0172364625__fig_dc_vrp_acl4_cfg_006601), an MPLS-based ACL is created for QoS services on DeviceD to allow DeviceD to allocate 54000 bit/s bandwidth to the MPLS packets with an EXP value smaller than 3 sent from Network A and to allocate 8000 bit/s bandwidth to the MPLS packets with an EXP value greater than 3 sent from Network B.


[Creating an MPLS-based ACL](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0067.html)

You can create an MPLS-based ACL and configure parameters for the ACL.

[Configuring an MPLS-based ACL Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0068.html)

MPLS-based ACL rules are defined based on MPLS packets' EXP, label, or TTL values to filter packets.

[Applying an MPLS-based ACL](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0069.html)

MPLS-based ACLs can be used in QoS services.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0070.html)

After configuring an MPLS-based ACL, verify the configuration.
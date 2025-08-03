Configuring an Advanced ACL6
============================

An advanced ACL6 defines rules to filter packets.

#### Usage Scenario

**Figure 1** Configuring an advanced ACL6  
![](images/fig_dc_vrp_acl6_cfg_005401.png "Click to enlarge")

As shown in [Figure 1](#EN-US_TASK_0172365065__fig_dc_vrp_acl6_cfg_005401), an advanced ACL6 is created on DeviceD to allow DeviceD to permit all ICMPv6 packets sent from Network B to Network C and deny all ICMPv6 packets sent from Network A to the Network C.


[(Optional) Creating a Validity Period for an ACL6 Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0055.html)

You can create a validity period for an ACL6 rule to control network traffic in a specified period.

[Creating an Advanced ACL6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0056.html)

You can create an advanced ACL6 and configure parameters for the ACL6.

[(Optional) Configuring an ACL IPv6 Address Pool](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0069.html)

This section describes how to configure an ACL IPv6 address pool to filter packets based on the source IPv6 addresses of BGP peers.

[Configuring an Advanced ACL6 Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0057.html)

Advanced ACL6 rules are defined based on the source IPv6 address, destination IPv6 address, protocol type carried over IPv6, source port, and destination port to filter packets.

[Applying an Advanced ACL6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0058.html)

Advanced ACL6s can be used in multicast packet filtering, QoS services, and routing policies.

[Verifying the Configuration of an Advanced ACL6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0059.html)

After configuring an advanced ACL6, verify the configuration.
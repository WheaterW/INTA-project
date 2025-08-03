Configuring a Layer 2 ACL
=========================

A Layer 2 ACL defines rules to filter packets.

#### Usage Scenario

A Layer 2 ACL is used to filter packets based on the source MAC address, destination MAC address, Ethernet frame protocol type, and VLAN ID.

**Figure 1** Configuring a Layer 2 ACL  
![](figure/en-us_image_0000001576970093.png)

As shown in [Figure 1](#EN-US_TASK_0172364597__fig_dc_vrp_acl4_cfg_007701), a Layer 2 ACL is created on DeviceD to deny all packets sent from a host (MAC address 1-1-1) connected to DeviceA to DeviceC and to permit all packets sent from a host (MAC address 2-1-1) connected to DeviceB to DeviceC.


[(Optional) Creating a Validity Period in Which an ACL Rule Takes Effect](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0078.html)

You can create a validity period in which an ACL rule takes effect to control network traffic in a specified period.

[Creating a Layer 2 ACL](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0079.html)

You can create a Layer 2 ACL and configure parameters for the ACL.

[Configuring Rules for a Layer 2 ACL](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0080.html)

This section describes how to configure rules for a Layer 2 ACL.

[Applying a Layer 2 ACL](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0081.html)

Layer 2 ACLs can be used in QoS services.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0082.html)

After configuring a Layer 2 ACL, verify the configuration.
Configuring a Basic ACL
=======================

A basic ACL defines rules to filter packets.

#### Usage Scenario

**Figure 1** Configuring a basic ACL![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001577089877.png)

As shown in [Figure 1](#EN-US_TASK_0172364575__fig_dc_vrp_acl4_cfg_004801), a basic ACL is created on DeviceA to allow DeviceA to permit all packets sent from Network A to the Internet and deny all packets sent from Network B and Network C to the Internet.


[(Optional) Creating a Validity Period for an ACL Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0049.html)

You can create a validity period for an ACL rule to control network traffic in a specified period.

[Creating a Basic ACL](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0050.html)

You can create a basic ACL and configure parameters for the ACL.

[Configuring a Basic ACL Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0051.html)

Basic ACL rules are defined based on whether the packets are the first fragments, packets' source IP addresses, and VPN instances to filter packets. 

[Applying a Basic ACL](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0052.html)

Basic ACLs can be used in device management, routing policies, multicast packet filtering, and QoS services.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0053.html)

After configuring a basic ACL, verify the configuration.
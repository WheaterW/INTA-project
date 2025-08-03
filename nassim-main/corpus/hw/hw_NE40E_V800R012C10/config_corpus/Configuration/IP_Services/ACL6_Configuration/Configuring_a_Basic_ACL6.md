Configuring a Basic ACL6
========================

A basic ACL6 defines rules to filter packets.

#### Usage Scenario

**Figure 1** Typical application of a basic ACL6![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_acl6_cfg_004801.png)

As shown in [Figure 1](#EN-US_TASK_0172365055__fig_dc_vrp_acl6_cfg_004801), a basic ACL6 is created on DeviceA to allow DeviceA to permit all packets sent from Network A to the Internet and deny all packets sent from Network B and Network C to the Internet.


[(Optional) Creating a Validity Period for an ACL6 Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0049.html)

You can create a validity period for an ACL6 rule to control network traffic in a specified period.

[Creating a Basic ACL6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0050.html)

You can create a basic ACL6 and configure parameters for the ACL6.

[Configuring a Basic ACL6 Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0051.html)

Basic ACL6 rules are defined based on whether the packets are the first fragments, packets' source IP addresses, and VPN instances to filter packets. 

[Applying a Basic ACL6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0052.html)

Basic ACL6s can be used in device management, QoS services, multicast packet filtering, and routing policies.

[Verifying the Configuration of a Basic ACL6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0053.html)

After configuring a basic ACL6, verify the configuration.
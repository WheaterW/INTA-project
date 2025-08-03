Configuring an Interface-based ACL6
===================================

An interface-based ACL6 defines rules to filter packets.

#### Usage Scenario

**Figure 1** Typical application of an interface-based ACL6![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents GE 0/1/0.


  
![](images/fig_dc_vrp_acl6_cfg_004301.png)

As shown in [Figure 1](#EN-US_TASK_0172365046__fig_dc_vrp_acl6_cfg_004301), an ACL6 based on interface 1 is created on DeviceA to allow DeviceA to permit all the packets sent from Network A to the Internet and deny all packets sent from Network B to the Internet.


[(Optional) Creating a Validity Period for an ACL6 Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0044.html)

You can create a validity period for an ACL6 rule to control network traffic in a specified period.

[Creating an Interface-based ACL6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0045.html)

You can create an interface-based ACL6 and configure parameters for the ACL6.

[Configuring an Interface-based ACL6 Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0046.html)

Interface-based ACL6 rules are defined based on packets' inbound interfaces to filter packets.

[Verifying the Configuration of an Interface-based ACL6](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl6_cfg_0047.html)

After configuring an interface-based ACL6, verify the configuration.
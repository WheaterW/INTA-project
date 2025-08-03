Configuring an Interface ACL
============================

An interface ACL defines rules to filter packets.

#### Usage Scenario

**Figure 1** Configuring an interface ACL![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001577089729.png)

As shown in [Figure 1](#EN-US_TASK_0172364566__fig_dc_vrp_acl4_cfg_004301), an ACL based on GE 0/1/0 is created on DeviceA to allow DeviceA to permit all packets sent from Network A to the Internet and deny all packets sent from Network B to the Internet.


[(Optional) Creating a Validity Period for an ACL Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0044.html)

You can create a validity period for an ACL rule to control network traffic in a specified period.

[Creating an Interface ACL](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0045.html)

You can create an interface ACL and configure parameters for the ACL.

[Configuring an Interface-based ACL Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0046.html)

Interface-based ACL rules are defined based on packets' inbound interfaces to filter packets.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0047.html)

After configuring an interface ACL, verify the configuration.
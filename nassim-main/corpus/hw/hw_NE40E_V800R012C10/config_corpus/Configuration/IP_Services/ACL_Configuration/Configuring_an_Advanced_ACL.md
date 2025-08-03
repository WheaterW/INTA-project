Configuring an Advanced ACL
===========================

An advanced ACL defines rules to filter packets.

#### Usage Scenario

**Figure 1** Configuring an advanced ACL  
![](images/fig_dc_vrp_acl4_cfg_005401.png)

As shown in [Figure 1](#EN-US_TASK_0172364585__fig_dc_vrp_acl4_cfg_005401), an advanced ACL is created on DeviceD to allow DeviceD to permit all ICMP packets sent from Network B to Network C and deny all ICMP packets sent from Network A to the Network C.


[(Optional) Creating a Validity Period for an ACL Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0055.html)

You can create a validity period for an ACL rule to control network traffic in a specified period.

[Creating an Advanced ACL](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0056.html)

You can create an advanced ACL and configure parameters for the ACL.

[(Optional) Configuring an ACL IP Address Pool](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0089.html)

An ACL IP address pool is applicable to the scenario in which multiple IP addresses need to be matched and reduces the configuration workload.

[(Optional) Configuring an ACL Port Pool](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0103.html)

When multiple port numbers need to be matched to ACL rules, you can configure an ACL port pool to reduce the configuration workload.

[Configuring an Advanced ACL Rule](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0057.html)

Advanced ACL rules are defined based on packets' source IP address, destination IP address, protocol type carried over IP, source port, and destination port to filter packets.

[Applying an Advanced ACL](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0058.html)

Advanced ACLs can be used in device management, routing policies, multicast packet filtering, and QoS services.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_acl4_cfg_0059.html)

After configuring an advanced ACL, verify the configuration.
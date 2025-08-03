Maintaining NAT
===============

You can configure NAT maintainability to strengthen the device administrator's capability to monitor NAT services in real time.

#### Usage Scenario

The following functions can be configured to maintain NAT:

* NAT logs: Flow logs record NAT user and translation information. They also help a device monitor and record private network access to public networks.
* NAT alarms: A device can be configured to generate alarms if the number of established NAT sessions or assigned NAT ports reaches a specified alarm threshold. After obtaining alarm information, the device administrator can add NAT service boards or modify service configurations.


#### Prerequisites

Before you configure NAT maintainability, complete the following tasks:

* Configure basic NAT functions.
* Configure NAT for traffic.


[Configuring the NAT Log Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0047.html)

You can configure the NAT log function to record NAT operation information in real time, which strengthens device maintainability.

[Configuring the NAT Alarm Function](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0048.html)

You can configure the NAT alarm function to strengthen the device administrator's capability to monitor NAT services in real time.

[Enabling NAT Statistics Collection](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0050_1.html)

Before checking the usage of IP addresses in an address pool and the number of packets and bytes matching ACL rules in the traffic diversion policy on the outbound interface, enable the NAT statistics collection function. Perform the following steps on the NE40E:

[Locking a NAT Address Segment](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0083_1.html)

Locking an address segment that is faulty or needs to be reclaimed can prevent user offline. This function is applicable to both the centralized and distributed scenarios.

[Deleting NAT Statistics](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0049.html)

Run the following [**reset**](cmdqueryname=reset) command in the user view to delete NAT statistics.

[Clearing NAT Session Entries](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0063.html)

This section describes how to use the [**reset**](cmdqueryname=reset) command to clear NAT session entries.

[Clearing User Information from a NAT Address Segment](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0084_1.html)

This section describes how to use the **reset** command to clear user information from a locked NAT address segment.

[Monitoring the NAT Operating Status](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_nat_cfg_0051.html)

You can use [**display**](cmdqueryname=display) commands to monitor the NAT operating status.
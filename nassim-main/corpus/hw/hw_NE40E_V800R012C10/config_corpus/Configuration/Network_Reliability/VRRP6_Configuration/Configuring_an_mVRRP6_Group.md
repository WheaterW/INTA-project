Configuring an mVRRP6 Group
===========================

mVRRP6 is used when multiple VRRP6 groups coexist. mVRRP6 helps decrease the number of VRRP6 Advertisement packets to be sent and minimize network bandwidth consumption.

#### Usage Scenario

**Figure 1** mVRRP6  
![](images/fig_dc_vrp_vrrp6_cfg_010801.png)  

As shown in [Figure 1](#EN-US_TASK_0172361861__fig_dc_vrp_vrrp6_cfg_010801), the switch is dual-homed to two Devices to improve the network reliability. Multiple VRRP6 groups can be configured on the two Devices to transmit various types of services. Each VRRP6 group maintains its own state machine, which causes the Devices to exchange a large number of VRRP6 Advertisement packets.

To simplify VRRP6 operations and decrease bandwidth consumption, configure a VRRP6 group as an mVRRP6 group and bind other common VRRP6 groups to the mVRRP6 group. The mVRRP6 group determines the status of the common VRRP6 groups.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Multiple common VRRP6 groups can be bound to an mVRRP6 group. An mVRRP6 group cannot be bound to another mVRRP6 group.
* An mVRRP6 group provides the following functions:
  + When the mVRRP6 group functions as a gateway, it determines the master/backup status of devices in the group and transmits service packets.
  + When the mVRRP6 group does not function as a gateway, it determines the master/backup status of devices in the group but does not transmit service packets.


#### Pre-configuration Tasks

Before configuring an mVRRP6 group, complete the following tasks:

* Configure network layer attributes for interfaces to ensure network connectivity.
* [Configure basic VRRP6 functions](dc_vrp_vrrp6_cfg_0103.html) if the mVRRP6 group functions as a gateway.


[Creating an mVRRP6 Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp6_cfg_0109.html)

You can create an mVRRP6 group and bind common VRRP6 groups to the mVRRP6 group. The mVRRP6 group determines the master/backup status of the common VRRP6 groups.

[Binding a Common VRRP6 Group to an mVRRP6 Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp6_cfg_0110.html)

A common VRRP6 group can be bound to an mVRRP6 group. The mVRRP6 group determines the master/backup status of the common VRRP6 group.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp6_cfg_0111.html)

After configuring an mVRRP6 group, verify the binding between the common VRRP6 and mVRRP6 groups and verify the configurations.
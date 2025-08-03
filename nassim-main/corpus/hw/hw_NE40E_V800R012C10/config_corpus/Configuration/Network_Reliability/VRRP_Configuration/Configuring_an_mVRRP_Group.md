Configuring an mVRRP Group
==========================

mVRRP is used when multiple VRRP groups coexist. mVRRP helps decrease the number of VRRP Advertisement packets to be sent and minimize network bandwidth consumption.

#### Usage Scenario

**Figure 1** mVRRP  
![](images/fig_dc_vrp_vrrp_cfg_011001.png)  

[Figure 1](#EN-US_TASK_0172361763__fig_dc_vrp_vrrp_cfg_011001) shows mVRRP. At the aggregation layer on a MAN, a switch is usually dual-homed to two Devices. Multiple VRRP groups can be configured on the two Routers to transmit various types of services. Each VRRP group maintains its own state machine, which causes the Routers to exchange a lot of VRRP Advertisement packets.

To simplify VRRP operations and decrease bandwidth consumption, configure a VRRP group as an mVRRP group and bind other service VRRP groups to the mVRRP group. The mVRRP group determines the status of the service VRRP groups.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* Multiple service VRRP groups can be bound to an mVRRP group. An mVRRP group cannot be bound to another mVRRP group.
* An mVRRP group provides the following functions:
  + When the mVRRP group functions as a gateway, it determines the master/backup status of devices in the group and transmits service packets.
  + When the mVRRP group does not function as a gateway, it determines the master/backup status of devices in the group but does not transmit service packets.

A common VRRP group, VRRP-disabled interface, or service pseudo wire (PW) can be bound to an mVRRP group. With mVRRP binding configured, problems that cannot be resolved by common VRRP groups can be solved. [Table 1](#EN-US_TASK_0172361763__tab_dc_vrp_vrrp_cfg_011001) describes objects that can be bound to an mVRRP group and usage scenarios.

**Table 1** Objects that can be bound to an mVRRP group and usage scenarios
| Object | Usage Scenario |
| --- | --- |
| Common VRRP group | If multiple VRRP groups are configured to forward traffic, large numbers of VRRP Advertisement packets are generated, which consumes network bandwidth resources and affects CPU performance. To resolve this issue, configure an mVRRP group and bind common VRRP groups to the mVRRP group. The mVRRP group sends VRRP Advertisement packets to determine the master/backup status of the common VRRP groups. |
| VRRP-disabled interface | An mVRRP group can be bound to VRRP-disabled interfaces. A master/backup mVRRP switchover can trigger an active/standby switchover on these interfaces, preventing traffic loss. |
| Service PW | An mVRRP group can be bound to service PWs. A master/backup mVRRP switchover can trigger a primary/secondary switchover on these service PWs, preventing traffic loss. |




#### Pre-configuration Tasks

Before configuring an mVRRP group, complete the following tasks:

* Configure network layer attributes for interfaces to ensure network connectivity.
* [Configure basic VRRP functions](dc_vrp_vrrp_cfg_0104.html) if the mVRRP group functions as a gateway.


[Creating an mVRRP Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0111.html)

You can create an mVRRP group. Other common VRRP groups can be bound to the mVRRP group and become service VRRP groups. The mVRRP group determines the master/backup status of the service VRRP groups.

[Configuring Bindings for an mVRRP Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0142.html)

VRRP groups, service interfaces, and service PWs can be bound to an mVRRP group. After the bindings are configured, the mVRRP group determines the status of the bound objects.

[Verifying the mVRRP Group Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0113.html)

You can view the status of an mVRRP group and verify the configuration.
Configuring VRRP6 Association
=============================

This section describes how to configure VRRP6 association. If a network link fails, VRRP6 association enables a VRRP6 group to rapidly perform a master/backup VRRP6 switchover, thereby ensuring correct service traffic forwarding.

#### Usage Scenario

A VRRP6 group uses VRRP6 Advertisement packets to negotiate the master/backup VRRP6 status. If a network fault occurs (for example, an interface goes down or a link fails) or a network is modified, a VRRP6 group cannot promptly detect the fault or modification, delaying a master/backup VRRP6 switchover from being performed. To resolve this issue, configure VRRP6 association. If an object associated with a VRRP6 group fails, the VRRP6 group is notified of the fault and performs a master/backup VRRP6 switchover. VRRP6 association ensures service continuity and link reliability.

**Table 1** Objects with which a VRRP6 group is associated and usage scenarios
| Association Type | Object | Usage Scenario |
| --- | --- | --- |
| A VRRP6 group monitors the status of certain feature. If the monitored object's status changes, the VRRP6 group is notified of the status change and performs a master/backup VRRP6 switchover. | Specified interface | A VRRP6 group checks status changes only for the interface on which the VRRP6 group is configured. You can associate a VRRP6 group with a specified interface that is not in the VRRP6 group. If the status of the monitored interface changes, the VRRP6-enabled devices change the VRRP6 priorities and elect a master device. |
| Specified interface monitoring group | To enable a VRRP6 group to track more uplink interfaces, associate the VRRP6 group with an interface monitoring group. If the rate of link failures within the interface monitoring group reaches a specified threshold, the VRRP6 group performs a master/backup switchover to ensure reliable service transmission. |
| Specified route | If an uplink route to a network becomes unreachable, user hosts cannot detect the change and still use the route to transmit traffic, potentially resulting in the loss of service traffic. In this case, configure a VRRP6 group to track the uplink route. If the uplink route is withdrawn or becomes inactive, the VRRP6 group is instructed to reduce the master's priority in order to trigger a master/backup switchover. |
| Specified route monitoring group | To enable a VRRP6 group to track more uplink routes, associate the VRRP6 group with a route monitoring group. If the rate of route failures within the route monitoring group reaches a specified threshold, the VRRP6 group performs a master/backup switchover to ensure reliable service transmission. |
| BFD | BFD can rapidly detect link faults. You can associate a VRRP6 group with a BFD session. If a link fault occurs, BFD detects the fault, changes the BFD session status, and notifies the VRRP6 group of the fault. This process triggers a rapid master/backup VRRP6 switchover. |



#### Pre-configuration Tasks

Before configuring VRRP6 association, complete the following tasks:

* Configure basic VRRP6 group functions.
* Configure common static BFD sessions or static BFD sessions with automatically negotiated discriminators.


[Configuring Association Between VRRP6 and Interface Status](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp6_cfg_0121.html)

This section describes how to associate a VRRP6 group with a VRRP6-disabled interface on the master device. If the master device detects that the status of the VRRP6-disabled interface changed, it rapidly performs a master/backup VRRP6 switchover.

[Configuring a VRRP6 Group to Track an Interface Monitoring Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp6_cfg_0142.html)

This section describes how to configure a VRRP6 group to track an interface monitoring group so that the VRRP6 group rapidly performs a master/backup switchover when the uplink interface status changes. This prevents service interruptions caused by uplink interface faults.

[Associating VRRP6 with IPv6 BFD to Implement a Rapid Master/Backup VRRP6 Switchover](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp6_cfg_0122.html)

You can associate a VRRP6 group with an IPv6 BFD session. If the status of the IPv6 BFD session changes, IPv6 BFD notifies the VRRP6 group of the change. After receiving the notification, the VRRP6 group rapidly performs a master/backup VRRP6 switchover.

[Configuring Association Between VRRP6 and Route Status](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp6_cfg_0129.html)

A VRRP6 group can be configured to track the status of an uplink route. If the tracked route is withdrawn or becomes inactive, the VRRP6 group is notified of the change and rapidly performs a master/backup VRRP6 switchover. This shortens the duration of traffic interruptions.

[Configuring a VRRP6 Group to Track a Route Monitoring Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp6_cfg_0146.html)

This section describes how to configure a VRRP6 group to track a route monitoring group. By tracking a route monitoring group, the VRRP6 group can perform a master/backup switchover after a specified number of routes in the route monitoring group are withdrawn or deactivated. This shortens the duration of traffic interruptions.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp6_cfg_0123.html)

After associating a VRRP6 group with a VRRP6-disabled interface or a BFD session, verify the configurations.
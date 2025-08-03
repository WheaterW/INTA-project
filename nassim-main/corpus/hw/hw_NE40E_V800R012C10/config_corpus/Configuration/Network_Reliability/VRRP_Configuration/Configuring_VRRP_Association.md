Configuring VRRP Association
============================

VRRP association helps a VRRP group rapidly perform a master/backup VRRP switchover if a network link fails. VRRP association ensures user data forwarding.

#### Usage Scenario

If an interface or a link fails or the network topology changes, devices in a VRRP group detect the change after a period of time, which delays a master/backup VRRP switchover. Although the master/backup VRRP switchover can be performed, route switching cannot be performed because no route is associated with the VRRP group. A VRRP switchover delay or route switching failure causes traffic loss.

VRRP association can prevent traffic loss. If an object associated with a VRRP group fails, the VRRP group is notified of the failure and performs a master/backup VRRP switchover. Alternatively, if a master/backup VRRP switchover is performed, the VRRP group instructs its associated object to perform a traffic switchover. The association ensures traffic forwarding and improves link reliability.

**Table 1** Objects with which VRRP is associated and usage scenarios
| Association Type | Object | Usage Scenario |
| --- | --- | --- |
| A VRRP group is associated with another feature. When a master/backup VRRP switchover is performed, the associated feature is notified of the switchover and also performs a traffic switchover. | Route priority | If a device in a VRRP group is not in the Master state, manually change the cost of the direct route on this device to allow all traffic to travel over a specified active link. |
| A VRRP group tracks an object. If the tracked object's status changes, the VRRP group is notified of the status change and performs a master/backup VRRP switchover. | Specified interface | VRRP checks status changes in interfaces only in a VRRP group. VRRP can be associated with a specified interface that is not in the VRRP group. If the monitored interface's status changes, the VRRP-enabled devices change the VRRP priorities and elect a master device. |
| A VRRP group tracks an object. If the tracked object's status changes, the VRRP group is notified of the status change and performs a master/backup VRRP switchover. | BFD | BFD can rapidly detect link faults. VRRP can be associated with BFD. If a link fault occurs, a BFD session detects the fault, changes the BFD session status, and notifies the VRRP group of the fault. This process triggers a rapid master/backup VRRP switchover. |
| A VRRP group tracks an object. If the tracked object's status changes, the VRRP group is notified of the status change and performs a master/backup VRRP switchover. | EFM | If a device does not support BFD, Ethernet in the First Mile (EFM) can be used to rapidly detect link faults. VRRP can be associated with EFM to track the EFM session status. This association allows a rapid master/backup VRRP switchover if a link fails. |
| A VRRP group tracks an object. If the tracked object's status changes, the VRRP group is notified of the status change and performs a master/backup VRRP switchover. | CFM | Connectivity fault management (CFM) provides functions, such as point-to-point connectivity fault detection, fault notification, fault verification, and fault locating. CFM can monitor the connectivity of the entire network and locate connectivity faults. CFM can also be used together with switchover techniques to improve network reliability. VRRP tracking CFM enables a VRRP group to rapidly perform a master/backup VRRP switchover when CFM detects a link fault. This implementation minimizes service interruption time. |
| A VRRP group tracks an object. If the tracked object's status changes, the VRRP group is notified of the status change and performs a master/backup VRRP switchover. | Route | A VRRP group can be associated with a specified route. VRRP-enabled interfaces can remove the network and host routes for the previous active link after a master/backup VRRP switchover is complete. This association prevents network-to-user traffic from following the unreachable route or traveling over a failed link. |
| A VRRP group tracks an object. If the tracked object's status changes, the VRRP group is notified of the status change and performs a master/backup VRRP switchover. | NQA | A VRRP group tracks a network quality analysis (NQA) test instance. If the status of the NQA test instance becomes Failed, NQA instructs the VRRP group to change a device priority, implementing a master/backup VRRP switchover. |



#### Pre-configuration Tasks

Before configuring VRRP association, complete the following tasks:

* Configure a VRRP group.
* Configure a BFD session, either a static BFD session or a static BFD session with automatically negotiated discriminators.


[Associating a VRRP Group with an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0115.html)

You can associate a VRRP group with a VRRP-disabled interface on the master device. If the master device detects that the status of the VRRP-disabled interface changes, it rapidly performs a master/backup VRRP switchover.

[Configuring a VRRP Group to Track an Interface Monitoring Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_01128.html)

This section describes how to configure a VRRP group to track an interface monitoring group so that the VRRP group rapidly performs a master/backup switchover when the uplink interface status changes. This prevents service interruptions caused by uplink interface faults.

[Associating a VRRP Group with a BFD Session to Implement a Rapid Master/Backup VRRP Switchover](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0116.html)

You can associate a VRRP group with a BFD session. If the status of a BFD session changes, BFD notifies the VRRP group of the change. After receiving the notification, the VRRP group rapidly performs a master/backup VRRP switchover.

[Associating VRRP with EFM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0136.html)

You can associate the Virtual Router Redundancy Protocol (VRRP) with Ethernet in the First Mile (EFM) to implement a rapid master/backup VRRP switchover.

[Associating a VRRP Group with an NQA Test Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0140.html)

You can associate a VRRP group with an NQA test instance. If the status of the NQA test instance becomes Failed, NQA notifies the VRRP group of the status change to implement a rapid master/backup VRRP switchover.

[Associating a VRRP Group with a Route](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0127.html)

A VRRP group can track an uplink route that is connected to a network. If the tracked route is withdrawn or becomes inactive, the VRRP group is notified of the change and rapidly performs a master/backup VRRP switchover. This process shortens traffic interruptions.

[Configuring a VRRP Group to Track a Route Monitoring Group](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_01129.html)

This section describes how to configure a VRRP group to track a route monitoring group. By tracking a route monitoring group, the VRRP group can perform a master/backup switchover after a specified number of routes in the route monitoring group are withdrawn or deactivated. This shortens the duration of traffic interruptions.

[Configuring Association Between VRRP and Direct Routes](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_01121.html)

This section describes how to associate VRRP and direct routes. In this way, the cost of the direct routes to the virtual IP network segment of the VRRP group can be adjusted based on the VRRP status.

[Verifying the VRRP Association Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vrrp_cfg_0117.html)

After configuring VRRP association, verify the configurations.
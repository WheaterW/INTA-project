Understanding Association Between VRRP and Interface Status
===========================================================

Understanding Association Between VRRP and Interface Status

#### Application Scenarios

After a VRRP group is configured, VRRP devices negotiate the master/backup state through VRRP Advertisement packets. If an interface or a link fails, or the network topology changes, devices in the VRRP group cannot immediately detect the failure or change. Consequently, the master/backup VRRP switchover is delayed. Additionally, after a master/backup VRRP switchover is complete, route switching fails to be performed because no route is associated with the VRRP group, interrupting the normal forwarding of traffic.

To resolve these problems, configure VRRP association. If an object associated with a VRRP group fails, the VRRP group is notified and performs a primary/secondary link switchover. In addition, when a master/backup VRRP switchover is performed, the VRRP group instructs its associated object to perform a switchover accordingly. VRRP association ensures proper traffic forwarding and improves link reliability.

By default VRRP detects status changes only in those interfaces where a VRRP group resides. To have VRRP detect the status changes of an interface that is not in the group, you can associate VRRP with the specified interface. Then, when the status of the interface changes, the VRRP device that monitors that interface changes its priority to allow a new master with a higher priority to be elected.


#### Fundamentals

If a VRRP-disabled interface monitored by a VRRP device goes down, the VRRP device changes its VRRP priority in either of the following modes:

* Increased mode: The VRRP device increases its VRRP priority by a specified value.
* Reduced mode: The VRRP device reduces its VRRP priority by a specified value.

In [Figure 1](#EN-US_CONCEPT_0000001176663805__fig_dc_vrp_vrrp_feature_010901), a VRRP group is configured on DeviceA and DeviceB. DeviceA is the master and forwards user-to-network traffic, and DeviceB is the backup.

DeviceA is configured to monitor interface 1. If this interface fails, DeviceA reduces its VRRP priority and sends a VRRP Advertisement packet carrying a reduced priority. After receiving the packet with a priority lower than its own, DeviceB preempts the master role and takes over traffic forwarding.

DeviceA then restores its VRRP priority to the original value after interface 1 goes up. If DeviceA works in preemption mode and receives a VRRP Advertisement packet carrying a priority lower than its own, it preempts the master role and takes over traffic forwarding.

**Figure 1** Network diagram of association between VRRP and interface status  
![](figure/en-us_image_0000001130624286.png)
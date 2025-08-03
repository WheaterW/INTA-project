Understanding Association Between VRRP6 and Interface Status
============================================================

Understanding Association Between VRRP6 and Interface Status

#### Application Scenarios

After a VRRP6 group is configured, VRRP6 devices negotiate the master/backup state through VRRP6 Advertisement packets. If an interface or a link fails, or the network topology changes, devices in the VRRP6 group cannot immediately detect the failure or change. Consequently, the master/backup VRRP switchover is delayed. To resolve this problem, configure VRRP6 association. If an object associated with a VRRP6 group fails, the VRRP6 group is notified and performs a master/backup VRRP switchover. VRRP6 association ensures proper traffic forwarding and improves link reliability.

By default VRRP6 detects status changes only in those interfaces where a VRRP6 group resides. To have VRRP6 detect the status changes of an interface that is not in the group, you can associate VRRP6 with the specified interface. Then, when the status of the interface changes, the VRRP6 device that monitors that interface changes its priority to allow a new master with a higher priority to be elected.


#### Fundamentals

If a VRRP6-disabled interface monitored by a VRRP6 device goes down, the VRRP6 device changes its priority in either of the following modes:

* Increased mode: The VRRP6 device increases its priority by a specified value.
* Reduced mode: The VRRP6 device reduces its priority by a specified value.

In [Figure 1](#EN-US_CONCEPT_0000001176661775__fig_dc_vrp_vrrp_feature_010901), a VRRP6 group is configured on DeviceA and DeviceB. DeviceA is the master and forwards user-to-network traffic, and DeviceB is the backup.

DeviceA is configured to monitor interface 1. If this interface fails, DeviceA reduces its priority and sends a VRRP6 Advertisement packet carrying a reduced priority. After receiving the packet with a priority lower than its own, DeviceB preempts the master role and takes over traffic forwarding.

DeviceA then restores its priority to the original value after interface 1 goes up. If DeviceA works in preemption mode and receives a VRRP6 Advertisement packet carrying a priority lower than its own, it preempts the master role and takes over traffic forwarding.

**Figure 1** Network diagram of association between VRRP6 and interface status  
![](figure/en-us_image_0000001176741695.png)
Understanding Association Between VRRP6 and Route Status
========================================================

Understanding Association Between VRRP6 and Route Status

#### Application Scenarios

After a VRRP6 group is configured, VRRP6 devices negotiate the master/backup state through VRRP6 Advertisement packets. If an interface or a link fails, or the network topology changes, devices in the VRRP6 group cannot immediately detect the failure or change. Consequently, the master/backup VRRP switchover is delayed. To resolve this problem, configure VRRP6 association. If an object associated with a VRRP6 group fails, the VRRP6 group is notified and performs a master/backup VRRP switchover. VRRP6 association ensures proper traffic forwarding and improves link reliability.

A VRRP6 group can monitor an uplink route. If the uplink route is withdrawn or becomes inactive, the VRRP6 group is instructed to adjust the device priority to trigger a master/backup switchover.


#### Fundamentals

A VRRP6 group can be configured to track an uplink route to determine whether the route is reachable. If the uplink route is withdrawn or becomes inactive after the uplink fails or the network topology changes, hosts on the LAN cannot access the external network through gateways. Then, after being notified of the failure or change, the master device in the VRRP6 group reduces its priority by a specified value to allow a backup device with a higher priority to preempt the master role. This process ensures uninterrupted communication between the hosts and external network. The master device in the VRRP6 group is restored to its original priority after the uplink recovers.

In [Figure 1](#EN-US_CONCEPT_0000001212421478__fig466013291353), a VRRP6 group is configured between DeviceA and DeviceB. DeviceA is the master and forwards user-to-network traffic, and DeviceB is the backup. DeviceA in the VRRP6 group is configured to track the 2001:db8:1::1 route.

When the uplink of DeviceA fails, the 2001:DB8:1::1 route becomes unreachable. As such, DeviceA reduces its priority in the VRRP6 group by a specified value so that its new priority is lower than the priority of DeviceB. DeviceB preempts the master role and takes over traffic forwarding on the Layer 3 network, thereby ensuring normal forwarding of service traffic.**Figure 1** Network diagram of configuring association between VRRP6 and route status  
![](figure/en-us_image_0000001257454671.png)

VRRP6 device configurations are as follows:

* DeviceA functions as the master in the VRRP6 group with a priority of 120.
* DeviceB works in immediate preemption mode and functions as the backup in the VRRP6 group with a priority of 100.
* The VRRP6 group on DeviceA tracks the 2001:db8:1::1/64 route. If the 2001:db8:1::1/64 route becomes unreachable, DeviceA reduces its priority by 40.

The implementation is as follows:

1. Normally, DeviceA periodically sends VRRP6 Advertisement packets to inform DeviceB that it is working properly.
2. When the uplink of DeviceA fails, the 2001:db8:1::1/64 route becomes unreachable, and the VRRP6 group is notified of the route status change. After receiving this notification, DeviceA reduces its priority to 80 (120 â 40 = 80). Because the priority of DeviceB, which is working in immediate preemption mode, is now higher than the priority of DeviceA, DeviceB immediately preempts the master role and sends gratuitous ARP packets to allow downstream devices to update address entries.
3. When the faulty link recovers, the 2001:db8:1::1/64 route becomes reachable again. DeviceA then restores its priority in the VRRP6 group to 120 (80 + 40 = 120), preempts the master role, and sends VRRP6 Advertisement and gratuitous ARP packets. After DeviceB receives the Advertisement packet carrying a priority higher than its own, it switches to the Backup state.
4. Both DeviceA and DeviceB are restored to their original states. As such, DeviceA forwards upstream traffic again.

The preceding process shows that association between a VRRP6 group and an uplink route can prevent traffic loss. In situations where the uplink route is unreachable, the VRRP6 group triggers a master/backup switchover through priority adjustment so that the backup device can take over upstream traffic.
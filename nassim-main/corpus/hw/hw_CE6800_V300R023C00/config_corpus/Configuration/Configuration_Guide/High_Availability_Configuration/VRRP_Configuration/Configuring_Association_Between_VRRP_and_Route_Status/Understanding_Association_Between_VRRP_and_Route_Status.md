Understanding Association Between VRRP and Route Status
=======================================================

Understanding Association Between VRRP and Route Status

#### Application Scenarios

After a VRRP group is configured, VRRP devices negotiate the master/backup state through VRRP Advertisement packets. If an interface or a link fails, or the network topology changes, devices in the VRRP group cannot immediately detect the failure or change. Consequently, the master/backup VRRP switchover is delayed. Additionally, after a master/backup VRRP switchover is complete, route switching fails to be performed because no route is associated with the VRRP group, interrupting the normal forwarding of traffic.

To resolve these problems, configure VRRP association. If an object associated with a VRRP group fails, the VRRP group is notified and performs a primary/secondary link switchover. In addition, when a master/backup VRRP switchover is performed, the VRRP group instructs its associated object to perform a switchover accordingly. VRRP association ensures proper traffic forwarding and improves link reliability.

A VRRP group can monitor an uplink route. If the uplink route is withdrawn or becomes inactive, the VRRP group is instructed to reduce the master's priority to trigger a master/backup VRRP switchover.


#### Fundamentals

A VRRP group can be configured to track an uplink route to determine whether the route is reachable. If the uplink route is withdrawn or becomes inactive after the uplink fails or the network topology changes, hosts on the LAN cannot access the external network through gateways. Then, after being notified of the failure or change, the master device in the VRRP group reduces its priority by a specified value to allow the backup device with a higher priority to preempt the master role. This process ensures uninterrupted communication between the hosts and external network. The master device is restored to its original priority after the uplink recovers.

In [Figure 1](#EN-US_CONCEPT_0000001176743731__fig1077233935817), a VRRP group is configured on DeviceA and DeviceB. DeviceA is the master and forwards user-to-network traffic, and DeviceB is the backup. DeviceA in the VRRP group is configured to track the 10.1.2.0/24 route.

When the uplink between DeviceA and DeviceC fails, the route to 10.1.2.0/24 becomes unreachable. As such, DeviceA reduces its VRRP priority by a specified value so that its new priority is lower than the priority of DeviceB. DeviceB preempts the master role and takes over traffic forwarding, thereby preventing user traffic loss.

**Figure 1** Network diagram of configuring association between VRRP and route status  
![](figure/en-us_image_0000001176663853.png)

VRRP device configurations are as follows:

* DeviceA functions as the master in the VRRP group with a priority of 120.
* DeviceB works in immediate preemption mode and functions as the backup in the VRRP group with a priority of 100.
* DeviceA tracks the 10.1.2.0/24 route and reduces its VRRP priority by 40 if it is notified that the route is unreachable.

The implementation is as follows:

1. Normally, DeviceA periodically sends VRRP Advertisement packets to inform DeviceB that it is working properly.
2. When the uplink between DeviceA and DeviceC fails, the 10.1.2.0/24 route becomes unreachable, and the VRRP group is notified of the route status change. After receiving this notification, DeviceA reduces its VRRP priority to 80 (120 â 40 = 80). Because the VRRP priority of DeviceB, which is working in immediate preemption mode, is now higher than the priority of DeviceA, DeviceB immediately preempts the master role and sends gratuitous ARP packets to allow DeviceE to update address entries.
3. When the faulty link recovers, the 10.1.2.0/24 route becomes reachable again. DeviceA then restores its VRRP priority to 120 (80 + 40 = 120), preempts the master role, and sends VRRP Advertisement and gratuitous ARP packets. After DeviceB receives the Advertisement packet carrying a priority higher than its own, it switches to the Backup state.
4. Both DeviceA and DeviceB are restored to their original statuses. As such, DeviceA forwards user-to-network traffic again.

The preceding process shows that association between a VRRP group and an uplink route can prevent traffic loss. In situations where the uplink route is unreachable, the VRRP group triggers a master/backup VRRP switchover through priority adjustment so that the backup device can take over user-to-network traffic.
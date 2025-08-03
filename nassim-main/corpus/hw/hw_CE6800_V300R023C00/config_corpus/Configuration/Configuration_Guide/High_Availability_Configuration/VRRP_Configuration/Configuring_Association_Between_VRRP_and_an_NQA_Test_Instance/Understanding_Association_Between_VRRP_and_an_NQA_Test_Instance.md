Understanding Association Between VRRP and an NQA Test Instance
===============================================================

Understanding Association Between VRRP and an NQA Test Instance

#### Application Scenarios

To improve network reliability, configure VRRP on a device to track the following:

* Interface status
* BFD session status

If the tracked object fails, a rapid master/backup VRRP switchover can be performed to ensure service continuity.

In [Figure 1](#EN-US_CONCEPT_0000001130784046__fig_dc_vrp_vrrp_feature_013101), however, if interface 2 on DeviceC goes down and its IP address (10.3.1.1) becomes unreachable, VRRP is unable to detect the fault. As a result, user traffic is lost.

**Figure 1** Network diagram of VRRP  
![](figure/en-us_image_0000001130624280.png)

To resolve the preceding problem, you can associate VRRP with a network quality analysis (NQA) test instance to implement rapid master/backup VRRP switchovers. With test instances configured, NQA sends probe packets to check the reachability of destination IP addresses. For the preceding example, you can configure an NQA test instance on DeviceA to check whether the IP address (10.3.1.1) of interface 2 on DeviceC is reachable.

![](public_sys-resources/note_3.0-en-us.png) 

Configure association between VRRP and an NQA test instance only on the local device (DeviceA).



#### Fundamentals

You can configure association between VRRP and an NQA test instance to monitor a gateway's cross-device uplink. If the uplink fails and hosts on the LAN cannot access the external network through the gateway, NQA instructs VRRP to reduce the gateway's priority by a specified value. This allows the backup device with a higher priority to preempt the master role, thereby ensuring uninterrupted communication between hosts on the LAN and the external network. NQA then instructs VRRP to restore the gateway's priority after the uplink recovers.

[Figure 2](#EN-US_CONCEPT_0000001130784046__fig108815382486) illustrates VRRP association with an NQA test instance.**Figure 2** Network diagram of VRRP association with an NQA test instance  
![](figure/en-us_image_0000001130784076.png)

* DeviceA and DeviceB run VRRP.
* An NQA test instance is created on DeviceA to detect the reachability of the destination IP address 10.3.1.1.
* If the status of the NQA test instance is Failed, DeviceA reduces its priority to trigger a master/backup VRRP switchover. A VRRP group can track a maximum of eight NQA test instances.

The implementation is as follows:

1. Normally, DeviceA periodically sends VRRP Advertisement packets to notify DeviceB that it is working properly and monitors the status of the NQA test instance.
2. If the uplink fails, the state of the NQA test instance changes to failed. NQA then notifies VRRP of the link detection failure, and DeviceA reduces its priority by a specified value. DeviceB, now with a priority higher than DeviceA, preempts the master role and takes over service forwarding.
3. When the uplink recovers, the state of the NQA test instance changes to success. NQA then notifies VRRP of the link detection success, and DeviceA restores its original priority. If DeviceA is configured to work in preemption mode, it preempts the master role and takes over service forwarding again after VRRP negotiation is complete.
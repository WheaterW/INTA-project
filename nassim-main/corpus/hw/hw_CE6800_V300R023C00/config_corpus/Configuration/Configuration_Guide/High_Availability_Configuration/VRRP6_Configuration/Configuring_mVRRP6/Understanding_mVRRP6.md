Understanding mVRRP6
====================

Understanding mVRRP6

#### Application Scenarios

A device is usually dual-homed to two devices for improved network reliability, and multiple VRRP6 groups can be configured on the two devices to transmit various types of services. As each VRRP6 group maintains its own state machine, a large number of VRRP6 Advertisement packets are transmitted between devices.

To reduce bandwidth and CPU resource consumption during transmission of VRRP6 Advertisement packets, you can configure a VRRP6 group as a management Virtual Router Redundancy Protocol for IPv6 (mVRRP6) group. Other VRRP6 groups are then bound to the mVRRP6 group and function as service VRRP6 groups, with only the mVRRP6 group sending VRRP6 Advertisement packets to negotiate the master/backup state of devices as shown in [Figure 1](#EN-US_CONCEPT_0000001130781998__fig_dc_vrp_vrrp_feature_010801). Service VRRP6 groups do not send VRRP6 Advertisement packets, and their master/backup states are determined by the state of the mVRRP6 group.

**Figure 1** Network diagram of mVRRP6  
![](figure/en-us_image_0000001176661777.png)

#### Related Concepts

**mVRRP6 group**

Similar to a common VRRP6 group, an mVRRP6 group also sends VRRP6 Advertisement packets to negotiate the master/backup state of VRRP6 devices. An mVRRP6 group provides the following functions:

* When the mVRRP6 group functions as a gateway, it negotiates the master/backup state of devices and transmits services.
* If the mVRRP6 group does not function as the gateway, it only negotiates the master/backup state of devices instead of transmitting services.

**Service VRRP6 group**

A common VRRP6 group becomes a service VRRP group after it is bound to an mVRRP6 group. A service VRRP6 group does not send VRRP6 Advertisement packets. The master/backup state of devices in the service VRRP6 group is determined by the state of the interface where it resides and the master/backup state of the devices in the mVRRP6 group. A common VRRP6 group can be bound to an mVRRP6 group in either of the following modes:

* Flowdown: If the mVRRP6 group enters the Backup or Initialize state, the interfaces where the service VRRP6 groups bound to the mVRRP6 group reside go down. These service VRRP6 groups then enter the Initialize state. This mode applies to networks on which both user-to-network and network-to-user traffic is transmitted over the same path. When a firewall is deployed in VRRP6 networking scenarios, it checks the paths for transmitting user-to-network and network-to-user traffic. Network-to-user traffic cannot pass through the firewall if it travels over a path different from the one used by user-to-network traffic. As a result, a backup device discards network-to-user traffic. To ensure that traffic is forwarded properly, specify the flowdown mode so that network-to-user traffic can be forwarded over the same path as user-to-network traffic.
* Unflowdown: If the mVRRP6 group enters the Backup or Initialize state, the interfaces where the service VRRP6 groups bound to the mVRRP6 group reside do not go down. These service VRRP6 groups then enter the same state as the mVRRP6 group. This mode applies to networks on which user-to-network and network-to-user traffic can be transmitted over different paths. User-to-network traffic is forwarded only through the master device, whereas network-to-user traffic can be forwarded through the master or backup device.

![](public_sys-resources/note_3.0-en-us.png) 

Multiple service VRRP6 groups can be bound to an mVRRP6 group. However, the mVRRP6 group cannot be bound to another mVRRP6 group as a service VRRP6 group.

If the interface where a service VRRP6 group resides goes down, the service VRRP group changes to the Initialize state and its state is no longer determined by the mVRRP6 group.
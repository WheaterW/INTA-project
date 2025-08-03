mode (Eth-Trunk interface view)
===============================

mode (Eth-Trunk interface view)

Function
--------



The **mode** command configures or changes the working mode of an Eth-Trunk interface.

The **undo mode** command restores the default working mode of an Eth-Trunk interface.



By default, an Eth-Trunk interface works in manual load balancing mode.


Format
------

**mode** { **lacp-static** | **lacp-dynamic** | **manual** **load-balance** }

**undo mode**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **lacp-static** | Indicates the static LACP mode. | - |
| **manual** | Indicates the manual mode. | - |
| **load-balance** | Indicates the manual load balancing mode. | - |
| **lacp-dynamic** | Indicates the dynamic Link Aggregation Control Protocol (LACP) mode. | - |



Views
-----

Layer 2 Eth-Trunk interface view,Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Currently, the device supports the following Eth-Trunk working modes:

* Dynamic LACP ModeThe source server connects to the target server through the local device. You can run the **mode lacp-dynamic** command on the local device to configure the Eth-Trunk interface to work in dynamic LACP mode to connect to the target server. If the source server is unconfigured after being restarted, LACP negotiation times out. Dynamic LACP ensures that the data obtained from the target server is successfully forwarded to the source server.If a device configured with an Eth-Trunk interface in dynamic LACP mode can receive LACPDUs from the peer device, the two devices negotiate aggregation parameters using LACPDUs. After the negotiation succeeds, the functions of the aggregated link are the same as those of the Eth-Trunk interface in static LACP mode at both ends. The dynamic LACP mode applies only to the scenario where the local device is connected to the source server. In other scenarios, the static LACP mode is recommended. If the dynamic LACP mode is deployed, loops may occur on the network.
* Static LACP modeWhen two devices that form an Eth-Trunk are directly connected and both support LACP, you can run the **mode lacp-static** command to create an Eth-Trunk interface to work in static LACP mode. In this mode, both load balancing and redundancy backup can be implemented. In static LACP mode, you must manually create an Eth-Trunk and add member interfaces to the Eth-Trunk. Different from link aggregation in manual load balancing mode, active interfaces are selected by sending LACPDUs. That is, after a group of interfaces are added to an Eth-Trunk interface, which interfaces are active and which interfaces are inactive need to be determined through LACP packet negotiation.
* Manual load balancing modeIf one of the devices at both ends of an Eth-Trunk link does not support LACP, you can run the **mode manual load-balance** command to configure the Eth-Trunk to work in manual load balancing mode and add multiple member interfaces to the Eth-Trunk to increase bandwidth and reliability. The manual load balancing mode is a basic link aggregation mode. In this mode, you need to manually create an Eth-Trunk, add interfaces to the Eth-Trunk, and specify active interfaces. LACP is not involved. In this mode, all active interfaces forward data and load balance traffic. Therefore, this mode is called load balancing mode. In manual load balancing mode, all member interfaces evenly load balance traffic. You can also set weights for member interfaces so that some interfaces can load balance more traffic. If an active link is faulty, the remaining active links in the LAG automatically share the traffic evenly or based on the weight.

**Prerequisites**



The Eth-Trunk interface has been correctly configured.Before configuring an Eth-Trunk interface to work in manual 1:1 master/backup mode, switch the Eth-Trunk interface to Layer 2 mode.



**Precautions**

If an Eth-Trunk interface does not work in manual load balancing mode, ensure that the Eth-Trunk interface does not have any member interface before changing the working mode of the Eth-Trunk interface.It is recommended that the gateway and dynamic LACP be deployed on different devices. Otherwise, LACP mode switching may cause service flapping, such as ARP, BFD, and MAC flapping.When the manual load balancing mode is switched to the LACP mode, to ensure that services are not affected, the Eth-Trunk interface mode can be successfully switched only after the 90-second protection time expires.When an Eth-Trunk interface is configured to work in lacp-dynamic mode and is in the Indep state, its member interfaces function as independent physical interfaces and inherit only the VLAN configuration of the Eth-Trunk interface. Other configurations such as Layer 2 and Layer 3 sub-interfaces are not inherited.When changing the working mode of an Eth-Trunk from manual mode to LACP mode, pay attention to the following points:

* If an Eth-Trunk interface has member interfaces, the protection time for mode switching is 90 seconds.
* During the mode switching, if the peer device does not switch the mode, the status of the local interface is the same as that before the switching.
* After the mode switching protection time expires, if the peer end does not switch the mode, the negotiation on the local interface fails, and the protocol status of the Eth-Trunk interface goes Down. As a result, services are affected.


Example
-------

# Change Eth-Trunk 1 and configure it to work in static LACP mode.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] mode lacp-static

```
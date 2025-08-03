storm suppression block outbound
================================

storm suppression block outbound

Function
--------



The **storm suppression block outbound** command configures to block unknown unicast, broadcast, or unknown multicast packets in the outbound direction of the interface.

Use the **undo storm suppression block outbound** command to cancel the blocking of unknown unicast, broadcast or unknown multicast packets in the outbound direction of the interface.



By default, the device does not block unknown multicast, broadcast, or unknown unicast packets in the outbound direction of an interface.


Format
------

**storm suppression** { **broadcast** | **multicast** | **unknown-unicast** } **block** **outbound**

**undo storm suppression** { **broadcast** | **multicast** | **unknown-unicast** } **block** **outbound**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **broadcast** | Enables storm suppression for broadcast packets. | - |
| **multicast** | Enables storm suppression for unknown multicast packets. | - |
| **unknown-unicast** | Enables storm suppression for unknown unicast packets. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, after an interface receives an unknown unicast packet, a broadcast packet, or an unknown multicast packet, it broadcasts this packet to all users in the VLAN to which this interface belongs. This may cause information leak. For example, if an unauthorized user is connected to an interface in a VLAN, the unauthorized user obtains a host's address from broadcast packets or unknown multicast and unknown unicast packets that are broadcasted and uses the address to attack the host. To prevent information leak, use the **storm suppression block outbound** command to block unknown unicast packets, broadcast packets, or unknown multicast packets on an interface if users connected to the interface do not need to receive these packets. For example, if users on an interface seldom change and require high security, you can use this command on the interface.

**Precautions**



This command is applicable only to the interfaces that do not need to receive broadcast, unknown multicast, or unknown unicast traffic. Running this command on other interfaces may affect network services. You need to use this command according to the actual situation of the network.For a specific interface, traffic suppression can be configured separately in the inbound and outbound directions of the interface without affecting each other. On an interface, you can run the **storm suppression** command to rate-limit unknown packets in the inbound direction and run the **storm suppression** command to block broadcast, unknown multicast, or unknown unicast packets in the outbound direction.




Example
-------

# Configure the interface to block broadcast packets in the outbound direction.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] storm suppression broadcast block outbound

```
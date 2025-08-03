isis silent
===========

isis silent

Function
--------



The **isis silent** command configures an IS-IS interface as a silent interface. That is, the interface is suppressed from sending and receiving IS-IS packets, but the routes to the network segment of the interface can be advertised.

The **undo isis silent** command restores the default configuration.



By default, no IS-IS interface is configured as a silent interface.


Format
------

**isis silent**

**isis silent advertise-zero-cost**

**undo isis silent**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **advertise-zero-cost** | Indicates that the route cost is 0. The default cost of IS-IS routes is 10. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When an IS-IS network is connected to other ASs, IS-IS must be enabled on the interfaces that connect the IS-IS network to other ASs so that the devices on the IS-IS network can learn the routes to other ASs. The interfaces, however, unnecessarily advertise IS-IS Hello packets on their network segments. In this situation, you can run the **isis silent** command to suppress the interfaces.

**Prerequisites**

IS-IS has been enabled using the **isis enable** command in the interface view.

**Precautions**

After this command is run on an interface, the interface does not send or receive IS-IS Hello packets or establish IS-IS neighbor relationships. If an IS-IS neighbor relationship has been established on the interface, the local device immediately disconnects the neighbor relationship, and the peer device disconnects the neighbor relationship only after the neighbor hold time expires.


Example
-------

# Configure 100GE1/0/1 as a silent interface.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis silent

```
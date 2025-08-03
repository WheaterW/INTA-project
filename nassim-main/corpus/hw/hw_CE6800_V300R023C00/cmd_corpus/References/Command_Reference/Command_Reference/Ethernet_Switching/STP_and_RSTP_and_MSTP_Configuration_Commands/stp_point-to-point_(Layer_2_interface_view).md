stp point-to-point (Layer 2 interface view)
===========================================

stp point-to-point (Layer 2 interface view)

Function
--------



The **stp point-to-point** command sets the link type of a port.

The **undo stp point-to-point** command restores the default link type.



By default,the link type of the ports on the device is auto. That is, the spanning tree protocol detects whether a port is connected to a point to point (P2P) link.


Format
------

**stp point-to-point** { **auto** | **force-false** | **force-true** }

**undo stp point-to-point**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **auto** | Indicates that the spanning tree protocol detects automatically whether the port is connected to a P2P link. | - |
| **force-false** | Indicates that the link type is non-P2P. | - |
| **force-true** | Indicates that the link type is P2P. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



On a Layer 2 network running STP, if a port of a device is connected to a non-P2P link, the port cannot perform fast status transition.If a port works in full-duplex mode, the port is connected to a P2P link, and force-true can be set in the stp point-to-point command.If a port works in half-duplex mode, run the **stp point-to-point force-true** command to forcibly set the type of the link to which the port is connected to P2P, implementing rapid network convergence.



**Configuration Impact**



The stp point-to-point command configuration on a port takes effect in all spanning tree instances where the port resides.




Example
-------

# Set the link type of 100GE1/0/1 to P2P.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[~HUAWEI-100GE1/0/1] stp point-to-point force-true

```
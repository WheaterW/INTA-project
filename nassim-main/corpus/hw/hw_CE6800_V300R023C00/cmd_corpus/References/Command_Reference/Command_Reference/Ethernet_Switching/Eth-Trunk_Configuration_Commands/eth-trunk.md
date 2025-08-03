eth-trunk
=========

eth-trunk

Function
--------

The **eth-trunk** command adds an Ethernet interface to an Eth-Trunk interface.

The **undo eth-trunk** command deletes an Ethernet interface from an Eth-Trunk interface.

By default, no Ethernet interface is added to an Eth-Trunk interface.



Format
------

**eth-trunk** *trunk-id*

**undo eth-trunk**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *trunk-id* | Specifies the ID of an Eth-Trunk interface. | The value is an integer. You can enter a question mark (?) and select a value from the displayed value range. |




Views
-----

Layer 2 100GE interface view,100GE interface view,Layer 2 10GE interface view,10GE interface view,Layer 2 200GE interface view,200GE interface view,25GE-L2 view,25GE interface view,400GE-L2 view,400GE interface view,Layer 2 50GE interface view,50GE interface view,Layer 2 GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

You can run the eth-trunk command to add physical interfaces to an Eth-Trunk interface to increase the bandwidth, improve reliability, and perform load balancing.

You can run the
**undo eth-trunk** command in the view of a member interface to delete the member interface from the Eth-Trunk interface. You can also run the
**undo trunkport** command in the Eth-Trunk interface view to delete a member interface from an Eth-Trunk interface.

**Prerequisites**

The Eth-Trunk interface to which an Ethernet interface is to be added has been created and the hardware RTU has been activated.

No service can be configured on the Ethernet interface. For example:Layer 3 configuration items such as IP addresses are not allowed.Static MAC address entries are not allowed.

**Configuration Impact**

After physical interfaces are added to an Eth-Trunk interface:

* Bandwidth is increased: The bandwidth of an Eth-Trunk interface is the total bandwidth of all member interfaces.
* Reliability is improved: When a member link fails, traffic automatically switches to other available member links. This ensures reliability of Eth-Trunk.If an Eth-Trunk interface is configured with services, interfaces added to the Eth-Trunk interface take over the services.

**Precautions**

* An Eth-Trunk consists of only Ethernet links.
* Eth-Trunk interfaces cannot be added to Eth-Trunk interfaces.
* An Ethernet interface can be added to only one Eth-Trunk interface. Before adding an Ethernet interface to another Eth-Trunk interface, you must remove it from the original Eth-Trunk interface.
* After the **lacp mixed-rate link enable** command is run, Ethernet interfaces of different rates can be added to the same Eth-Trunk interface. If no weight is configured for any member interface, the weight of each member interface is the same. In this case, the lowest forwarding capability among all member interfaces is adopted and applied to each member interface. Therefore, it is not recommended that you bundle interfaces with different forwarding capacities into an Eth-Trunk interface.
* Ethernet interfaces on different boards can be added to the same Eth-Trunk interface. If a member interface of an Eth-Trunk interface is connected to the remote device, the directly connected interface on the remote device must also be a member interface of an Eth-Trunk interface; otherwise, the local and remote devices cannot communicate with each other.
* When a physical interface is added to or removed from an Eth-Trunk interface, statistics about the Eth-Trunk member interface are cleared.



Example
-------

# Add
100GE
1/0/1 to Eth-Trunk 1.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] eth-trunk 1

```
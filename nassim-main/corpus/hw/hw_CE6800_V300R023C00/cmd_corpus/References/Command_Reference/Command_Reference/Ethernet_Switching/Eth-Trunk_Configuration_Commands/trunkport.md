trunkport
=========

trunkport

Function
--------



The **trunkport** command adds an interface to an Eth-Trunk interface in the Eth-Trunk interface view.

The **undo trunkport** command deletes an interface from an Eth-Trunk interface in the Eth-Trunk interface view.



By default, no member interface is added to an Eth-Trunk interface.


Format
------

**trunkport** *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-16>

**trunkport** *interface-name*

**undo trunkport** *interface-type* { *interface-number1* [ **to** *interface-number2* ] } &<1-16>

**undo trunkport** *interface-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-number1* | Specifies the start number of the Eth-Trunk interface. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **to** *interface-number2* | Specifies the end number of the Eth-Trunk interface. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **trunkport** *interface-name* | Specifies the name of the interface that is added to the Eth-Trunk interface. | The value is a string of 1 to 49 case-sensitive characters. It cannot contain spaces. |
| **trunkport** *interface-type* | Specifies the type of the interface that is added to the Eth-Trunk interface. | - |



Views
-----

Layer 2 Eth-Trunk interface view,Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To increase bandwidth, improve reliability, and implement load balancing, you can run this command to add physical interfaces to an Eth-Trunk interface in batches.



**Prerequisites**



No service is configured on the Ethernet interfaces to be added to the Eth-Trunk interface. For example:Layer 3 configurations such as IP addressesStatic MAC entries



**Configuration Impact**

After physical interfaces are added to an Eth-Trunk interface:

* Bandwidth is increased: The bandwidth of an Eth-Trunk interface is the total bandwidth of all member interfaces.
* Reliability is improved: When a member link fails, traffic automatically switches to other available member links. This ensures reliability of Eth-Trunk.If an Eth-Trunk interface is configured with services, interfaces added to the Eth-Trunk interface take over the services.

**Follow-up Procedure**



To implement different load balancing capabilities for member interfaces, configure different weights for the member interfaces.



**Precautions**

An Eth-Trunk consists of only Ethernet links.Eth-Trunk interfaces cannot be nested. That is, member interfaces cannot be Eth-Trunk interfaces.An Ethernet interface can be added to only one Eth-Trunk interface. To add the interface to another Eth-Trunk interface, you must remove the interface from the original Eth-Trunk interface first.Ethernet interfaces of different rates can be added to the same Eth-Trunk interface. If no weight is configured for member interfaces, the weight of each member interface is the same. In this case, the forwarding capability of each interface is the same as that of the interface with the lowest capability. Therefore, you are advised not to bundle interfaces with different forwarding capabilities into the same Eth-Trunk.Ethernet interfaces on different boards can be added to the same Eth-Trunk.If an interface of the local device is added to an Eth-Trunk interface, an interface of the remote device directly connected to the interface of the local device must also be added to an Eth-Trunk interface so that the two ends can communicate.When entering the interface range, ensure that the interface format is correct.

1. The interface number after to must be greater than the interface number before to.
2. Interfaces in the range specified using to must have the same type.
3. The interfaces in the range must exist.
4. If the command is run more than once, all configurations take effect.

In a CU separation vBRAS-vUP scenario, when an L3VE interface is added to a trunk interface as a member interface, ensure that the interface is Up. If the L3VE interface is Down when it is added to a trunk interface, this down status cannot make the L2VE interface go down. As a result, the link is disconnected, and the related users are logged out.



Example
-------

# Add multiple physical interfaces to Eth-Trunk 2.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 2
[*HUAWEI-Eth-Trunk2] trunkport 100GE 1/0/1 to 1/0/4

```

# Add a physical interface to Eth-Trunk1.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] trunkport 100GE 1/0/1

```
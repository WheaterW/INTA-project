erps ring (Layer 2 interface view)
==================================

erps ring (Layer 2 interface view)

Function
--------

The **erps ring** command adds a port to an ERPS ring and specifies a role for the port.

The **undo erps ring** command removes a port from an ERPS ring and the port role configuration.

By default, ports are not added to ERPS rings, and no port roles are specified.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.





Format
------

**erps ring** *ring-id* [ **rpl** { **neighbour** | **owner** } ]

**undo erps ring** *ring-id*



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ring-id* | Specifies the ID of an ERPS ring. | The value is an integer ranging from 1 to 255. |
| **rpl** | Specifies the port type to be added to an ERPS ring. | - |
| **neighbour** | Specifies the port to be added to an ERPS ring as the RPL neighbor port. | - |
| **owner** | Specifies the port to be added to an ERPS ring as the RPL owner port. | - |




Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

After an ERPS ring is created, run the **erps ring** command in the interface view to add Layer 2 ports to the ERPS ring to allow transmission of R-APS PDUs. Each device that is added to an ERPS ring is a node, and each node cannot have more than two ports being added to the ERPS ring.

ERPS defines three port roles: RPL owner port, RPL neighbor port (only in ERPSv2), and ordinary port. The link where the RPL owner port resides is the RPL.

* RPL owner portAn RPL owner port is a ring port responsible for blocking traffic over the RPL to prevent loops. An ERPS ring has only one RPL owner port.When the node on which the RPL owner port resides receives an R-APS PDU indicating that a link or node on the ring fails, it unblocks the RPL owner port to allow the port to send and receive traffic. This mechanism ensures that traffic is not interrupted.
* RPL neighbor portAn RPL neighbor port is a ring port directly connected to an RPL owner port and helps reduce the number of times FDB entries are refreshed.RPL owner and neighbor ports are both blocked under normal conditions to prevent loops.If an ERPS ring fails, both RPL owner and neighbor ports are unblocked.
* Ordinary portOrdinary ports are ring ports other than the RPL owner and neighbor ports.An ordinary port monitors the status of the directly-connected ERPS link and sends R-APS PDUs to inform the other ports if the link status changes.

**Prerequisites**

The **erps ring** command has been run to create the specific ERPS ring.

Before adding a port to an ERPS ring, ensure that:

* Spanning Tree Protocol (STP) is not enabled on the port. If the port has STP enabled, run the **stp disable** command to disable STP.
* The port is not a Layer 3 port. If the port is a Layer 3 port, run the **portswitch** command to switch the port to the Layer 2 mode.
* The control VLAN and ERP instance have been configured using the **control-vlan** and **protected-instance** commands in the ERPS ring view.
* ERPSv2 has been specified for the ERPS ring using the **version v2** command if the port will be specified as an RPL neighbor port.

**Precautions**

Before removing a port from an ERPS ring or changing the port role, run the **shutdown** command to shut down the port. Then remove the port or change the port role and run the **undo shutdown** command to enable the port. If the port is left disabled, traffic will be interrupted.

If ports added to an ERPS ring are all ordinary ports, any port on the device with the largest MAC address will be blocked.A port cannot be added to an ERPS ring in any of the following conditions:

* STP has been enabled on the interface.
* The interface has been added to an Eth-Trunk interface.
* The interface has been added to a Smart Link group.


Example
-------

# Add an interface to ERPS ring 2.
```
<HUAWEI> system-view
[~HUAWEI] erps ring 2
[*HUAWEI-erps-ring2] control-vlan 100
[*HUAWEI-erps-ring2] protected-instance all
[*HUAWEI-erps-ring2] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] stp disable
[*HUAWEI-100GE1/0/1] erps ring 2

```
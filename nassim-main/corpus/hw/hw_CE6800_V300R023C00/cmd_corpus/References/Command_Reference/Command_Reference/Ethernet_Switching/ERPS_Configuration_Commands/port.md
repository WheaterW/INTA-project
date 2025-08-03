port
====

port

Function
--------



The **port** command specifies the port to be added to an ERPS ring and sets the port role.

The **undo port** command deletes a port from the ERPS ring and cancels the port role.



By default, ports are not added to ERPS rings, and no port roles are specified.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**port** { *interface-name* | *interface-type* *interface-number* } [ **rpl** { **neighbour** | **owner** } ]

**undo port** { *interface-name* | *interface-type* *interface-number* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *interface-type* | Specifies the type of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *interface-number* | Specifies the port number. | - |
| **rpl** | Specifies the port type to be added to an ERPS ring. | - |
| **neighbour** | Specifies the port to be added to an ERPS ring as the RPL neighbor port. | - |
| **owner** | Specifies the port to be added to an ERPS ring as the RPL owner port. | - |



Views
-----

ERPS ring view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After an ERPS ring is created, run the **port** command to add Layer 2 ports to the ERPS ring to allow transmission of R-APS PDUs. Each device that is added to an ERPS ring is a node, and each node cannot have more than two ports being added to the ERPS ring.ERPS defines three port roles: RPL owner port, RPL neighbor port (only in ERPSv2), and ordinary port. The link where the RPL owner port resides is the RPL.

* RPL owner portAn RPL owner port is a ring port responsible for blocking traffic over the RPL to prevent loops. An ERPS ring has only one RPL owner port.When the node on which the RPL owner port resides receives an R-APS PDU indicating that a link or node on the ring fails, it unblocks the RPL owner port to allow the port to send and receive traffic. This mechanism ensures that traffic is not interrupted.
* RPL neighbor portAn RPL neighbor port is a ring port directly connected to an RPL owner port and helps reduce the number of times FDB entries are refreshed.RPL owner and neighbor ports are both blocked under normal conditions to prevent loops.If an ERPS ring fails, both RPL owner and neighbor ports are unblocked.
* Ordinary portOrdinary ports are ring ports other than the RPL owner and neighbor ports.An ordinary port monitors the status of the directly-connected ERPS link and sends R-APS PDUs to inform the other ports if the link status changes.

**Prerequisites**

Before adding a port to an ERPS ring, ensure that:ERPSv2 has been specified for the ERPS ring using the **version v2** command if the port will be specified as an RPL neighbor port.

**Configuration Impact**

If any port has been added to the ERPS ring, the control VLAN cannot be changed. If the configured control VLAN needs to be deleted, run the **undo port** command in the ERPS ring view, and run the **undo control-vlan** command to delete the control VLAN.

**Precautions**

If ports added to an ERPS ring are all ordinary ports, any port on the device with the largest MAC address will be blocked.


Example
-------

# Add 100GE 1/0/1 to ERPS ring 10, and set the port to the RPL owner port.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] shutdown
[*HUAWEI-100GE1/0/1] stp disable
[*HUAWEI-100GE1/0/1] quit
[~HUAWEI] erps ring 10
[*HUAWEI-erps-ring10] version v2
[*HUAWEI-erps-ring10] control-vlan 100
[*HUAWEI-erps-ring10] protected-instance all
[*HUAWEI-erps-ring10] port 100GE 1/0/1 rpl owner

```
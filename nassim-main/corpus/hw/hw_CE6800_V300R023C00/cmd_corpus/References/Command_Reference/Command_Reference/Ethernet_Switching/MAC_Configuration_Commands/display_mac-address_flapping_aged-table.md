display mac-address flapping aged-table
=======================================

display mac-address flapping aged-table

Function
--------



The **display mac-address flapping aged-table** command displays aged MAC address flapping records.




Format
------

**display mac-address flapping aged-table** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Displays aged MAC address flapping records in a specified slot. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After MAC address flapping is configured, you can view the aging records of MAC address flapping, you can run this command to view aged MAC address flapping records in all slots or a specified slot.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display aged MAC address flapping records.
```
<HUAWEI> display mac-address flapping aged-table
S: start time    E: end time    (D): error down
-------------------------------------------------------------------------------
Time         : S:2019-10-26 10:39:27           E:2019-10-26 10:50:09
VLAN/BD      : 100/-
MAC Address  : 00e0-fc12-3456
Original-Port: 10GE1/0/1
Move-Ports   : 10GE1/0/2
MoveNum      : 65535
-------------------------------------------------------------------------------
Total items on slot 1: 1

```

**Table 1** Description of the **display mac-address flapping aged-table** command output
| Item | Description |
| --- | --- |
| S: start time | Start time MAC address flapping occurs. |
| E: end time | End time MAC address flapping occurs. |
| (D): error down | If the error-down command is run on an interface, the interface is shut down when the number of flapping times reaches the value of the corresponding level. |
| Time | Start time and end time MAC address flapping occurs. |
| VLAN/BD | VLAN or VXLAN BD where MAC address flapping occurs. |
| MAC Address | Flapping MAC address. |
| Move-Ports | Interface that learns the MAC address later. Multiple interfaces can learn the MAC address later. |
| MoveNum | Number of times the MAC address flaps. |
| Total items on slot 1 | Number of aged MAC address flapping records on the board. |
| Original-Port | Interface that learns the MAC address first. |
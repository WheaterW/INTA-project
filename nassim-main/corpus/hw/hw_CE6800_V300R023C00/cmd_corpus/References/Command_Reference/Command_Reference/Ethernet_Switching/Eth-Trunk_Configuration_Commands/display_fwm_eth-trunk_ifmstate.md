display fwm eth-trunk ifmstate
==============================

display fwm eth-trunk ifmstate

Function
--------



The **display fwm eth-trunk ifmstate** command displays the management status table of an Eth-Trunk interface.




Format
------

**display fwm eth-trunk ifmstate interface** *interface-type* *interface-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies the interface type and number.   * interface-type specifies the interface type. * interface-number specifies the number of the interface. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After an Eth-Trunk interface is successfully configured, you can run the command to view the configuration of the Eth-Trunk interface, you can run this command to query management status table of the Eth-Trunk interface.

**Prerequisites**

Before querying the Eth-Trunk ifmstate table, specify a physical interface name. Otherwise, no message is displayed if no data is found.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the Eth-Trunk interface management status table.
```
<HUAWEI> display fwm eth-trunk ifmstate interface 100ge 1/0/1
IFMSTATE table information:
-------------------------------------------------------
SlotID                : 1
TB                    : 4
TP                    : 1
IfIndex               : 5
Eth-Trunk ID          : 0
Physical state        : 0
Eth-Trunk member flag : 0

```

**Table 1** Description of the **display fwm eth-trunk ifmstate** command output
| Item | Description |
| --- | --- |
| IFMSTATE table information | Interface information. |
| SlotID | Slot ID. |
| TB | Target Blade index. |
| TP | Target Port index. |
| IfIndex | Interface index. |
| Eth-Trunk ID | ID of an Eth-Trunk interface. The value 1024 indicates that the specified interface is not an Eth-Trunk member interface. |
| Eth-Trunk member flag | Eth-Trunk member interface flag. |
| Physical state | Physical status. |
display interface eth-trunk forwarding-table
============================================

display interface eth-trunk forwarding-table

Function
--------



The **display interface eth-trunk forwarding-table** command displays the forwarding table of an Eth-Trunk interface.




Format
------

**display interface** { *interface-name* | *interface-type* *interface-number* } **forwarding-table**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| *interface-type* | Specifies the type of an interface. | The interface type must be Eth-Trunk. |
| *interface-number* | Specifies the number of an interface. | The value is an integer that ranges from 0 to 1023. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After an Eth-Trunk interface is successfully configured, you can run this command to view the forwarding table of the Eth-Trunk interface and the status of member interfaces of the Eth-Trunk interface. When the weight is configured, multiple copies of the same interface are displayed.

**Precautions**

An Eth-Trunk interface already exists on the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display forwarding table of Eth-Trunk 1.
```
<HUAWEI> display interface Eth-Trunk1 forwarding-table
Eth-Trunk1's forwarding table:                                                                                                      
----------------------------------------------------                                                                                
100GE1/0/2                                                                                                                           
100GE1/0/5                                                                                                                           
----------------------------------------------------

```

**Table 1** Description of the **display interface eth-trunk forwarding-table** command output
| Item | Description |
| --- | --- |
| Eth-Trunk1's forwarding table | Forwarding table of Eth-Trunk 1, including active interfaces of Eth-Trunk 1. |
display ip interface multi-address
==================================

display ip interface multi-address

Function
--------



The **display ip interface multi-address** command displays all interfaces configured with multiple IP addresses.




Format
------

**display ip interface multi-address**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



If an interface on a device is configured with multiple IP addresses, the device cannot be configured to differentiate primary IP addresses from secondary IP addresses. To check whether an interface configured with multiple IP addresses exists on a device, run the display ip interface multi-address command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all interfaces configured with multiple IP addresses.
```
<HUAWEI> display ip interface multi-address
Interface                         AddrNum
-----------------------------------------
100GE1/0/1                               3
100GE1/0/2                               2

```

**Table 1** Description of the **display ip interface multi-address** command output
| Item | Description |
| --- | --- |
| Interface | Type and number of the interface configured with multiple IP addresses. |
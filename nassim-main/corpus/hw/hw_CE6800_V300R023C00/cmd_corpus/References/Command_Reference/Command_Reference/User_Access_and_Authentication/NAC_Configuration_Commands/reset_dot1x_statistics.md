reset dot1x statistics
======================

reset dot1x statistics

Function
--------



The **reset dot1x statistics** command clears 802.1X authentication statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**reset dot1x statistics** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Clears 802.1X statistics on a specified interface. | - |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 255 case-sensitive characters. It cannot contain spaces. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

802.1X authentication statistics include the number of successful and failed authentications on an interface and the number of sent and received packets.The statistics need to be cleared in the following scenarios:

* When redeploying services, you need to clear the statistics, collect the statistics again, and run the display dot1x command to check whether the authentication and packet sending and receiving are normal.
* After rectifying a fault, run the reset dot1x statistics command to clear the statistics, collect the statistics again, and then run the display dot1x command to check whether the authentication result is correct and whether packets are correctly sent and received. If the authentication result is correct and packets are correctly sent and received, the fault is rectified.

Example
-------

# Clear 802.1X statistics.
```
<HUAWEI> reset dot1x statistics

```
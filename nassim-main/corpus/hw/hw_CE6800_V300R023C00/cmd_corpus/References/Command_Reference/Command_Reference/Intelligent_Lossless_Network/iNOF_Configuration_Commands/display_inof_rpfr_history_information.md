display inof rpfr history information
=====================================

display inof rpfr history information

Function
--------

The **display inof rpfr history information** command displays historical RPFR information.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6885-SAN and CE8850-SAN.



Format
------

**display inof rpfr history information** [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to view historical RPFR information.

**Precautions**

If no slot ID is specified, historical RPFR information in all slots is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display historical RPFR information.
```
<HUAWEI> display inof rpfr history information
Slot : 1
-----------------------------------------------------------------------------------------------------------
DIP                SIP                   FaultTime                     ProxyTime                   Reason   
-----------------------------------------------------------------------------------------------------------
192.168.1.1        192.168.1.2           2020-07-03 10:33:37.001       2020-07-03 10:33:37.123     LinkDown 
192.168.2.1        192.168.2.2           2020-07-03 10:33:37.006       2020-07-03 10:33:37.123     LinkDown
-----------------------------------------------------------------------------------------------------------

```

**Table 1** Description of the **display inof rpfr history information** command output
| Item | Description |
| --- | --- |
| Slot | Slot ID. |
| DIP | Destination IP address, that is, the IP address of the compute node. |
| SIP | Source IP address, that is, the IP address of the storage node. |
| FaultTime | Fault time. |
| ProxyTime | Time when a proxy packet is sent. |
| Reason | Fault cause. |
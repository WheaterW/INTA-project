display access-user dot1x-identity statistics
=============================================

display access-user dot1x-identity statistics

Function
--------



The **display access-user dot1x-identity statistics** command displays statistics about 802.1X Identity packets on the device.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display access-user dot1x-identity statistics**


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

You can run this command to view statistics about 802.1X Identity packets on the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about 802.1X Identity packets on the device.
```
<HUAWEI> display access-user dot1x-identity statistics
-----------------------------------------------------------------------
Receive(Packet)    Pass(Packet)    Drop(Packet)    Last-dropping-time  
-----------------------------------------------------------------------
0                  0               0               -                   
-----------------------------------------------------------------------
...

```

**Table 1** Description of the **display access-user dot1x-identity statistics** command output
| Item | Description |
| --- | --- |
| Receive(Packet) | Total number of 802.1X Identity packets received by the device. |
| Pass(Packet) | Number of 802.1X Identity packets sent to the CPU. |
| Drop(Packet) | Number of 802.1X Identity packets discarded by the device. |
| Last-dropping-time | Last time when the device discards 802.1X Identity packets. If no packet loss record exists on the device, "-" is displayed. |
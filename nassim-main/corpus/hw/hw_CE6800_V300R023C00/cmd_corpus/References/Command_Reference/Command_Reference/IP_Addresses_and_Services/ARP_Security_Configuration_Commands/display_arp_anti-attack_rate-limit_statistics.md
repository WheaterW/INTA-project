display arp anti-attack rate-limit statistics
=============================================

display arp anti-attack rate-limit statistics

Function
--------



The **display arp anti-attack rate-limit statistics** command displays statistics about ARP packets discarded due to rate limiting on an interface.




Format
------

**display arp anti-attack rate-limit statistics**


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

The statistics include the number of forwarded packets and the number of discarded packets. The statistics help the network administrator set the rate limit for ARP packets on an interface based on the actual situation.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Displays statistics about ARP rate limiting on a device interface.
```
<HUAWEI> display arp anti-attack rate-limit statistics
Statistics on Slot 1 :
----------------------------------------------------------------------------------------
Interface        Rate(pps)              Total Passed        Total Dropped       Stat
----------------------------------------------------------------------------------------
10GE1/0/1        100             	1024                1000                success
10GE1/0/2        100                	2048                1000                fail
----------------------------------------------------------------------------------------
Total: 2

```

**Table 1** Description of the **display arp anti-attack rate-limit statistics** command output
| Item | Description |
| --- | --- |
| Interface | Interface. |
| Total Passed | Number of arp packets that pass through the device. |
| Total Dropped | Number of attack packets discarded by the device. |
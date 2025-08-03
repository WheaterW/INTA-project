reset access-user dot1x-identity statistics
===========================================

reset access-user dot1x-identity statistics

Function
--------



The **reset access-user dot1x-identity statistics** command clears statistics about 802.1X Identity packets.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**reset access-user dot1x-identity statistics**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

Before collecting statistics about 802.1X Identity packets in a specified period, run the **reset access-user dot1x-identity statistics** command to clear the existing statistics. After the statistics collection ends, run the **display access-user dot1x-identity statistics** command to view new statistics.


Example
-------

# Clear statistics about 802.1X Identity packets on the device.
```
<HUAWEI> system-view
[~HUAWEI] reset access-user dot1x-identity statistics

```
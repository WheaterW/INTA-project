display access-user statistics
==============================

display access-user statistics

Function
--------



The **display access-user statistics** command displays user statistics on the device.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S.



Format
------

**display access-user statistics**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

This command displays user statistics on the device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display user statistics.
```
<HUAWEI> display access-user statistics
Current online user statistics:
  Total access number             : 0
  MAC access number               : 0
  802.1x access number            : 0
  Unauthenticated access number   : 0
Current wired online user statistics:
  Total wired access number             : 0
  MAC wired access number               : 0
  802.1x wired access number            : 0
  Unauthenticated wired access number   : 0

```

**Table 1** Description of the **display access-user statistics** command output
| Item | Description |
| --- | --- |
| Current online user statistics | Statistics on current online users. |
| Current wired online user statistics | Statistics about online wired users. |
| Total access number | Total number of online access users. |
| Total wired access number | Total number of wired access users. |
| MAC access number | Number of online MAC address authentication users. |
| MAC wired access number | Number of wired MAC address authentication users. |
| 802.1x access number | Number of online 802.1X users. |
| 802.1x wired access number | Number of wired 802.1X users. |
| Unauthenticated access number | Number of unauthenticated users. |
| Unauthenticated wired access number | Number of unauthenticated wired users. |
display isis troubleshooting
============================

display isis troubleshooting

Function
--------



The **display isis troubleshooting** command displays IS-IS information of neighbor relationship disconnections or flaps.




Format
------

**display isis troubleshooting**


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

If an IS-IS neighbor relationship is disconnected or flaps, you can run the display isis troubleshooting command to check IS-IS status flag information. The command output helps diagnose the fault.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Check the cause of the IS-IS neighbor relationship disconnection or flapping.
```
<HUAWEI> display isis troubleshooting
Total counts: 5 
-------------------------------------------------------------------------------- 
Sequence   Time                      Event Description                          
-------------------------------------------------------------------------------- 
1          2015-11-23 19:53:47       The IS-IS 1 peer 1111.1111.1111 went Down b 
                                     ecause IS-IS was disabled from the interfac 
                                     e 100GE1/0/1. Please check IS-IS configu 
                                     rations on the interface 100GE1/0/1.    
2          2015-11-23 16:51:37       The IS-IS 1 peer 1111.1111.1111 went Down b 
                                     ecause the hold time expired. Please run th 
                                     e display isis statistics packet interface 
                                     100GE1/0/1 command to check Hello packet 
                                      statistics.(CPU = 2%, PingResult = 5 packe 
                                     ts success, 0 packets timeout)             
3          2015-11-23 16:48:28       The IS-IS 1 peer 1111.1111.1111 went Down b 
                                     ecause the hold time expired. Please run th 
                                     e display isis statistics packet interface 
                                     100GE1/0/1 command to check Hello packet 
                                      statistics.(CPU = 7%, PingResult =5 packe 
                                     ts success, 0 packets timeout)

```

**Table 1** Description of the **display isis troubleshooting** command output
| Item | Description |
| --- | --- |
| Total counts | Number of IS-IS peer relationship disconnection times. |
| Sequence | Event sequence, in the order of 1, 2, 3, 4, and 5. |
| Time | Time when an IS-IS neighbor relationship was disconnected. |
| Event Description | Detailed information about the IS-IS neighbor relationship disconnection, including the neighbor's system ID, cause of the disconnection, and troubleshooting suggestions. Ping results are also displayed in the case of neighbor timeout and BFD disconnections. |
display bgp troubleshooting
===========================

display bgp troubleshooting

Function
--------



The **display bgp troubleshooting** command displays the cause of BGP peer relationship disconnection or flapping.




Format
------

**display bgp troubleshooting**


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

If a BGP peer relationship is disconnected or flaps, the device automatically records the cause, including information about the routes, CPU usage, ping operations, and alarms. To check the cause, run the **display bgp troubleshooting** command, which helps troubleshooting.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the cause of BGP peer relationship disconnection or flapping.
```
<HUAWEI> display bgp troubleshooting
Total counts: 2 
--------------------------------------------------------------------------------  
Sequence   Time                      Event Description 
-------------------------------------------------------------------------------- 

1          2015-12-17 16:17:59+08:00 The BGP peer 10.1.1.1 went Down because the 
                                      peer ignore command was configured manuall 
                                     y. Please check local BGP configurations.   
2          2015-12-17 16:16:57+08:00 The BGP peer 10.1.1.1 went Down because the 
                                      BGP instance was reset manually. Please ch 
                                     eck the opearion record.                    
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display bgp troubleshooting** command output
| Item | Description |
| --- | --- |
| Total counts | Number of BGP peer relationship disconnection times. |
| Sequence | Sequence number of a record. |
| Time | Time when a BGP peer relationship was disconnected. |
| Event Description | Description of the event that a BGP peer relationship was disconnected. |
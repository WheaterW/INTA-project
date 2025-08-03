display ospf troubleshooting
============================

display ospf troubleshooting

Function
--------



The **display ospf troubleshooting** command displays information about OSPF neighbor disconnections.




Format
------

**display ospf troubleshooting**


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

To check information about OSPF neighbor disconnections, run the **display ospf troubleshooting** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display diagnostic information about OSPF neighbor disconnections.
```
<HUAWEI> display ospf troubleshooting
Total counts: 2
--------------------------------------------------------------------------------
Sequence   Time                      Event Description                          
--------------------------------------------------------------------------------
 1         2015-11-25 09:28:18       The OSPF 1 peer 1.1.1.1 went Down because o
                                     f mismatched Hello timers. Please check the
                                      OSPF Hello timer configuration.(Interface 
                                     = 100GE1/0/1, PingResult = 5 packets suc
                                     cess, 0 packets timeout)
 2         2015-11-25 09:27:42       The OSPF 1 peer 1.1.1.1 went Down because 1
                                     -way Hello packets were received. Please ch
                                     eck the status of neighbor interface.(Inter
                                     face = 100GE1/0/1)
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display ospf troubleshooting** command output
| Item | Description |
| --- | --- |
| Total counts | The count of OSPF neighbor disconnections. |
| Sequence | Sequence number. |
| Time | Time when the OSPF neighbor disconnection occurred. |
| Event Description | Description of the OSPF neighbor disconnection event. |
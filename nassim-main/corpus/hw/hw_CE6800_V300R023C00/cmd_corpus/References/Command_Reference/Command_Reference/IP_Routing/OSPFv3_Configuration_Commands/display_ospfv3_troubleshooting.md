display ospfv3 troubleshooting
==============================

display ospfv3 troubleshooting

Function
--------



The **display ospfv3 troubleshooting** command displays information about OSPFv3 neighbor disconnections.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3 troubleshooting**


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

To check information about OSPFv3 neighbor disconnections, run the **display ospfv3 troubleshooting** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about OSPFv3 neighbor disconnections.
```
<HUAWEI> display ospfv3 troubleshooting
Total counts: 1
--------------------------------------------------------------------------------
Sequence   Time                      Event Description                          
--------------------------------------------------------------------------------
 1         2015-11-25 09:29:02       The OSPFv3 1 peer 10.10.10.10 went Down bec
                                     ause the OSPFv3 area 0.0.0.1 was reset. Ple
                                     ase check the area configuration.(Interface
                                      = 100GE1/0/1)                          
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display ospfv3 troubleshooting** command output
| Item | Description |
| --- | --- |
| Total counts | The count of OSPFv3 neighbor disconnections. |
| Sequence | Sequence number. |
| Time | Time when the OSPFv3 neighbor disconnection occurred. |
| Event Description | Description of the OSPFv3 neighbor disconnection event. |
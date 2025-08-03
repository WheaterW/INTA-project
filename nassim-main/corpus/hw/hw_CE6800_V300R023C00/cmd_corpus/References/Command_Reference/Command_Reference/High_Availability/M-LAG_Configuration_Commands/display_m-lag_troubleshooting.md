display m-lag troubleshooting
=============================

display m-lag troubleshooting

Function
--------



The **display m-lag troubleshooting** command displays causes about M-LAG faults.




Format
------

**display m-lag troubleshooting** { **current** | **history** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **current** | Displays current fault information. | - |
| **history** | Displays historical fault information. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When an M-LAG fault occurs, run the **display m-lag troubleshooting** command to check causes about M-LAG faults.The **display m-lag troubleshooting** command displays the causes of a maximum of 100 recent faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display causes about M-LAG historical faults.
```
<HUAWEI> display m-lag troubleshooting history
Total : 3
--------------------------------------------------------------------------------
Seq  Time                     Event Description
--------------------------------------------------------------------------------
1    2021-01-21 16:04:48      DFS pairing failed because the DFS group could not
                               receive Hello packets. Check the DFS configuratio
                              n of the local or remote switch.
2    2021-01-21 16:04:37      DFS pairing failed because the peer-link was down.
                               Check the status of the peer-link interface.
3    2021-01-21 15:58:55      DFS pairing failed because the DFS status of the r
                              emote switch was incorrect. Check the DFS configur
                              ation of the remote switch.
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display m-lag troubleshooting** command output
| Item | Description |
| --- | --- |
| Total | M-LAG fault count. |
| Seq | Sequence number. |
| Time | M-LAG fault occurrence time. |
| Event Description | Cause for the M-LAG fault. |
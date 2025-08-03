display dragonfly pfc adjust statistics
=======================================

display dragonfly pfc adjust statistics

Function
--------



The **display dragonfly pfc adjust statistics** command displays statistics on dragonfly deadlock prevention.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

For CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K:

**display dragonfly abs-pfc adjust statistics**

For CE8855, CE8851-32CQ4BQ:

**display dragonfly pfc adjust statistics**


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

You can run this command to view statistics on dragonfly deadlock prevention.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics on dragonfly deadlock prevention.
```
<HUAWEI> display dragonfly abs-pfc adjust statistics
O/N: Original/New
Slot: 1  Chip: 0
------------------------------------------------------
Priority   Dscp           Count    LastAdjustmentTime
O/N        O/N                                 
------------------------------------------------------
0/2        1/3          4532410    2022-03-22 10:34:55
1/3        9/11               0    --                 
------------------------------------------------------

```

# Display statistics on dragonfly deadlock prevention.
```
<HUAWEI> display dragonfly pfc adjust statistics
O/N: Original/New
Slot: 1  Chip: 0
------------------------------------------------------
Priority   Dscp           Count    LastAdjustmentTime
O/N        O/N                                 
------------------------------------------------------
0/2        1/3          4532410    2022-03-22 10:34:55
1/3        9/11               0    --                 
------------------------------------------------------

```

**Table 1** Description of the **display dragonfly pfc adjust statistics** command output
| Item | Description |
| --- | --- |
| Priority | Original and changed queues of packets in the hook-shaped flow. |
| Dscp | Original and changed DSCP values of packets in the hook-shaped flow. |
| Count | Number of times ACL rules match packets in the hook-shaped flow. |
| LastAdjustmentTime | Time when the queue priority and DSCP value of the packets in the hook-shaped flow matching the adaptive routing are adjusted when the ACL rule is matched last time. |
| Slot | Slot number. |
| Chip | Chip ID. |
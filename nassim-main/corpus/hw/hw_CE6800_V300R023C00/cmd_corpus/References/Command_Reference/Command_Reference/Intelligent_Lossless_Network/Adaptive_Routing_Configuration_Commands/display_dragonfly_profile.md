display dragonfly profile
=========================

display dragonfly profile

Function
--------



The **display dragonfly profile** command displays information about a dragonfly profile.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display dragonfly profile default**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **default** | Specifies the default dragonfly profile. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the display dragonfly profile command to view all information about a dragonfly profile.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all information about the default dragonfly profile. (CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM)
```
<HUAWEI> display dragonfly profile default
ABS-PFC Info: 
  ABS-PFC Enable Priority: 2 3 4 
  ABS-PFC Threshold(KB): 0 
Adjust Info: 
  O/N: Original/New 
  ----------------
  Priority   Dscp
  O/N        O/N
  ---------------- 
  4/3        32/24 
  3/2        24/16 
  ----------------
Adaptive-Routing Info:  
  -------------------------------------------------------------------- 
  Bandwidth-Level(High/Low)   Buffer-Level(High/Low)   Tx-Interval(ms) 
  -------------------------------------------------------------------- 
  6/3                         6/3                      500  
  --------------------------------------------------------------------

```

# Display all information about the default dragonfly profile. (CE8855 and CE8851-32CQ4BQ)
```
<HUAWEI> display dragonfly profile default
Adjust Info: 
  O/N: Original/New 
  ----------------
  Priority   Dscp
  O/N        O/N
  ---------------- 
  4/3        32/24 
  3/2        24/16 
  ----------------
Adaptive-Routing Info:  
  -------------------------------------------------------------------- 
  Bandwidth-Level(High/Low)   Buffer-Level(High/Low)   Tx-Interval(ms) 
  -------------------------------------------------------------------- 
  6/3                         6/3                      500  
  --------------------------------------------------------------------

```

**Table 1** Description of the **display dragonfly profile** command output
| Item | Description |
| --- | --- |
| ABS-PFC Enable Priority | Queue for which dragonfly antilocking PFC is enabled. |
| ABS-PFC Threshold(KB) | Threshold for dragonfly antilocking PFC. |
| ABS-PFC Info | Dragonfly antilocking PFC information. |
| Adjust Info | Dragonfly deadlock prevention information. |
| Adaptive-Routing Info | Adaptive routing information. |
| Bandwidth-Level(High/Low) | Bandwidth utilization level (upper threshold/lower threshold). |
| Buffer-Level(High/Low) | Queue depth level (upper threshold/lower threshold). |
| Tx-Interval(ms) | Interval for sending ARN messages about congestion. |
| Priority(O/N) | Queue switching rule for dragonfly deadlock prevention. |
| Dscp(O/N) | DSCP switching rule for dragonfly deadlock prevention. |
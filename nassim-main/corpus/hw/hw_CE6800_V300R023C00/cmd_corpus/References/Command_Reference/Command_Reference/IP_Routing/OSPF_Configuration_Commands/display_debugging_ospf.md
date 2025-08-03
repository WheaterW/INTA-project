display debugging ospf
======================

display debugging ospf

Function
--------



The **display debugging ospf** command displays information about current OSPF debugging functions.




Format
------

**display debugging ospf**


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

When a large amount of information is output, the **display debugging ospf** command can be used to view information about the enabled OSPF debugging functions. Based on the command output, you can disable some unnecessary debugging functions to minimize the debugging information output.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about current OSPF debugging functions.
```
<HUAWEI> display debugging ospf
OSPF 1 All Route Calculation debugging switch is on 
OSPF 1 RTCALC-NSSA debugging switch is on 
OSPF 1 RTCALC-INTER debugging switch is on 
OSPF 1 RTCALC-ASE debugging switch is on 
OSPF 1 RTCALC-INTRA debugging switch is on 
OSPF 1 RTCALC-ASBR debugging switch is on

```

**Table 1** Description of the **display debugging ospf** command output
| Item | Description |
| --- | --- |
| OSPF 1 RTCALC-ASBR debugging switch is on | The OSPF 1 RTCALC-ASBR debugging function is enabled. |
| OSPF 1 All Route Calculation debugging switch is on | The OSPF 1 All Route Calculation debugging function is enabled. |
| OSPF 1 RTCALC-NSSA debugging switch is on | The OSPF 1 RTCALC-NSSA debugging function is enabled. |
| OSPF 1 RTCALC-INTER debugging switch is on | The OSPF 1 RTCALC-INTER debugging function is enabled. |
| OSPF 1 RTCALC-ASE debugging switch is on | The OSPF 1 RTCALC-ASE debugging function is enabled. |
| OSPF 1 RTCALC-INTRA debugging switch is on | The OSPF 1 RTCALC-INTRA debugging function is enabled. |
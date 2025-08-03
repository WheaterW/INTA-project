display load-balance profile dynamic
====================================

display load-balance profile dynamic

Function
--------



The **display load-balance profile dynamic** command displays detailed information about a dynamic load balancing profile.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display load-balance profile dynamic** [ *profile-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *profile-name* | Specifies the name of a dynamic load balancing profile. | The value is a string of 1 to 31 case-sensitive characters. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the display load-balance profile dynamic command to check details of a dynamic load balancing profile, including the load balancing mode and flowlet interval.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about a dynamic load balancing profile.
```
<HUAWEI> display load-balance profile dynamic
Load-balance Profile: default
---------------------------------------------------
Type        Mode       Gap time(us)      
---------------------------------------------------
Eth-Trunk      spray           --             
---------------------------------------------------
Eth-Trunk Interface List:                           
---------------------------------------------------
Eth-Trunk 1    Eth-Trunk 11
Eth-Trunk 12   Eth-Trunk 20
Eth-Trunk 21   Eth-Trunk 111

```

**Table 1** Description of the **display load-balance profile dynamic** command output
| Item | Description |
| --- | --- |
| Type | Dynamic load balancing type.   * Eth-Trunk: dynamic load balancing for a LAG. |
| Mode | Dynamic load balancing mode.   * eligible: eligible dynamic load balancing. * spray: spray dynamic load balancing. * fixed: fixed dynamic load balancing. |
| Gap time(us) | Flowlet interval, in 1024 nanoseconds. |
| Eth-Trunk Interface List | Eth-Trunk that uses the load balancing profile. |
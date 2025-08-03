display bgp evpn all routing-table dampening parameter
======================================================

display bgp evpn all routing-table dampening parameter

Function
--------



The **display bgp evpn all routing-table dampening parameter** command displays configured BGP EVPN route dampening parameters.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display bgp evpn all routing-table dampening parameter**

**display bgp instance** *instance-name* **evpn** **all** **routing-table** **dampening** **parameter**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To view BGP EVPN route dampening parameters, run the **display bgp evpn all routing-table dampening parameter** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the BGP VPNv4 route dampening parameters.
```
<HUAWEI> display bgp evpn all routing-table dampening parameter
  
 EBGP:
 Maximum Suppress Time(in second) : 3973
 Ceiling Value                    : 16000
 Reuse Value                      : 750
 HalfLife Time(in second)         : 900
 Suppress-Limit                   : 2000
  
 IBGP:
 Maximum Suppress Time(in second) : 3973
 Ceiling Value                    : 16000
 Reuse Value                      : 750
 HalfLife Time(in second)         : 900
 Suppress-Limit                   : 2000

```

# Display the BGP instance EVPN route dampening parameters.
```
<HUAWEI> display bgp instance aaa evpn all routing-table dampening parameter
  
 EBGP:
 Maximum Suppress Time(in second) : 3973
 Ceiling Value                    : 16000
 Reuse Value                      : 750
 HalfLife Time(in second)         : 900
 Suppress-Limit                   : 2000
  
 IBGP:
 Maximum Suppress Time(in second) : 3973
 Ceiling Value                    : 16000
 Reuse Value                      : 750
 HalfLife Time(in second)         : 900
 Suppress-Limit                   : 2000

```

**Table 1** Description of the **display bgp evpn all routing-table dampening parameter** command output
| Item | Description |
| --- | --- |
| Maximum Suppress Time(in second) | Maximum route suppression time, in seconds. |
| Ceiling Value | Penalty ceiling. |
| Reuse Value | Threshold for the routes to be unsuppressed. |
| HalfLife Time(in second) | Half life of a reachable route, in seconds. |
| Suppress-Limit | Threshold for the routes to be suppressed. |
| EBGP | EBGP route dampening parameters. |
| IBGP | IBGP route dampening parameters. |
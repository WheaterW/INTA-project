display bgp routing-table dampening parameter
=============================================

display bgp routing-table dampening parameter

Function
--------



The **display bgp routing-table dampening parameter** command displays configured BGP route dampening parameters.




Format
------

**display bgp routing-table dampening parameter**

**display bgp vpnv4 vpn-instance** *vpn-instance-name* **routing-table** **dampening** **parameter**

**display bgp instance** *instance-name* **vpnv4** **vpn-instance** *vpn-instance-name* **routing-table** **dampening** **parameter**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpnv4** | Displays the BGP route dampening parameters of a VPNv4 instance. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **instance** *instance-name* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check configured BGP route dampening parameters, run the **display bgp routing-table dampening parameter** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the BGP instance VPNv4 route dampening parameters.
```
<HUAWEI> display bgp instance aaa vpnv4 all routing-table dampening parameter
 Maximum Suppress Time(in second) : 3973
 Ceiling Value                    : 16000
 Reuse Value                      : 750
 HalfLife Time(in second)        : 900
 Suppress-Limit                   : 2000

```

# Display the BGP VPNv4 route dampening parameters.
```
<HUAWEI> display bgp vpnv4 all routing-table dampening parameter
 Maximum Suppress Time(in second)  : 3973
 Ceiling Value                     : 16000
 Reuse Value                       : 750
 HalfLife Time(in second)          : 900
 Suppress-Limit                    : 2000

```

# Display BGP route dampening parameters.
```
<HUAWEI> display bgp routing-table dampening parameter
Maximum Suppress Time(in second) : 3973
Ceiling Value                    : 16000
Reuse Value                      : 750
HalfLife Time(in second)        : 900
Suppress-Limit                   : 2000

```

**Table 1** Description of the **display bgp routing-table dampening parameter** command output
| Item | Description |
| --- | --- |
| Maximum Suppress Time(in second) | Maximum route suppression time, in seconds. |
| Ceiling Value | Indicates the penalty ceiling. |
| Reuse Value | Threshold for the routes to be unsuppressed. |
| HalfLife Time(in second) | Half life of a reachable route, in seconds. |
| Suppress-Limit | Indicates the threshold for a route to be suppressed. |
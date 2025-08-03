display bgp error discard unnumbered peer interface
===================================================

display bgp error discard unnumbered peer interface

Function
--------



The **display bgp error discard unnumbered peer interface** command displays BGP errors of unnumbered BGP peers.




Format
------

**display bgp error discard unnumbered peer interface** { *interface-name* | *IfType* *IFNum* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 characters. |
| *IfType* | Specifies an interface type. | - |
| *IFNum* | Specifies an interface number. | The value is a string of 1 to 63 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



When a BGP fault occurs, run this command to check BGP error information. BGP error information includes peer error information, route error information, and resource threshold-crossing error information.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about discarded error packets of BGP unnumbered peers.
```
<HUAWEI> display bgp error discard unnumbered peer interface 100GE 1/0/1
BGP discard Info Counts: 
 Routes received with cluster ID loop            : 0
 Routes received with As path count over limit   : 0
 Routes advertised with As path count over limit : 0
 Routes received with As loop                    : 0
 Routes received with Zero RD(0:0)               : 0
 Routes received with no prefix                  : 0
 Routes received with error path-attribute       : 0
 Routes received with originator ID loop         : 0
 Routes received with total number over limit    : 0
 Routes received with error router id            : 0

```

**Table 1** Description of the **display bgp error discard unnumbered peer interface** command output
| Item | Description |
| --- | --- |
| BGP discard Info Counts | Number of routes discarded by BGP. |
| Routes received with cluster ID loop | Number of routes discarded due to duplicate cluster IDs. |
| Routes received with As path count over limit | Number of received routes that are discarded because the number of AS numbers in the AS\_Path exceeds the upper limit. |
| Routes advertised with As path count over limit | Number of sent routes that are discarded because the number of AS numbers in the AS\_Path exceeds the upper limit. |
| Routes received with As loop | Number of routes discarded due to repeated AS numbers. |
| Routes received with Zero RD(0:0) | Number of routes discarded because the RD value is 0. |
| Routes received with no prefix | Number of routes discarded because there are no route prefixes. |
| Routes received with total number over limit | Total number of routes discarded because the number of routes exceeds the upper limit. |
| Routes received with originator ID loop | Total number of routes with the original ID loop. |
| Routes received with error path-attribute | Total number of routes with incorrect attributes. |
| Routes received with error router id | Number of routes with incorrect router IDs and connection failures. |
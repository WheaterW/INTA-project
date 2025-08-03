display bgp instance error discard
==================================

display bgp instance error discard

Function
--------



The **display bgp instance error discard** command displays BGP errors.




Format
------

**display bgp instance** *bgpName* **error** **discard**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *bgpName* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



When a BGP fault occurs, the display bgp instance error discard command can be used to display BGP errors. BGP errors include neighbor errors, route errors, and errors indicating that the resource usage exceeds the limit.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display error information about a BGP multi-instance.
```
<HUAWEI> display bgp instance a error discard
BGP Discard Info Counts:
Routes received with cluster ID loop : 0
Routes received with as path count over limit : 0
Routes advertised with as path count over limit : 0
Routes received with As loop : 0
Routes received with Zero RD(0:0) : 0
Routes received with no prefix : 0
Routes received with error path-attribute : 0
Routes received with originator ID loop : 0
Routes received with total number over limit : 0

BGP Discard info:(IPv4 VPNv4)
Routes received with cluster ID loop : 0
Routes received with as path count over limit : 0
Routes advertised with as path count over limit : 0
Routes received with As loop : 0
Routes received with Zero RD(0:0) : 0
Routes received with error path-attribute : 0
Routes received with originator ID loop : 0
Routes received with total number over limit : 0

No discard record.

```

**Table 1** Description of the **display bgp instance error discard** command output
| Item | Description |
| --- | --- |
| BGP Discard Info Counts | Number of discarded BGP routes. |
| BGP Discard info | Information of discarded BGP routes. |
| Routes received with cluster ID loop | Number of BGP routes discarded due to a duplicate cluster ID. |
| Routes received with as path count over limit | Number of received BGP routes discarded due to the number of AS\_Paths exceeding the upper threshold. |
| Routes advertised with as path count over limit | Number of sent BGP routes discarded due to the number of AS\_Paths exceeding the upper threshold. |
| Routes received with As loop | Number of BGP routes discarded due to a duplicate As number. |
| Routes received with Zero RD(0:0) | Number of BGP routes discarded because the RD is 0. |
| Routes received with no prefix | Number of BGP routes discarded because there are no route prefixes. |
| Routes received with error path-attribute | Number of BGP routes with error path-attribute. |
| Routes received with originator ID loop | Number of BGP routes with originator ID loop. |
| Routes received with total number over limit | Total number of BGP routes that were dropped due to exceeding the upper limit. |
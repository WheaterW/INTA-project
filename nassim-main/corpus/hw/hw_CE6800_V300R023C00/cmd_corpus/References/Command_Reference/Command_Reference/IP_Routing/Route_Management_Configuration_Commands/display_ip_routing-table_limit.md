display ip routing-table limit
==============================

display ip routing-table limit

Function
--------

The **display ip routing-table limit** command displays limits on the number of routes and prefixes.



Format
------

**display ip routing-table limit vpn-instance** *vpn-instance-name*

**display ip routing-table limit all-vpn-instance**

**display ip routing-table limit**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all-vpn-instance** | Displays limits on the number of routes and prefixes in all VPN instances. | - |
| **vpn-instance** *vpn-instance-name* | Displays limits on the number of routes and prefixes in a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

The command displays limits on the number of routes and prefixes.

* The **display ip routing-table limit** command displays limits on the number of public routes and prefixes.
* The **display ip routing-table limit all-vpn-instance** command displays limits on the number of routes and prefixes of all VPN instances.
* The **display ip routing-table limit vpn-instance** command displays limits on the number of routes and prefixes of a specified VPN instance.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display limits on the number of routes and prefixes of VPN instance named vpn1.
```
<HUAWEI> display ip routing-table limit vpn-instance vpn1
VPN Instance Name: vpn1
Limit-Object     Limit-Type      Upper-Limit    Warning    Current    Log-Interval
Route            -               -              -          -          -
Prefix           Alert-Percent   1000           800        760        5

```

# Display limits on the number of routes and prefixes of all VPN instances.
```
<HUAWEI> display ip routing-table limit all-vpn-instance
Limit-Object Limit-Type     Upper-Limit  Warning    Current    Log-Interval
----------------------------------------------------------------------------
VPN Instance Name: __dcn_vpn__
Route        Default        -            -          -          -           
Prefix       Default        -            -          7          5           
----------------------------------------------------------------------------
VPN Instance Name: vpna
Route        Default        -            -          -          -           
Prefix       Default        -            -          1          5

```

# Display limits on the number of public routes and prefixes.
```
<HUAWEI> display ip routing-table limit
_public_ Instance
Limit-Object Limit-Type     Upper-Limit  Warning    Current    Log-Interval
Route        Default        -            -          0          5           
Prefix       Default        -            -          0          5

```


**Table 1** Description of the
**display ip routing-table limit** command output

| Item | Description |
| --- | --- |
| VPN Instance Name | VPN instance name. |
| Limit-Object | Object whose total number is limited:   * Prefix. * Route. |
| Limit-Type | Limit type for the routes and prefixes in the routing table:   * Simply-Alert: indicates that only alarms are generated when the number of routes or prefixes exceeds the upper limit. * Alert-Percent: indicates the percentage of the alarm threshold of routes. * Default: indicates that the number of routes or prefixes is not limited by default. |
| Upper-Limit | Upper limit of routes or prefixes in the routing table. |
| Warning | Alarm threshold of routes or prefixes in the routing table. |
| Current | Number of routes or prefixes in the routing table. |
| Log-Interval | Interval at which logs are displayed when the number of routes or prefixes in the routing table exceeds the upper limit, in seconds. |
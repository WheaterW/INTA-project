display ipv6 routing-table limit
================================

display ipv6 routing-table limit

Function
--------

The **display ipv6 routing-table limit** command displays limits on the number of routes and prefixes.

![](../public_sys-resources/note_3.0-en-us.png)
 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.





Format
------

**display ipv6 routing-table limit vpn-instance** *vpn-instance-name*

**display ipv6 routing-table limit all-vpn-instance**

**display ipv6 routing-table limit**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all-vpn-instance** | Displays limits on the number of routes and prefixes in all IPv6 VPN instances. | - |
| **vpn-instance** *vpn-instance-name* | Displays limits on the number of routes and prefixes in a specified IPv6 VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

This command displays limits on the number of IPv6 routes and prefixes.

* The **display ipv6 routing-table limit** command displays limits on the number of IPv6 public routes and prefixes.
* The **display ipv6 routing-table limit all-vpn-instance** command displays limits on the number of routes and prefixes of all IPv6 VPN instances.
* The **display ipv6 routing-table limit vpn-instance** command displays limits on the number of routes and prefixes of a specified IPv6 VPN instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display limits on the number of IPv6 routes and prefixes of VPN instance named vpn1.
```
<HUAWEI> display ipv6 routing-table limit vpn-instance vpn1
IPv6 VPN Instance Name: vpn1
Limit-Object     Limit-Type      Upper-Limit    Warning    Current    Log-Interval
Route            Simply-Alert    -              -          -          -
Prefix           Alert-Percent   1000           800        760        5

```

# Display limits on the number of IPv6 routes and prefixes of all VPN instances.
```
<HUAWEI> display ipv6 routing-table limit all-vpn-instance
Limit-Object Limit-Type     Upper-Limit  Warning    Current    Log-Interval
----------------------------------------------------------------------------
VPN Instance Name: vrf1
Route        Default        -            -          -          -           
Prefix       Default        -            -          1          5           
----------------------------------------------------------------------------
VPN Instance Name: vrf2
Route        Default        -            -          -          -           
Prefix       Default        -            -          1          5

```

# Display limits on the number of IPv6 VPN instance routes and prefixes.
```
<HUAWEI> display ipv6 routing-table limit
_public_ Instance
Limit-Object Limit-Type     Upper-Limit  Warning    Current    Log-Interval
Route        Default        -            -          -          -           
Prefix       Default        -            -          0          5

```


**Table 1** Description of the
**display ipv6 routing-table limit** command output

| Item | Description |
| --- | --- |
| IPv6 VPN Instance Name | Name of a IPv6 VPN instance. |
| VPN Instance Name | Name of a VPN instance. |
| Limit-Object | Object whose number is limited:   * Prefix. * Route. |
| Limit-Type | Limit type for the routes and prefixes in the routing table:   * Simply-Alert: indicates that only alarms are generated when the number of routes or prefixes exceeds the upper limit. * Alert-Percent: indicates the percentage of the alarm threshold of routes. * Default: indicates that the number of routes or prefixes is not limited by default. |
| Upper-Limit | Upper limit of routes or prefixes in the routing table. |
| Warning | Alarm threshold of routes or prefixes in the routing table. |
| Current | Number of routes or prefixes in the routing table. |
| Log-Interval | Interval at which logs are displayed when the number of routes or prefixes in the routing table exceeds the upper limit, in seconds. |
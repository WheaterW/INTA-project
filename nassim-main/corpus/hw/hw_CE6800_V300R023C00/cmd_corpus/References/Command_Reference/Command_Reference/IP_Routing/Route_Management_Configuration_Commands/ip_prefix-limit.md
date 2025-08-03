ip prefix-limit
===============

ip prefix-limit

Function
--------



The **ip prefix-limit** command configures a limit on the number of IPv4 public route prefixes.

The **undo ip prefix-limit** command restores the default configuration.



By default, the maximum number of IPv4 public route prefixes is not limited.


Format
------

**ip prefix-limit** *number* { *alert-percent* [ **route-unchanged** ] | **simply-alert** }

**undo ip prefix-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the maximum number of IPv4 public route prefixes. | The value is an integer ranging from 1 to 4294967295. |
| *alert-percent* | Specifies the percentage of the maximum number of IPv4 public route prefixes. If you specify alert-percent in the command, when the number of IPv4 public route prefixes exceeds number x alert-percent/100, an alarm is generated. Additional IPv4 public route prefixes can still be added to the routing table until the number of IPv4 public route prefixes reaches number. Subsequent route prefixes are discarded. | The value is an integer ranging from 1 to 100. |
| **route-unchanged** | Indicates that the routing table remains unchanged. If you decrease alert-percent after the number of IPv4 public route prefixes exceeds number, whether the routing table remains unchanged is determined by route-unchanged:   * If you specify route-unchanged in the command, the routing table remains unchanged. * If you do not specify route-unchanged in the command, the system deletes the routes from the routing table and re-adds routes.   By default, the system deletes the routes from the routing table and re-adds routes. | - |
| **simply-alert** | Indicates the following function: If you specify simply-alert in the command, new IPv4 public route prefixes can still be added to the routing table and only an alarm is generated after the number of IPv4 public route prefixes exceeds number. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If the device imports a large number of routes, system performance may be affected when processing services because the routes consume excessive system resources. To improve system security and reliability, run the **ip prefix-limit** command to configure a limit on the number of IPv4 public route prefixes. When the number of IPv4 public route prefixes exceeds the limit, an alarm is generated, prompting you to check whether unneeded IPv4 public route prefixes exist.



**Configuration Impact**

After the **ip prefix-limit** command is run, the device may discard unneeded IPv4 public route prefixes.

* If the number of IPv4 public route prefixes exceeds the value calculated from number\* alert-percent/100, an alarm (L3VPN\_1.3.6.1.2.1.10.166.11.0.3 mplsL3VpnVrfRouteMidThreshExceeded) is generated.
* If the number of IPv4 public route prefixes exceeds number, an alarm (L3VPN\_1.3.6.1.2.1.10.166.11.0.4 mplsL3VpnVrfNumVrfRouteMaxThreshExceeded) is generated.
* If the number of IPv4 public route prefixes falls below the value calculated from number\* alert-percent/100, a clear alarm (L3VPN\_1.3.6.1.4.1.2011.5.25.177.1.3.8 hwL3vpnVrfRouteMidThreshCleared) is generated.
* If the number of IPv4 public route prefixes exceeds number, a clear alarm (L3VPN\_1.3.6.1.2.1.10.166.11.0.6 mplsL3VpnNumVrfRouteMaxThreshCleared) is generated.

**Precautions**

If the **ip prefix-limit** command is run more than once, the last configuration overrides the previous one.After the number of IPv4 public route prefixes exceeds the limit, note the following rules:

* If you run the **ip prefix-limit** command to increase or the **undo ip prefix-limit** command to delete the limit, the device relearns IPv4 public route prefixes.
* Direct and static routes can still be added to the IP routing table.


Example
-------

# Configure simply-alert so that only an alarm is generated when the device imports more than 1000 IPv4 public route prefixes.
```
<HUAWEI> system-view
[~HUAWEI] ip prefix-limit 1000 simply-alert

```
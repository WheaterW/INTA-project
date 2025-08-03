conflict auto-recycle interval
==============================

conflict auto-recycle interval

Function
--------

The **conflict auto-recycle interval** command enables automatic reclaim of conflicting IP addresses in the global address pool and configures the interval for the automatic reclaim.

The **undo conflict auto-recycle interval** command disables automatic reclaim of conflicting IP addresses in the global address pool and deletes the configured interval for the automatic reclaim.

By default, automatic reclaim of conflicting IP addresses in the global address pool is disabled.



Format
------

**conflict auto-recycle interval day** *day* [ **hour** *hour* [ **minute** *minute* ] ]

**undo conflict auto-recycle interval**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **day** *day* | Specifies the interval for the automatic reclaim, in days. | The value is an integer that ranges from 0 to 999. The default value is 0. |
| **hour** *hour* | Specifies the interval for the automatic reclaim, in hours. | The value is an integer that ranges from 0 to 23. The default value is 0. |
| **minute** *minute* | Specifies the interval for the automatic reclaim, in minutes. | The value is an integer that ranges from 0 to 59. The default value is 0. |




Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. When a DHCP server allocates IP addresses to clients, IP address conflict may occur because IP addresses of some hosts have been manually configured. In this case, the DHCP server considers these IP addresses as conflicting IP addresses, and allocates available IP addresses from the conflicting IP addresses to clients only after available IP addresses in the address pool are used up. To reclaim conflicting IP addresses promptly, the administrator can run this command to enable automatic reclaim of conflicting IP addresses and specify the reclaim interval. The automatic reclaim timer is started after the configuration is delivered. When the configured interval expires, all conflicting IP addresses in the address pool are automatically reclaimed.

**Prerequisites**

A global IP address pool has been created using the ip pool command.



Example
-------

# Enable automatic reclaim for conflicting IP addresses in the global address pool global1, and set the interval for automatic reclaim to one day.
```
<HUAWEI> system-view
[~HUAWEI] ip pool global1
[*HUAWEI-ip-pool-global1] conflict auto-recycle interval day 1

```
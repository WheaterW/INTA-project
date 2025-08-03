dhcp server conflict auto-recycle interval
==========================================

dhcp server conflict auto-recycle interval

Function
--------

The **dhcp server conflict auto-recycle interval** command enables automatic reclaim of conflicting IP addresses in the interface address pool and configures the interval for the automatic reclaim.

The **undo dhcp server conflict auto-recycle interval** command disables automatic reclaim of conflicting IP addresses in the interface address pool and deletes the configured interval for the automatic reclaim.

By default, automatic reclaim of conflicting IP addresses in the interface address pool is disabled.



Format
------

**dhcp server conflict auto-recycle interval day** *day* [ **hour** *hour* [ **minute** *minute* ] ]

**undo dhcp server conflict auto-recycle interval**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **day** *day* | Specifies the interval for the automatic reclaim, in days. | The value is an integer that ranges from 0 to 999. |
| **hour** *hour* | Specifies the interval for the automatic reclaim, in hours. | The value is an integer ranging from 0 to 23. |
| **minute** *minute* | Specifies the interval for the automatic reclaim, in minutes. | The value is an integer that ranges from 0 to 59. |




Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

This command applies to DHCP servers. When a DHCP server allocates IP addresses to clients, IP address conflict may occur because IP addresses of some hosts have been manually configured. In this case, the DHCP server considers these IP addresses as conflicting IP addresses, and allocates available IP addresses from the conflicting IP addresses to clients only after available IP addresses in the address pool are used up. To reclaim conflicting IP addresses promptly, the administrator can run this command to enable automatic reclaim of conflicting IP addresses and specify the reclaim interval. The automatic reclaim timer is started after the configuration is delivered. When the configured interval expires, all conflicting IP addresses in the address pool are automatically reclaimed.

**Prerequisites**

1. IP addresses in the interface address pool have been configured using the **ip address** command.
2. The DHCP server function has been enabled on the interface using the **dhcp select interface** command.


Example
-------

# Enable automatic reclaim for conflicting IP addresses in the address pool on interface
100GE
1/0/1, and set the interval for automatic reclaim to one day.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip address 192.168.1.1 24
[*HUAWEI-100GE1/0/1] dhcp select interface
[*HUAWEI-100GE1/0/1] dhcp server conflict auto-recycle interval day 1

```
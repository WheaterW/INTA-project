netstream ip
============

netstream ip

Function
--------



The **netstream ip** command enables IPv4 flow statistics collection on the inbound and outbound interfaces.

The **undo netstream ip** command restores the default setting.



By default, statistics collection for flows is disabled on the inbound and outbound interfaces


Format
------

**netstream** { **inbound** | **outbound** } **ip**

**undo netstream** { **inbound** | **outbound** } **ip**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **inbound** | Enables IPv4 flow statistics collection on the inbound interface. | - |
| **outbound** | Enables IPv4 flow statistics collection on the outbound interface. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Sub-interface view,Interface group view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To export IPv4 flow statistics, you must run the **netstream ip** command to enable the IPv4 flow statistics collection function on the interface.You can run the netstream ip and **netstream ipv6** commands on an interface to collect statistics about IPv4 and IPv6 traffic respectively.


Example
-------

# Enable flow statistics collection for the incoming IPv4 packets on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] netstream inbound ip

```
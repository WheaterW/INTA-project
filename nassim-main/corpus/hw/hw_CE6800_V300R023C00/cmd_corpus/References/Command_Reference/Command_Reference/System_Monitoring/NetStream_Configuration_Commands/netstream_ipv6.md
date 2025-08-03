netstream ipv6
==============

netstream ipv6

Function
--------



The **netstream ipv6** command enables IPv6 flow statistics collection on the inbound and outbound interfaces.

The **undo netstream ipv6** command restores the default setting.



By default, statistics collection for flows is disabled on the inbound and outbound interfaces.


Format
------

**netstream** { **inbound** | **outbound** } **ipv6**

**undo netstream** { **inbound** | **outbound** } **ipv6**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **inbound** | Enables IPv6 flow statistics collection on the inbound interface. | - |
| **outbound** | Enables IPv6 flow statistics collection on the outbound interface. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,Sub-interface view,Interface group view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To export IPv6 flow statistics, you must run the **netstream ipv6** command to enable the IPv6 flow statistics collection function on the interface.You can run the **netstream ipv6** command and the **netstream ip** command on an interface to collect statistics about IPv6 traffic and IPv4 traffic respectively.


Example
-------

# Enable statistics collection for the incoming IPv6 flows on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] netstream inbound ipv6

```
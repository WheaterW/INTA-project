arp limit
=========

arp limit

Function
--------



The **arp limit** command limits the maximum number of dynamic Address Resolution Protocol (ARP) entries that an interface can learn.

The **undo arp limit** command restores the default number of dynamic ARP entries that an interface can learn.



By default, the maximum number of dynamic ARP entries that an interface can learn is 1048576.


Format
------

**arp limit** *limitMaxNum*

**undo arp limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limitMaxNum* | Specifies the maximum number of the ARP entries that the interface can learn. | For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 131072. The default value is 131072.  For the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S:The value is an integer ranging from 1 to 261120. The default value is 261120. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Interface group view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



If an unauthorized user sends a large number of ARP messages to a device, the device learns a large number of ARP entries in a short period of time, causing the ARP buffer to overflow. As a result, normal operation of the network is affected. To address such a problem, you can set the maximum number of ARP entries that each interface can learn. The ARP entries include dynamic entries learned through ARP packets, ARP entries delivered by the controller to forwarders, and redirection entries synchronized remotely through BGP EVPN routes.



**Configuration Impact**

If the number of ARP entries that an interface can learn changes, and the number of the learned ARP entries exceeds the changed value, the interface cannot learn additional ARP entries. You can delete the excess ARP entries based on the system prompt.If this command is run more than once, all configurations take effect.


Example
-------

# Configure the maximum number of dynamic ARP entries that interface can learn to 20.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] arp limit 20

```
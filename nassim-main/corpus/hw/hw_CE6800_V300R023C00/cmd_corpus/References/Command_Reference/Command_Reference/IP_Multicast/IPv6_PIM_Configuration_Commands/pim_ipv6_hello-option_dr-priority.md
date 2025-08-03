pim ipv6 hello-option dr-priority
=================================

pim ipv6 hello-option dr-priority

Function
--------



The **pim ipv6 hello-option dr-priority** command sets the priority of a PIM interface for DR election.

The **undo pim ipv6 hello-option dr-priority** command restores the default value of the priority.



By default, the DR election priority of an IPv6 PIM interface is 1.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6 hello-option dr-priority** *priority*

**undo pim ipv6 hello-option dr-priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies a DR election priority. A larger value indicates a higher priority. | The value is an integer ranging from 0 to 4294967295. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On an IPv6 PIM-SM shared network segment, a DR is dynamically elected among candidate Router interfaces. DR election is based on priorities and IP addresses of interfaces on Routers. In a DR election process, Routers exchange Hello messages carrying DR election priorities.

* If all Routers support Hello messages that carry DR election priorities, the interface with the highest DR election priority wins. If all interfaces have the same DR election priority, the interface with the largest IP address wins.
* If one or more Routers do not support Hello messages that carry DR priorities, the interface with the largest IP address wins.To change the DR election priority of an IPv6 PIM interface, run the pim hello-option dr-priority command.

Example
-------

# Set the DR election priority of 100GE1/0/1 to 3.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 hello-option dr-priority 3

```
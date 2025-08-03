ipv6 nd nud reachable-time
==========================

ipv6 nd nud reachable-time

Function
--------



The **ipv6 nd nud reachable-time** command configures the neighbor reachable time.

The **undo ipv6 nd nud reachable-time** command restores the default neighbor reachable time.



By default, the IPv6 neighbor reachable time is 1200000 milliseconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd nud reachable-time** *value*

**undo ipv6 nd nud reachable-time**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the neighbor reachable time. | The value is an integer ranging from 1 to 3600000, in milliseconds. |



Views
-----

100ge sub-interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The IPv6 neighbor reachable time provides the following functions:

* Controlling the aging time of ND entries on a local device
* Being a parameter in an RA message to help a host to generate the neighbor reachable timeEach RA message sent by a device carries the neighbor reachable time so that all the nodes along the same link can use the same time.

**Prerequisites**

IPv6 has been enabled on the involved interface using the **ipv6 enable** command.

**Configuration Impact**

A smaller neighbor reachable time set on a device indicates that the device can probe the neighbor reachability more quickly but more network bandwidth and CPU resources are occupied. Therefore, on a normal IPv6 network, you are not recommended to set the neighbor reachable time to a smaller value. The default value, 1200000 milliseconds, is recommended.The **ipv6 nd nud reachable-time** command is circular in nature. That is, if the neighbor reachable times set two times are different, the latest setting takes effect.

**Precautions**

Commonly, the neighbor reachable time set on a device is the same as that carried in an RA message. In the following cases, however, the neighbor reachable time set on a device is the default value 1200000 milliseconds whereas the neighbor reachable time carried in the RA message is 0 milliseconds:

* The neighbor reachable time is not set on the device, that is, the default value is used.
* The **undo ipv6 nd nud reachable-time** command is run to restore the default setting.After a host receives an RA message with the neighbor reachable time being 0 milliseconds, it uses the default neighbor reachable time 1200000 milliseconds.

Example
-------

# Set the neighbor reachable time on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd nud reachable-time 10000

```
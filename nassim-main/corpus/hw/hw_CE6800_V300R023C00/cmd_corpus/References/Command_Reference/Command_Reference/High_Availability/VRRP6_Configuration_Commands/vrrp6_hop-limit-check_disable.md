vrrp6 hop-limit-check disable
=============================

vrrp6 hop-limit-check disable

Function
--------



The **vrrp6 hop-limit-check disable** command disables a router from checking the hop count in a received Virtual Router Redundancy Protocol for IPv6 (VRRP6) packet.

The **undo vrrp6 hop-limit-check disable** command enables a router to check the hop count in a received VRRP6 packet.



By default, a router checks the hop count in a received VRRP6 packet.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vrrp6 hop-limit-check disable**

**undo vrrp6 hop-limit-check disable**


Parameters
----------

None

Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

According to relevant standards, a router checks the hop count in every received VRRP6 packet and discards a packet if its hop count is not 255.If a non-Huawei device that does not support a hop count check sends a VRRP6 packet carrying a hop count other than 255 to a Huawei device that supports a hop count check, the Huawei device discards the packet. To resolve this issue, run the vrrp6 hop-limit-check disable command to disable a router from checking the hop count in a received VRRP6 packet.

**Configuration Impact**

After the vrrp6 hop-limit-check disable command is run on a router, the router does not check the hop count in a received VRRP6 packet.

**Precautions**

To prevent a router from being attacked by invalid packets, exercise caution when running the vrrp6 hop-limit-check disable command.


Example
-------

# Disable a router from checking the hop count in a received VRRP6 packet.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8::1 64
[*HUAWEI-100GE1/0/1] vrrp6 vrid 1 virtual-ip fe80::1 link-local
[*HUAWEI-100GE1/0/1] vrrp6 hop-limit-check disable

```
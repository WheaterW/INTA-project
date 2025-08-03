vrrp6 checksum exclude pseudo-header
====================================

vrrp6 checksum exclude pseudo-header

Function
--------



The **vrrp6 checksum exclude pseudo-header** command configures a device to calculate a Virtual Router Redundancy Protocol for IPv6 (VRRP6) packet's checksum based on the content excluding the IPv6 pseudo header.

The **undo vrrp6 checksum exclude pseudo-header** command restores the default configuration.



By default, a device calculates a VRRP6 packet's checksum based on the content including the IPv6 pseudo header.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vrrp6 checksum exclude pseudo-header**

**undo vrrp6 checksum exclude pseudo-header**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Various devices deployed on a network on a large scale have different packet processing capabilities and modes. In VRRP6 scenarios, a VRRP6 backup group may contain Huawei and non-Huawei devices. After a Huawei device receives a VRRP6 packet, it calculates the packet's checksum based on the content including the IPv6 pseudo header. However, a non-Huawei device may calculate the packet's checksum based on the content excluding the IPv6 pseudo header. As a result, VRRP negotiation between the Huawei and non-Huawei devices may fail. To resolve this issue, run the vrrp6 checksum exclude pseudo-header command to configure the Huawei device to calculate the packet's checksum based on the content excluding the IPv6 pseudo header.


Example
-------

# Configure a device to calculate a VRRP6 packet's checksum based on the content excluding the IPv6 pseudo header.
```
<HUAWEI> system-view
[~HUAWEI] vrrp6 checksum exclude pseudo-header

```
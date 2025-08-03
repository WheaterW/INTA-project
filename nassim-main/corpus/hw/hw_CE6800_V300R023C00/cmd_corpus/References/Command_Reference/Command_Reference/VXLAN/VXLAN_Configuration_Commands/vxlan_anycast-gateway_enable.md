vxlan anycast-gateway enable
============================

vxlan anycast-gateway enable

Function
--------



The **vxlan anycast-gateway enable** command enables distributed gateway.

The **undo vxlan anycast-gateway enable** command disables distributed gateway.



By default, distributed gateway is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**vxlan anycast-gateway enable**

**undo vxlan anycast-gateway enable**


Parameters
----------

None

Views
-----

VBDIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable distributed gateway on a VBDIF interface and allow the gateway to learn only user-side ARP, ND, or DHCP packets, run thevxlan anycast-gateway enable command. After distributed gateway is enabled, the gateway:

* Processes only received user-side ARP, ND, or DHCP packets and generates host routes accordingly.
* Deletes network-side ARP, ND, or DHCP entries already learned and deletes the corresponding host routes.

**Configuration Impact**

After distributed gateway is enabled:

* VXLAN tunnel-side static ARP, ND, or DHCP entries cannot be configured on the gateway.
* If distributed gateways have the same IP address, they do not report ARP, ND, or DHCP conflicts.
* If ARP proxy is not enabled but the network-side devices and user-side hosts have the same IP address, the gateways do not report IP address conflict alarms.

Example
-------

# Enable distributed gateway on VBDIF 10.
```
<HUAWEI> system-view
[~HUAWEI] bridge-domain 10
[*HUAWEI-bd10] quit
[*HUAWEI] interface vbdif 10
[*HUAWEI-Vbdif10] vxlan anycast-gateway enable

```
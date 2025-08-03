tunnel pathmtu enable
=====================

tunnel pathmtu enable

Function
--------



The **tunnel pathmtu enable** command enables path MTU auto-discovery on a tunnel.

The **undo tunnel pathmtu enable** command disables path MTU auto-discovery on a tunnel.



By default, path MTU auto-discovery is disabled for a tunnel.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**tunnel pathmtu enable**

**undo tunnel pathmtu enable**


Parameters
----------

None

Views
-----

Tunnel interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a GRE tunnel is set up between two BGP nodes on which the **peer path-mtu auto-discovery** command has been run, path MTU auto-discovery can be enabled on the tunnel interface. This prevents TCP packets that contain BGP data from being fragmented multiple times during transmission, improving efficiency of BGP data transmission.

**Prerequisites**

The **tunnel-protocol gre** command has been configured in the tunnel interface view.

**Precautions**

The tunnel pathmtu enable and **mtu** commands cannot be run on the same tunnel interface. If the **mtu** command has been run on a tunnel interface, the **tunnel pathmtu enable** command cannot be executed on the interface.

* In a scenario where path MTU (PMTU) learning is enabled for an IPv4 GRE tunnel and the smallest IPv4 MTU of the tunnel is less than 1312 bytes (1280+32), the IPv6 MTU learned by the IPv4 GRE interface is less than 1280 bytes. If the ingress sends an IPv6 packet longer than the learned IPv6 MTU, the IPv6 packet is dropped. To address this problem, perform either of the following operations:
* Disable PMTU learning for the IPv4 GRE tunnel.
* If the IPv4 GRE tunnel must have PMTU learning enabled and must carry IPv6 packets, ensure that the tunnel's transit nodes each have an IPv4 MTU no less than 1312 bytes.
* PMTU learning is always enabled for IPv6 GRE tunnels. In a scenario where the smallest IPv6 MTU of an IPv6 GRE tunnel is less than 1332 bytes (1280+52), the MTU learned by the IPv6 GRE interface is less than 1280 bytes. If the ingress sends an IPv6 packet longer than the learned IPv6 MTU, the IPv6 packet is dropped. To address this problem, ensure that the tunnel's transit nodes each have an IPv6 MTU no less than 1332 bytes.


Example
-------

# Enable path MTU auto-discovery on interface Tunnel 10.
```
<HUAWEI> system-view
[~HUAWEI] interface Tunnel 10
[*HUAWEI-Tunnel10] tunnel-protocol gre
[*HUAWEI-Tunnel10] tunnel pathmtu enable

```
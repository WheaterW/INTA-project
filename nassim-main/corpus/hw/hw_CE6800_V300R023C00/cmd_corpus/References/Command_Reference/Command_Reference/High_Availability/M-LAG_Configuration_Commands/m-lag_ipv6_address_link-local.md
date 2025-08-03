m-lag ipv6 address link-local
=============================

m-lag ipv6 address link-local

Function
--------



The **m-lag ipv6 address link-local** command configures an IPv6 link-local address dedicated for OSPFv3/BGP4+ over M-LAG.

The **undo m-lag ipv6 address link-local** command deletes the IPv6 link-local address dedicated for OSPFv3/BGP4+ over M-LAG.



By default, the m-lag ipv6 address link-local command is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**m-lag ipv6 address** *ipv6-address* **link-local**

**undo m-lag ipv6 address** *ipv6-address* **link-local**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **m-lag ipv6 address link-local** command to configure an IPv6 link-local address dedicated for OSPFv3/BGP4+ over M-LAG.

**Precautions**

1. The M-LAG link-local address on an interface references the link-local address of the interface. Each interface can be configured with only one M-LAG link-local address.
2. The M-LAG link-local address cannot be the same as any link-local address on the remote M-LAG member device.
3. Before configuring an M-LAG IPv6 address for an interface, you must enable IPv6 on the interface.
4. If you unbind a VNI from a BD and a dedicated M-LAG IPv6 link-local address has been configured on the corresponding VBDIF interface using the **m-lag ipv6 address link-local** command, the dedicated M-LAG IPv6 link-local address on the VBDIF interface is also deleted.
5. The **m-lag ipv6 address link-local** command can be configured on a VBDIF interface only after a VNI is bound to the corresponding BD.
6. If an M-LAG IPv6 link-local address configured for an interface using the **m-lag ipv6 address link-local** command is the same as a primary or secondary IPv6 address on the interface, the M-LAG IPv6 link-local address cannot be delivered.
7. If the ipv6 address link-local command is configured on an interface, the **m-lag ipv6 address link-local** command cannot be configured on the interface.
8. When an IPv6 address is configured using the **m-lag ipv6 address link-local** command, the prefix of the specified IPv6 address must match FE80::/10. When an IPv6 address is configured using the m-lag ipv6 address command, the prefix of the specified IPv6 address cannot be FE80::/10.
9. On a device, all VLANIF or VBDIF interfaces bound to the same VPN instance cannot be configured with the same M-LAG link-local address. If Layer 3 interfaces on M-LAG master and backup devices are bound to the same VPN instance, the link-local address of the Layer 3 interface on the local M-LAG device cannot be the same as the M-LAG link-local address configured on the remote M-LAG device.
10. The M-LAG link-local address on an interface of a device cannot be the same as the VRRP6 link-local address on the interface.

Example
-------

# Configure an IPv6 link-local address dedicated for OSPFv3/BGP4+ over M-LAG.
```
<HUAWEI> system-view
[~HUAWEI] interface vlanif 100
[*HUAWEI-Vlanif100] m-lag ipv6 address FE80:1000::1 link-local

```
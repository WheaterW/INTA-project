m-lag ipv6 address
==================

m-lag ipv6 address

Function
--------



The **m-lag ipv6 address** command configures a dedicated IPv6 address for BGP4+ over M-LAG.

The **undo m-lag ipv6 address** command deletes a dedicated IPv6 address for BGP4+ over M-LAG.



By default, no M-LAG IPv6 address is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**m-lag ipv6 address** *ipv6-address*

**undo m-lag ipv6 address** *ipv6-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **address** *ipv6-address* | Specifies the IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **m-lag ipv6 address** command to configure an IPv6 address dedicated for BGP4+ over M-LAG.

**Precautions**

1. An M-LAG IPv6 address can only be a global unicast address. An interface can be configured with only one M-LAG IPv6 address and a maximum of 16 global unicast addresses.
2. An M-LAG IPv6 address must be unique on the entire network, and cannot be the same as any IPv6 address on the local device or other devices on the network.
3. A multicast, anycast, or loopback address cannot be configured as an M-LAG IPv6 address.
4. If an M-LAG IPv6 address has been configured on an interface and a new M-LAG IPv6 address is configured on the interface, the new address overwrites the original one.
5. A link-local address cannot be configured as an M-LAG IPv6 address.
6. Before configuring an M-LAG IPv6 address for an interface, you must enable IPv6 on the interface.
7. If you unbind a VNI from a BD and an IPv6 address has been configured on the corresponding VBDIF interface using the **m-lag ipv6 address** command, the dedicated M-LAG IPv6 address on the VBDIF interface is also deleted.
8. The **m-lag ipv6 address** command can be configured on a VBDIF interface only after a VNI is bound to the corresponding BD.
9. If an M-LAG IPv6 address configured for an interface using the **m-lag ipv6 address** command is the same as a primary or secondary IPv6 address on the interface, the M-LAG IPv6 address cannot be delivered.
10. When an IPv6 address is configured using the **m-lag ipv6 address** command, the prefix of the specified IPv6 address cannot be FE80::/10. When an IPv6 address is configured using the **m-lag ipv6 address link-local** command, the prefix of the specified IPv6 address must match FE80::/10.

Example
-------

# Configure an IPv6 address dedicated for BGP4+ over M-LAG.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[*HUAWEI-vlan100] interface vlanif 100
[*HUAWEI-Vlanif100] ipv6 enable
[*HUAWEI-Vlanif100] m-lag ipv6 address 2001:db8:1::1

```
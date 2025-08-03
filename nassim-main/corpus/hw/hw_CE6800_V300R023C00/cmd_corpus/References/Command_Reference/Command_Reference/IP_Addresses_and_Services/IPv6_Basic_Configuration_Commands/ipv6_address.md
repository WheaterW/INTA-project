ipv6 address
============

ipv6 address

Function
--------



The **ipv6 address** command configures a global unicast address for an interface.

The **undo ipv6 address** command deletes the global unicast address configured for an interface.



By default, no global unicast address is configured for an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 address** { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } [ **tag** *tag-value* ]

**undo ipv6 address**

**undo ipv6 address** { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } [ **tag** *tag-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address to be configured for the interface. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the prefix length of an IPv6 address. | The value is an integer that ranges from 1 to 128. In the EUI-64 address format, the prefix length must be less than 64. |
| *ipv6-address/prefix-length* | Specifies the IPv6 address and prefix length of an interface. | IPv6 address/IPv6 address prefix length. |
| **tag** *tag-value* | Specifies a label value. | <1-4294967295> |



Views
-----

100ge sub-interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A global unicast address equals an IPv4 public network address. Global unicast addresses are for links that can be aggregated and are provided for network service providers. The structure of global unicast addresses allows route-prefix aggregation for limiting the number of global routing entries. A global unicast address is composed of a 48-bit route prefix managed by operators, a 16-bit subnet ID managed by local nodes, and a 64-bit interface ID.Configuring an IPv6 address with the prefix length of 127 has the following advantages:

* Avoids loops in traffic forwarding on P2P links that have no neighbor discovery mechanisms.
* Addresses the ND cache exhaustion issue when network devices are attacked.
* Saves IPv6 address resources.

**Prerequisites**

Before running the **ipv6 address** command to configure a global unicast address for an interface, you need to run the **ipv6 enable** command in the interface view to enable the IPv6 function on the interface.

**Configuration Impact**

If the ipv6 address is run to configure an IPv6 address for an interface but no link-local address is configured for the interface, the system automatically generates a link-local address for the interface.If no parameter (IPv6 address and prefix length) is specified in the **undo ipv6 address** command, all the IPv6 addresses configured for the interface are deleted.

**Precautions**

* An interface can be configured with a maximum of 16 global unicast addresses.
* The following configurations are not supported on different interfaces of the same device:
  + The IPv6 addresses are the same.
  + The network prefixes corresponding to the IPv6 addresses are the same. For example, the IPv6 address of interface A is 2001:db8:1::1/32 and the corresponding network prefix is 2001:db8::. The IPv6 address of interface B is 2001:db8::1/16 and the corresponding network prefix is 2001::. If the network prefixes of interfaces A and B are different, the configuration is successful. If the IPv6 address of interface B is 2001:db8:2::1/32 and the corresponding network prefix is 2001:db8::, the configuration fails because the network prefixes of interfaces A and B are the same.The 6to4 addresses can be configured for a 6to4 tunnel interface but not a 6over4 tunnel interface.The following IPv6 addresses cannot be configured for an interface:
  + Loopback address (::1/128)
  + Unspecified address (::/128)
  + Multicast address
  + Anycast address
* IPv4-mapped IPv6 addresses (0:0:0:0:0:FFFF:IPv4-address) can be configured on the public network but not on the private network.A global unicast address cannot be the same as its network prefix, because this type of address is a subnet-router anycast address reserved for a device. However, this rule does not apply to an IPv6 address with a 127-bit network prefix. For example, if the **ipv6 address** command is run to configure an IPv6 address as 2001:db8:5::10 with the prefix length of 124 bits and the network prefix of the IPv6 address is also 2001:db8:5::10, this IPv6 address is a subnet-router anycast address and cannot be configured as a global unicast address. To configure an anycast address, run the **ipv6 address anycast** command.


Example
-------

# Configure a global unicast address 2001:db8::/127 for 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8:: 127

```
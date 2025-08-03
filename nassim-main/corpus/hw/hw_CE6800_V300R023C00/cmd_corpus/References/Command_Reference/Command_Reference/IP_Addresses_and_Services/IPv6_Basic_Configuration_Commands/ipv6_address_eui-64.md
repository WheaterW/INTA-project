ipv6 address eui-64
===================

ipv6 address eui-64

Function
--------



The **ipv6 address eui-64** command configures an EUI-64 global unicast address for an interface.

The **undo ipv6 address eui-64** command deletes the configuration.



By default, no EUI-64 global unicast address is configured for an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 address** { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } **eui-64** [ **tag** *tag-value* ]

**undo ipv6 address** { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } **eui-64** [ **tag** *tag-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address to be configured for the interface. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the prefix length of an IPv6 address. | The value is an integer that ranges from 1 to 128. In the EUI-64 address format, the prefix length must be less than 64. |
| *ipv6-address/prefix-length* | Specifies the IPv6 address and prefix length of an interface. | IPv6 address/IPv6 address prefix length. |
| **tag** *tag-value* | Specifies a tag. | <1-4294967295> |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the IPv6 addressing scheme, every IPv6 unicast address needs an interface identifier. The interface identifier is unique, similar to a 48-bit MAC address.The interface identifier of an IPv6 host address complies with the IEEE EUI-64 format. A 64-bit interface identifier is generated based on an existing MAC address; therefore, such an interface identifier is unique globally.If the interface has been configured with a MAC address, the EUI-64 address is generated based on the MAC address of the interface, with FFFE added in the middle.If the interface has not been configured with a MAC address, the EUI-64 address is generated based on the following rules:

* For Layer 3 physical interfaces and sub-interfaces, the EUI-64 address is generated based on the MAC address of a physical interface, with FFFE added in the middle.
* For loopback interfaces , VBDIF interfaces, and tunnel interface, the EUI-64 address is generated based on the MAC address of an interface, with the last two bytes following the interface index added in the middle.
* For Eth-Trunk interfaces and its sub-interfaces, Global-VE sub-interfaces, VE sub-interfaces, and VLANIF interfaces, the EUI-64 address is generated based on the MAC address of an interface, with FFFE added in the middle.

**Prerequisites**

Before running the **ipv6 address eui-64** command to configure an EUI-64 global unicast address for an interface, you need to run the **ipv6 enable** command in the interface view to enable the IPv6 function on the interface.

**Configuration Impact**

If the ipv6 address eui-64 is run to configure an EUI-64 IPv6 address for an interface but no link-local address is configured for the interface, the system automatically generates a link-local address for the interface.

**Precautions**

The following conditions are prohibited for different interfaces on the same device:

* The EUI-64 IPv6 addresses are the same.
* The network prefixes of the EUI-64 IPv6 addresses are the same. For example, if the IPv6 address of interface A is 2001:db8:1::1/32 and its network prefix is 2001:db8:: and the IPv6 address of interface B is 2001:db8::1/16 and its network prefix is 2001::, the configuration succeeds. If the IPv6 address of interface B is 2001:db8:2::1/32 and its network prefix is also 2001:db8::, the configuration fails.An interface can be configured with a maximum of 16 global unicast addresses.The following EUI-64 IPv6 addresses cannot be configured for an interface:
* Loopback address (::1/128)
* Unspecified address (::/128)
* Multicast address
* Anycast addressIPv4-mapped IPv6 addresses (0:0:0:0:0:FFFF:IPv4-address) can be configured on public networks but not on VPNs.The **ipv6 address** command is used to specify a 128 bit IP address. Using the **ipv6 address eui-64** command, you can specify the high-order 64 bits of an IPv6 address. The low-order 64 bits of an IP address are automatically generated in the EUI-64 format. Even when the low-order 64 bits are manually specified, the automatically generated ones will override them.

Example
-------

# Configure an EUI-64 IPv6 address 2001:db8:1::1/64 on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswich
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8:1::1 64 eui-64

```
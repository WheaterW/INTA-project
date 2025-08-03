ipv6 address anycast
====================

ipv6 address anycast

Function
--------



The **ipv6 address anycast** command configures an anycast IPv6 address.

The **undo ipv6 address anycast** command deletes an anycast IPv6 address.



By default, anycast IPv6 addresses are not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 address** { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } **anycast** [ **tag** *tag-value* ]

**undo ipv6 address** { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } **anycast** [ **tag** *tag-value* ]


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

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



An anycast address is used to identify a group of interfaces that are configured on different nodes. The packets that are sent to an anycast address are transmitted to an interface that is in the interface group identified by the anycast address and is closest to the source node. (The distance between an interface and the source node is calculated based on a routing protocol).When the 6to4 tunnel is used for communication between the 6to4 network and the native IPv6 network, you can configure an anycast address whose prefix is 2002:c058:6301/48 on the tunnel interface of the 6to4 relay router. If an anycast address is used, you need to configure the same address for the tunnel interfaces of all devices. In this manner, the number of addresses is reduced.



**Prerequisites**

IPv6 has been enabled on the involved interface using the **ipv6 enable** command.

**Configuration Impact**

When the **undo** command is run, if no parameter is specified, all IPv6 addresses (including anycast addresses but excluding the link-local address that is configured automatically) are deleted.

**Precautions**

* A maximum of 16 IPv6 anycast addresses can be configured on an interface.
* An anycast address cannot be used as a source address. Therefore, when a device needs to send packets, a global unicast address must be configured.
* Anycast addresses are not limited to subnet-router anycast addresses. You can run the **ipv6 address anycast** command to configure a global unicast address as an anycast address.


Example
-------

# Configure the anycast address 2001:db8:5::10/124 on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 address 2001:db8:5::10 124 anycast

```
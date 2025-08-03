ipv6 nd ra prefix
=================

ipv6 nd ra prefix

Function
--------



The **ipv6 nd ra prefix** command configures the prefix carried in RA messages sent by the routing device.

The **undo ipv6 nd ra prefix** command configures RA messages not to carry the specified prefix.



By default, RA messages contain only the prefix specified through the ipv6 address command.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd ra prefix** { *ipv6-address* *prefix-length* | *ipv6-prefix/ipv6-prefix-length* } *valid-lifetime* *preferred-lifetime* [ **no-autoconfig** ] [ **off-link** ]

**undo ipv6 nd ra prefix** { *ipv6-address* *prefix-length* | *ipv6-prefix/ipv6-prefix-length* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address carried in the RA message. | The value is a 32-digit hexadecimal number in format X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the prefix length of an IPv6 address. | The value is an integer that ranges from 0 to 128. Based on the IPv6 address and prefix length, a host can calculate the IPv6 prefix carried in the RA message. When allocating the IPv6 address by means of stateless auto-configuration, specify the length of address prefixes as 64 bites. Otherwise, the address will be invalid and RA messages will be discarded. |
| *ipv6-prefix/ipv6-prefix-length* | Specifies the prefix of an IPv6 address. | The value is a 32-digit hexadecimal number in format X:X:X:X:X:X:X:X. |
| *valid-lifetime* | Specifies the valid lifetime of a prefix. The valid lifetime determines the on-link status of the prefix. If this parameter is specified, the prefix carried in a received RA message is valid within the specified lifetime. | The value is an integer ranging from 0 to 4294967295, in seconds. |
| *preferred-lifetime* | If this parameter is specified, the address generated based on the prefix through stateless address autoconfiguration in a received RA message is retained for a specified preferred lifetime. The preferred lifetime is less than or equal to the valid lifetime. | The value is an integer that ranges from 0 to 4294967295, in seconds. The preferred lifetime cannot be bigger than the valid lifetime. |
| **no-autoconfig** | Deletes the A-Flag. If this parameter is specified, the configured prefix cannot be used for stateless address autoconfiguration. That is, the configured prefix cannot be used to generate addresses. | - |
| **off-link** | Indicates the L flag. If this parameter is specified, the prefix can be used for on-link determination. If this parameter is not specified, the advertisement makes no statement about on-link or off-link properties of the prefix. In other words, if the L flag is not set, a host must not conclude that an address derived from the prefix is off-link. That is, it must not update a previous indication that the address is on-link. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the **ipv6 nd ra prefix** command is run to configure a prefix, the device advertises both the address prefix configured using the **ipv6 nd ra prefix** command and that using the **ipv6 address** command.By default, RA messages do not carry the default prefix generated based on the interface IPv6 address. If a user does not want the RA message to carry the default address prefix, run the **ipv6 nd ra prefix default no-advertise** command.

**Prerequisites**

IPv6 has been enabled on the involved interface using the **ipv6 enable** command.

**Configuration Impact**



After a host receives the RA message with the prefix configured through the **ipv6 nd ra prefix** command, the host updates the local prefix information.



**Precautions**

The prefix configured through the **ipv6 nd ra prefix** command cannot be fe80:: (prefix of a link-local address), ff00:: (prefix of a multicast address), or prefix of an unspecified address. It neither can be the prefix that has been used by another interface (including the interface address prefix and prefix carried in RA messages).


Example
-------

# Configure the prefix in the RA packet on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd ra prefix 2001:db8:1::100 64 100 10
[*HUAWEI-100GE1/0/1] ipv6 nd ra prefix 2001:db8:2::100 128 1000 400 no-autoconfig
[*HUAWEI-100GE1/0/1] ipv6 nd ra prefix 2001:db8:1::100 64 1000 400 off-link

```
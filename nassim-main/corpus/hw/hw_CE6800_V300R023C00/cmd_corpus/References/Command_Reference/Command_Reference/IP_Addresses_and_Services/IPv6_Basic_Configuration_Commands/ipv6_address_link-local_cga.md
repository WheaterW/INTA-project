ipv6 address link-local cga
===========================

ipv6 address link-local cga

Function
--------



The **ipv6 address link-local cga** command configures a CGA IPv6 link-local address for an interface.

The **undo ipv6 address link-local cga** command deletes the CGA IPv6 link-local address configured for an interface.



By default, no CGA IPv6 link-local address is configured for an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 address** *ipv6-address* **link-local** **cga** [ **tag** *tag-value* ]

**undo ipv6 address** *ipv6-address* **link-local** **cga** [ **tag** *tag-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **tag** *tag-value* | Specifies a label value. | <1-4294967295> |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Link-local addresses are used for the communications between link-local nodes in either the neighbor discovery or the stateless auto-configuration process. The packets with link-local addresses being the source or destination addresses are not forwarded to other links, that is, link-local addresses are valid only on local links.You can also run the **ipv6 address link-local** command to manually configure a link-local address for an interface.To enable IPv6 SEND to protect ND messages that carry CGA and RSA options, you need to configure a CGA IPv6 address on the interface. Running the **ipv6 address link-local** command with the keyword cga generates a CGA IPv6 link-local address.

**Prerequisites**

Before running the **ipv6 address link-local** command to configure a link-local address for an interface, you need to run the **ipv6 enable** command in the interface view to enable the IPv6 function on the interface.Before configuring a CGA link-local address, you must complete the following configurations:1.Run the **rsa key-pair label** command in the system view to create an RSA key pair.2.Run the **ipv6 security rsakey-pair** command in the interface view to bind the created RSA key pair to the interface.3.Run the **ipv6 security modifier** command in the interface view to configure a modifier value and a security level for the CGA address.

**Configuration Impact**

If an automatically allocated link-local address has already been configured on an interface, the ipv6 address link-local configuration overrides the existing link-local address.

**Precautions**

Try to avoid changing link-local addresses.You can configure multiple IPv6 addresses but only one link-local address for an interface.The following IPv6 addresses cannot be configured for an interface:

* Loopback address (::1/128)
* Unspecified address (::/128)
* Multicast address
* Anycast addressIPv4-mapped IPv6 addresses (0:0:0:0:0:FFFF:IPv4-address) can be configured on public networks but not on VPNs.After the **undo rsa key-pair label label-name** command is run in the system view, the IPv6 link-local address of the CGA type of the RSA key corresponding to each interface will be deleted.

Example
-------

# Configure a CGA IPv6 link-local address on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] rsa key-pair label huawei modulus 2048
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 security rsakey-pair huawei
[*HUAWEI-100GE1/0/1] ipv6 security modifier sec-level 1
[*HUAWEI-100GE1/0/1] ipv6 address fe80::1 link-local cga

```
ipv6 address cga
================

ipv6 address cga

Function
--------



The **ipv6 address cga** command configures a CGA global unicast address or link-local address.

The **undo ipv6 address cga** command deletes a CGA global unicast address or link-local address.



By default, no CGA global unicast address.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 address** { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } **cga** [ **tag** *tag-value* ]

**undo ipv6 address** { *ipv6-address* *prefix-length* | *ipv6-address/prefix-length* } **cga** [ **tag** *tag-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address to be configured for the interface. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the prefix length of an IPv6 address. | The value is an integer ranging from 1 to 64. When a link-local address of the CGA type is configured, the prefix length value ranges from 10 to 64. When a global unicast address of the CGA type is configured, the prefix length value ranges from 1 to 64. |
| *ipv6-address/prefix-length* | Specifies the IPv6 address and prefix length of an interface. | IPv6 address/IPv6 address prefix length. |
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

To enable IPv6 SEND to protect ND messages, you need to configure a CGA IPv6 address on an interface. Running the ipv6 address cga command configures a CGA IPv6 global unicast address or link-local address.

**Prerequisites**

Before running the ipv6 address cga command, you must complete the following configurations:1.Run the **rsa key-pair label** command in the system view to create an RSA key pair.2.Run the **ipv6 enable** command in the interface view to enable IPv6 on the interface.3.Run the **ipv6 security rsakey-pair** command in the interface view to bind the created RSA key pair to the interface.4.Run the **ipv6 security modifier** command in the interface view to configure a modifier value and a security level for the CGA address.

**Configuration Impact**

If a CGA IPv6 address is configured for an interface, an ND message sent by the interface will carry CGA and RSA options. After receiving the ND message, the remote interface checks the validity of the ND message sender and the integrity of the ND message based on the CGA and RSA options. If the strict security mode is configured on a local interface, the interface processes secure packets and discards insecure packets sent from a remote interface.

**Follow-up Procedure**

Run the **ipv6 nd security strict** command to enable the strict security mode on the interface.

**Precautions**

* If no parameter is specified in the **undo ipv6 address** command, all IPv6 addresses, including CGA global unicast addresses, except the automatically configured link-local address are deleted.
* After you run the **undo rsa key-pair label label-name** command in the system view, the CGA IPv6 addresses of the RSA key pairs on all interfaces are deleted.
* An interface can be configured with a maximum of one link-local address, including the CGA address. An interface can be configured with a maximum of 16 global unicast addresses, including the CGA address.


Example
-------

# Configure a CGA link-local address unicast address fe80::1/64 on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] rsa key-pair label huawei modulus 2048
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswich
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 security rsakey-pair huawei
[*HUAWEI-100GE1/0/1] ipv6 security modifier sec-level 1
[*HUAWEI-100GE1/0/1] ipv6 address fe80::1/64 cga

```
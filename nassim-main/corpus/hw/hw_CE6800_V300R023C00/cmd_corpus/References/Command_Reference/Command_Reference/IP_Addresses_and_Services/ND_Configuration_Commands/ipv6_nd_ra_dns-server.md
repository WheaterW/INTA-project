ipv6 nd ra dns-server
=====================

ipv6 nd ra dns-server

Function
--------



The **ipv6 nd ra dns-server** command configures parameters for the RDNSS option carried in an RA message.

The **undo ipv6 nd ra dns-server** command deletes parameters configured for the RDNSS option carried in an RA message.



By default, no parameter is configured for the RDNSS option carried in an RA message.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd ra dns-server** *ipv6-address* *lifetime*

**ipv6 nd ra dns-server** *ipv6-address*

**undo ipv6 nd ra dns-server** *ipv6-address* *lifetime*

**undo ipv6 nd ra dns-server** *ipv6-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *lifetime* | Specifies a lifetime for the RDNSS option carried in an RA message. If this parameter is not specified, the lifetime of the RDNSS option is three times the maximum interval for advertising RA messages. | The value is an integer ranging from 1 to 4294967295, in seconds. |
| **dns-server** *ipv6-address* | Specifies an address for the RDNSS option carried in an RA message. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. The address cannot be an unspecified address or a multicast address. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In ND address autoconfiguration scenarios, if a DNS server address changes, hosts cannot promptly detect the change. As a result, DNS resolution fails and services that rely on DNS cannot be used. To resolve this issue, configure a DNS server address on a routing device. After the configuration is complete, the device periodically advertises the DNS server address in RA messages. Upon receipt of such messages, hosts can obtain the latest available DNS server address and use the DNS service accurately.

**Precautions**

Before configuring parameters for the RDNSS option carried in an RA message, you must run the **ipv6 nd ra halt disable** command to enable the system to advertise RA messages.


Example
-------

# Configure the IP address of the ND RA DNS server.
```
<HUAWEI> system-view
[~HUAWEI] Vlan 1
[*HUAWEI-vlan1] interface Vlanif 1
[*HUAWEI-vlanif1] ipv6 enable
[*HUAWEI-vlanif1] ipv6 nd ra dns-server 2001:db8:1::1 3000

```

# Configure a DNS server address for the RDNSS option carried in an RA message.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd ra dns-server 2001:db8:1::1 3000

```
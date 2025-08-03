host
====

host

Function
--------



The **host** command adds a member to a customized zone.

The **undo host** command deletes a member from a customized zone.



By default, no member is added to a customized zone.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6885-SAN, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**host** { { *ip-address* | *ip-address1* **to** *ip-address2* } | { *ipv6-address* | *ipv6-address1* **to** *ipv6-address2* } }

**undo host** { { *ip-address* | *ip-address1* **to** *ip-address2* } | { *ipv6-address* | *ipv6-address1* **to** *ipv6-address2* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IPv4 address of a zone member. | The value is in dotted decimal notation. |
| *ip-address1* | Specifies the start IPv4 address of zone members. | The value is in dotted decimal notation. |
| **to** *ip-address2* | Specifies the end IPv4 address of zone members. <ip-address1> and <ip-address2> together determine the members to be added to a zone. The value of <ip-address2> must be greater than or equal to that of <ip-address1>. | The value is in dotted decimal notation. |
| **to** *ipv6-address2* | Specifies the end IPv6 address of zone members. <ipv6-address1> and <ipv6-address2> together determine the member to be added to a zone. The value of <ipv6-address2> must be greater than or equal to the value of <ipv6-address1>. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *ipv6-address* | Specifies the IPv6 address of a zone member. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *ipv6-address1* | Specifies the start IPv6 address of zone members. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

iNOF customized zone view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In the iNOF system, the device can manage access hosts through configured zones. The device has a default zone, which cannot be deleted. You can run this command to add members to a customized zone.If this command is run more than once, all configurations take effect. A maximum of 8000 host IP addresses (including IPv4 and IPv6 host IP addresses) can be configured. All zones configured on the device support a maximum of 32000 members. A member can be added to multiple zones.

**Precautions**

* The IPv4 address of a zone member cannot be a non-class A/B/C or loopback address.
* The IPv6 address of a zone member cannot be a link-local address, multicast address, unspecified address, or loopback address.

Example
-------

# Add a member with the IP address 192.168.1.6 to the zone named zone1.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] zone zone1
[*HUAWEI-ai-service-inof-zone-zone1] host 192.168.1.6

```

# Add a member with the IP address 2001:DB8:1::6 to the zone named zone1.
```
<HUAWEI> system-view
[~HUAWEI] ai-service
[*HUAWEI-ai-service] inof
[*HUAWEI-ai-service-inof] zone zone1
[*HUAWEI-ai-service-inof-zone-zone1] host 2001:DB8:1::6

```
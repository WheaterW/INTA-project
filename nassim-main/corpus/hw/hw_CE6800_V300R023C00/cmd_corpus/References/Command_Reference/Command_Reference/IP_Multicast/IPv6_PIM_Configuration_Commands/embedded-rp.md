embedded-rp
===========

embedded-rp

Function
--------



The **embedded-rp** command enables the embedded-Rendezvous Point (RP) function or set the range of IPv6 multicast groups to which embedded-RP applies.

The **undo embedded-rp** command disables the embedded-RP function or restore the default range of IPv6 multicast groups to which embedded-RP applies.



By default, the embedded-RP function is enabled and the default range of IPv6 multicast groups to which embedded-RP applies is FF70::/12.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**embedded-rp** [ *basic-acl6-number* | **acl6-name** *acl6-name* ]

**undo embedded-rp** [ *basic-acl6-number* | **acl6-name** *acl6-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl6-number* | Specifies the number of a basic ACL. This ACL defines the range of multicast groups to which embedded-RP applies. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name* | Specifies the name of an IPv6 named basic ACL. | The value is a string of 1 to 64 case-sensitive characters without spaces. The value must start with a letter (a to z or A to Z, case sensitive). |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Embedded-RP is a mode used by the Router in the Any-Source Multicast (ASM) model to obtain an RP address, and is applicable to an IPv6 PIM-SM domain or between IPv6 PIM-SM domains. In this mode, an RP address is embedded in an IPv6 group address. When obtaining an IPv6 group address, the Router can obtain the RP address to which the IPv6 group address corresponds. Embedded-RP allows IPv6 PIM-SM domains to learn RP information from each other even though Multicast Source Discovery Protocol (MSDP) does not support IPv6 networks.To avoid inconsistent results of RP elections, an RP obtained in embedded-RP mode takes precedence over other RPs elected by using other mechanisms. The address range of IPv6 groups served by an RP obtained in embedded-RP mode is FF70::/12.

**Prerequisites**

The IPv6 PIM view has been displayed using the **pim-ipv6** command.


Example
-------

# Enable the embedded-RP function for multicast group FF72:13::.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 number 2000
[*HUAWEI-acl6-basic-2000] rule permit source ff72:13:: 128
[*HUAWEI-acl6-basic-2000] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] embedded-rp 2000

```

# Configure an IPv6 named ACL to enable the embedded-RP for multicast group FF72:13::1.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name myacl6 basic
[*HUAWEI-acl6-basic-myacl6] rule permit source ff72:13::1 128
[*HUAWEI-acl6-basic-myacl6] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] embedded-rp acl6-name myacl6

```
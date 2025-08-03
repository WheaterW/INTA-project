static-rp(IPv6)
===============

static-rp(IPv6)

Function
--------



The **static-rp** command configures a static rendezvous point (RP).

The **undo static-rp** command deletes the configured static RP.



By default, no static RP is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**static-rp** *rp-address* [ *basic-acl6-number* | **acl6-name** *acl6-name* ] [ **preferred** ]

**undo static-rp** *rp-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rp-address* | Specifies a static RP address. | The value must be a valid global IPv6 unicast address. |
| *basic-acl6-number* | Specifies the number of a basic IPv6 ACL that defines the range of multicast groups served by a static RP. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name* | Specifies the name of a named basic IPv6 ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **preferred** | Indicates that a static RP is preferred. | If this parameter is not specified, the RP elected through the BSR mechanism is preferred. |



Views
-----

IPv6 PIM view,VPN instance IPv6 PIM view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When only one RP exists on a network, you can run the **static-rp** command to configure a static RP. Compared with dynamic RP election using the bootstrap router (BSR) mechanism, the static RP mechanism can reduce bandwidth occupied by messages exchanged between candidate-rendezvous points (C-RPs) and the BSR. To make the static RP work properly, you must run the **static-rp** command on all Routers in the PIM-SM domain.

**Prerequisites**

IPv6 PIM has been enabled and the IPv6 PIM instance view has been displayed using the command.


Example
-------

# In the public network instance, specify the address 2001:db8:1::1 as a static RP address that serves groups permitted by the IPv6 ACL 2001. Configure the static RP to be used preferentially.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] acl ipv6 number 2001
[*HUAWEI-acl6-basic-2001] quit
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] static-rp 2001:db8:1::1 2001 preferred

```

# In the public network instance, specify the address 2001:db8:1::1 as a static RP address that serves groups permitted by the IPv6 ACL named myacl6. Configure the static RP to be used preferentially.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] acl ipv6 name myacl6 basic
[*HUAWEI-acl6-basic-myacl6] rule permit source ff03::101 128
[*HUAWEI-acl6-basic-myacl6] quit
[*HUAWEI] pim ipv6
[*HUAWEI-pim6] static-rp 2001:db8:1::1 acl6-name myacl6 preferred

```
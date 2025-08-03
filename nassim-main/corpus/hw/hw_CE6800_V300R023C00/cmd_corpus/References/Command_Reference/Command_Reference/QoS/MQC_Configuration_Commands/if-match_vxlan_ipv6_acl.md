if-match vxlan ipv6 acl
=======================

if-match vxlan ipv6 acl

Function
--------



The **if-match vxlan ipv6 acl** command creates a matching rule based on inner information in VXLAN packets in an IPv6 ACL on the VXLAN network.

The **undo if-match vxlan ipv6 acl** command deletes a matching rule based on an IPv6 ACL that defines inner information in VXLAN packets on the VXLAN network.



By default, a matching rule based on inner information in VXLAN packets in an IPv6 ACL is not configured on the VXLAN network.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match vxlan** [ **transit** ] **ipv6** **acl** { *acl-number* | *acl-name* } [ **loose-mode** | **strict-mode** ]

**undo if-match vxlan** [ **transit** ] **ipv6** **acl** { *acl-number* | *acl-name* } [ **loose-mode** | **strict-mode** ]

For CE6820H, CE6820H-K, CE6820S:

**if-match vxlan transit ipv6 acl** { *acl-number* | *acl-name* } [ **loose-mode** | **strict-mode** ]

**undo if-match vxlan transit ipv6 acl** { *acl-number* | *acl-name* } [ **loose-mode** | **strict-mode** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **transit** | Indicates that VXLAN packets of a transmission device are matched.  When transit is not specified, the traffic policy containing this matching rule takes effect only on the device at the VXLAN tunnel egress. | - |
| *acl-number* | Specifies the number of an IPv6 ACL. | The value is an integer ranging from 2000 to 2999 or an integer ranging from 3000 to 3999. |
| *acl-name* | Specifies a named IPv6 ACL. | the name is a string of 1 to 32 characters, which begins with 0-9 or a-z or A-Z, and cannot contain only digits. |
| **loose-mode** | Indicates that the loose mode is used to match IPv6 ACLs. In this mode, the leftmost 64 bits of IPv6 addresses are matched. | - |
| **strict-mode** | Indicates that the strict mode is used to match IPv6 ACLs. In this mode, all the 128 bits of IPv6 addresses are matched. | - |
| **undo** | Cancels the current configuration. | - |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **if-match vxlan ipv6 acl** command creates a matching rule based on inner information in VXLAN packets in an IPv6 ACL on the VXLAN network. You must first define an IPv6 ACL, configure rules in the IPv6 ACL, and then run the **if-match vxlan ipv6 acl** command to configure a matching rule based on the IPv6 ACL in a traffic classifier. This ensures that the device processes packets matching the traffic classifier in the same way.

**Prerequisites**

An IPv6 ACL and IPv6 ACL rules have been created.

**Precautions**

* The traffic policy containing this matching rule takes effect only on the device at the VXLAN tunnel egress.
* When you run the **if-match vxlan ipv6 acl** command to match inner information in VXLAN packets, a traffic policy containing this traffic classifier can be applied to the outbound direction on an ingress node of a VXLAN tunnel, but cannot be applied to the outbound direction on the transit node of a VXLAN tunnel.
* To define a matching rule for traffic classification based on an ACL, you must create the ACL first. The ACL can only match the source MAC address, source IP address, destination IP address, source port number, destination port number, protocol type, and time range.
* If an ACL contains multiple rules, a packet that matches one ACL rule matches the ACL, regardless of whether the relationship between rules in a traffic classifier is AND or OR.
* If a traffic classifier contains this matching rule, only traffic mirroring, traffic policing, redirection, packet filtering, PBR, and traffic statistics collection can be configured in the traffic behavior.


Example
-------

# In the traffic classifier c1, create a matching rule based on inner information in VXLAN packets in IPv6 ACL 2046 on the VXLAN network.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 2046
[*HUAWEI-acl6-basic-2046] rule permit source any
[*HUAWEI-acl6-basic-2046] quit
[*HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] if-match vxlan ipv6 acl 2046

```
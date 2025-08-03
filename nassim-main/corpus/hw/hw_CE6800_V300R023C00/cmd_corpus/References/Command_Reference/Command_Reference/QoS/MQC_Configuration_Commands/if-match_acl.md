if-match acl
============

if-match acl

Function
--------



The **if-match acl** command configures a matching rule based on an Access Control List (ACL) in a traffic classifier.

The **undo if-match acl** command deletes a matching rule based on an ACL.



By default, a matching rule based on an ACL is not configured in a traffic classifier.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match acl** { *acl-number* | *acl-name* }

**undo if-match acl** { *acl-number* | *acl-name* }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match ipv6 acl** { *acl-number* | *acl6-name* } [ **loose-mode** | **strict-mode** ]

**undo if-match ipv6 acl** { *acl-number* | *acl6-name* } [ **loose-mode** | **strict-mode** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specify the number of the ACL. | The value is an integer. For IPv4 ACLs, the value ranges from 2000 to 2999, 3000 to 3999, 4000 to 4999, 5000 to 5999, or 23000 to 23999. For IPv6 ACLs, the value ranges from 2000 to 2999 or 3000 to 3999. |
| *acl6-name* | Specifies a named IPv6 ACL.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces and starts with a letter (a to z or A to Z). |
| **ipv6** | Configures a matching rule based on an IPv6 ACL.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| *acl-name* | Specifies a named ACL. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces and starts with a letter (a to z or A to Z). |
| **loose-mode** | Indicates that the loose mode is used to match IPv6 ACLs. In this mode, the leftmost 64 bits of IPv6 addresses are matched.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **strict-mode** | Indicates that the strict mode is used to match IPv6 ACLs. In this mode, all the 128 bits of IPv6 addresses are matched.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

Traffic classifier view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To classify packets based on the interface that receives packets, source IP address, destination IP address, protocol over IP, source and destination TCP port numbers, ICMP type and code, and source and destination MAC addresses, ARP packets, reference an ACL in a traffic classifier. You must first define an ACL and configure rules in the ACL, and then run the **if-match acl** command to configure a matching rule based on the ACL so that the device processes packets matching the same rule in the same manner.

**Prerequisites**

Create an ACL and configure rules in the ACL.

**Precautions**

* If an ARP ACL rule is specified in the command, only the following information can be matched: VLAN ID, 802.1p priority, packets with double tags, IPv4, and Ethernet frame protocol type.
* Regardless of whether the relationship between rules in a traffic classifier is and or or, if an ACL contains multiple rules, the packet that matches one ACL rule matches the ACL.
* If an ACL6 rule is specified in the command, for Layer 2 information, only the VLAN ID can be matched, in the same classifier, the strict mode, loose mode, and common mode are mutually exclusive, and only one mode can be configured.
* If a traffic classifier defines an ACL rule that matches fragmented packets, the traffic classifier cannot match transport-layer information such as the TCP flag.


Example
-------

# Configure a matching rule based on ACL 2046 in the traffic classifier c1.
```
<HUAWEI> system-view
[~HUAWEI] acl 2046
[*HUAWEI-acl4-basic-2046] rule permit source any
[*HUAWEI-acl4-basic-2046] quit
[*HUAWEI] traffic classifier c1 type and
[*HUAWEI-classifier-c1] if-match acl 2046

```
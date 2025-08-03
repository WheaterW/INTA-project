filter
======

filter

Function
--------



The **filter** command configures a filter.

The **undo filter** command deletes a filter.



By default, no filter is configured.


Format
------

For CE6820H, CE6820H-K, CE6820S, CE6855-48XS8CQ, CE6860-SAN, CE6863H, CE6863H-K, CE6866, CE6860-HAM, CE6866K, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE8850-SAN, CE8851-32CQ8DQ-P, CE8850-HAM, CE8851K, CE8855, CE8851-32CQ4BQ:

**filter** *filter-id* **acl** { *acl-number* | **ipv6** *ipv6-acl-number* } [ **interface** { { *interface-name1* | *interface-type* *interface-number1* } [ **to** { *interface-name2* | *interface-type* *interface-number2* } ] } &<1-8> ] [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-8> ]

**undo filter** *filter-id* [ [ **acl** { *acl-number* | **ipv6** *ipv6-acl-number* } ] [ **interface** { { *interface-name1* | *interface-type* *interface-number1* } [ **to** { *interface-name2* | *interface-type* *interface-number2* } ] } &<1-8> ] [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-8> ] ]

For CE6885-LL (low latency mode):

**filter** *filter-id* **acl** { *acl-number* } [ **interface** { { *interface-name1* | *interface-type* *interface-number1* } [ **to** { *interface-name2* | *interface-type* *interface-number2* } ] } &<1-8> ] [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-8> ]

**undo filter** *filter-id* [ [ **acl** { *acl-number* } ] [ **interface** { { *interface-name1* | *interface-type* *interface-number1* } [ **to** { *interface-name2* | *interface-type* *interface-number2* } ] } &<1-8> ] [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-8> ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *filter-id* | Specifies the ID of a filter. | The value is an integer that ranges from 1 to 8. |
| **acl** | ACL referenced by a filter. | - |
| *acl-number* | Specifies the number of an ACL referenced by a filter. | The value is an integer that ranges from 2000 to 2999, 23000 to 23999, 3000 to 3999, or 4000 to 4999. |
| **ipv6** *ipv6-acl-number* | Specifies the number of an ACL6 referenced by a filter.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is an integer in the range from 2000 to 2999 or from 3000 to 3999. |
| **interface** *interface-name1* | Specifies the name of the first interface. | - |
| **interface** *interface-type* *interface-number1* | Specifies the numbers of interfaces in the filter.  interface-type specifies the interface type.  interface-number1 specifies the first interface number. | - |
| **to** *vlan-id2* | vlan-id2 specifies the last VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** *interface-name2* | Specifies the name of the last interface. | - |
| **to** *interface-type* *interface-number2* | interface-number2 specifies the last interface number. | - |
| **vlan** *vlan-id1* | Specifies the VLAN IDs in the filter.  vlan-id1 specifies the first VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |



Views
-----

Attack defense policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If a type of protocol packets from certain IP addresses needs to be filtered, you can configure ACL rules to filter the packets. A permit rule indicates that the packets can be sent to the CPU, and a deny rule indicates that the packets cannot be sent to the CPU.A protocol in a filter can only be bound to one ACL or IPv6 ACL. If you bind multiple ACLs or IPv6 ACLs to a filter, only the last one takes effect.

**Precautions**



The following parameters cannot be specified for the ACL referenced by a filter. If these parameters are specified, the filter is invalid.Basic ACL: vpn-instanceAdvanced ACL: vpn-instance, icmp-type, igmp-type, source-pool, source-port-pool, destination-pool, destination-port-poolLayer 2 ACL: 802.3Basic ACL6: vpn-instanceAdvanced ACL6: destination, vpn-instance, and icmpv6-type




Example
-------

# Specify ACL 2001 as the rule referenced by filter 2.
```
<HUAWEI> system-view
[~HUAWEI] cpu-defend policy test
[*HUAWEI-cpu-defend-policy-test] filter 2 acl 2001

```
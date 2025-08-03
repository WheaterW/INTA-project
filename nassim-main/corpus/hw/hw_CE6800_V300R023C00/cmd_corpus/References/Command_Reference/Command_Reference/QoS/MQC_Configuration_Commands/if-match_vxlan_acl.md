if-match vxlan acl
==================

if-match vxlan acl

Function
--------



The **if-match vxlan acl** command creates a matching rule based on inner information in VXLAN packets in an IPv4 ACL on the VXLAN network.

The **undo if-match vxlan acl** command deletes a matching rule based on inner information in VXLAN packets in an IPv4 ACL on the VXLAN network.



By default, a matching rule based on inner information in VXLAN packets in an IPv4 ACL is not configured on the VXLAN network.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match vxlan** [ **transit** ] **acl** { *acl-number* | *acl-name* }

**undo if-match vxlan** [ **transit** ] **acl** { *acl-number* | *acl-name* }

For CE6820H, CE6820H-K, CE6820S:

**if-match vxlan transit acl** { *acl-number* | *acl-name* }

**undo if-match vxlan transit acl** { *acl-number* | *acl-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **transit** | Indicates that VXLAN packets of a transmission device are matched.  When transit is not specified, the traffic policy containing this matching rule takes effect only on the device at the VXLAN tunnel egress. | - |
| *acl-number* | Specify the number of the ACL. | The value is an integer that ranges from 2000 to 2999, 3000 to 3999, or 4000 to 4999. |
| *acl-name* | Specifies a named ACL. | the name is a string of 1 to 32 characters, which begins with 0-9 or a-z or A-Z, and cannot contain only digits. |
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

The **if-match vxlan acl** command creates a matching rule based on inner information in VXLAN packets in an IPv4 ACL on the VXLAN network. You must first define an IPv4 ACL, configure rules in the IPv4 ACL, and then run the **if-match vxlan acl** command to configure a matching rule based on the IPv4 ACL. This ensures that the device processes packets matching the traffic classifier in the same way.

**Prerequisites**

An IPv4 ACL and IPv4 ACL rules have been created.

**Precautions**

* If transit is specified in if-match vxlan acl, a traffic policy containing this traffic classifier can be applied to the outbound direction on the ingress node of a VXLAN tunnel, but cannot be applied to the outbound direction on the transit node of the VXLAN tunnel.
* The **if-match vxlan acl** command can match decapsulated IPv4 packets in the inbound direction of a device, and the **if-match acl** command can match IP packets encapsulated with an outer VXLAN header.
* If a traffic classifier contains this matching rule, only traffic mirroring, traffic policing, redirection, packet filtering, PBR, and traffic statistics collection can be configured in the traffic behavior. A device at the VXLAN tunnel egress supports the action of redirecting packets to ports.
* If an ACL contains multiple rules, a packet that matches one ACL rule matches the ACL, regardless of whether the relationship between rules in a traffic classifier is AND or OR.
* To define a matching rule for traffic classification based on an ACL, you must create the ACL first. The ACL can only match the source MAC address, source IP address, destination IP address, source port number, destination port number, protocol type, TCP flag, and time range.


Example
-------

# In the traffic classifier c1, create a matching rule based on inner information in VXLAN packets in IPv4 ACL 2046 on the VXLAN network.
```
<HUAWEI> system-view
[~HUAWEI] acl 2046
[*HUAWEI-acl4-basic-2046] rule permit source any
[*HUAWEI-acl4-basic-2046] quit
[*HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] if-match vxlan acl 2046

```

# On a transmission device on a VXLAN network, configure a matching rule based on IPv4 ACL 2046 for VXLAN packets in the traffic classifier c1. (Only the CE6820H series supports this example.)
```
<HUAWEI> system-view
[~HUAWEI] acl 2046
[*HUAWEI-acl4-basic-2046] rule permit source any
[*HUAWEI-acl4-basic-2046] quit
[*HUAWEI] traffic classifier c1
[*HUAWEI-classifier-c1] if-match vxlan transit acl 2046

```
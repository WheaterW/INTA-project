if-match vxlan vni
==================

if-match vxlan vni

Function
--------



The **if-match vxlan vni** command configures a matching rule based on VNI information in VXLAN packets in a traffic classifier.

The **undo if-match vxlan vni** command deletes a matching rule based on VNI information in VXLAN packets in a traffic classifier.



By default, a matching rule based on the VNI·ID of VXLAN packets is not configured in a traffic classifier.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**if-match vxlan** [ **transit** ] **vni** *vni-id*

**undo if-match vxlan** [ **transit** ] **vni** *vni-id*

For CE6820H, CE6820H-K, CE6820S:

**if-match vxlan transit vni** *vni-id*

**undo if-match vxlan transit vni** *vni-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **transit** | Indicates that VXLAN packets of a transmission device are matched.  When transit is not specified, the traffic policy containing this matching rule takes effect only on the device at the VXLAN tunnel egress. | - |
| *vni-id* | Specifies the VNI ID of VXLAN packets. | The value is an integer that ranges from 1 to 16777215. |
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

VXLAN is a network virtualization technology that uses MAC-in-UDP encapsulation, and adds a UDP header and a VXLAN header ahead of an Ethernet header in a packet.You can run the **if-match vxlan** command to classify VXLAN packets based on inner Ethernet packet information so that the device processes packets matching the same traffic classifier in the same manner and provides fine-granular services.

**Precautions**

* If an ACL contains multiple rules, a packet that matches one ACL rule matches the ACL, regardless of whether the relationship between rules in a traffic classifier is AND or OR.
* If a traffic classifier contains this matching rule, only flow mirroring, traffic policing, redirection, packet filtering, PBR, and traffic statistics collection can be configured in the traffic behavior.

Example
-------

# Create a matching rule based on the VNI ID of VXLAN packets in a traffic classifier.
```
<HUAWEI> system-view
[~HUAWEI] traffic classifier class1
[*HUAWEI-classifier-class1] if-match vxlan vni 10

```
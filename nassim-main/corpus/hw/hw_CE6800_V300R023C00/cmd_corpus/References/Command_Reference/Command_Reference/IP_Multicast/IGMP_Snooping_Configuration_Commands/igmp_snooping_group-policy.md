igmp snooping group-policy
==========================

igmp snooping group-policy

Function
--------



The **igmp snooping group-policy** command limits the range of multicast groups that hosts can join.

The **undo igmp snooping group-policy** command cancels the configuration.



By default, hosts can join any multicast group.


Format
------

**igmp snooping group-policy** { *acl-number* | **acl-name** *acl-name* } [ **version** *number* ] **vlan** { *vid1* [ **to** *vid2* ] } &<1-10>

**undo igmp snooping group-policy** [ { *acl-number* | **acl-name** *acl-name* } [ **version** *number* ] ] [ **vlan** { **all** | { *vid1* [ **to** *vid2* ] } &<1-10> } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl-number* | Specifies the number of an ACL. | It is an integer ranging from 2000 to 3999. |
| **acl-name** *acl-name* | Specifies the name of a named ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **version** *number* | Specifies the version number of IGMP packets. | The value is an integer that is 1, 2, or 3. |
| **vlan** *vid1* | Specifies the VLAN range of multicast groups to which the group policy will be applied. vlan-id1 specifies the start VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094.  For the CE6885-LL (low latency mode):The value is an integer ranging from 1 to 1023. |
| **to** *vid2* | Specifies the VLAN range of multicast groups to which the group policy will be applied. to vlan-id2 specifies the end VLAN ID.If the to vlan-id2 parameter is not specified, the group policy is effective only for the multicast groups that have the specified start VLAN ID. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer ranging from 1 to 4094. vlan-id2 must be greater than vlan-id1. vlan-id2 and vlan-id1 specify a VLAN range.  For the CE6885-LL (low latency mode):The value is an integer that ranges from 1 to 1023. vlan-id2 must be greater than vlan-id1. vlan-id1 and vlan-id2 specify a VLAN range. |
| **all** | Specifies all of the VLANs. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The igmp-snooping group-policy command is used to limit the range of multicast groups that user hosts can join.

**Prerequisites**

IGMP snooping has been enabled globally and in a VLAN.Rules have been configured for a specified basic ACL.

**Configuration Impact**

After the igmp snooping group-policy command is run, user hosts cannot join multicast groups beyond the configured multicast group range. If the igmp-snooping group-policy command is run more than once, all configurations take effect.

**Precautions**

If no IGMP version is specified, the device applies the multicast group address limit to the received IGMP messages of all versions (V1, V2, and V3). In addition, the configured ACL must be a basic ACL.When you run this command in the VLAN view, the configuration fails in the following situations:

* The dot1q sub-interface has been bound to the VLAN.

For numbered ACLs and named ACLs:

* In the basic ACL view, you can set the range of multicast groups that an interface is allowed to join by specifying the source parameter in the **rule** command.
* In the advanced ACL view, you can set the range of multicast sources that an interface is allowed to join by specifying the source parameter in the **rule** command, and set the range of multicast groups that an interface is allowed to join by specifying the destination parameter in the **rule** command.IGMPv1/v2 Report messages are not filtered based on the source parameter.

Example
-------

# Allow hosts on 100GE 1/0/1.1 to join only multicast group 225.1.1.123.
```
<HUAWEI> system-view
[*HUAWEI] acl number 2008
[*HUAWEI-acl-basic-2008] rule permit source 225.1.1.123 0
[*HUAWEI-acl-basic-2008] rule deny source any
[*HUAWEI-acl-basic-2008] quit
[*HUAWEI] interface 100GE 1/0/1.1 mode l2
[*HUAWEI-100GE1/0/1.1] portswitch
[*HUAWEI-100GE1/0/1.1] igmp snooping group-policy 2008

```
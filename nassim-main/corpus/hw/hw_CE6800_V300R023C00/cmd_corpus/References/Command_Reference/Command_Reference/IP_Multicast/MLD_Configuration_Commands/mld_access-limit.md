mld access-limit
================

mld access-limit

Function
--------



The **mld access-limit** command sets the maximum number of MLD group memberships that can be created on an interface.

The **undo mld access-limit** command cancels the setting.



By default, the maximum number of MLD group memberships on an interface is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld access-limit** *number* [ **except** { *ExceptAclNumValue* | **acl6-name** *ExceptAclNameValue* } ]

**undo mld access-limit** [ *number* [ **except** { *ExceptAclNumValue* | **acl6-name** *ExceptAclNameValue* } ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Specifies the maximum number of MLD entries that can be created on an interface. | The value is an integer ranging from 1 to 16384. |
| **except** *ExceptAclNumValue* | Specifies the number of a basic or an advanced ACL. | The number of a basic ACL is an integer that ranges from 2000 to 2999. The basic ACL filters group addresses only. The number of an advanced ACL is an integer that ranges from 3000 to 3999. The advanced ACL filters source and group addresses. |
| **acl6-name** *ExceptAclNameValue* | Specifies the name of a named ACL. | The value is a string of 1 to 32 case-sensitive characters without spaces. The value starts with a letter or digit but cannot contain only digits. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view,Eth-Trunk interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a large number of users watch multiple programs at the same time, a large amount of bandwidth of the router is occupied, which degrades the performance of the router. To prevent this problem, run the **mld access-limit** command on the router interface to limit the number of MLD entries. When receiving an MLD Join message, the router checks whether the number of entries exceeds the limit. If the number of entries does not exceed the limit, the router sets up a member relationship and forwards the data flow of the multicast group to the user. This improves the clarity and stability of programs for users who have joined multicast groups.The methods of counting the number of MLD entries are as follows:

* Each (\*, G) entry and each (S, G) entry are counted separately as an interface entry.
* The (\*, G) entries used for SSM-Mapping are not counted. The (S, G) entries generated based on mapping are counted as one interface entry.

**Prerequisites**

The multicast ipv6 routing function has been enabled using the multicast routing-enable command.

**Precautions**

If except is not specified, the maximum number of MLD entries is limited for all groups or source/groups. If except is specified, the interface filters the received MLD Join messages based on the ACL. The number of entries that match the ACL rule is not limited by the maximum number of MLD entries.The **mld access-limit** command is used together with the acl (basic ACL) or acl (advanced ACL) command.

* For a numbered ACL, in the basic ACL view, you can set the address range of multicast groups that are not limited by number by specifying the source parameter in the **rule** command.
* In the advanced ACL view, set the source parameter in the **rule** command to a multicast source address that is not limited by number, and set the destination parameter to a multicast group address that is not limited by number. For (\*, G) filtering, any source parameter can be matched.

If the command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Set the maximum number of MLD entries that can be created on 100GE1/0/1 to 1024.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld access-limit 1024

```

# Create an ACL6 named myacl, and configure a rule for the ACL6 to allow hosts to receive messages sent from multicast source 2001:db8:100::1 to multicast group FF1E::/120. Set the maximum number of MLD entries that can be created on 100GE1/0/1 to 1024, and the multicast group FF1E::/120 is not limited.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] acl ipv6 name myacl
[*HUAWEI-acl6-advance-myacl] rule permit ipv6 source 2001:db8:100::1 128 destination FF1E::1 120
[*HUAWEI-acl6-advance-myacl] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld access-limit 1024 except acl6-name myacl

```
pim ipv6 neighbor-policy
========================

pim ipv6 neighbor-policy

Function
--------



The **pim ipv6 neighbor-policy** command configures a policy for filtering PIM neighbors and sets a range of valid PIM neighbor addresses.

The **undo pim ipv6 neighbor-policy** command restores the default setting.



By default, no policy is configured for filtering PIM neighbors, and the valid range of PIM neighbor addresses is not limited.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6 neighbor-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* }

**undo pim ipv6 neighbor-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl6-number* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name* | Specifies the name of a named basic IPv6 ACL. | The value is a string of 1 to 64 case-sensitive characters without spaces. The value must start with a letter (a to z or A to Z, case sensitive). |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To protect a Router against pseudo PIM Hello message attacks, run the pim ipv6 neighbor-policy command to set a range of valid PIM neighbor addresses. The Router then discards Hello messages received from devices whose addresses are not in the specified range.


Example
-------

# In the public network instance view, create a basic ACL to configure 100GE1/0/1 to set up the IPv6 PIM neighbor relationship with the router with the address 2001:DB8:1::1.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 number 2001
[*HUAWEI-acl6-basic-2001] rule permit source 2001:DB8:1::1 128
[*HUAWEI-acl6-basic-2001] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 neighbor-policy 2001

```

# In the public network instance view, create a named ACL to configure 100GE1/0/1 to set up the IPv6 PIM neighbor relationship with the router with the address 2001:DB8:1::1.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name myacl basic
[*HUAWEI-acl6-basic-myacl] rule permit source 2001:DB8:1::1 128
[*HUAWEI-acl6-basic-myacl] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] pim ipv6 neighbor-policy acl6-name myacl

```
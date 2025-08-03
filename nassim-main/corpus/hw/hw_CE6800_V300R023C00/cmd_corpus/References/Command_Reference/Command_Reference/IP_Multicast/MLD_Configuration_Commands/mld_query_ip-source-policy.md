mld query ip-source-policy
==========================

mld query ip-source-policy

Function
--------



The **mld query ip-source-policy** command configures source address-based Multicast Listener Discovery (MLD) Query message filtering.

The **undo mld query ip-source-policy** command restores the default configuration.



By default, no source address-based MLD Query message filtering is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld query ip-source-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* }

**undo mld query ip-source-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl6-number* | Specifies the number of a basic IPv6 ACL, which defines the range of source addresses. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Source address-based MLD Query message filtering prevents a device from forging MLD Query messages with small IP addresses to cause the actual querier to become invalid. As a result, group members cannot promptly leave and traffic waste occurs. After you run the **mld query ip-source-policy** command to configure source address-based MLD Query message filtering, the device filters out the MLD Query messages whose source addresses do not match the permit action in a specified ACL rule. In this way, querier election is controlled.


Example
-------

# In the public network instance, create an ACL named myacl, and configure 100GE1/0/1 to accept MLD Query messages with the source address 2001:DB8:FE80::1 and discard MLD Query messages with the source address 2001:DB8:FE70::1.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] acl ipv6 name myacl basic
[*HUAWEI-acl6-basic-myacl] rule permit source 2001:DB8:FE80::1 128
[*HUAWEI-acl6-basic-myacl] rule deny source 2001:DB8:FE70::1 128
[*HUAWEI-acl6-basic-myacl] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld query ip-source-policy acl6-name myacl

```

# In the public network instance, create ACL 2001, and configure 100GE1/0/1 to accept MLD Query messages with the source address 2001:DB8:FE80::1 and discard MLD Query messages with the source address 2001:DB8:FE70::1.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] acl ipv6 number 2001
[*HUAWEI-acl6-basic-2001] rule permit source 2001:DB8:FE80::1 128
[*HUAWEI-acl6-basic-2001] rule deny source 2001:DB8:FE70::1 128
[*HUAWEI-acl6-basic-2001] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld query ip-source-policy 2001

```
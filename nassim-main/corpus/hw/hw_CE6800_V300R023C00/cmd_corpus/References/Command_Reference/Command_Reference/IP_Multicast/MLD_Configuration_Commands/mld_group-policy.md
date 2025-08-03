mld group-policy
================

mld group-policy

Function
--------



The **mld group-policy** command sets a rule used by an interface to filter the Multicast Listener Discovery (MLD) groups that hosts can join.

The **undo mld group-policy** command restores the default configuration.



By default, no filtering rule is set. That is, hosts can join any multicast group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld group-policy** { *acl6-number* | **acl6-name** *acl6-name* } { **1** | **2** }

**mld group-policy** { *acl6-number* | **acl6-name** *acl6-name* }

**undo mld group-policy**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *acl6-number* | Specifies the number of a basic or advanced IPv6 ACL. | The number of a basic IPv6 ACL is an integer that ranges from 2000 to 2999; the number of an advanced IPv6 ACL ranges from 3000 to 3999. |
| **acl6-name** *acl6-name* | Specifies the name of a named IPv6 ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |
| **1** | Indicates that the MLD version is 1 (MLDv1). | - |
| **2** | Indicates that the MLD version is 2 (MLDv2). | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To make hosts on the network segment where an interface resides join specified IPv6 multicast groups and receive multicast packets for these groups, run the **mld group-policy** command on this interface and define an IPv6 ACL rule as a filter to restrict the range of multicast groups. In this manner, MLD security is guaranteed.


Example
-------

# Allow only hosts connected to 100GE1/0/1 to join multicast group FF03::101.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 number 3000
[*HUAWEI-acl6-advance-3000] rule permit ipv6 destination ff03::101 128
[*HUAWEI-acl6-advance-3000] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld group-policy 3000

```

# Create an ACL named myacl6, and configure a rule for the ACL to allow hosts to receive messages from multicast group FF03::101. Configure a filter on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] acl ipv6 name myacl6
[*HUAWEI-acl6-advance-myacl6] rule permit ipv6 destination ff03::101 128
[*HUAWEI-acl6-advance-myacl6] quit
[*HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld group-policy acl6-name myacl6

```
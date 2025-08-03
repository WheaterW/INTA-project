mld prompt-leave
================

mld prompt-leave

Function
--------



The **mld prompt-leave** command enables prompt leave on an interface. When the interface receives a Multicast Listener Discovery (MLD) Done message for a specific multicast group, the interface immediately deletes entries of this group without sending a last-listener query message.

The **undo mld prompt-leave** command restores the default configuration.



By default, the device sends a last-listener query message after receiving an MLD Done message for a specific multicast group.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld prompt-leave**

**mld prompt-leave group-policy** { *basic-acl6-number* | **acl6-name** *acl6-name* }

**undo mld prompt-leave**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *basic-acl6-number* | Specifies the number of a basic IPv6 ACL. This list specifies the range of a multicast group. | The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6-name* | Specifies the name of a named basic IPv6 ACL. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. The name must start with a letter or digit, and cannot contain only digits. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In most cases, after receiving a Leave message of a multicast group, an interface sends a last member Query message to check whether this multicast group has other members. To minimize the response delay and save network bandwidth, configure prompt leave on the interface. If prompt leave is configured on an interface, after receiving a Leave message of a multicast group, the interface immediately deletes the corresponding multicast group records, without sending a last member Query message.


Example
-------

# Create an ACL named myacl6, and configure a rule for the ACL to allow hosts to receive messages from multicast group FF03::101. Configure 100GE1/0/1 to immediately delete the downstream interface in the forwarding entry corresponding to the multicast group after receiving a Leave message for the multicast group.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] acl ipv6 name myacl6
[*HUAWEI-acl6-advance-myacl6] rule permit ipv6 destination ff03::101 128
[*HUAWEI-acl6-advance-myacl6] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld prompt-leave group-policy acl6-name myacl6

```

# Enable prompt leave on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld prompt-leave

```
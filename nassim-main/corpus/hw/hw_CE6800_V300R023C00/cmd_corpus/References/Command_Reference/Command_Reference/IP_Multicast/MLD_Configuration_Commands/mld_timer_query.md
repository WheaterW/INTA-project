mld timer query
===============

mld timer query

Function
--------



The **mld timer query** command sets the interval at which an interface sends Multicast Listener Discovery (MLD) general query messages.

The **undo mld timer query** command restores the default value.



By default, the interval at which an interface sends MLD general query messages is 125 seconds.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld timer query** *interval*

**undo mld timer query**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies the interval at which an interface sends MLD general query messages. | The value is an integer ranging from 1 to 18000, in seconds. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A multicast Router sends MLD general query messages at an interval to check whether multicast group members exist on the network. The query interval can be adjusted as required.The query interval can be set in both the interface view and the MLD view. The system prefers the configuration in the interface view. The configuration in the MLD view is used only when the configuration in the interface view is not done.


Example
-------

# Set the interval at which 100GE1/0/1 sends General Query messages to 200s.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] mld timer query 200

```
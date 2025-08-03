ipv6 nd dad attempts
====================

ipv6 nd dad attempts

Function
--------



The **ipv6 nd dad attempts** command sets the number of NS messages that are sent when Duplicate Address Detection (DAD) is performed.

The **undo ipv6 nd dad attempts** command restores the default setting.



By default, one NS message is sent when DAD is performed.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd dad attempts** *value*

**undo ipv6 nd dad attempts**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies the number of NS messages that are sent when DAD is performed. | It is an integer ranging from 0 to 600. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view,Management interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When you configure IPv6 addresses (including global unicast IPv6 addresses and link-local IPv6 addresses) for interfaces, the DAD function is required. DAD verifies the uniqueness of new unicast IPv6 addresses before the addresses are assigned to interfaces on the local link. It ensures that the IPv6 address to be allocated to an interface is not used by any other interfaces connected with this interface and thus avoids address conflicts.

**Prerequisites**

IPv6 has been enabled on the involved interface using the **ipv6 enable** command.

**Configuration Impact**

If the number of NS messages that are sent when DAD is performed is set to 0, it indicates that DAD is prohibited.

**Precautions**

When the physical link on an interface fails, DAD cannot be implemented on the interface.When traffic is heavy, setting the value to a larger value is recommended to increase the number of NS messages that can be sent.


Example
-------

# Set the number of NS messages that are sent when DAD is performed to 20.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd dad attempts 20

```

# Disable the DAD function.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd dad attempts 0

```
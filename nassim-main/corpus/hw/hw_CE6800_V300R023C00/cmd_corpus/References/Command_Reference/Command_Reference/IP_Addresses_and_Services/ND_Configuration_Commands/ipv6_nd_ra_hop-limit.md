ipv6 nd ra hop-limit
====================

ipv6 nd ra hop-limit

Function
--------



The **ipv6 nd ra hop-limit** command sets the maximum number of hops through which IPv6 unicast packets sent by the device are allowed to pass.

The **undo ipv6 nd ra hop-limit** command restores the default maximum number of hops for an RA message.



By default, the default maximum number of hops for an RA message is 64.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd ra hop-limit** *limit*

**undo ipv6 nd ra hop-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit* | Specifies the maximum number of hops for an RA message. | The value is an integer ranging from 0 to 255. |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The hop limit is a parameter carried in an RA message. It defines the maximum number of hops that the RA message (which is an IPv6 unicast packet) passes through.

**Prerequisites**

IPv6 has been enabled on the involved interface using the **ipv6 enable** command.

**Configuration Impact**

After this command is run, the device discards received RA messages in which the hop limit is different from that configured on the device itself.

**Precautions**

* If the **ipv6 nd ra hop-limit** command has been run on an interface, the hop limit for an RA message uses the value configured on the interface.
* If the **ipv6 nd ra hop-limit** command has not been run on an interface, the hop limit for an RA message uses the value configured globally, that is, the value configured in the **ipv6 nd hop-limit** command.

Example
-------

# Configure the maximum number of hops for an RA message to be 126.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ipv6 enable
[*HUAWEI-100GE1/0/1] ipv6 nd ra hop-limit 126

```
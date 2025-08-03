ipv6 nd hop-limit
=================

ipv6 nd hop-limit

Function
--------



The **ipv6 nd hop-limit** command sets the maximum number of hops through which IPv6 unicast packets sent by the Router are allowed to pass.

The **undo ipv6 nd hop-limit** command restores the default setting.



By default, the IPv6 unicast packets sent by the Router can pass through 64 hops.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd hop-limit** *limit*

**undo ipv6 nd hop-limit**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *limit* | Specifies the hop limit. | It is an integer ranging from 1 to 255. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A hop limit on the Router provides the following functions:

* Controlling the number of hops through which IPv6 unicast packets are allowed to pass.
* Helping a host automatically generate a hop limit

**Prerequisites**



IPv6 has been enabled on the involved interface using the **ipv6 enable** command.



**Configuration Impact**

The hop limit for unicast packets is set using the **ipv6 nd hop-limit** command in the system view.The hop limit for RA messages can be set using the**ipv6 nd hop-limit** command in the system view, or can be set using the**ipv6 nd ra hop-limit** command in the interface view:

* If the hop limit for RA messages is not set in the interface view or in the system view, the hop limit for RA messages is 64 by default.
* If the hop limit for RA messages is not set in the interface view but in the system view, the configuration in the system view takes effect.
* If the hop limit for RA messages is set in the interface view, the configuration in the interface view takes effect, no matter whether the hop limit is set in the system view.

**Precautions**

The hop limit for IPv6 unicast packets sent by the Router is usually of the same value as the hop limit carried in an RA message. In the following cases, however, the hop limit for IPv6 unicast packets sent by the Router is 64 (the default value) whereas the hop limit carried in an RA message is 0.

* No hop limit is set for IPv6 unicast packets sent by the Router.
* The **undo ipv6 nd hop-limit** command is run to restore the default hop limit set on the Router.After receiving an RA message with the hop limit of 0, a host uses the default hop limit 64, which is the same as the default hop limit on the Router.


Example
-------

# In the system view, set the hop limit to 100 for IPv6 unicast packets sent by the device.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 nd hop-limit 100

```
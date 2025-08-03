apply extcommunity
==================

apply extcommunity

Function
--------



The **apply extcommunity** command configures VPN-Target extended community attributes for BGP routes.

The **undo apply extcommunity** command cancels the configuration.



By default, no BGP VPN-Target extended community attributes are configured.


Format
------

**apply extcommunity** { **rt** *extCmntyValue* } &<1-16> [ **additive** ]

**apply extcommunity rt none**

**undo apply extcommunity** [ **rt** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **rt** *extCmntyValue* | Indicates the value of VPN-Target extended community. | The value of the VPN-Target extended community attribute can be expressed in one of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number is an integer ranging from 0 to 65535, and the user-defined number is an integer ranging from 0 to 4294967295. * IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535. * 4-byte AS number in integer format:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. A user-defined number also ranges from 0 to 65535. |
| **additive** | Indicates that existing community attributes can be added to routes. | - |
| **none** | Clears the existing extended community attributes of a route. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **apply extcommunity** command is applicable to the VPN. At present, there are two types of BGP extended community attributes.

* VPN route-target (RT) extended community
* Source of Origin (SoO) extended communityThe **apply extcommunity** command configures VPN-Target extended community attributes for BGP routes.

**Prerequisites**



A route-policy has been configured using the route-policy command.



**Configuration Impact**



After a route matches a route-policy, the VPN-Target extended community attribute of the route is changed.



**Precautions**



If additive is not set in the **apply extcommunity** command, the original VPN-Target extended community attribute is replaced.For the address families that support the peer advertise-ext-community and ext-community-change enable commands, run the two commands in the corresponding address family view and then run the **apply extcommunity** command in the route-policy view to make the configuration take effect.




Example
-------

# Add 100:2, 1.1.1.1:22, 100.100:100 to the VPN-Target extended community attribute of BGP.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] apply extcommunity rt 100:2 rt 1.1.1.1:22 rt 100.100:100 additive

```
apply extcommunity soo
======================

apply extcommunity soo

Function
--------



The **apply extcommunity soo** command configures Source of Origin (SoO) extended community attributes for BGP routes.

The **undo apply extcommunity soo** command cancels the configuration.



By default, no SoO extended community attributes are configured.


Format
------

**apply extcommunity soo** { *site-of-origin* } &<1-16> **additive**

**undo apply extcommunity soo**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *site-of-origin* | Specifies SoO extended community attributes. | The SoO attribute value can be expressed in any of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number is an integer ranging from 0 to 65535, and the user-defined number is an integer ranging from 0 to 4294967295. * IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535. * 4-byte AS number in integer format:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. A user-defined number also ranges from 0 to 65535. |
| **additive** | Indicates that existing extended community attributes can be added to routes. | - |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The apply extcommunity command is applicable to the VPN. At present, there are two types of BGP extended community attributes.

* VPN route-target (RT) extended community
* Source of Origin (SoO) extended communityAt present, SoO extended community attributes can be set only through a route-policy.

**Prerequisites**



A route-policy has been configured using the route-policy command.




Example
-------

# Add 1.2.3.4:5 to the SoO extended community attribute of BGP.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] apply extcommunity soo 1.2.3.4:5 additive

```
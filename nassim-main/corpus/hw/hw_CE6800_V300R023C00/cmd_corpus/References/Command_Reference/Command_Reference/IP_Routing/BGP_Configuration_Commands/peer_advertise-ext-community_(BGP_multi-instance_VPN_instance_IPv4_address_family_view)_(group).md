peer advertise-ext-community (BGP multi-instance VPN instance IPv4 address family view) (group)
===============================================================================================

peer advertise-ext-community (BGP multi-instance VPN instance IPv4 address family view) (group)

Function
--------



The **peer advertise-ext-community** command enables a device to advertise extended community attributes to BGP peers in a peer group.

The **undo peer advertise-ext-community** command cancels the existing configuration.



By default, a device advertises no extended community attribute its peer or peer group.


Format
------

**peer** *group-name* **advertise-ext-community**

**undo peer** *group-name* **advertise-ext-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



The **peer advertise-ext-community** command is used to advertise the extended community attribute to a specified peer or peer group.



**Precautions**



Before running the **peer advertise-ext-community** command to configure extended community attributes, you can use a routing policy to define specific community attributes.




Example
-------

# Configure the device to advertise the extended community attribute to a peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] group test
[*HUAWEI-bgp-instance-a-vpna] peer test advertise-ext-community

```
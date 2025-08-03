peer soo-reverse (BGP-IPv4 unicast address family view)(group)
==============================================================

peer soo-reverse (BGP-IPv4 unicast address family view)(group)

Function
--------



The **peer soo-reverse** command configures the reverse Site-of-Origin (SoO) for a BGP peer group.

The **undo peer soo-reverse** command cancels the configuration.



By default, no SoO is configured for a BGP peer group.


Format
------

**peer** *groupName* **soo-reverse** *sooString*

**undo peer** *groupName* **soo-reverse** *sooString*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *groupName* | Specifies the name of a BGP peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *sooString* | Sets the reverse SoO extended community attribute for a specified peer group. | The value of the SoO attribute may be expressed in one of the following forms:   * Integral 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number ranges from 0 to 65535, and the user-defined number ranges from 0 to 4294967295. The AS number and user-defined number cannot be both 0s. That is, the SoO cannot be 0:0. * IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number ranges from 0 to 65535. * Integral 4-byte AS number:2-byte user-defined number, for example, 65537:3. The AS number ranges from 65536 to 4294967295, and the user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535, and a user-defined number ranges from 0 to 65535. The AS number and user-defined number cannot be both 0s. That is, an SoO cannot be 0.0:0. |



Views
-----

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When BGP SoO is applied to a BGP public network scenario:

* When advertising a public network unicast route, a device adds the SoO attribute to the route and advertises the route to other peers.
* When a device receives a public network unicast route with the SoO attribute, the device checks the SoO attribute of the route. If the SoO attribute is the same as the locally configured SoO attribute, the device does not accept the public network unicast route. If the SoO attribute is different from the locally configured SoO attribute, the device accepts this unicast route.

**Precautions**



After the **peer soo-reverse** command is run, the device checks whether the routes received from a specified peer carry the same SoO. If the routes carry the same SoO, the device discards the routes. In addition, the routes cannot be saved using the **keep-all-routes** command.If a BGP peer does not support the Route-Refresh capability, the **peer soo-reverse** command disconnects the BGP peer.




Example
-------

# Configure reverse SoO for a BGP peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer test enable
[*HUAWEI-bgp-af-ipv4] peer test soo-reverse 10:10

```
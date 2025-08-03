peer soo (BGP multi-instance VPN instance IPv4 address family view) (group)
===========================================================================

peer soo (BGP multi-instance VPN instance IPv4 address family view) (group)

Function
--------



The **peer soo** command configures the Site-of-Origin (SoO) attribute for a BGP peer in a BGP VPN instance.

The **undo peer soo** command cancels the configuration.



By default, SoO is not configured for BGP peers in a BGP VPN instance.


Format
------

**peer** *group-name* **soo** *site-of-origin*

**undo peer** *group-name* **soo**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *site-of-origin* | Specifies the SoO attribute. | The SoO attribute value can be expressed in any of the following formats:   * 2-byte AS number:4-byte user-defined number, for example, 1:3. The AS number is an integer ranging from 0 to 65535, and the user-defined number is an integer ranging from 0 to 4294967295. The AS number and user-defined number cannot both be set to 0. That is, the SoO must not be 0:0. * IPv4 address:2-byte user-defined number, for example, 192.168.122.15:1. The IP address ranges from 0.0.0.0 to 255.255.255.255, and the user-defined number is an integer ranging from 0 to 65535. * 4-byte AS number in integer format:2-byte user-defined number, for example, 65537:3. An AS number ranges from 65536 to 4294967295, and a user-defined number ranges from 0 to 65535. * 4-byte AS number in dotted notation:2-byte user-defined number, for example, 0.0:3 or 0.1:0. A 4-byte AS number in dotted notation is in the format of x.y, where x and y are integers that range from 0 to 65535. A user-defined number also ranges from 0 to 65535. The AS number and user-defined number must not be both 0s. That is, the SoO must not be 0.0:0. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In an L3VPN scenario, if the ASs where two VPN sites reside use private AS numbers, the AS numbers of the two VPN sites may be the same. As a result, different sites in the same VPN cannot communicate with each other. In this case, you need to run the **peer substitute-as** command on the PE to enable AS number substitution.However, enabling AS number substitution causes another problem. When multiple CEs at a VPN site access different PEs on the L3VPN backbone network through BGP and routing protocols are deployed between the CEs, if AS number substitution is configured on the PEs, the AS numbers of the VPN routes at the VPN site will be replaced on the PEs. In this case, the routes may be sent back to the VPN site through the backbone network and other CEs. As a result, a routing loop occurs. To solve this problem, run the **peer soo** command on the PEs to configure the SoO feature for the specified CE.After this command is run on a PE, the PE adds the SoO attribute to the routes received from a CE and advertises the routes to other PE peers. When advertising these routes to the connected CE, the other PE peers check the SoO attribute carried in the VPN routes. If the SoO attribute is the same as the locally configured SoO attribute, the PEs do not advertise the routes to the CE. This prevents routing loops in the VPN site.



**Precautions**



After the **peer substitute-as** command is run, the AS number of the route is replaced, which may cause routing loops. To solve this problem, run the **peer soo** command to configure the SoO feature. Disabling the SoO feature may cause routing loops. Therefore, exercise caution when running the **undo peer soo** command.




Example
-------

# Configure SoO for a BGP peer group.
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
[*HUAWEI-bgp-instance-a-vpna] group test external
[*HUAWEI-bgp-instance-a-vpna] peer test as-number 200
[*HUAWEI-bgp-instance-a-vpna] peer test soo 10.2.2.2:45

```
peer public-as-only (BGP-VPN-Target address family view) (group)
================================================================

peer public-as-only (BGP-VPN-Target address family view) (group)

Function
--------



The **peer public-as-only** command configures the AS-Path attribute in a BGP Update message not to carry the private AS number. Only the public AS number is contained in the update messages.

The **undo peer public-as-only** command allows the AS-Path attribute in a BGP Update message to carry the private AS number.



By default, the AS-Path attribute in a BGP Update message is allowed to carry private AS numbers.


Format
------

**peer** *group-name* **public-as-only**

**undo peer** *group-name* **public-as-only**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Generally, AS numbers range from 1 to 4294967295, including the public, private, and reserved AS numbers. If the **private-4-byte-as enable** command is not run, private AS numbers range from 64512 to 65534. AS number 65535 is reserved for special use. After the **private-4-byte-as enable** command is run, the private AS numbers range from 64512 to 65534 and from 4200000000-4294967294 to 65535 or 4294967295, which are reserved for special use.Public AS numbers can be used over the Internet, whereas private AS numbers cannot be advertised to the Internet. If private AS numbers are advertised to the Internet, routing loops may occur. Therefore, private AS numbers are used only within a routing domain.This command can be used to process the private and reserved AS numbers in the AS\_Path attribute of BGP routes as required. The processing of the reserved AS numbers is the same as that of the private AS numbers.After this command is configured, if the AS path attribute contains only private AS numbers, BGP deletes the private AS numbers and then advertises these update routes.



**Configuration Impact**



If the **peer public-as-only** command is run for a peer group, the peers of the peer group inherit the configuration.




Example
-------

# Configure a device to remove all private AS numbers from the AS\_Path attribute when sending a BGP Update message to its peer group.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test internal
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer test enable
[*HUAWEI-bgp-af-vpn-target] peer test public-as-only

```
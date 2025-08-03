peer enable (BGP-VPN-Target address family view) (group)
========================================================

peer enable (BGP-VPN-Target address family view) (group)

Function
--------



The **peer enable** command enables a BGP device to exchange routes with a specified peer group in the address family view.

The **undo peer enable** command disables a BGP device from exchanging routes with a specified peer group.



By default, a device is disabled from exchanging routing information with a specified peer group.


Format
------

**peer** *group-name* **enable**

**undo peer** *group-name* **enable**


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



By default, the device is automatically enabled to exchange routing information only with peer groups in the BGP-IPv4 unicast address family. That is, after the **peer as-number** command is run in the BGP view, the system automatically configures the corresponding **peer enable** command. This function must be manually enabled in other address family views.



**Configuration Impact**



Enabling or disabling a BGP peer group in this address family causes the BGP connections of the peer group in other address families to be disconnected and automatically renegotiated.



**Precautions**



If a peer group has established peer relationships in another address family, running the **peer enable** command may disconnect and re-establish all peer relationships in the peer group, causing route flapping. Therefore, exercise caution when running this command.




Example
-------

# Enable the device to exchange relevant routing information with a specified peer group in the address family view.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test internal
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer test enable

```
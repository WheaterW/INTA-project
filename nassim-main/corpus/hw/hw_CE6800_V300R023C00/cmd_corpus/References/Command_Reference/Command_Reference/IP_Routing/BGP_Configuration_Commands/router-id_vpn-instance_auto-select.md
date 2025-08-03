router-id vpn-instance auto-select
==================================

router-id vpn-instance auto-select

Function
--------



The **router-id vpn-instance auto-select** command configures automatic router ID selection for all BGP-VPN instances. Each router ID identifies only one device in an AS.

The **undo router-id vpn-instance auto-select** command deletes the configuration of automatic router ID selection for a BGP-VPN instance.



By default, no BGP Router ID is configured, and the Router ID configured for the route management module through the router id command is used.


Format
------

**router-id vpn-instance auto-select**

**undo router-id vpn-instance auto-select**


Parameters
----------

None

Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **router-id** command is used to specify a router ID for a device. Each router ID identifies a device in an AS.You can run the **router-id vpn-instance auto-select** command to configure automatic router ID selection for a BGP-VPN instance so that the router ID of the BGP-VPN instance is distinguished from the BGP router ID. If a router ID has been manually specified for a BGP VPN instance, the manually specified router ID takes precedence over the automatically selected router ID. For more information about the router ID of a BGP-VPN instance, see router-id (BGP-VPN instance IPv4 address family view).

**Prerequisites**

The **bgp** command is run to enable BGP.

**Configuration Impact**

If a BGP session has been established in a BGP-VPN instance, deleting the router ID configured for the BGP-VPN instance will reset the BGP session. Therefore, exercise caution when running this command.

**Precautions**

By default, the Device that is not configured with any interface uses the Router ID of 0.0.0.0 assigned by routing management.


Example
-------

# Configure automatic Router ID selection for all BGP-VPN instance.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] router-id vpn-instance auto-select

```
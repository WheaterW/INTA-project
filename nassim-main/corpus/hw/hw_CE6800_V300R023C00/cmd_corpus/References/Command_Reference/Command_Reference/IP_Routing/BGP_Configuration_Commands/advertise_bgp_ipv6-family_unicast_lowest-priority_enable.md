advertise bgp ipv6-family unicast lowest-priority enable
========================================================

advertise bgp ipv6-family unicast lowest-priority enable

Function
--------



The **advertise bgp ipv6-family unicast lowest-priority enable** command enables BGP to set the priorities of BGP routes to be advertised to the lowest.

The **undo advertise bgp ipv6-family unicast lowest-priority enable** command restores the default configuration.



By default, BGP is disabled from setting the priorities of BGP routes to be advertised to the lowest.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**advertise bgp ipv6-family unicast lowest-priority enable**

**undo advertise bgp ipv6-family unicast lowest-priority enable**


Parameters
----------

None

Views
-----

maintenance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In an M-LAG dual-homing access scenario where O&M needs to be performed on an M-LAG member device, you can run the **advertise bgp ipv6-family unicast lowest-priority enable** command to enable BGP on the device to forcibly set the priorities of BGP routes to be advertised to the lowest (changing the MED to the maximum value and the Local\_Pref to the minimum value). This configuration ensures that the other devices on the network are instructed not to use this device to forward data and that service traffic can be switched to the other M-LAG member device.



**Precautions**

The **advertise bgp ipv6-family unicast lowest-priority enable** command takes effect for all routes in the BGP-IPv6 unicast and BGP-VPN instance IPv6 address families.If at least one of the advertise bgp ipv6-family unicast lowest-priority enable and **advertise lowest-priority all-address-family peer-up** commands is run, BGP can set the priorities of routes (to be advertised) in the preceding address families to the lowest when BGP peers in these address families go up from down.After the **advertise bgp ipv6-family unicast lowest-priority enable** command is run, modifying the MED and Local\_Pref attributes of BGP routes to be advertised through an export routing policy does not take effect.


Example
-------

# Enable BGP to set the priorities of BGP routes to be advertised to the lowest.
```
<HUAWEI> system-view
[~HUAWEI] maintenance
[~HUAWEI-maintenance] advertise bgp ipv6-family unicast lowest-priority enable

```
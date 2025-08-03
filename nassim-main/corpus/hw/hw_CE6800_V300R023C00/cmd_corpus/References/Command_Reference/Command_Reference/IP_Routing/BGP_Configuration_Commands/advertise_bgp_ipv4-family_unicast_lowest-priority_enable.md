advertise bgp ipv4-family unicast lowest-priority enable
========================================================

advertise bgp ipv4-family unicast lowest-priority enable

Function
--------



The **advertise bgp ipv4-family unicast lowest-priority enable** command enables a device to reduce the preference of BGP routes to be advertised.

The **undo advertise bgp ipv4-family unicast lowest-priority enable** command restores the default configuration.



By default, BGP is disabled from setting the priorities of BGP routes to be advertised to the lowest.


Format
------

**advertise bgp ipv4-family unicast lowest-priority enable**

**undo advertise bgp ipv4-family unicast lowest-priority enable**


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



In an M-LAG dual-homing access maintenance scenario, you can run the **advertise bgp ipv4-family unicast lowest-priority enable** command to enable BGP on the device to forcibly set the priorities of BGP routes to be advertised to the lowest (changing the MED to the maximum value and the Local\_Pref to the minimum value). This configuration ensures that the other devices on the network are instructed not to use this device to forward data and that service traffic can be switched to the other M-LAG member device.



**Precautions**

The **advertise bgp ipv4-family unicast lowest-priority enable** command takes effect for all routes in the BGP-Ipv4 unicast and BGP-VPN instance Ipv4 address families.If at least one of the advertise bgp ipv4-family unicast lowest-priority enable and **advertise lowest-priority all-address-family peer-up** commands is run, BGP can set the priorities of routes (to be advertised) in the preceding address families to the lowest when BGP peers in these address families go up from down.After the **advertise bgp ipv4-family unicast lowest-priority enable** command is run, modifying the MED and Local\_Pref attributes of BGP routes to be advertised through an export routing policy does not take effect.


Example
-------

# Enable BGP to set the priorities of BGP routes to be advertised to the lowest.
```
<HUAWEI> system-view
[~HUAWEI] maintenance
[~HUAWEI-maintenance] advertise bgp ipv4-family unicast lowest-priority enable

```
advertise delay on-startup delay-time(BGP-VPN instance IPv4 address family view/BGP-VPN instance IPv6 address family view)
==========================================================================================================================

advertise delay on-startup delay-time(BGP-VPN instance IPv4 address family view/BGP-VPN instance IPv6 address family view)

Function
--------



The **advertise delay on-startup delay-time** command configures a delay in advertising BGP routes after a device restarts.

The **undo advertise delay on-startup** command restores the default configuration.



By default, BGP does not delay route advertisement after a device restart.


Format
------

**advertise delay on-startup delay-time** *time-value*

**undo advertise delay on-startup** [ **delay-time** *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-value* | Specifies a delay. | The value is an integer ranging from 1 to 864000, in seconds. |



Views
-----

BGP-VPN instance IPv4 address family view,BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a device is restarted, routes on the device need to be advertised after a delay to prevent traffic loss during forwarding entry delivery. To configure a BGP route advertisement delay after the device restarts, run the **advertise delay on-startup delay-time** command before restarting the device. The command specifies how long the device must wait after a restart before it starts to advertise BGP routes. If the specified delay has not expired after forwarding entries are delivered, you can run the refresh bgp all export, refresh bgp vpn-instance <vpn-instance-name> ipv4-family all export, refresh bgp vpn-instance <vpn-instance-name> ipv6-family all export, or reset bgp advertise delay on-startup command to enable the device to advertise BGP routes immediately.

**Precautions**

The **advertise delay on-startup delay-time** command setting takes effect only after the **reboot** command is executed and the configuration is saved.If both this command and the **advertise lowest-priority on-startup** command are run, the latest configuration overrides the previous one.This command and the **advertise lowest-priority all-address-family peer-up delay** command are mutually exclusive.


Example
-------

# Configure delayed BGP route advertisement.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] advertise delay on-startup delay-time 100

```
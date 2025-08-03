advertise lowest-priority on-startup
====================================

advertise lowest-priority on-startup

Function
--------



The **advertise lowest-priority on-startup** command configures BGP to minimize the priorities of the BGP routes to be advertised.

The **undo advertise lowest-priority on-startup** command restores the default configuration.



By default, the priorities of the BGP routes to be advertised remain unchanged.


Format
------

**advertise lowest-priority on-startup** [ **delay-time** *time-value* ]

**undo advertise lowest-priority on-startup** [ **delay-time** *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **delay-time** *time-value* | Specifies a delay. | The value is an integer ranging from 1 to 864000, in seconds.  The default value is 0, indicating that the delay function is disabled. |



Views
-----

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When a device restarts during ARP entry delivery, the route advertised by the device needs to have a low priority to prevent traffic loss.<br />
Before restarting the device, you can run the **advertise lowest-priority on-startup** command to set the lowest priority for the routes advertised to peers. That is, you can change the MED value to 4294967295 and the Local\_Pref value to 0. As such, a BGP route advertised by the device has the lowest priority among routes of the the same type after the device restarts, preventing the BGP route from being preferentially selected. To restore the priorities of these BGP routes after ARP entries are delivered, run the **reset bgp advertise lowest-priority on-startup** command.You can also run the **advertise lowest-priority on-startup delay-time** command before the device restarts to ensure that the priority of the routes advertised by the device is the lowest among the routes of the same type within the configured delay after the device restarts. ARP entries are delivered within the delay time. After the delay time expires, the priority of the routes advertised by the device is automatically restored. Within the delay, you can also run the **reset bgp advertise lowest-priority on-startup** command to restore the default priority of the routes to be advertised.In addition, when advertising low-priority routes, you can run the undo undo advertise lowest-priority on-startup [delay-time ] command to restore the default priority of routes to be advertised, regardless of whether there is a delay.

**Precautions**

If the **advertise lowest-priority on-startup** command is run after BGP configurations are committed, the configuration of this command takes effect only after the **reboot** command is run. If the **advertise lowest-priority on-startup** command and BGP configurations are committed as a whole, the configuration of this command takes effect immediately.This command and the **advertise delay on-startup delay-time** command overwrite each other.This command and the **advertise lowest-priority all-address-family peer-up delay** command are mutually exclusive.


Example
-------

# Configure BGP to change the priorities of the routes to be advertised to peers to the lowest priority.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] advertise lowest-priority on-startup

```
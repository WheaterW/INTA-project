advertise delay on-startup delay-time
=====================================

advertise delay on-startup delay-time

Function
--------



The **advertise delay on-startup delay-time** command configures a delay for BGP route advertisement after a device restart.

The **undo advertise delay on-startup** command restores the default configuration.



By default, BGP does not delay advertising routes after a device restart.


Format
------

**advertise delay on-startup delay-time** *time-value*

**undo advertise delay on-startup** [ **delay-time** *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **delay-time** *time-value* | Specifies a delay. | The value is an integer ranging from 1 to 864000, in seconds. |



Views
-----

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a device is restarted, routes on the device need to be advertised after a delay to prevent traffic loss during forwarding entry delivery.<Gtms Id="5ca1a0f2-3bc6-4589-a657-cfa388b5a0e0"/><Gtms Id="7dd8868f-3f43-43a8-bf82-d544b4bb5e1f"/><Gtms Id="c78bd149-6046-481a-af05-848b8185c2c9"/>

**Precautions**

The **advertise delay on-startup delay-time** command takes effect only after the **reboot** command is executed and the configuration is saved.If both this command and the **advertise lowest-priority on-startup** command are run, the latest configuration overrides the previous one.This command and the **advertise lowest-priority all-address-family peer-up delay** command are mutually exclusive.


Example
-------

# Configure a delay for BGP route advertisement after a device restart.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] advertise delay on-startup delay-time 100

```
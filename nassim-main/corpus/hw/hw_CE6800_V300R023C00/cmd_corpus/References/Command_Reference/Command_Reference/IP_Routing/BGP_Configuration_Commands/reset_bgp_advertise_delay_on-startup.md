reset bgp advertise delay on-startup
====================================

reset bgp advertise delay on-startup

Function
--------



The **reset bgp advertise delay on-startup** command allows immediate advertisement of BGP routes after a device restart.




Format
------

**reset bgp advertise delay on-startup**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the **advertise delay on-startup delay-time** command is run and its configuration is saved on a device as well as the **reboot** command is run, the device delays advertising BGP routes after the restart. To enable the device to immediately advertise BGP routes, run the **reset bgp advertise delay on-startup** command.


Example
-------

# Allow immediate advertisement of BGP routes after a device restart.
```
<HUAWEI> reset bgp advertise delay on-startup

```
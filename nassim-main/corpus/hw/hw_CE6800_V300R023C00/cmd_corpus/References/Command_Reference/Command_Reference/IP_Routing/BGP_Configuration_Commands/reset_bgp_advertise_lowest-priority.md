reset bgp advertise lowest-priority
===================================

reset bgp advertise lowest-priority

Function
--------



The **reset bgp advertise lowest-priority on-startup** command configures BGP to restore the original priorities of the BGP routes to be advertised.

The **reset bgp advertise lowest-priority all-address-family peer-up** command configures BGP to restore the priorities of the routes to be advertised to BGP peers when the peers go Up from Down.




Format
------

**reset bgp advertise lowest-priority on-startup**

**reset bgp advertise lowest-priority all-address-family peer-up**

**reset bgp instance** *instance-name* **advertise** **lowest-priority** **all-address-family** **peer-up**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **instance** *instance-name* | Specifies a BGP multi-instance. | The value is a string of 1 to 31 case-sensitive characters without spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **reset bgp advertise lowest-priority on-startup** command restores the original priority of the routes advertised by BGP to peers.After the advertise lowest-priority on-startup and **reboot** commands are run and configurations are saved, the priorities of the BGP routes to be advertised are minimized. To restore the original priorities of these routes, run the **reset bgp advertise lowest-priority on-startup** command.The **reset bgp advertise lowest-priority all-address-family peer-up** command applies to delayed route advertisement scenarios. After this command is run, routes with normal priorities are sent to peers for re-selection. When the peer status is Up, low-priority routes are preferentially sent. After forwarding entries are delivered, the original priorities are restored. This prevents traffic loss caused by forwarding entry delivery failures. Otherwise, the priority of the route with a lower priority cannot be automatically restored if no delay timer is configured.

**Precautions**

After the **reset bgp advertise lowest-priority on-startup** command is run, the advertise lowest-priority on-startup configuration can still take effect after the **reboot** command is run.


Example
-------

# Configure BGP to restore the priorities of the BGP multi-instance routes to be advertised to BGP peers when the peers go Up from Down.
```
<HUAWEI> reset bgp instance huawei advertise lowest-priority all-address-family peer-up

```

# Configure BGP to restore the priorities of the BGP routes to be advertised to BGP peers when the peers go Up from Down.
```
<HUAWEI> reset bgp advertise lowest-priority all-address-family peer-up

```
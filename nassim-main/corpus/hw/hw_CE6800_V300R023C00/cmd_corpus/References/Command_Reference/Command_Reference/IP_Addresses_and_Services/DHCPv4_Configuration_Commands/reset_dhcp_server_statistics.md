reset dhcp server statistics
============================

reset dhcp server statistics

Function
--------

The **reset dhcp server statistics** command clears statistics on the DHCP server.



Format
------

**reset dhcp server statistics**



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

**Usage Scenario**

This command applies to DHCP servers. Collecting statistics on the DHCP messages sent and received within a specified period helps you locate DHCP faults. Run the **reset dhcp server statistics** command to clear original statistics on DHCP messages and then run the display dhcp server statistics to view message statistics on the DHCP server.

**Precautions**

The reset dhcp client statistics command can be run multiple times at any interval.



Example
-------

# Clear message statistics on the DHCP server.
```
<HUAWEI> reset dhcp server statistics

```
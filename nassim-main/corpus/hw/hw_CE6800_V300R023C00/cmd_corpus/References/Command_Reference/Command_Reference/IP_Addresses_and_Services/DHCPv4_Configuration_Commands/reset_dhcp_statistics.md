reset dhcp statistics
=====================

reset dhcp statistics

Function
--------



The **reset dhcp statistics** command clears packet statistics about a DHCP.




Format
------

**reset dhcp statistics**


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

During DHCP troubleshooting, statistics about the packets sent and received within a specified period need to be checked. Therefore, before collecting packet statistics, run the **reset dhcp statistics** command to clear the existing packet statistics. Then you can run the **display dhcp statistics** command to view DHCP message statistics.


Example
-------

# Clear packet statistics about the DHCP.
```
<HUAWEI> reset dhcp statistics

```
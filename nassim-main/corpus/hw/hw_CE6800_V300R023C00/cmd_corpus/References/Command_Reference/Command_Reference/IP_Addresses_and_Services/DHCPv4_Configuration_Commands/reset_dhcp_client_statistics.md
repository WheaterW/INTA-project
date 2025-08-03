reset dhcp client statistics
============================

reset dhcp client statistics

Function
--------



The **reset dhcp client statistics** command clears packet statistics about a DHCP client.




Format
------

**reset dhcp client statistics** [ **interface** { *interface-type* *interface-number* | *interface-name* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Clear packet statistics about the DHCP client of the specified interface.   * <interface-type> specifies the interface type. * <interface-number> specifies the interface number. | - |
| *interface-name* | Clears client statistics on a specified interface.   * <interface-name> specifies the name of an interface. | - |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **reset dhcp client statistics** command is applicable to DHCP client. During DHCP troubleshooting, statistics about the packets sent and received within a specified period need to be checked. Therefore, before collecting packet statistics, run the **reset dhcp client statistics** command to clear the existing packet statistics. Then you can run the **display dhcp client statistics** command to check packet statistics about the DHCP client.

**Precautions**

The command can be run multiple times at any interval.


Example
-------

# Clear packet statistics about the DHCP client.
```
<HUAWEI> reset dhcp client statistics

```
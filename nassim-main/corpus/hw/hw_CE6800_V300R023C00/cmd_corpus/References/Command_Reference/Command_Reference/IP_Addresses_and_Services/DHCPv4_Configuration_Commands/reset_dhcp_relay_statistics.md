reset dhcp relay statistics
===========================

reset dhcp relay statistics

Function
--------



The **reset dhcp relay statistics** command clears message statistics on a DHCP relay agent.




Format
------

**reset dhcp relay statistics** [ **server-group** *group-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **server-group** *group-name* | Specifies the name of a DHCP server group. | The value is a string of 1 to 32 case-sensitive characters. It can contain only digits, letters, and special characters ('\_', '-', and '.') and cannot use "-" or "--" as a name. If the string is enclosed in double quotation marks ("), spaces are allowed in the string. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

This command is applicable to DHCP relay agents. Collecting statistics on the DHCP messages sent and received within a specified period helps you locate DHCP faults. Run the **reset dhcp relay statistics** command to clear original statistics on DHCP messages, and run the **display dhcp relay statistics** command to view packet statistics about the DHCP relay agent.

* reset dhcp relay statistics server-group group-name: clears message statistics on DHCP relay agents connected to DHCP servers in a DHCP server group. You need to specify the name of the DHCP server group. You can run the command to clear the statistics obtained using the display dhcp relay statistics server-group group-name command.
* reset dhcp relay statistics: clears message statistics on all DHCP relay agents. The command does not clear the statistics obtained using the display dhcp relay statistics server-group group-name command.

**Precautions**

The reset dhcp client statistics command can be run multiple times at any interval.


Example
-------

# Clear message statistics on the DHCP relay agent.
```
<HUAWEI> reset dhcp relay statistics

```
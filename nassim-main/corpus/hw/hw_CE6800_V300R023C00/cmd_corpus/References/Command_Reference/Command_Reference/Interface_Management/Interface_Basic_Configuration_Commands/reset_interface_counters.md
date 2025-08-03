reset interface counters
========================

reset interface counters

Function
--------



The **reset interface counters** command deletes traffic statistics on an interface.




Format
------

**reset interface counters** [ **if-mib** ] [ *interface-type* [ *interface-number* ] | *interface-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **if-mib** | Indicates IF-MIB statistics on an interface. | - |
| *interface-type* *interface-number* | Specifies the type and number of an interface.  If interface-type interface-num parameter is not specified, traffic statistics on all interfaces are deleted. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Before collecting bit error statistics on a control interface within a period, run the reset counters controller command to delete the existing bit error statistics on the interface.



**Precautions**



After this command is executed, all packet statistics displayed in the **display interface** command output are cleared. Therefore, exercise caution when running this command.The reset interface counters [if-mib] [ interface-type [ interface-num ] | ifname ] command cannot be used to clear statistics about the number of discarded bytes, rate at which packets are discarded, and rate at which bytes are discarded in the outbound direction of an Ethernet physical interface. To clear these statistics, run the **reset qos queue statistics** command in the user view.




Example
-------

# Delete traffic statistics on all interfaces.
```
<HUAWEI> reset interface counters

```
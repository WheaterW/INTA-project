reset statistics
================

reset statistics

Function
--------



The **reset rip statistics** command clears statistics maintained by a particular RIP process.

The **reset ripng statistics** command clears statistics about a specific RIPng process.




Format
------

**reset rip** *process-id* **statistics** **interface** { **all** | { *interface-name* | *interface-type* *interface-number* } [ **neighbor** *neighbor-address* ] }

**reset ripng** *process-id* **statistics** **interface** { **all** | { *interface-name* | *interface-type* *interface-number* } [ **neighbor** *neighbor-ipv6-address* ] }

**reset rip all statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Displays information about the ABR or ASBR of an OSPF route in a specified OSPF process. | The value is an integer ranging from 1 to 4294967295. |
| **interface** | Clears statistics about a specified interface. | - |
| **all** | Clears statistics about all interfaces. | - |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies the interface number. | - |
| **neighbor** *neighbor-address* | Clears statistics about RIP exchanges with a neighbor. | The value is in dotted decimal notation. |



Views
-----

User view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To clear statistics about the specified or all processes, run the reset the command in the user view. The command output helps you repeatedly record statistics during debugging.

**Precautions**



Running the **reset ripng statistics** command clears statistics about a RIPng process. Therefore, exercise caution when running the command.




Example
-------

# Reset the statistics for RIP process 100.
```
<HUAWEI> reset rip 100 statistics interface all

```
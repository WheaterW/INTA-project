reset isis statistics
=====================

reset isis statistics

Function
--------



The **reset isis statistics** command deletes IS-IS packet or socket statistics.




Format
------

**reset isis statistics** { **packet** | **socket** } [ **interface** [ *interface-name* | *interface-type* *interface-number* ] ]

**reset isis** *process-id* **statistics** **packet**

**reset isis statistics packet lsp** [ *process-id* | { **vpn-instance** *vpn-instance-name* } ]

**reset isis** [ *process-id* ] **statistics** **packet** **lsp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **packet** | Deletes packet statistics. | - |
| **socket** | Deletes socket statistics. | - |
| **interface** | Deletes IS-IS packet statistics on a specified interface. | - |
| *interface-type* | Specifies the type and number of an interface.  If the parameter is not specified, IS-IS packet statistics on all interfaces are deleted. | - |
| *interface-number* | Specifies the type and number of an interface.  If the parameter is not specified, IS-IS packet statistics on all interfaces are deleted. | - |
| *process-id* | Deletes IS-IS packet statistics of the specified IS-IS process. | The value is an integer ranging from 1 to 4294967295. |
| **lsp** | Deletes statistics about LSPs. | - |
| **vpn-instance** *vpn-instance-name* | Deletes statistics about LSPs of specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

When troubleshooting IS-IS network faults, you can run the **reset isis statistics** command to delete the existing statistics before checking new information about incorrect LSPs and Hello packets.


Example
-------

# Delete packet statistics of IS-IS process 1.
```
<HUAWEI> reset isis 1 statistics packet

```
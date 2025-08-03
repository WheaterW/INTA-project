reset isis statistics purge-lsp
===============================

reset isis statistics purge-lsp

Function
--------



The **reset isis statistics purge-lsp** command deletes statistics about purge LSPs of a specified IS-IS process.




Format
------

**reset isis statistics purge-lsp** [ *process-id* | { **vpn-instance** *vpn-instance-name* } ] [ **level-1** | **level-2** ]

**reset isis** [ *process-id* ] **statistics** **purge-lsp** [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an IS-IS process. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Deletes statistics about IS-IS purge LSPs of specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **level-1** | Deletes statistics about IS-IS Level-1 purge LSPs. | - |
| **level-2** | Deletes statistics about IS-IS Level-2 purge LSPs. | - |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To locate a problem on an IS-IS network, you can run the **reset isis statistics purge-lsp** command to delete existing statistics about purge LSPs and then check the latest statistics.


Example
-------

# Delete statistics about purge LSPs of IS-IS process 1.
```
<HUAWEI> reset isis 1 statistics purge-lsp

```
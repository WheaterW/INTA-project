reset ospf peer
===============

reset ospf peer

Function
--------



The **reset ospf peer** command restarts OSPF neighbors.




Format
------

**reset ospf** [ *process-id* ] **peer** [ *interface-name* [ **all-areas** | **area** { *area-id* | *area-id-address* } ] | *interface-type* *interface-number* [ **all-areas** | **area** { *area-id* | *area-id-address* } ] ] *router-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an OSPF process ID. If the parameter is not specified, all OSPF processes are restarted. | The value is an integer ranging from 1 to 4294967295. |
| *interface-name* | Specifies the name of an interface. | - |
| **all-areas** | Clears statistics of all OSPF areas. | - |
| **area** *area-id* | Specifies an area ID in the format of a decimal integer. | The value is an integer ranging from 0 to 4294967295. |
| *area-id-address* | Specifies an area ID in the format of an IP address. | The value is in dotted decimal notation. |
| *interface-type* | Interface type. | - |
| *interface-number* | Specifies the number of an interface based on which information about VLANs in which users go online dynamically is to be displayed. | - |
| *router-id* | Specifies a router ID in the format of an IPv4 address. | The value is in dotted decimal notation. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To restart OSPF neighbors, run the **reset ospf peer** command.Once deleted, statistics cannot be restored. Therefore, exercise caution when deleting statistics.


Example
-------

# Restart OSPF neighbors.
```
<HUAWEI> reset ospf peer 1.1.1.1

```
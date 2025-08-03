reset ospf counters
===================

reset ospf counters

Function
--------



The **reset ospf counters** command clears OSPF statistics.




Format
------

**reset ospf** [ *process-id* ] **counters** [ **neighbor** [ *interface-name* [ **all-areas** | **area** { *area-id* | *area-id* } ] | *interface-type* *interface-number* [ **all-areas** | **area** { *area-id* | *area-id* } ] ] [ *router-id* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |
| **neighbor** | Indicates a neighbor. | - |
| *interface-name* | Specifies the name of an interface. | - |
| **all-areas** | Clears statistics of all OSPF areas. | - |
| **area** *area-id* | Specifies the ID of an OSPF area. | The value can be a decimal integer or an IP address. If the value is an integer, it ranges from 0 to 4294967295. |
| *interface-type* | Interface type. | - |
| *interface-number* | Specifies the number of an interface based on which information about VLANs in which users go online dynamically is to be displayed. | - |
| *router-id* | The router ID of a neighbor. | The value is in dotted decimal notation. |



Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

To reset OSPF statistics, run the reset ospf counters command. Clearing OSPF statistics does not affect OSPF services.Once deleted, statistics cannot be restored. Therefore, exercise caution when deleting statistics.


Example
-------

# Reset OSPF statistics.
```
<HUAWEI> reset ospf counters

```
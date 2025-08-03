display ip routing-table statistics
===================================

display ip routing-table statistics

Function
--------

The **display ip routing-table statistics** command displays integrated route statistics of the IPv4 routing table.



Format
------

**display ip routing-table all-routes statistics**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all-routes** | Displays integrated route statistics about all IPv4 routes. | - |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

Integrated route statistics include:

* Total number of routes that are added or deleted through the routing protocol
* Number of active routes or inactive routes that are labeled for deletion but have not been deleted



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display integrated route statistics.
```
<HUAWEI> display ip routing-table all-routes statistics
Summary Prefixes : 12
Protocol   total      active     added      deleted    
           routes     routes     routes     routes     
DIRECT     11         11         11         0          
STATIC     1          1          1          0          
RIP        0          0          0          0          
OSPF       1          0          1          0          
IS-IS      0          0          0          0          
BGP        0          0          0          0          
Total      13         12         13         0

```


**Table 1** Description of the
**display ip routing-table statistics** command output

| Item | Description |
| --- | --- |
| Summary Prefixes | Total number of route prefixes in the routing table. |
| total | Total number of routes in the current routing table. |
| active | Number of active routes in the routing table. |
| added | Number of active and inactive routes added in the routing table. |
| deleted | Number of routes deleted from the routing table. |
| Protocol | Routing protocol.   * DIRECT: displays direct routes. * STATIC: displays static routes. * RIP: displays RIP routes. * OSPF: displays OSPF routes. * IS-IS: displays IS-IS routes. * BGP: displays BGP routes. |
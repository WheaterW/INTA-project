display ip routing-table statistics(All views)
==============================================

display ip routing-table statistics(All views)

Function
--------

The **display ip routing-table statistics** command displays integrated route statistics of the IPv4 routing table.



Format
------

**display ip routing-table all-vpn-instance statistics**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all-vpn-instance** | Displays integrated route statistics about routes of all VPN instances. | - |




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



# Display statistics of the MBGP routing table.
```
<HUAWEI> display mbgp routing-table statistics
Protocol     total      active      added        deleted
             routes     routes      routes       routes 
OSPF         0          0           0            0      
IS-IS        5          5           45           40     
Total        5          5           45           40

```

# Display integrated route statistics about the IPv4 routes of all VPN instances.
```
<HUAWEI> display ip routing-table all-vpn-instance statistics
Summary Prefixes : 5
Protocol   total      active     added      deleted
           routes     routes     routes     routes
DIRECT     6          6          6          0
STATIC     0          0          0          0
RIP        0          0          0          0
OSPF       2          0          2          0
IS-IS      0          0          0          0
BGP        0          0          0          0
Total      8          6          8          0

```


**Table 1** Description of the
**display ip routing-table statistics(All views)** command output

| Item | Description |
| --- | --- |
| total | Total number of routes in the routing table. |
| active | Number of active routes in the routing table. |
| added | Number of active and inactive routes added to the routing table. |
| deleted | Number of routes to be deleted from the routing table. |
| Protocol | Routing protocol.   * DIRECT: displays direct routes. * STATIC: displays static routes. * RIP: displays RIP routes. * OSPF: displays OSPF routes. * IS-IS: displays IS-IS routes. * BGP: displays BGP routes. |
| Summary Prefixes | Total number of route prefixes in the routing table. |
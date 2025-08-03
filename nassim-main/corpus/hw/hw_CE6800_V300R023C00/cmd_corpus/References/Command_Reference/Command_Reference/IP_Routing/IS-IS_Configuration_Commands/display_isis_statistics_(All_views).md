display isis statistics (All views)
===================================

display isis statistics (All views)

Function
--------



The **display isis statistics** command displays the statistics of an IS-IS process, including the routes that are learned from other IS-IS routers, routes that are imported from other protocols, the convergence priority of IS-IS routes, and LSPs that are generated locally.




Format
------

**display isis statistics** [ **level-1** | **level-2** | **level-1-2** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ]

**display isis** *process-id* **statistics** [ **level-1** | **level-2** | **level-1-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level-1** | Displays statistics about an IS-IS Level-1 router. | - |
| **level-2** | Displays statistics of IS-IS Level-2. | - |
| **level-1-2** | Displays statistics of IS-IS Level-1-2. | - |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Displays mesh-group information about a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To monitor the status of a device or diagnose a fault, run the **display isis statistics** command to view the status of the device and statistics that it collects. The command output helps you collect traffic statistics and troubleshoot the device.If the statistics are all 0, check whether an IS-IS neighbor relationship is established, the LSDB information is complete, or the SPT calculation is correct.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the statistics of IS-IS.
```
<HUAWEI> display isis statistics

Statistics Information for ISIS(1)
--------------------------------------------------------------------------------

Level-1 Statistics
--------------------------------------------------------------------------------

Forwarding routes information:
         Total IPv4 Learnt Routes: 0
                         Critical: 0
                         High    : 0
                         Medium  : 0
                         Low     : 0
         Total IPv4 Forwarding Routes: 0
         Total IPv6 Learnt Routes: 0
                         Critical: 0
                         High    : 0
                         Medium  : 0
                         Low     : 0
         Total IPv6 Forwarding Routes: 0

Imported routes information:
         IPv4 Imported Routes:
                         Static: 0       Direct: 0
                         ISIS:   0       BGP:    0
                         RIP:    0       OSPF:   0
                         OPR:    0       
         IPv6 Imported Routes:
                         Static: 0       Direct: 0
                         ISIS:   0       BGP:    0
                         RIPng:  0       OSPFv3: 0
                         OPR:    0       

Number of routes added to Routing Table:
         IPv4 Routes: 0
         IPv6 Routes: 0

Number of routes not added to Routing Table:
         IPv4 Routes: 0
         IPv6 Routes: 0

Lsp information:
                  LSP Source ID:          No. of used LSPs
                  0000.0000.0001                  001

         Total lsp count                     : 1
         Total 00-00 lsp count               : 1
         Total 00-00 and holdTime=0 lsp count: 0
         Total holdTime=0 lsp count          : 0
         Total seqNum=0 lsp count            : 0

Peer information:
         IPv4 total count     : 0
         IPv4 up state count  : 0
         IPv4 init state count: 0
         IPv6 total count     : 0
         IPv6 up state count  : 0 
         IPv6 init state count: 0

Level-2 Statistics
--------------------------------------------------------------------------------

Forwarding routes information:
         Total IPv4 Learnt Routes: 0
                         Critical: 0
                         High    : 0
                         Medium  : 0
                         Low     : 0
         Total IPv4 Forwarding Routes: 0
         Total IPv6 Learnt Routes: 0
                         Critical: 0
                         High    : 0
                         Medium  : 0
                         Low     : 0
         Total IPv6 Forwarding Routes: 0

Imported routes information:
         IPv4 Imported Routes:
                         Static: 0       Direct: 0
                         ISIS:   0       BGP:    0
                         RIP:    0       OSPF:   0
                         OPR:    0       
         IPv6 Imported Routes:
                         Static: 0       Direct: 0
                         ISIS:   0       BGP:    0
                         RIPng:  0       OSPFv3: 0
                         OPR:    0       

Number of routes added to Routing Table:
         IPv4 Routes: 0
         IPv6 Routes: 0

Number of routes not added to Routing Table:
         IPv4 Routes: 0
         IPv6 Routes: 0

Lsp information:
                  LSP Source ID:          No. of used LSPs
                  0000.0000.0001                  001

         Total lsp count                     : 1
         Total 00-00 lsp count               : 1
         Total 00-00 and holdTime=0 lsp count: 0
         Total holdTime=0 lsp count          : 0
         Total seqNum=0 lsp count            : 0

Peer information:
         IPv4 total count     : 0
         IPv4 up state count  : 0
         IPv4 init state count: 0
         IPv6 total count     : 0
         IPv6 up state count  : 0 
         IPv6 init state count: 0
      
Global Statistics
--------------------------------------------------------------------------------

Interface information:
         IPv4 total count     : 0
         IPv4 up state count  : 0
         IPv4 down state count: 0
         IPv6 total count     : 0
         IPv6 up state count  : 0 
         IPv6 down state count: 0

```

**Table 1** Description of the **display isis statistics (All views)** command output
| Item | Description |
| --- | --- |
| Total IPv4 Learnt Routes | Number of IPv4 routes learned by IS-IS.   * Critical: number of IPv4 routes with critical convergence priority. * High: number of IPv4 routes with high convergence priority. * Medium: number of IPv4 routes with medium convergence priority. * Low: number of IPv4 routes with low convergence priority. |
| Total IPv4 Forwarding Routes | Number of IPv4 routes counted based on the destination address. If multiple routes share the same destination, these routes are counted as one route. |
| Total IPv6 Learnt Routes | Number of IPv6 routes learned by IS-IS.   * Critical: number of IPv6 routes with critical convergence priority. * High: number of IPv6 routes with high convergence priority. * Medium: number of IPv6 routes with medium convergence priority. * Low: number of IPv6 routes with low convergence priority. |
| Total IPv6 Forwarding Routes | Number of IPv6 routes counted based on the destination address. If there are multiple routes to the same destination, these routes are counted as one route. |
| Total lsp count | Total number of LSPs. |
| Total 00-00 lsp count | Number of non-pseudonode LSPs with the fragment number of 0. |
| Total 00-00 and holdTime=0 lsp count | Number of non-pseudonode LSPs with the fragment number of 0 and lifetime of 0. |
| Total holdTime=0 lsp count | Number of LSPs with the lifetime of 0. |
| Total seqNum=0 lsp count | Number of LSPs with the sequence number being 0. |
| IPv4 Imported Routes | Information about imported IPv4 routes:   * Static: number of imported static routes. * Direct: number of imported direct routes. * ISIS: number of imported IS-IS routes. * BGP: number of imported BGP routes. * RIP: number of imported RIP routes. * OSPF: number of imported OSPF routes. |
| IPv4 total count | Number of IPv4 neighbors. |
| IPv4 up state count | Number of IPv4 neighbors that are Up. |
| IPv4 init state count | Number of IPv4 neighbors that are in Init status. |
| IPv4 down state count | Number of IPv4 neighbors that are Down. |
| IPv6 Imported Routes | Information about imported IPv6 routes:   * Static: number of imported static routes. * Direct: number of imported direct routes. * ISIS: number of imported IS-IS routes. * BGP: number of imported BGP routes. * RIPng: number of imported RIPng routes. * OSPFv3: number of imported OSPFv3 routes. |
| IPv6 total count | Number of IPv6 neighbors. |
| IPv6 up state count | Number of IPv6 neighbors that are Up. |
| IPv6 init state count | Number of IPv6 neighbors that are in Init status. |
| IPv6 down state count | Number of IPv6 neighbors that are Down. |
| Imported routes information | Information about imported routes. |
| Number of routes added to Routing Table | Number of routes added to the routing table. |
| Number of routes not added to Routing Table | Number of routes that are not added to the routing table. |
| Lsp information | Information about LSPs. |
| LSP Source ID | System ID of the device that generates the LSP. |
| No. of used LSPs | Number of the used fragmentation. |
| Peer information | Information about neighbors. |
| Interface information | Information about interfaces. |
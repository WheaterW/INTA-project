display isis statistics packet
==============================

display isis statistics packet

Function
--------



The **display isis statistics packet** command displays the statistics of an IS-IS process, including the routes that are learned from other IS-IS routers, routes that are imported from other protocols, the convergence priority of IS-IS routes, and LSPs that are generated locally.




Format
------

**display isis statistics packet** [ **interface** [ *interface-name* | *interfacetype* *interfacenumber* ] ]

**display isis** *process-id* **statistics** **packet**

**display isis statistics packet lsp** [ *process-id* | { **vpn-instance** *vpn-instance-name* } ]

**display isis** [ *process-id* ] **statistics** **packet** **lsp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interfacetype* *interfacenumber* | Displays statistics of the packets on a specified interface. | - |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **packet** | Displays statistics of various IS-IS packets. | - |
| **lsp** | Displays statistics about IS-IS LSPs. | - |
| **vpn-instance** *vpn-instance-name* | Displays mesh-group information about a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To monitor the status of a device or diagnose a fault, run the **display isis statistics packet** command to view the status of the device and statistics that it collects. The command output helps you collect traffic statistics and troubleshoot the device.If the statistics are all 0, check whether an IS-IS neighbor relationship is established, the LSDB information is complete, or the SPT calculation is correct.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics of IS-IS packets.
```
<HUAWEI> display isis statistics packet

         Statistic for ISIS Packets
         --------------------------

Interface Ethernet1/0/1
Level-1 Hellos(sent/received) : 64127/134978
Level-1 MaxHelloInterval      : 10 s
Level-1 DR Elections          : 3
Level-1 LSPs  (sent/received) : 509/1014
Level-1 CSNPs (sent/received) : 0/45448
Level-1 PSNPs (sent/received) : 4/0
Level-2 Hellos(sent/received) : 64155/134911
Level-2 MaxHelloInterval      : 10 s
Level-2 DR Elections          : 3
Level-2 LSPs  (sent/received) : 508/1016
Level-2 CSNPs (sent/received) : 0/45454
Level-2 PSNPs (sent/received) : 4/0

```

**Table 1** Description of the **display isis statistics packet** command output
| Item | Description |
| --- | --- |
| Level-1 Hellos | Number of Level-1 Hello packets. |
| Level-1 MaxHelloInterval | Interval at which Level-1 Hello packets are sent. |
| Level-1 DR Elections | Level-1 DIS election. |
| Level-1 LSPs | Number of Level-1 LSP packets. |
| Level-1 CSNPs | Number of Level-1 CSNP packets. |
| Level-1 PSNPs | Number of Level-1 PSNP packets. |
| Level-2 Hellos | Number of Level-2 Hello packets. |
| Level-2 MaxHelloInterval | Interval at which Level-2 Hello packets are sent. |
| Level-2 DR Elections | Level-2 DIS election. |
| Level-2 LSPs | Number of Level-2 LSP packets. |
| Level-2 CSNPs | Number of Level-2 CSNP packets. |
| Level-2 PSNPs | Number of Level-2 PSNP packets. |
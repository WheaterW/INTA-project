display arp broadcast-suppress user bridge-domain
=================================================

display arp broadcast-suppress user bridge-domain

Function
--------



The **display arp broadcast-suppress user bridge-domain** command displays ARP broadcast suppression entries in a BD.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display arp broadcast-suppress user bridge-domain** *bd-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *bd-id* | Displays ARP broadcast suppression entries in a specified BD. | The value is an integer ranging from 1 to 16777215. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

ARP broadcast suppression can effectively ease the pressure on gateways in handling ARP packets. If ARP broadcast suppression is enabled, a gateway checks whether host information corresponding to the destination IP address (mapping between the IP address and MAC address of the peer device) exists upon receipt of an ARP request.

* If such mapping exists, the gateway replaces the broadcast MAC address in the ARP request with the MAC address of the peer device and then sends the ARP request through the interface corresponding to the MAC address of the peer device.
* If such mapping does not exist, the gateway broadcasts the ARP request in the BD as usual.To view ARP broadcast suppression entries in a specified BD, run the command.
* If both the suppression table statically configured on the local device and the suppression table pushed by the remote device exist, the suppression table statically configured on the local device takes precedence.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display ARP broadcast suppression entries in BD 5.
```
<HUAWEI> display arp broadcast-suppress user bridge-domain 5
Flags: S - Static, D - Dynamic, C - Conflict
Total:4
------------------------------------------------------------------------------------
IP Address      MAC Address      Vtep IP         Flags       Aging(M)      Interface
------------------------------------------------------------------------------------
10.1.1.1        00e0-fc21-0110   --              D           15            100GE1/0/1.1
10.1.1.2        00e0-fc02-0002   --              D           15            100GE1/0/1.2 
10.1.1.3        00e0-fc01-0101   2.2.2.2         D           --            --

```

**Table 1** Description of the **display arp broadcast-suppress user bridge-domain** command output
| Item | Description |
| --- | --- |
| IP Address | IP address of an ARP broadcast suppression entry. |
| MAC Address | MAC address of an ARP broadcast suppression entry. |
| Vtep IP | Source VTEP address of a VXLAN tunnel. |
| Flags | Type of an ARP broadcast suppression entry.   * S: Static, which is only an example and does not mean that the product actually supports the flag. * D: Dynamic, indicating that the ARP broadcast suppression entry is dynamically generated. Specifically,  1. Layer 2 proxy locally learned entries 2. Entries advertised by remote hosts 3. BD Layer 3 ARP entry conversion.  * C: Conflict, which is only an example and does not mean that the product actually supports the flag. |
| Aging(M) | Aging time of ARP broadcast suppression entries, in minutes.  For remote entries, this field is displayed as "-". |
| Interface | Interface on which the device learns ARP broadcast suppression entries.  For remote entries, this field is displayed as "-". |
| Total | Total number of ARP broadcast suppression entries in the BD. |
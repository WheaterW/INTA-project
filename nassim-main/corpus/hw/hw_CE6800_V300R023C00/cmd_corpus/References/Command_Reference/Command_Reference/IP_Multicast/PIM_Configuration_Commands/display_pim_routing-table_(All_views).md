display pim routing-table (All views)
=====================================

display pim routing-table (All views)

Function
--------



The **display pim routing-table** command displays PIM routing entries in the PIM routing table.




Format
------

**display pim routing-table**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display pim routing-table** command displays contents in a PIM routing table, including information about multicast source and group addresses, RPs, inbound interfaces, and outbound interface lists in (S, G) and (\*, G) entries.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display contents in the PIM-SM multicast routing table of the public network instance.
```
<HUAWEI> display pim routing-table
VPN-Instance: public net
 Total 0 (*, G) entry; 1 (S, G) entry

 (192.168.0.2, 227.0.0.1)
     RP: 2.2.2.2
     Protocol: pim-sm, Flag: SPT LOC ACT
     UpTime: 02:54:43
     Upstream interface: 100GE1/0/1, Refresh time: 02:54:43
         Upstream neighbor: NULL
         RPF prime neighbor: NULL
     Downstream interface(s) information:
     Total number of downstreams: 1
         1: 100GE1/0/2
             Protocol: pim-sm, UpTime: 02:54:43, Expires: 00:02:47

```

**Table 1** Description of the **display pim routing-table (All views)** command output
| Item | Description |
| --- | --- |
| Total 0 (\*, G) entry; 1 (S, G) entry | Total number of (S, G) and (\*, G) entries in the PIM routing table. |
| Total number of downstreams | Number of downstream interfaces. |
| (192.168.0.2, 227.0.0.1) | (S, G) entry in the PIM routing table. |
| Upstream neighbor | Upstream neighbor of the (S, G) or (\*, G) entry. |
| Upstream interface | Inbound interface of the (S, G) or (\*, G) entry. |
| Refresh time | Refresh time of upstream interface. |
| RPF prime neighbor | RPF neighbor of the (S, G) or (\*, G) entry.   * For the (\*, G) entry, when the local Router is an RP, the RPF neighbor in the (\*, G) entry is null. * For the (S, G) entry, when the local Router is directly connected to a source, the RPF neighbor in the (S, G) entry is null. |
| Downstream interface(s) information | Information about downstream interfaces, including:   * Total number of downstream interfaces. * Name of a downstream interface. * PIM protocol type configured for a downstream interface. * Keepalive period and timeout period of a downstream interface. |
| VPN-Instance | Instance in which PIM routing entries are displayed. |
| RP | RP address. |
| Flag | Flag of a PIM (S, G) or (\*, G) entry.  Run the display pim routing-table command on the MSDP peer nearest to the source to view routing information. If an (S, G) entry does not have a 2MSDP flag, the MSDP peer is not an RP. Change the configurations of the RP or MSDP peer on the PIM-SM network to ensure that the MSDP peer is an RP. |
| UpTime | Keepalive period of the interface. |
| Expires | Timeout period of the (S, G) or (\*, G) entry. |
| Protocol | PIM protocol type, which can be PIM-DM, PIM-SM, or PIM-SSM. |
display multicast routing-table
===============================

display multicast routing-table

Function
--------



The **display multicast routing-table** command displays information about multicast routing tables.




Format
------

**display multicast routing-table**


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

The **display multicast routing-table** command is used to display the information of a multicast routing table.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display routing entries in the multicast routing table of the public network instance.
```
<HUAWEI> display multicast routing-table
Multicast routing table of VPN Instance: public net
Total 0 (*, G) entry; 1 (S, G) entries 
 00001: (192.168.0.2, 227.0.0.1)
       Uptime: 00:00:28
       Upstream Interface: 100GE1/0/1
       List of 2 downstream interfaces
           1:  100GE1/0/2
           2:  100GE1/0/3

```

**Table 1** Description of the **display multicast routing-table** command output
| Item | Description |
| --- | --- |
| Multicast routing table of VPN Instance | VPN instance to which the multicast routing information corresponds. |
| Total 0 (\*, G) entry; 1 (S, G) entries | Number of eligible routing entries. |
| (192.168.0.2, 227.0.0.1) | (S, G) entry in the multicast routing table. |
| Upstream Interface | Upstream interface of the (S, G) entry or MVPN extranet entry. |
| List of 2 downstream interfaces | Downstream interface list. |
| 00001 | Sequence number of the (S, G) entry. |
| Uptime | Indicates the period during which the (S, G) entry exists. |
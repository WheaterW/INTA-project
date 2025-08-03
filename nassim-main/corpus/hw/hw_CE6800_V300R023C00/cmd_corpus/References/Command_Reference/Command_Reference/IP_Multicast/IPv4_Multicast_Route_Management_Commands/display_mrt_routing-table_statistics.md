display mrt routing-table statistics
====================================

display mrt routing-table statistics

Function
--------



The **display mrt routing-table statistics** command displays the statistics of the multicast routing table (MRT) routes.




Format
------

**display mrt routing-table** [ **vpn-instance** *vpn-instance-name* ] **statistics**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

Route statistics include:

* Total number of routes that are added or deleted by the protocol
* Number of active routes or inactive routes that are labeled for deletion but are not actually deleted

Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics of the MRT routing table.
```
<HUAWEI> display mrt routing-table statistics
Summary Prefixes : 0
Protocol   total      active     added      deleted
           routes     routes     routes     routes
MSTATIC    0          0          0          0

```

**Table 1** Description of the **display mrt routing-table statistics** command output
| Item | Description |
| --- | --- |
| Summary Prefixes | Number of route prefixes. |
| Protocol | Routing protocol. |
| total routes | Total number of routes in the routing table. |
| active routes | Number of active routes in the routing table. |
| added routes | Number of active and inactive routes added in the routing table. |
| deleted routes | Number of routes to be deleted from the routing table. |
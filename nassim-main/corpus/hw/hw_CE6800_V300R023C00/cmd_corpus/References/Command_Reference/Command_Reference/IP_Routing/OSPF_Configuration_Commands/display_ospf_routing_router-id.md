display ospf routing router-id
==============================

display ospf routing router-id

Function
--------



The **display ospf routing router-id** command displays OSPF node information.




Format
------

**display ospf** [ *process-id* ] **routing** **router-id** [ *router-id-value* ] [ **age** { **min-value** *min-age-value* | **max-value** *max-age-value* } \* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the OSPF process ID. | The value is an integer ranging from 1 to 4294967295. |
| **router-id** *router-id-value* | Specifies the router ID of a destination router. | The value is in dotted decimal notation. |
| **age** | Displays information based on the age time. | - |
| **min-value** *min-age-value* | Displays information about only LSAs with the age value greater than or equal to the min-age-value value. | The value is an integer ranging from 0 to 4294967295. |
| **max-value** *max-age-value* | Displays information only about LSAs with the age value less than or equal to the max-age-value value. | The value is an integer ranging from 0 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can view the route of a specified interface or next hop.The command output helps you troubleshoot OSPF faults.You can run the **display ospf routing router-id** command to query the next hop of a device.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the routes to a specified OSPF router.
```
<HUAWEI> display ospf routing router-id 10.1.1.1
OSPF Process 1 with Router ID 10.1.1.1

 Destination    : 10.1.1.2             Route Type          : Intra-area
 Area           : 0.0.0.1              AdvRouter           : 10.1.1.2
 Type           : ASBR                 Age                 : 00:00:33
 URT Cost       : 1
 NextHop        : 10.1.2.2             Interface           : 100GE1/0/1
 Backup NextHop : 10.1.3.3             Backup Interface    : 100GE1/0/2
 Backup Type    : LFA LINK

```

**Table 1** Description of the **display ospf routing router-id** command output
| Item | Description |
| --- | --- |
| Destination | Destination network. |
| Route Type | Route type. |
| Type | Node type. |
| Area | Area ID. |
| AdvRouter | Advertiser. |
| Age | Time after the route was generated. |
| URT Cost | Cost value. |
| NextHop | Next-hop address to the destination address. |
| Interface | Outbound interface of a route. |
| Backup NextHop | IP address of the next backup hop. |
| Backup Interface | Outbound interface of the next backup route. |
| Backup Type | Type of the backup next hop:   * LFA LINK: OSPF LFA protection link. * LFA LINK-NODE: OSPF LFA link protection node. * REMOTE LFA LINK: OSPF remote LFA link protection node. * REMOTE LFA LINK-NODE: OSPF TI-LFA link protection node. * TI-LFA LINK-NODE: OSPF TI-LFA link protection node. |
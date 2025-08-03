display ospf hostname-table
===========================

display ospf hostname-table

Function
--------



The **display ospf hostname-table** command displays information about OSPF dynamic hostnames.




Format
------

**display ospf** [ *process-id* ] **hostname-table**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPF process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To facilitate network management, configure dynamic hostnames to identify routers. After you run the **hostname** command to configure a dynamic hostname for a device, the device generates a router information (RI) Opaque LSA.After a device receives a RI Opaque LSA, you can run the **display ospf hostname-table** command on the router to check the mapping between the router ID and the dynamic hostname.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about OSPF dynamic hostnames.
```
<HUAWEI> display ospf hostname-table
OSPF Process 1 with Router ID 10.3.3.3
                Hostname table information

                Area: 0.0.0.1

 Router ID            Hostname
 10.3.3.3             RTR_BLR
 10.1.1.1             RTR_SHANGHAI
 255.255.255.254      RTR_BJI

                Area: 0.0.0.2

 Router ID            Hostname
 10.3.3.3             RTR_BLR
 10.30.1.1            RTR_DELHI

                AS-Scope

 Router ID            Hostname
 10.20.1.1            RTR_SHENZHEN
 255.255.255.254      RTR_BJI

```

**Table 1** Description of the **display ospf hostname-table** command output
| Item | Description |
| --- | --- |
| Router ID | Router ID. |
| Hostname | OSPF hostname. |
| Area | Area ID. |
| Scope | Flooding scope.  -Area OSPF area range (divided based on the area ID).  -AS-Scope: OSPF autonomous system (AS) scope. |
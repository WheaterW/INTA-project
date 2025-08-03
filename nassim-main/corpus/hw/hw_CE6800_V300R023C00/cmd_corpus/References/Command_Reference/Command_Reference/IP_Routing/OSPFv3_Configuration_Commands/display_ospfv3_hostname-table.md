display ospfv3 hostname-table
=============================

display ospfv3 hostname-table

Function
--------



The **display ospfv3 hostname-table** command displays information about OSPFv3 dynamic hostnames.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **hostname-table**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of an OSPFv3 process. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To facilitate network management, configure dynamic hostnames to identify routers. After you run the **hostname** command to configure a dynamic hostname for a router. You can run the **display ospfv3 hostname-table** command on the router to check the mapping between the router ID and the dynamic hostname.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about OSPFv3 dynamic hostnames.
```
<HUAWEI> display ospfv3 hostname-table
OSPFv3 Process 1 with Router ID 10.3.3.3
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

**Table 1** Description of the **display ospfv3 hostname-table** command output
| Item | Description |
| --- | --- |
| Router ID | Router ID. |
| Hostname | OSPFv3 hostname. |
| AS-Scope | Flooded hostname in the OSPFv3 AS. |
| Area | Flooded OSPFv3 hostname in the area. |
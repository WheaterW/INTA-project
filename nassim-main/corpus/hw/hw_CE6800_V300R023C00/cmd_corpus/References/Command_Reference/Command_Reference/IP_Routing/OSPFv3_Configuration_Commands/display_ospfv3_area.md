display ospfv3 area
===================

display ospfv3 area

Function
--------



The **display ospfv3 area** command displays OSPFv3 area information.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ospfv3** [ *process-id* ] **area** [ *area-id* | *area-idIpv4* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Displays information about the ABR or ASBR of an OSPFv3 route in a specified OSPFv3 process. | The value is an integer ranging from 1 to 4294967295. |
| **area** *area-id* | Displays information about the virtual node in a specified OSPF area. | The value can be a decimal integer or an IP address. When the value is an integer, the value ranges from 0 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If no process ID is specified, the brief information of all OSPFv3 processes is displayed in the ascending order of the process ID.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display OSPFv3 area information.
```
<HUAWEI> display ospfv3 area
OSPFv3 Process (1)
 Area BACKBONE(0) Status: down
       Number of interfaces in this area is 0
       SPF algorithm executed 0 times
       Number of LSA 0. Checksum Sum 0x0000
       Number of Unknown LSA 0
       Area Bdr Router count: 0
       Area ASBdr Router count: 0
       Authentication : HMAC-SHA256
       Router ID conflict state: Normal
       Next SPF Trigger Time 0 millisecs
 Area 0.0.0.2(NSSA)  InActive
       Number of interfaces in this area is 0
       SPF algorithm executed 0 times
       Number of LSA 0.  Checksum Sum 0x0
       Number of Unknown LSA 0
       Area Bdr Router count: 0
       Area ASBdr Router count: 0
       Router ID conflict state: Normal
       Next SPF Trigger Time 0 millisecs
       Import routes limitation is enabled
         Self NSSA LSA count: 0
         Current status: Normal

```

**Table 1** Description of the **display ospfv3 area** command output
| Item | Description |
| --- | --- |
| Area BACKBONE(0) Status | Area status.   * up: OSPFv3 is active in this area. * down: OSPFv3 is inactive in this area. |
| Area Bdr Router count | Number of Area Border Routers (ABRs) in the area. |
| Area ASBdr Router count | Number of AS Boundary Routers (ASBRs) in the area. |
| Number of interfaces in this area | Number of interfaces in an area. |
| Number of LSA | Number of Link State Advertisements (LSAs) in this area. |
| Number of Unknown LSA | Number of unknown LSAs in the area. |
| SPF algorithm executed | Number of Shortest Path First (SPF) calculations. |
| Checksum | Area checksum. |
| Router ID conflict state | Router ID conflict state.   * Normal: No router ID conflicts exist. * Wait select: A new router ID is to be selected. * Selecting: A new router ID is being selected. * RtrId Changed: The router ID has been changed. * Suspend: Automatic recovery from the OSPF router ID conflict is suspended because of a process reset. * NA: The state is not reported. |
| Authentication | HMAC-SHA256 authentication mode which can be configured using the authentication-mode (OSPFv3) command. |
| Next SPF Trigger Time | Delay in SPT calculation after the topology changes. |
| Import routes limitation | Whether a limit is configured on the number of LSAs generated when an OSPFv3 process imports external routes. |
| Self NSSA LSA count | Number of existing NSSA LSAs.  This field is displayed only in an OSPFv3 process. |
| Current status | A limit has been configured on the number of LSAs generated when an OSPFv3 process imports external routes. The current status can be as follows:   * Normal: The number of LSAs generated when an OSPFv3 process imports external routes is less than or equal to the lower alarm threshold (in percentage) multiplied by the maximum number allowed. * Approach limit: The number of LSAs generated when an OSPFv3 process imports external routes is approaching (reaching or exceeding 90% of) the upper alarm threshold. * Exceed limit: The number of LSAs generated when an OSPFv3 process imports external routes has reached or exceeded the maximum number allowed.   To configure the upper and lower alarm thresholds, run the import-route limit command. |
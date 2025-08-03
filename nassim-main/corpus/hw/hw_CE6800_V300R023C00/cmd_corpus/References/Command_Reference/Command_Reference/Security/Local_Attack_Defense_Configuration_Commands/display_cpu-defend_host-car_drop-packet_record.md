display cpu-defend host-car drop-packet record
==============================================

display cpu-defend host-car drop-packet record

Function
--------



The **display cpu-defend host-car drop-packet record** command displays records of packet loss caused by user-level rate limiting.




Format
------

**display cpu-defend host-car drop-packet record** [ **car-id** *car-id* ] [ **slot** *slot-id* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **car-id** *car-id* | Specifies a bucket. | The value is an integer that ranges from 0 to 8191. |
| **slot** *slot-id* | Specifies the slot ID. | The value must be set according to the device configuration. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After user-level rate limiting is configured and packet loss monitoring is enabled for user-level rate limiting, you can run this command to check information about packet loss caused by user-level rate limiting.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display packet loss records caused by user-level rate limiting.
```
<HUAWEI> display cpu-defend host-car drop-packet record
Hostcar drop packet record on Slot 1:
-------------------------------------------------------------------------------
MAC Address    CarID Packet Type      Count      LastCount  Last-dropping-time
-------------------------------------------------------------------------------
00e0-fc12-3456 3170  arp              23445      23445      2021-06-19 22:57:56
-------------------------------------------------------------------------------
Total: 1

```

**Table 1** Description of the **display cpu-defend host-car drop-packet record** command output
| Item | Description |
| --- | --- |
| MAC Address | Source MAC address of packets. |
| CarID | Bucket ID. |
| Packet Type | Protocol type of packets. |
| Count | Total number of discarded packets. |
| LastCount | Number of packets discarded in the last statistical period. |
| Last-dropping-time | Time when the last discarded packet was sent to the CPU. |
| Total | Number of packets discarded due to user-level rate limiting. |
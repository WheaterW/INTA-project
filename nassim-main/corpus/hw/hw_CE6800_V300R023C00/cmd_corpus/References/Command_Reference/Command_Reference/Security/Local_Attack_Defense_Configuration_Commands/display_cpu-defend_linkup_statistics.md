display cpu-defend linkup statistics
====================================

display cpu-defend linkup statistics

Function
--------



The **display cpu-defend linkup statistics** command displays statistics on packets sent to the CPU.




Format
------

**display cpu-defend linkup statistics** [ **packet-type** *packet-type* ] **slot** *slot-id*

**display cpu-defend linkup statistics** [ **packet-type** *packet-type* ] **all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **packet-type** *packet-type* | Displays the configuration of rate limiting for packets of a specified type. | For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ: The options are as follows:   * bgp * bgp4plus * ftp * isis * m-lag * m-lag-sync * ospf * ospfv3 * ssh * telnet * tftp  For the CE6885-LL (low latency mode): The options are as follows:   * bgp * ftp * isis * m-lag * m-lag-sync * ospf * ssh * telnet * tftp |
| **slot** *slot-id* | Displays the configuration of protocol association sessions in a specified slot. | The value must be set according to the device configuration. |
| **all** | Indicates all boards. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The display cpu-defend linkup configuration command displays statistics on packets sent to the CPU, including the number of forwarded and discarded packets.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the linkup statistics of all devices.
```
<HUAWEI> display cpu-defend linkup statistics packet-type telnet all
Linkup statistics(packets) on slot 1 :
--------------------------------------------------------------------------------
PacketType               Total Passed        Total Dropped   Last Dropping Time
                    Last 5 Min Passed   Last 5 Min Dropped
--------------------------------------------------------------------------------
telnet                              0                    0   -
                                    0                    0
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display cpu-defend linkup statistics** command output
| Item | Description |
| --- | --- |
| Linkup statistics(packets) on slot 1 | Linkup statistics on the device. |
| PacketType | Packet type. |
| Total Passed | Total number of forwarded packets. |
| Total Dropped | Total number of discarded packets. |
| Last 5 Min Passed | Number of packets forwarded in the last 5 minutes. |
| Last 5 Min Dropped | Number of packets discarded in the last 5 minutes. |
| Last Dropping Time | Last packet discarding time. |
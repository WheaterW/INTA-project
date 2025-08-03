display ip statistics
=====================

display ip statistics

Function
--------

The **display ip statistics** command displays IP packet statistics.



Format
------

**display ip statistics**

**display ip statistics interface** { *interface-name* | *interface-type* *interface-number* }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Displays statistics about IP packets on a specified interface name. | - |
| **interface** *interface-type* *interface-number* | Displays statistics about IP packets on a specified interface type and number. | - |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

To check statistics about IP packets, including sent, received, fragmented, and reassembled packets, run the display ip statistics command. The received packets displayed also include the packets carrying the Source Route options that are received and then discarded.

**Precautions**

If the "bad protocol" and "no route" field values displayed are large, the local device receives a large number of packets of unknown protocols and IP packets for which no routes can be found. In this case, check whether the local device is attacked by the connected device.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display IP packet statistics.
```
<HUAWEI> display ip statistics
------------------------ Display IP Statistics ----------------------
Received packets:
        Sum:                    27477      Local:                 0         
        Bad Protocol:           19602      Bad Format:            0         
        Bad Checksum:           0          Bad Options:           0         
        Discard SRR:            0          Discard RR:            0         
        Discard RA:             0          Discard TS:            0         
        TTL Exceeded:           0          Fragment Input:        0         
        Fragment Dropped:       0          Couldn't Fragment:     0         
        Reassembling:           0          Reassembling Timeouts: 0         
Sent packets:
        Forwarding:             0          Local:                 0         
        Dropped:                0          No Route:              0         
        Fragment output:        0          Fragmented:            0         
---------------------------------------------------------------------

```


**Table 1** Description of the
**display ip statistics** command output

| Item | Description |
| --- | --- |
| TTL Exceeded | Number of packets discarded due to TTL timeouts. |
| Received packets | Received packet statistics. |
| Bad Protocol | Number of received IP packets of unknown protocol types. The protocol field in the IP header cannot be identified by the upper-layer protocol. |
| Bad Format | Number of packets with incorrect formats. |
| Bad Checksum | Number of packets with incorrect checksums. |
| Bad Options | Number of packets with incorrect options. |
| Discard SRR | Number of packets discarded carrying Source Route options. |
| Discard RR | Number of packets discarded carrying the Record Route option. |
| Discard RA | Number of packets discarded carrying the Router Alert option. |
| Discard TS | Number of packets discarded carrying the timestamp option. |
| Fragment Input | Number of received fragmented packets. |
| Fragment Dropped | Number of discarded fragmented packets. |
| Fragment output | Number of sent fragmented packets. |
| Couldn't Fragment | Number of packets incapable of fragmentation. |
| Reassembling | Reassembled packet statistics. |
| Reassembling Timeouts | Number of fragmented packets that fail to be reassembled due to timeouts. |
| Sent packets | Sent packet statistics. |
| No Route | Number of packets for which no correct route can be found, including the packets sent and forwarded by the local device. |
| Sum | Total number of received packets. |
| Local | Number of packets sent to the upper-layer protocol. |
| Forwarding | Number of forwarded packets. |
| Dropped | Number of discarded packets. |
| Fragmented | Number of successfully fragmented packets. |
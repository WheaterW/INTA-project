display rawlink statistics
==========================

display rawlink statistics

Function
--------

The **display rawlink statistics** command displays RawLink packet statistics.



Format
------

**display rawlink statistics**



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

**Usage Scenario**

To check statistics about RawLink packets, include the number of sent and received RawLink packets, run the display rawlink statistics command.

IS-IS packets are encapsulated into RawLink packets during transmission. If IS-IS packets are abnormally sent, run the display rawlink statistics command to check the numbers of RawLink packets sent and received by the local device to see if the network abnormality is caused by abnormal sending and receiving of RawLink packets.

**Precautions**

The number of packets received by the Router includes the number of forwarded packets, packets sent to the upper layer, and discarded packets.



Example
-------

![](../public_sys-resources/note_3.0-en-us.png)
 

The actual command output varies according to the device. The command output here is only an example.



# Display RawLink packet statistics.
```
<HUAWEI> display rawlink statistics
Received packets:
    Total: 10
    Input packets missing pcb cache: 0
Sent packets:
    Total: 13

```


**Table 1** Description of the
**display rawlink statistics** command output

| Item | Description |
| --- | --- |
| Received packets | Received packet statistics. |
| Input packets missing pcb cache | Number of packets discarded because no corresponding Protocol Control Block (PCB) exists. |
| Sent packets | Number of sending packets. |
| Total | Total number of received/sent packets. |
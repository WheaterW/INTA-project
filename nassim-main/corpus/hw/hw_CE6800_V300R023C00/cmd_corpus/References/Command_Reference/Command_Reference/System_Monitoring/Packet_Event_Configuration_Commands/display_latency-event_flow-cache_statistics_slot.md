display latency-event flow-cache statistics slot
================================================

display latency-event flow-cache statistics slot

Function
--------



The **display latency-event flow-cache statistics slot** command is used to display the flow table statistics of latency event.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display latency-event flow-cache statistics slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *slot-id* | Slot ID. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can use the display latency-event flow-cache statistics slot command to view the detailed statistics of the flow table of latency event on the device in real time.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics of built-in CPU flow table for latency event.
```
<HUAWEI> display latency-event flow-cache statistics slot 1
Slot: 1
--------------------------------------------------------------------------------
Type             Current          Aged       Created      Exported     Exported 
                (Streams)       (Streams)   (Streams)     (Streams)    (Packets)
--------------------------------------------------------------------------------
V4                     0             0             0             0             0
--------------------------------------------------------------------------------
V6                     0             0             0             0             0
--------------------------------------------------------------------------------
VXLAN I4O6             0             0             0             0             0
--------------------------------------------------------------------------------
VXLAN I6O4             0             0             0             0             0
--------------------------------------------------------------------------------
Packet Type:
    V4:Ethernet packets, common IPv4 packets, and VXLAN packets with inner 
	    and outer IPv4 packets.
    V6:Common IPv6 packets and VXLAN packets with inner and outer IPv6 packets.
    VXLAN I4O6:VXLAN packets with inner IPv4 packets and outer IPv6 packets.
    VXLAN I6O4:VXLAN packets with inner IPv6 packets and outer IPv4 packets.

```

**Table 1** Description of the **display latency-event flow-cache statistics slot** command output
| Item | Description |
| --- | --- |
| Type | Flow type. |
| Current | Number of active flows. |
| Aged | Number of aged flows. |
| Created | Number of aged flows. |
| Exported (packets) | Number of packets sent to the TDA. |
| Exported(streams) | Number of flows sent to the TDA. |
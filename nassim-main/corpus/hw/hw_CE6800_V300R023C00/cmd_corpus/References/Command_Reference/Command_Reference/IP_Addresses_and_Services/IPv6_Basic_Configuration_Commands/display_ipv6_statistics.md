display ipv6 statistics
=======================

display ipv6 statistics

Function
--------



The **display ipv6 statistics** command displays IPv6 traffic statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 statistics** [ **interface** *interface-name* | **interface** *interface-type* *interface-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **interface** *interface-type* *interface-number* | Displays IPv6 traffic statistics on the interface with a specified type and number. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view statistics about the sent and received IPv6 packets, run the display ipv6 statistics command.

During transmission of IPv6 packets, when the source end implements fragmentation on IPv6 packets, run the display ipv6 statistics command to view the number of successfully fragmented IPv6 packets and the total number of sent fragmented packets. On the destination end, this command also displays whether the number of received fragmented packets is correct. The incorrect packets are discarded and the number of discarded packets is increased correspondingly.



**Precautions**

The packets received by a router include the forwarded packets, the packets transmitted to the upper layer, and the discarded packets.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display IPv6 traffic statistics on a router.
```
<HUAWEI> display ipv6 statistics
  Sent packets:
    Total                : 16         
    Local sent out       : 16           Forwarded            : 0          
    Raw packets          : 16           Discarded            : 0          
    Fragmented           : 0            Fragments            : 0          
    Fragments failed     : 0            Multicast            : 0          
  Received packets:
    Total                : 576453       Local host           : 281268     
    Hop count exceeded   : 0            Header error         : 0           
    Too big              : 0            Routing failed       : 0          
    Address error        : 0            Protocol error       : 0          
    Truncated            : 0            Option error         : 0          
    Fragments            : 0            Reassembled          : 0          
    Reassembly timeout   : 0            Multicast            : 576453   
    Fragments error      : 1
    Extension header:
      Hop-by-hop options    : 284107       Mobility header        : 0         
      Destination options   : 0            Routing header         : 0         
      Fragment header       : 0            Authentication header  : 0         
      Encapsulation header  : 0            No header              : 0         
      TLV length error      : 0            Header length error    : 0         
      Unknown header type   : 0            Unknown TLV type       : 0
    filter:
      Hop-by-hop options    : 2            Fragment header        : 0         
      Destination options   : 0            Routing header         : 0         
      Authentication header : 0            Encapsulation header   : 0

```

**Table 1** Description of the **display ipv6 statistics** command output
| Item | Description |
| --- | --- |
| Sent packets | Statistics on sent packets. |
| Total | Total number of sent packets. |
| Total | Total number of received rackets. |
| Local sent out | Total number of locally sent packets. |
| Local host | Total number of packets received by the local host, including the packets with the unicast destination address set to the local address and the packets with the multicast destination address belonging to the same multicast group as the local address. Packets with incorrect IPv6 headers, the packet length shorter than 40 bytes, or the extension header length greater than the packet length are not counted. |
| Forwarded | Total number of forwarded packets. |
| Raw packets | Total number of packets sent through the raw socket, such as ping or tracert packets. |
| Discarded | Total number of discarded packets. |
| Fragmented | Total number of successfully fragmented IPv6 packets. |
| Fragments | Total number of sent fragments. |
| Fragments failed | Total number of IPv6 packets that fail to be fragmented. |
| Fragments | Total number of received fragments. |
| Fragments error | Total number of packets with incomplete first fragment headers. |
| Multicast | Total number of sent multicast packets. |
| Multicast | Total number of received multicast packets. |
| Received packets | Statistics on received packets. |
| Hop count exceeded | Total number of packets whose hops exceed the upper limit. |
| Header error | Total number of packets with incorrect header formats, including Address error and Truncated packets. |
| Header length error | Number of extension headers in which the length field is wrong. |
| Too big | Total number of received packets that fail to be forwarded because of excessive size. |
| Routing failed | Total number of packets that fail to be routed. |
| Routing header | Total number of Routing headers. |
| Address error | Total number of packets with an address error. |
| Protocol error | Total number of packets with a protocol error. |
| Truncated | Total number of packets discarded because the actual packet length is shorter than that specified in the packet length field. |
| Option error | Total number of packets with an option error. |
| Reassembled | Total number of successfully reassembled packets. |
| Reassembly timeout | Total number of packets that fail to be reassembled because of timeout. |
| Extension header | Statistics on extension headers of received packets. |
| Hop-by-hop options | Total number of Hop-by-Hop Options headers. |
| Mobility header | Total number of Mobility headers. |
| Destination options | Total number of Destination Options headers. |
| Fragment header | Packets with the Fragment header. |
| Authentication header | Packets with the Authentication header. |
| Encapsulation header | Packets with the Encapsulating Security Payload header. |
| No header | Total number of headers not followed by any upper-layer protocols. |
| TLV length error | Total number of extension headers in which the TLV Length field is wrong. |
| Unknown header type | Number of unknown extension header types. |
| Unknown TLV type | Number of unknown TLV types. |
| filter | Number of packets discarded based on the configured IPv6 extension header. |
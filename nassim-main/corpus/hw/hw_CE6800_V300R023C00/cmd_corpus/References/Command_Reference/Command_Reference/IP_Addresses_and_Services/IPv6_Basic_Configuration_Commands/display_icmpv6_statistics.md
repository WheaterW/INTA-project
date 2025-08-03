display icmpv6 statistics
=========================

display icmpv6 statistics

Function
--------



The **display icmpv6 statistics** command displays ICMPv6 traffic statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display icmpv6 statistics** [ **interface** *interface-name* | **interface** *interface-type* *interface-number* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-name* | Specifies the name of an interface. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |
| **interface** *interface-type* *interface-number* | Specifies the interface type and interface number. If this parameter is specified, ICMPv6 traffic statistics on the specified interface are displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

Through the output of the **display icmpv6 statistics** command displays the statistics about sent and received ICMPv6 error messages and four types of ICMPv6 messages in the neighbor discovery mechanism, including RS, RA, NS, and NA messages.In the ping IPv6 operation, you can run the **display icmpv6 statistics** command on the device and check whether the total number of sent and received messages on the device is correct based on the command output.

**Precautions**



The total number of messages received by the Router includes the number of messages forwarded by the Router, the number of messages delivered by the Router to the upper layer, and the number of messages discarded by the Router.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the statistics about ICMPv6 messages processed by the device.
```
<HUAWEI> display icmpv6 statistics
ICMPv6 protocol:
  Sent packets:
    Total              : 0            
    Unreached          : 0              Prohibited         : 0    
    Hop count exceeded : 0              Parameter problem  : 0    
    Too big            : 0              Echoed             : 0    
    Echo replied       : 0              Router solicit     : 0    
    Router advert      : 0              Neighbor solicit   : 2    
    Neighbor advert    : 0              Redirected         : 0    
    Rate limited       : 0            

  Received packets:
    Total              : 0              Format error       : 0    
    Checksum error     : 0              Too short          : 0    
    Bad code           : 0              Bad length         : 0    
    Unknown info type  : 0              Unknown error type : 0    
    Unreached          : 0              Prohibited         : 0    
    Hop count exceeded : 0              Parameter problem  : 0    
    Too big            : 0              Echoed             : 0    
    Echo replied       : 0              Router solicit     : 0    
    Router advert      : 0              Neighbor solicit   : 0    
    Neighbor advert    : 0              Redirected         : 0    
    Rate limited       : 0            
    Rejected Packets:
      Echoed               : 0            Echo replied         : 0
      Hop limit exceeded   : 0            Port unreachable     : 0
      Packet too big       : 0            Neighbor solicit     : 0
      Neighbor advert      : 0            Router solicit       : 0
      Router advert        : 0            Redirected           : 0
      Host unreachable     : 0            Network unreachable  : 0
      Frag time exceeded   : 0            Err header field     : 0
      Host admin prohib    : 0            Unknown ipv6 opt     : 0
      Unknown next header  : 0            Others               : 0
      Echoed multicast     : 0

```

**Table 1** Description of the **display icmpv6 statistics** command output
| Item | Description |
| --- | --- |
| ICMPv6 protocol | Statistics about ICMPv6 messages. |
| Sent packets | Statistics about the sent ICMPv6 messages. |
| Total | Total number of the sent or received ICMPv6 messages. |
| Unreached | Total number of sent or received ICMPv6 Destination Unreachable messages. |
| Prohibited | Total number of the sent or received ICMPv6 messages to notify that the destination is administratively prohibited. |
| Hop count exceeded | Total number of the sent or received ICMPv6 messages to notify that the hop limit is crossed. |
| Parameter problem | Total number of the sent or received ICMPv6 Parameter Problem messages. |
| Too big | Total number of the sent or received ICMPv6 Packet Too Big messages. |
| Too short | Total number of the received ICMPv6 messages notifying that the packet length is too short. |
| Echoed | Total number of the sent or received ICMPv6 Echo-Request messages. |
| Echoed multicast | Count of ICMPv6 packets discarded due to echo multicast switch shutdown. |
| Echo replied | Total number of the sent or received ICMPv6 Echo-Reply messages. |
| Router solicit | Total number of the sent or received Router Solicitation (RS) messages. |
| Router advert | Total number of the sent or received Router Advertisement (RA) messages. |
| Neighbor solicit | Total number of the sent or received Neighbor Solicitation (NS) messages. |
| Neighbor advert | Total number of the sent or received Neighbor Advertisement (NA) messages. |
| Redirected | Total number of the sent or received ICMPv6 Redirection messages. |
| Rate limited | Total number of the ICMPv6 packets that fail to be sent or received because of rate limit. |
| Received packets | Statistics about the received ICMPv6 messages. |
| Format error | Total number of the received ICMPv6 messages notifying format errors. |
| Checksum error | Total number of the received ICMPv6 messages notifying checksum errors. |
| Bad code | Total number of the received ICMPv6 messages notifying code errors. |
| Bad length | Total number of the received ICMPv6 messages notifying packet length errors. |
| Unknown info type | Total number of the received ICMPv6 messages notifying that the packet is with an unrecognized information type. |
| port unreachable | Statistics about discarded ICMPv6 unreachable packets. |
| hop limit exceeded | Statistics about ICMPv6 hop limit exceeded messages. |
| unknown next header | Statistics about unknown next header messages. |
| others | Statistics about others messages. |
| network unreachable | Statistics about network unreachable messages. |
| host unreachable | Statistics about host unreachable messages. |
| rejected packets | Statistics about rejected packets messages. |
| unknown error type | Statistics about unknown error type messages. |
| packet too big | Statistics about discarded ICMPv6 oversized packets. |
| host admin prohib | Statistics about discarded ICMPv6 host administratively prohibited messages. |
| unknown ipv6 opt | Statistics about discarded ICMPv6 packets with unknown options. |
| err header field | Statistics on header fields of discarded ICMPv6 error packets. |
| frag time exceeded | Statistics about frag time exceeded messages. |
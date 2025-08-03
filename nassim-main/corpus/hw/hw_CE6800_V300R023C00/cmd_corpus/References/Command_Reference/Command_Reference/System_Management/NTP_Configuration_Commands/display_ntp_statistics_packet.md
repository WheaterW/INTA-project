display ntp statistics packet
=============================

display ntp statistics packet

Function
--------

The **display ntp statistics packet** command displays statistics about global NTP packets.



Format
------

**display ntp statistics packet** [ **ipv6** ]

**display ntp statistics packet** [ **ipv6** ] **interface** { *ifname* | *interface\_type* *interface\_num* | **all** }

**display ntp statistics packet peer** [ [ *ipv4Addr* [ **vpn-instance** *vpnName* ] ] | **ipv6** [ *ipv6Addr* [ **vpn-instance** *vpnName* ] ] | **domain** [ *domainName* [ **vpn-instance** *vpnName* ] ] ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ipv6** *ipv6Addr* | Displays NTP packet statistics on a specified IPv6 peer. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **ipv6** | IPv6 peer packet statistics. | - |
| **interface** *interface\_type* | Specifies an interface type. | - |
| **interface** *interface\_num* | Specifies an interface number. | - |
| **interface** *ifname* | Specifies an interface name. | - |
| **all** | Indicates all interfaces. | - |
| **peer** | Displays NTP packet statistics on a specified IPv4 peer. | - |
| *ipv4Addr* | Displays NTP packet statistics on a specified IPv4 peer. | The value is an IPv4 address in dotted decimal notation. |
| **vpn-instance** *vpnName* | Specifies the name of a VPN instance associated with the NTP peer. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |
| **domain** *domainName* | Specifies a domain name. | The value is a string of 1 to 255 case-sensitive characters. It cannot contain spaces. |




Views
-----

All views



Default Level
-------------

1: Monitoring level



Usage Guidelines
----------------

**Usage Scenario**

The following information is displayed, which is important for NTP debugging:

* Number of NTP packets received from the remote peer
* Number of NTP packets sent to the remote peer
* Number of processed NTP packets
* Number of discarded NTP packets


Example
-------

# Display statistics about global NTP packets.
```
<HUAWEI> display ntp statistics packet
 NTP IPv4 Packet Statistical Information
 --------------------------------------------------
 Sent                                  :          100
    Send failures                      :          10
 Received                              :          1000
    Processed                          :          800
    Dropped                            :          200
       Validity test failures          :          50
          Authentication failures      :          20
       Invalid packets                 :          50
       Access denied                   :          50
       Rate-limited                    :          0
       Processing delay                :          30
       Interface disabled              :          0
       Max dynamic association reached :          0
       Server disabled                 :          0
       Offset limit                    :          0
       Others                          :          0
Last 2 packets drop reasons:

```


**Table 1** Description of the
**display ntp statistics packet** command output

| Item | Description |
| --- | --- |
| NTP IPv4 Packet Statistical Information | Statistics about NTP IPv4 packets. |
| Sent | Number of packets sent. |
| Send failures | Number of times packet sending failed. |
| Received | Number of packets received. |
| Processed | Number of packets processed. |
| Dropped | Number of packets dropped. |
| Validity test failures | Number of packets dropped due to NTP validity test failures. |
| Authentication failures | Number of packets dropped due to authentication failures. |
| Invalid packets | Number of packets dropped due to invalid packets. |
| Access denied | Number of packets dropped due to denial of access. |
| Rate-limited | Number of packets dropped due to rate limit. |
| Processing delay | Number of packets dropped due to processing delay. |
| Interface disabled | Number of packets dropped as the interface is disabled. |
| Max dynamic association reached | Number of packets dropped as the maximum number of dynamic associations is reached. |
| Server disabled | Number of packets dropped as server disabled. |
| Offset limit | Indicates the number of packets discarded because the time offset between the clock source and the client is greater than the threshold. |
| Others | Number of packets dropped due to other reasons. |
| Last 2 packets drop reasons | Reason for dropping the last n packets, where the maximum value of n can be 10. |
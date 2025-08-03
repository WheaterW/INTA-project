display dhcp statistics
=======================

display dhcp statistics

Function
--------



The **display dhcp statistics** command displays DHCP message statistics.




Format
------

**display dhcp statistics**


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

The **display dhcp statistics** command displays statistics about sent and received DHCP messages.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display DHCP message statistics.
```
<HUAWEI> display dhcp statistics
Input: total 172 packets, discarded 0 packets                                   
  Bootp request           :          0,  Bootp reply             :          0   
  Discover                :          0,  Offer                   :        172   
  Request                 :          0,  Ack                     :          0   
  Release                 :          0,  Nak                     :          0   
  Decline                 :          0,  Inform                  :          0   
                                                                                
  Rx buffers full         :       2978,  L2fdb lookup failed     :         38 
                                                                                
Output: total 172 packets, discarded 0 packets

```

**Table 1** Description of the **display dhcp statistics** command output
| Item | Description |
| --- | --- |
| Bootp request | Number of BOOTP requests sent by the device that functions as the client. |
| Bootp reply | Number of BOOTP replies received by the client from the server. |
| Discover | Number of Discover messages received by the server from the client. |
| Offer | Number of Offer messages received by the client from the server. |
| Request | Number of BOOTP requests received by the server from the client. |
| Ack | Number of ACK messages received by the client from the server. |
| Release | Number of Release messages received by the server from the client. |
| Nak | Number of NAK messages received by the client from the server. |
| Decline | Number of Decline messages sent by the client. |
| Inform | Number of Inform messages sent by the client. |
| Rx buffers full or L2fdb lookup failed | Information displayed when the DHCP service is abnormal. The displayed information includes:   * Rx buffers full: Total number of DHCP packets discarded because the remaining queue length is shorter than the reserved threshold. * L2fdb lookup failed: Total number of DHCP packets discarded because entries fail to be queried. * High cpu occupancy: Total number of DHCP packets discarded because the CPU usage is excessively high. * Port blocked: Total number of DHCP packets discarded because the inbound interface is blocked. * Bad vlan id: Total number of DHCP packets discarded because the VLAN ID is incorrect. * Memory exhausted: Total number of DHCP packets discarded because the memory is exhausted. * L3if protocol down: Total number of DHCP packets discarded because the Layer 3 protocol of the source interface goes Down. * Rate limit: Total number of DHCP packets discarded because rates of the packets exceed the limit. * Bad packet length: Total number of DHCP packets discarded because the packet length is incorrect. * Bad ip header length: Total number of DHCP packets discarded because the IP header length is incorrect. * Bad ip header checksum: Total number of DHCP packets discarded because the checksum of the IP header is incorrect. * Bad udp checksum: Total number of DHCP packets discarded because the checksum of the UDP header is incorrect. * Hops exceeded: Total number of DHCP packets discarded because the number of next hops is incorrect. * Bad magic cookie: Total number of DHCP packets discarded because the magic-cookie field is incorrect. * Duplicate option: Total number of DHCP packets discarded because the option fields are duplicate. * Bad option length: Total number of DHCP packets discarded because the option field length is incorrect. * End option absent: Total number of DHCP packets discarded because of the incorrect end option. * Dest-port equals source: Total number of DHCP packets discarded because the source interface is also the outbound interface. * Bad chaddr: Total number of DHCP packets discarded because the MAC address of the client is incorrect. * Bad giaddr: Total number of DHCP packets discarded because the relay gateway is incorrect. * Bad request: Total number of DHCP packets discarded because the request packets are incorrect. * Bad reply: Total number of DHCP packets discarded because the response packets are incorrect. * Bad dest udp-port: Total number of DHCP packets discarded because the destination interface is incorrect. * Bad message type: Total number of DHCP packets discarded because of incorrect destination interfaces. * L2fdb lookup failed: Total number of incoming DHCP packets discarded because entries fail to be queried. * Max-user limit: Total number of DHCP packets discarded because the maximum number of users is exceeded. * Add bindtable failed: Total number of DHCP packets discarded because dynamic binding entries are added. * Client transfered: Total number of DHCP packets discarded due to interface flapping. * Bad original interface: Total number of DHCP packets discarded because dynamic binding entries are added. * Bad client-id: Total number of DHCP packets discarded because the client ID is incorrect. * Bad server-id: Total number of DHCP packets discarded because the server ID is incorrect. * Bad dest-ip: Total number of DHCP packets discarded because the destination IP address is incorrect. * Other error: Total number of DHCP packets discarded due to other reasons. |
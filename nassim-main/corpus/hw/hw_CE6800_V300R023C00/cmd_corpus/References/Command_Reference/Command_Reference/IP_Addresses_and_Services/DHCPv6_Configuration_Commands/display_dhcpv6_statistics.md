display dhcpv6 statistics
=========================

display dhcpv6 statistics

Function
--------



The **display dhcpv6 statistics** command displays DHCPv6 packet statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display dhcpv6 statistics**


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

The device may become faulty when running the DHCPv6 service. Some fault location methods are required for administrators or device maintenance personnel to locate faults quickly. The most convenient and effective method is to provide statistics about packets and packet loss reasons. Run the **display dhcpv6 statistics** command to view DHCPv6 packet statistics.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display DHCPv6 packet statistics.
```
<HUAWEI> display dhcpv6 statistics
Input: total 10 packets, discarded 0 packets                                     
  Solicit                 :         10,  Advertise               :          0   
  Request                 :          0,  Confirm                 :          0   
  Renew                   :          0,  Rebind                  :          0   
  Reply                   :          0,  Release                 :          0   
  Decline                 :          0,  Reconfigure             :          0   
  Information-request     :          0,  Relay-forward           :          0   
  Relay-reply             :          0,  Leasequery              :          0   
  Leasequery-reply        :          0,                                         
                                                                                
  Max-user limit          :        831,  Add bindtable failed    :          100
Output: total 0 packets, discarded 0 packets

```

**Table 1** Description of the **display dhcpv6 statistics** command output
| Item | Description |
| --- | --- |
| Input: total x packets, discarded y packets | Statistics about DHCPv6 packets received by the device. The number of received DHCPv6 packets is x and the number of discarded DHCPv6 packets is y. |
| Solicit | Number of SOLICIT packets received by the device. |
| Advertise | Number of ADVERTISE packets received by the device. |
| Request | Number of REQUEST packets received by the device. |
| Confirm | Number of CONFIRM packets received by the device. |
| Renew | Number of RENEW packets received by the device. |
| Rebind | Number of REBIND packets received by the device. |
| Reply | Number of REPLY packets received by the device. |
| Release | Number of RELEASE packets received by the device. |
| Decline | Number of DECLINE packets received by the device. |
| Reconfigure | Number of RECONFIGURE packets received by the device. |
| Information-request | Number of INFORMATION-REQUEST packets received by the device. |
| Relay-forward | Number of RELAY-FORWARD packets received by the device. |
| Relay-reply | Number of RELAY-REPLY packets received by the device. |
| Leasequery | Number of LEASEQUERY packets received by the device. |
| Leasequery-reply | Number of LEASEQUERY-REPLY packets received by the device. |
| Max-user limit or Add bindtable failed | * Information displayed if the DHCPv6 service is abnormal. The displayed information includes: * Max-user limit: Total number of DHCP packets discarded because the maximum number of users is exceeded. * Add bindtable failed: Total number of DHCP packets discarded because dynamic binding entries fail to be added. * High cpu occupancy: Total number of DHCP packets discarded because the CPU usage is excessively high. * Port blocked: Total number of DHCP packets discarded because the inbound interface is blocked. * Rx buffers full: Total number of DHCP packets discarded because the remaining queue length is shorter than the reserved threshold. * L2fdb lookup failed: Total number of DHCP packets discarded because entries fail to be queried. * Bad vlan id: Total number of DHCP packets discarded because the VLAN ID is incorrect. * Memory exhausted: Total number of DHCP packets discarded because the memory is exhausted. * L3if protocol down: Total number of DHCP packets discarded because the Layer 3 protocol of the source interface goes Down. * Rate limit: Total number of DHCP packets discarded because rates of the packets exceed the limit. * Bad packet length: Total number of DHCP packets discarded because the packet length is incorrect. * Bad ip header length: Total number of DHCP packets discarded because the IP header length is incorrect. * Bad ip header checksum: Total number of DHCP packets discarded because the checksum of the IP header is incorrect. * Bad udp checksum: Total number of DHCP packets discarded because the checksum of the UDP header is incorrect. * Hops exceeded: Total number of DHCP packets discarded because the number of next hops is incorrect. * Bad magic cookie: Total number of DHCP packets discarded because the magic-cookie field is incorrect. * Duplicate option: Total number of DHCP packets discarded because the option fields are duplicate. * Bad option length: Total number of DHCP packets discarded because the option field length is incorrect. * End option absent: Total number of DHCP packets discarded because of the incorrect end option. * Dest-port equals source: Total number of DHCP packets discarded because the source interface is also the outbound interface. * Bad chaddr: Total number of DHCP packets discarded because the MAC address of the client is incorrect. * Bad giaddr: Total number of DHCP packets discarded because the relay gateway is incorrect. * Bad request: Total number of DHCP packets discarded because the request packets are incorrect. * Bad reply: Total number of DHCP packets discarded because the response packets are incorrect. * Bad dest udp-port: Total number of DHCP packets discarded because the destination interface is incorrect. * Bad message type: Total number of DHCP packets discarded because of incorrect destination interfaces. * L2fdb lookup failed: Total number of incoming DHCP packets discarded because entries fail to be queried. * Client transferred: Total number of DHCP packets discarded due to interface flapping. * Bad original interface: Total number of DHCP packets discarded because dynamic binding entries are added. * Bad client-id: Total number of DHCP packets discarded because the client ID is incorrect. * Bad server-id: Total number of DHCP packets discarded because the server ID is incorrect. * Bad dest-ip: Total number of DHCP packets discarded because the destination IP address is incorrect. * Other error: Total number of DHCP packets discarded due to other reasons. |
| Output: total x packets, discarded y packets | Statistics about DHCPv6 packets sent by the device. The number of sent DHCPv6 packets is x and the number of discarded DHCPv6 packets is y. |
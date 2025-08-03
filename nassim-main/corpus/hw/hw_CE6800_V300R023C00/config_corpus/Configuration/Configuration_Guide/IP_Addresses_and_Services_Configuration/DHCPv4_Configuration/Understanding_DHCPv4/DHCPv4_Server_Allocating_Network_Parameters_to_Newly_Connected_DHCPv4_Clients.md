DHCPv4 Server Allocating Network Parameters to Newly Connected DHCPv4 Clients
=============================================================================

As shown in [Figure 1](#EN-US_CONCEPT_0000001512846590__fig2660191813218), when no DHCPv4 relay agent is deployed, the newly connected DHCPv4 client and server exchange DHCPv4 messages through four steps.

**Figure 1** Message exchange between the newly connected DHCPv4 client and server  
![](figure/en-us_image_0000001564126257.png)
#### Step 1: Discovery Stage

The newly connected DHCPv4 client does not know the IPv4 address of the DHCPv4 server. To learn the IPv4 address of the DHCPv4 server, the DHCPv4 client broadcasts a DHCPDISCOVER message with the destination IPv4 address of 255.255.255.255 to all devices on the same network segment, including the DHCPv4 server and relay agent (if possible). The DHCPDISCOVER message carries information, such as the client's MAC address ([chaddr field](galaxy_dhcpv4_cfg_0005.html#EN-US_CONCEPT_0000001564006389__c1)), requested parameter list option ([Option 55](galaxy_dhcpv4_cfg_0005.html#EN-US_CONCEPT_0000001564006389__op55)), and broadcast flag ([flags field](galaxy_dhcpv4_cfg_0005.html#EN-US_CONCEPT_0000001564006389__f1)).


#### Step 2: Offer Stage

All the DHCPv4 servers on the same network segment as the DHCPv4 client receive the DHCPDISCOVER message. Each DHCPv4 server selects an address pool on the same network segment as the IPv4 address of the interface receiving the DHCPDISCOVER message, and from the address pool allocates an idle IPv4 address. The DHCPv4 server then sends a DHCPOFFER message carrying the allocated IPv4 address to the DHCPv4 client.

In most cases, the leases of IPv4 addresses are specified in an address pool. If the DHCPDISCOVER message carries an expected lease, the DHCPv4 server compares the expected lease with the specified lease and allocates the IPv4 address with a smaller lease to the DHCPv4 client.

The DHCPv4 server allocates an IPv4 address from the address pool to a client in the following sequence:![](public_sys-resources/note_3.0-en-us.png) 

The IPv4 address allocation sequence cannot be modified.

1. IPv4 address statically bound to the MAC address of the client on the DHCPv4 server.
2. IPv4 address specified in [Option 50](galaxy_dhcpv4_cfg_0005.html#EN-US_CONCEPT_0000001564006389__op50) (requested IPv4 address) in the DHCPDISCOVER message.
3. IPv4 address in the Expired state in the address pool, that is, the IPv4 address that has been assigned to the client and whose lease has expired.
4. Random IPv4 address in the Idle state in the address pool.
5. If no IPv4 address is available for allocation, the DHCPv4 server automatically reclaims the expired and conflicting IPv4 addresses in sequence. If an available IPv4 address is found after the reclaim, the DHCPv4 server allocates the IPv4 address. If no IPv4 address is available, the DHCPv4 client resends a DHCPDISCOVER message to apply for an IPv4 address after waiting for a response times out.

DHCPv4 servers can exclude some IPv4 addresses that cannot be allocated through DHCPv4 from address pools. For example, if 192.168.1.100/24 has been manually configured for a DNS server, the DHCPv4 server excludes this IPv4 address from the address pool on network segment 192.168.1.0/24 so that it is not allocated through DHCPv4. This helps prevent IPv4 address conflicts.

To prevent the allocated IPv4 address from conflicting with the IPv4 addresses of other clients on the network, before sending a DHCPOFFER message, the DHCPv4 server sends an ICMP Echo request message with the source address being the IPv4 address of the DHCPv4 server and the destination address being the pre-allocated IPv4 address to detect conflicts for the allocated IPv4 address. If the DHCPv4 server receives no ICMP Echo reply message within the detection period, no client is using this IPv4 address, and the DHCPv4 server can allocate it. If the DHCPv4 server receives an ICMP Echo reply message within the detection period, this IPv4 address is being used by another client, and the DHCPv4 server lists this IPv4 address as a conflicting one. The DHCPv4 server then waits for the next DHCPDISCOVER message to start the IPv4 address selection process again.

The IPv4 address allocated in this stage may not be the final IPv4 address used by the client. This is because the IPv4 address can be allocated to another client if the DHCPv4 server receives no response 16 seconds after the DHCPOFFER message is sent. The IPv4 address for the client can be determined only after the request and acknowledgment stages.


#### Step 3: Request Stage

If multiple DHCPv4 servers reply with a DHCPOFFER message to the DHCPv4 client, the client accepts only the first received DHCPOFFER message. The client then broadcasts a DHCPREQUEST message carrying the selected DHCPv4 server identifier ([Option 54](galaxy_dhcpv4_cfg_0005.html#EN-US_CONCEPT_0000001564006389__op54)) and IPv4 address ([Option 50](galaxy_dhcpv4_cfg_0005.html#EN-US_CONCEPT_0000001564006389__op50), with the IPv4 address specified in the yiaddr field of the accepted DHCPOFFER message).

The DHCPv4 client broadcasts a DHCPREQUEST message to notify all the DHCPv4 servers that it has selected the IPv4 address offered by a DHCPv4 server. Then the other servers can allocate IPv4 addresses to other clients.

![](public_sys-resources/note_3.0-en-us.png) 

If a device functions as a DHCPv4 client and multiple DHCPv4 servers exist on the network, the DHCPv4 client polls the DHCPv4 servers according to the sequence of receiving DHCPOFFER messages. If a DHCPv4 server fails to assign an IPv4 address, the client selects the next DHCPv4 server.



#### Step 4: Acknowledgement Stage

After receiving the DHCPREQUEST message, the DHCPv4 server sends a DHCPACK message to the client, carrying the IPv4 address specified in [Option 50](galaxy_dhcpv4_cfg_0005.html#EN-US_CONCEPT_0000001564006389__op50) of the DHCPREQUEST message.

After receiving the DHCPACK message, the DHCPv4 client broadcasts gratuitous ARP packets to check whether any other terminal is using the IPv4 address allocated by the DHCPv4 server. If no response is received within the specified time, the DHCPv4 client can use the IPv4 address. If the DHCPv4 client receives a response within the specified time, this IPv4 address is being used by another terminal. The client then sends a DHCPDECLINE message to the DHCPv4 server and applies for a new IPv4 address. The DHCPv4 server lists this IPv4 address as a conflicting one. The DHCPv4 server allocates conflicting IPv4 addresses only when there is no idle IPv4 address in the address pool, minimizing IPv4 address conflicts.

Occasionally, the DHCPv4 server may fail to allocate the IPv4 address specified in [Option 50](galaxy_dhcpv4_cfg_0005.html#EN-US_CONCEPT_0000001564006389__op50) because, for example, an error occurs during negotiation or it takes a long time to receive the DHCPREQUEST message. In this case, the DHCPv4 server replies with a DHCPNAK message to notify the DHCPv4 client that the requested IPv4 address cannot be allocated. In this case, the DHCPv4 client has to send another DHCPDISCOVER message for a new application.
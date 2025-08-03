DHCPv6 Server Allocating Addresses and Network Configuration Parameters to Newly Connected DHCPv6 Clients
=========================================================================================================

This section describes how a DHCPv6 server allocates addresses and network configuration parameters to newly connected DHCPv6 clients (that is, those that connect to the network for the first time). If a DHCPv6 relay agent exists on the network, the working mechanism is different.

#### DHCPv6 Server Allocating Addresses and Network Configuration Parameters to Newly Connected DHCPv6 Clients When No DHCPv6 Relay Agent Exists

This scenario involves two allocation modes: DHCPv6 four-message exchange and DHCPv6 two-message exchange.

**DHCPv6 four-message exchange**

The DHCPv6 four-message exchange is used when multiple DHCPv6 servers exist on the network.

**Figure 1** DHCPv6 four-message exchange  
![](figure/en-us_image_0000001512691266.png)

1. Discovery stage: The DHCPv6 client discovers a DHCPv6 server and requests the server to allocate an IPv6 address and network configuration parameters.
   
   The DHCPv6 client sends a Solicit message to discover a DHCPv6 server and request the server to allocate an IPv6 address and network configuration parameters. Because the DHCPv6 client does not know the IPv6 addresses of DHCPv6 servers, it multicasts a Solicit message to all DHCPv6 servers on the same link. The Solicit message carries the client's DUID, IAID, requested non-temporary address, and requested network configuration parameters.
2. Offer stage: The DHCPv6 server offers an IPv6 address and network configuration parameters.
   
   The DHCPv6 server selects an idle IPv6 address from the address pool on the same network segment as the IPv6 address of the interface that receives the Solicit message. The server then unicasts an Advertise message carrying the allocated IPv6 address to the DHCPv6 client. The Advertise message carries the server's DUID, client's DUID, server's priority, IPv6 address and lease assigned to the client, and network configuration parameter list.
   
   The DHCPv6 server classifies IPv6 addresses in the address pool into different IPv6 address lists based on their states.
   
   * Places the unassigned IPv6 addresses in the list of assignable IPv6 addresses.
   * Places the assigned IPv6 addresses in the list of IPv6 addresses in use.
   * Places the conflicting IPv6 addresses in the list of conflicting IPv6 addresses.
   * Places the IPv6 addresses that cannot be assigned in the list of IPv6 addresses that cannot be assigned.The DHCPv6 server allocates an IPv6 address from the address pool to a client in the following sequence:
   1. IPv6 address statically bound to the DUID of the client on the DHCPv6 server.
   2. IPv6 address specified by the IA\_NA field in the Solicit message sent by the client.
   3. IPv6 address that has been allocated by the DHCPv6 server to the client.
   4. Latest available IPv6 address that is obtained by cyclic searching in ascending order of IPv6 addresses.
   5. If no available IPv6 address is obtained, the DHCPv6 server sends a Reply message indicating that no IPv6 address can be allocated to the client. The DHCPv6 client must then resend a Solicit message to apply for an IPv6 address again.
3. Request stage: The DHCPv6 client selects an IPv6 address.
   
   Because Solicit messages are multicast, all DHCPv6 servers on the same link reply with Advertise messages upon receipt of the Solicit messages. If multiple DHCPv6 servers send Advertise messages to the DHCPv6 client, the client selects the Advertise message with the highest server priority. If the DHCPv6 servers have the same priority, the client selects the Advertise message that carries the required configuration parameters. The client then multicasts a Request message to all DHCPv6 servers on the same link. The Request message contains the DUID of the DHCPv6 server selected by the client, DUID of the client, and IPv6 address of the client.
4. Acknowledgment stage: The DHCPv6 server acknowledges the IPv6 address offered to the client.
   
   After receiving the Request message, the DHCPv6 server checks the DUID of the DHCPv6 server carried in the message.
   * If the DUID carried in the message is not the local one, the DHCPv6 server does not respond to the Request message. Instead, it reclaims the requested IPv6 address in the Request message.
   * If the DUID carried in the message is the local one, the DHCPv6 server unicasts a Reply message to the client, acknowledging that the requested IPv6 address in the Request message is allocated to the client.

After receiving the Reply message, the DHCPv6 client sends DAD packets to check whether any other terminal is using the IPv6 address allocated by the server. If the client receives no response within the specified time, it can use the IPv6 address. If the client receives a response, it cannot use the IPv6 address because another terminal is already using it. In this case, the client unicasts a Decline message to the server and resends a Solicit message to request another IPv6 address. After receiving the Decline message, the server lists the IPv6 address carried in the message as a conflicting one.

**DHCPv6 two-message exchange**

The DHCPv6 two-message exchange is used when only one DHCPv6 server exists on the network. In the DHCPv6 two-message exchange, a DHCPv6 client receives only an IPv6 address allocated by a DHCPv6 server. This means that the offer and request stages, as used in the DHCPv6 four-message exchange, are not required in the DHCPv6 two-message exchange.

The DHCPv6 two-message exchange is used only when a Solicit message sent by the DHCPv6 client carries the Rapid Commit option (indicating that the client expects the server to quickly allocate addresses and network configuration parameters) and the DHCPv6 server supports fast address allocation. In other cases, the DHCPv6 four-message exchange is used.

**Figure 2** DHCPv6 two-message exchange  
![](figure/en-us_image_0000001513170406.png)

1. Discovery stage: The DHCPv6 client discovers a DHCPv6 server and requests the server to allocate an IPv6 address and network configuration parameters.
   
   The DHCPv6 client sends a Solicit message to discover a DHCPv6 server and request the server to allocate an IPv6 address and network configuration parameters. Because the DHCPv6 client does not know the IPv6 addresses of DHCPv6 servers, it multicasts a Solicit message to all DHCPv6 servers on the same link. The Solicit message carries the Rapid Commit option, the client's DUID, requested non-temporary address, and requested network configuration parameters.
2. Acknowledgment stage: The DHCPv6 server acknowledges the IPv6 address offered to the client.
   
   When the DHCPv6 server supports fast address allocation and receives a Solicit message carrying the Rapid Commit option, it selects an available IPv6 address from the address pool on the same network segment as the IPv6 address of the interface that receives the Solicit message. The server then unicasts a Reply message to the DHCPv6 client. The Reply message carries the Rapid Commit option, server's DUID, client's DUID, server's priority, IPv6 address and lease assigned to the client, and network configuration parameter list.

After receiving the Reply message, the DHCPv6 client sends DAD packets to check whether any other terminal is using the IPv6 address allocated by the server. If the client receives no response within the specified time, it can use the IPv6 address. If the client receives a response, it cannot use the IPv6 address because another terminal is already using it. In this case, the client unicasts a Decline message to the server and resends a Solicit message to request another IPv6 address. After receiving the Decline message, the server lists the IPv6 address carried in the message as a conflicting one.


#### DHCPv6 Server Allocating Addresses and Network Configuration Parameters to Newly Connected DHCPv6 Clients When a DHCPv6 Relay Agent Exists

This scenario also involves two allocation modes: DHCPv6 four-message exchange and DHCPv6 two-message exchange. The working principles of the two modes are the same as those in the scenario where no DHCPv6 relay agent exists. For details, see [DHCPv6 Server Allocating Addresses and Network Configuration Parameters to Newly Connected DHCPv6 Clients When No DHCPv6 Relay Agent Exists](#EN-US_CONCEPT_0000001563770737__section_norelay). The following describes how a DHCPv6 server allocates an address and network configuration parameters to newly connected clients in the DHCPv6 two-message exchange.

**Figure 3** DHCPv6 server allocating addresses and network configuration parameters to newly connected DHCPv6 clients when a DHCPv6 relay agent exists  
![](figure/en-us_image_0000001564010673.png)

1. The DHCPv6 client multicasts a Solicit message to all DHCPv6 relay agents on the same link to discover a DHCPv6 server and request the DHCPv6 server to allocate an IPv6 address and network configuration parameters.
2. A DHCPv6 relay agent processes messages in the following ways:
   * If the DHCPv6 relay agent and DHCPv6 client are on the same link (that is, the relay agent is the first-hop relay agent of the client), the relay agent encapsulates the Solicit message into the Relay Message option of a Relay-forward message, and unicasts the Relay-forward message to the DHCPv6 server or next-hop relay agent.
   * If the DHCPv6 relay agent and DHCPv6 client are on different links (that is, the relay agent receives a Relay-forward message from another relay agent), the relay agent encapsulates the received Relay-forward message into the Relay Message option of a newly created Relay-forward message. It then unicasts this new Relay-forward message to the DHCPv6 server or next-hop relay agent.
3. The DHCPv6 server parses the Relay-forward message to obtain the DHCPv6 client's request and selects an IPv6 address and other network configuration parameters to construct a reply message. The server then encapsulates the reply message in the Relay Message option in a Relay-reply message and unicasts the Relay-reply message to the DHCPv6 relay agent.
4. The DHCPv6 relay agent parses the Relay-reply message to obtain the DHCPv6 server's reply message and unicasts the reply message to the DHCPv6 client through an Advertise message.

After receiving the Advertise message, the DHCPv6 client sends DAD packets to check whether any other terminal is using the IPv6 address allocated by the server. If the client receives no response within the specified time, it can use the IPv6 address. If the client receives a response, it cannot use the IPv6 address because another terminal is already using it. In this case, the client unicasts a Decline message to the server and resends a Solicit message to request another IPv6 address. After receiving the Decline message, the server lists the IPv6 address carried in the message as a conflicting one.
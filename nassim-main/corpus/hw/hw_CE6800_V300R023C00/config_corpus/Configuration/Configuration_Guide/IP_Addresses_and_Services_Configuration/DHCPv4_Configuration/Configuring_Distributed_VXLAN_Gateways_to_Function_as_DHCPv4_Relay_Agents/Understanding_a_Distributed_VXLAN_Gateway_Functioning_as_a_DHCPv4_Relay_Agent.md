Understanding a Distributed VXLAN Gateway Functioning as a DHCPv4 Relay Agent
=============================================================================

After DHCPv4 relay is configured on a distributed Virtual Extensible LAN (VXLAN) gateway, terminal tenants can dynamically obtain IPv4 addresses using DHCPv4. The following describes how a distributed VXLAN gateway functioning as a DHCPv4 relay agent forwards messages in cases where DHCPv4 clients and a DHCPv4 server do or do not belong to the same VPN.

#### DHCPv4 Clients and Server on the Same VPN

As shown in [Figure 1](#EN-US_CONCEPT_0000001512846618__fig_dc_vrp_dhcp_feature_002001):

* Distributed Layer 3 VXLAN gateways are deployed on Leaf1, Leaf2, and Leaf3, which are connected over Layer 3 VXLAN tunnels.
* VM1 and VM3 belong to the subnet with VNI 10, whereas VM2 and VM4 belong to the subnet with VNI 20.
* The DHCPv4 server connected to Leaf3 belongs to the same VPN as VM1, VM2, VM3, and VM4, but belongs to a different subnet.

After DHCPv4 relay is configured on Leaf1 and Leaf2, VM1, VM2, VM3, and VM4 can all function as DHCPv4 clients to dynamically obtain IPv4 addresses from the DHCPv4 server.
**Figure 1** VXLAN gateways supporting DHCPv4 relay in an intra-VPN scenario  
![](figure/en-us_image_0000001564126297.png)

DHCPv4 relay is enabled on the VBDIF interfaces of leaf nodes to which DHCPv4 clients are connected. In distributed VXLAN scenarios, the gateway address is the same for the clients in a subnet. As shown in [Figure 1](#EN-US_CONCEPT_0000001512846618__fig_dc_vrp_dhcp_feature_002001), the gateway addresses of the users in the subnet with VNI 10 where Leaf1 and Leaf2 reside are 10.1.1.1.

DHCPv4 relay is required if clients go online or send broadcast renewal requests. The following uses VM1 access as an example to describe how DHCPv4 relay agents forward messages. Generally, VM1 sends an address request to the DHCPv4 server through Leaf1, and the DHCPv4 server responds with a reply message to Leaf1. However, a reply message may also be sent to Leaf2. In this case, VM1 can still obtain an IPv4 address. The forwarding process is as follows:

1. VM1 sends a DHCPDISCOVER broadcast message to discover the DHCPv4 server.
2. After receiving the broadcast message, Leaf1 converts it to a DHCPDISCOVER unicast message with the destination IPv4 address as the DHCPv4 server. Leaf1 uses the VBDIF interface address of the corresponding gateway as the address specified by the giaddr field and encapsulates the configured suboption 9 of Option 82 into the message. Leaf1 then encapsulates a VXLAN header into the message and forwards it to Leaf3 over a VXLAN tunnel.
3. Leaf3 decapsulates the received message and forwards it to the DHCPv4 server based on the destination IPv4 address.
4. After receiving the DHCPDISCOVER unicast message, the DHCPv4 server allocates an IPv4 address from the address pool and replies with a DHCPOFFER unicast message in which the destination IPv4 address is that specified by the giaddr field in the DHCPDISCOVER unicast message.
5. After receiving the DHCPOFFER unicast message, Leaf3 searches the routing table based on the destination IPv4 address (VBDIF interface address of the Layer 3 VXLAN gateway) and finds two available routes to the destination IPv4 address. Leaf3 then encapsulates a VXLAN header into the message based on the next hop of the selected route and forwards the message.
   * If the route to Leaf1 is selected, Leaf3 directly forwards the DHCPOFFER unicast message to Leaf1.
   * If the route to Leaf2 is selected, Leaf2 decapsulates the DHCPOFFER unicast message, encapsulates a VXLAN header into the message based on Option 82's suboption 9, and then forwards the message to Leaf1.
6. After receiving the DHCPOFFER unicast message, Leaf1 decapsulates the message and then forwards it to VM1.

DHCPv4 relay is not required if clients go offline or send unicast renewal requests. The following uses the scenario where VM1 sends a unicast renewal request as an example to describe the message forwarding process:

* Before the lease expires, VM1 sends a DHCPREQUEST unicast message to renew the lease, with the source and destination IPv4 addresses being the user address and DHCPv4 server address, respectively.
* After receiving the DHCPREQUEST unicast message, Leaf1 searches the routing table and forwards the message to the DHCPv4 server over a Layer 3 VXLAN tunnel.
* After receiving the DHCPREQUEST unicast message, the DHCPv4 server searches the routing table and sends a DHCPACK unicast message with the destination IPv4 address being the user IPv4 address to VM1 over a Layer 3 VXLAN tunnel.


#### DHCPv4 Clients and Server on Different VPNs

[Figure 2](#EN-US_CONCEPT_0000001512846618__fig_dc_vrp_dhcp_feature_002002) shows an inter-VPN scenario where VM1, VM2, VM3, and VM4 belong to VPN 10 and the DHCPv4 server belongs to VPN 20.

Leaf3 cannot identify the destination VPN of a reply message because VPN information is not carried in the message. Therefore, network segments in VPNs must not overlap. For example, if another network VPN 30 exists, the VBDIF interface address of the Layer 3 VXLAN gateway functioning a DHCPv4 relay agent in VPN 30 cannot be the address 10.1.1.1 in VPN 10.

To allow network segments in VPNs to overlap, configure the Layer 3 VXLAN gateway to insert Option 82's suboptions 151 and 5. [Table 1](#EN-US_CONCEPT_0000001512846618__tab_1) describes the key fields in a DHCPv4 relay message.

**Table 1** Key fields in a DHCPv4 relay message
| Field | Function | Relay Agent's Action | Server's Action |
| --- | --- | --- | --- |
| giaddr | Indicates an IPv4 address that uniquely identifies a DHCPv4 relay agent and is reachable to the DHCPv4 server. NOTE:  The giaddr field originally indicates a DHCPv4 client's gateway address, which is used as a reference for the DHCPv4 server to allocate IPv4 addresses. However, the server may also use the address specified by the giaddr field as the destination IPv4 address of a reply message. Therefore, in the current scenario, the value of the giaddr field is changed to an address that uniquely identifies a relay agent and is reachable to the server, and Option 82's suboption 5 is used to indicate the gateway address of a client. | Fills the VBDIF interface address of the Layer 3 VXLAN gateway of Leaf1 in this field. | Uses the gateway address of a client to fill the destination IPv4 address in a reply message. |
| Option 82's suboption 5 | Indicates the gateway address of a client. | Inserts this suboption with the VBDIF interface address of the Layer 3 VXLAN gateway. | Searches address pools based on suboptions 5 and 151 to allocate addresses, and inserts the two suboptions into a reply message after address allocation is successful. |
| Option 82's suboption 151 | Indicates the VPN information of a client. | Inserts this suboption with the client's VPN instance. |
| Option 82's suboption 11 | Indicates the IPv4 address of a DHCPv4 relay interface. | Inserts this suboption with the VBDIF interface address of the Layer 3 VXLAN gateway. | Encapsulates the content of suboption 11 into Option 54 in a reply message. |



**Figure 2** VXLAN gateways supporting DHCPv4 relay in an inter-VPN scenario  
![](figure/en-us_image_0000001513166198.png)

The forwarding process in an inter-VPN scenario is as follows:

1. VM1 sends a DHCPDISCOVER broadcast message to discover the DHCPv4 server.
2. After receiving the broadcast message, Leaf1 converts it to a DHCPDISCOVER unicast message with the destination IPv4 address as the DHCPv4 server. Leaf1 uses the VBDIF interface address of the corresponding gateway as the address specified by the giaddr field and encapsulates the configured suboption 9 of Option 82 into the message. Leaf1 then encapsulates a VXLAN header into the message and forwards it to Leaf3 over a VXLAN tunnel.![](public_sys-resources/note_3.0-en-us.png) 
   
   To allow network segments in VPNs to overlap, you must configure the Layer 3 VXLAN gateway to insert Option 82's suboptions 151 and 5 into DHCPDISCOVER messages.
3. Leaf3 decapsulates the received message and forwards it to the DHCPv4 server based on the destination IPv4 address.
4. After receiving the DHCPDISCOVER unicast message, the DHCPv4 server allocates an IPv4 address from the address pool and replies with a DHCPOFFER unicast message in which the destination IPv4 address is that specified by the giaddr field in the DHCPDISCOVER unicast message.
5. After receiving the DHCPOFFER unicast message, Leaf3 searches the routing table based on the destination IPv4 address (VBDIF interface address of the Layer 3 VXLAN gateway) and finds two available routes to the destination IPv4 address. Leaf3 then encapsulates a VXLAN header into the message based on the next hop of the selected route and forwards the message.
   * If the route to Leaf1 is selected, Leaf3 directly forwards the DHCPOFFER unicast message to Leaf1.
   * If the route to Leaf2 is selected, Leaf2 decapsulates the DHCPOFFER unicast message, encapsulates a VXLAN header into the message based on Option 82's suboption 9, and then forwards the message to Leaf1.
6. After receiving the DHCPOFFER unicast message, Leaf1 decapsulates the message and then forwards it to VM1.

**Figure 3** Lease renewal process in an inter-VPN scenario  
![](figure/en-us_image_0000001512687078.png)

Due to the lack of VPN information in an inter-VPN scenario, Leaf1 cannot find the next hop of routes based only on the destination IPv4 address (that is, the DHCPv4 server's IPv4 address) of lease renewal messages. Therefore, a relay agent is required.

The lease renewal process in an inter-VPN scenario is as follows:

1. VM1 sends a DHCPDISCOVER broadcast message to discover the DHCPv4 server.
2. After receiving the broadcast message, Leaf1 converts it to a DHCPDISCOVER unicast message with the destination IPv4 address as the DHCPv4 server. Leaf1 uses the VBDIF interface address of the corresponding gateway as the address specified by the giaddr field and encapsulates the configured suboptions 9 and 11 of Option 82 into the message. Leaf1 then encapsulates a VXLAN header into the message and forwards it to Leaf3 over a VXLAN tunnel.![](public_sys-resources/note_3.0-en-us.png) 
   
   In an inter-VPN scenario, a DHCPv4 relay agent must insert Option 82's suboption 11 into DHCPDISCOVER messages. Otherwise, lease renewal of DHCPv4 clients is affected.
3. Leaf3 decapsulates the received message and forwards it to the DHCPv4 server based on the destination IPv4 address.
4. After receiving the DHCPDISCOVER unicast message, the DHCPv4 server allocates an IPv4 address from the address pool and then encapsulates the content of Option 82's suboption 11 into Option 54 in a DHCPOFFER unicast message. After receiving the DHCPOFFER unicast message, VM1 uses the IPv4 address of the DHCPv4 relay interface as the destination IPv4 address of a lease renewal message. The address specified by the giaddr field in a request message is used as the destination IPv4 address of a lease renewal message.
5. After receiving the DHCPOFFER unicast message, Leaf3 searches the routing table based on the destination IPv4 address (VBDIF interface address of the Layer 3 VXLAN gateway) and finds two available routes to the destination IPv4 address. Leaf3 then encapsulates a VXLAN header into the message based on the next hop of the selected route and forwards the message.
   * If the route to Leaf1 is selected, Leaf3 directly forwards the DHCPOFFER unicast message to Leaf1.
   * If the route to Leaf2 is selected, Leaf2 decapsulates the DHCPOFFER unicast message, encapsulates a VXLAN header into the message based on Option 82's suboption 9, and then forwards the message to Leaf1.
6. After receiving the DHCPOFFER unicast message, Leaf1 decapsulates the message and then forwards it to VM1.
7. After receiving the DHCPOFFER unicast message, VM1 uses the IPv4 address carried in Option 54 as the destination IPv4 address of a lease renewal message. Lease renewal messages are sent to the DHCPv4 relay agent for inter-VPN forwarding.
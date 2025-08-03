Understanding NS Multicast Suppression
======================================

On an IPv6 overlay network, IPv6 host neighbor discovery is implemented using NS multicast. When a gateway receives an NS message for IPv6 address resolution, it multicasts the message in its BD. If the gateway forwards a large number of NS messages that are received within a period of time, excessive VXLAN resources are consumed, affecting normal services. To address this issue, configure NS multicast suppression. After this function is configured, the gateway checks whether it can obtain the destination user information in a received NS message. If so, it performs proxy ND or multicast-to-unicast processing to reduce or suppress NS message flooding.

Only VXLAN gateways support this function. For details about VXLAN support, see "[Configuration Precautions for VXLAN](spec/VXLAN_limitation_23.0.html)" in VXLAN Configuration.

#### NS Multicast Suppression

When NS multicast suppression is enabled, a VXLAN gateway collects local IPv6 host information, generates an ND table (containing outbound interface information) or proxy ND table, and floods the ND table or proxy ND table through BGP EVPN routes (ND or IRBv6 routes). After receiving the ND table or proxy ND table, the other gateways generate proxy ND tables locally. In this way, after a gateway receives an NS message, it searches its local proxy ND table. If the gateway can find the corresponding IPv6 host information, it directly performs proxy ND or multicast-to-unicast processing.

The following describes the implementation of NS multicast suppression, as shown in [Figure 1](#EN-US_CONCEPT_0000001176662071__fig_dc_fd_vxlan_004101).

![](public_sys-resources/note_3.0-en-us.png) 

The implementation process in a centralized gateway scenario is similar to that in a distributed gateway scenario. However, in a centralized gateway scenario, the BGP EVPN routes that flood an ND table or proxy ND table are ND routes, whereas those in a distributed gateway scenario can be either ND or IRBv6 routes. The following uses a distributed gateway scenario as an example.


**Figure 1** Network diagram of NS multicast suppression  
![](figure/en-us_image_0000001130622574.png)

1. Host1 goes online from Leaf1. If no Layer 3 gateway exists, Leaf1 is enabled to generate a proxy ND table for Host1 in the BD and floods the table through a BGP EVPN route. If a Layer 3 gateway exists, Leaf1 is enabled to generate an ND table for Host1 and floods the table through a BGP EVPN route.
2. Leaf2 receives the BGP EVPN route from Leaf1, extracts IPv6 host information from the route, and generates a proxy ND table for Host1 locally.
3. Host2 sends an NS multicast message to Leaf2 for requesting the MAC address of Host1.
4. Leaf2 searches the local proxy ND table based on the destination IPv6 address in the multicast NS message and finds the MAC address of Host1. Based on the user configuration, Leaf2 constructs a unicast NA message as a reply to Host2 or converts the multicast NS message into a unicast NS message for forwarding.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After receiving the unicast NS message converted from a multicast NS message, Host1 replies with a unicast NA message. Host2 can then obtain the MAC address of Host1 from the unicast NA message.

#### Application Scenarios

In distributed or centralized VXLAN gateway deployment using BGP EVPN, when the overlay network is an IPv6 network, NS multicast suppression can be deployed to reduce or suppress NS message flooding, thereby alleviating network pressure and ensuring common user services.
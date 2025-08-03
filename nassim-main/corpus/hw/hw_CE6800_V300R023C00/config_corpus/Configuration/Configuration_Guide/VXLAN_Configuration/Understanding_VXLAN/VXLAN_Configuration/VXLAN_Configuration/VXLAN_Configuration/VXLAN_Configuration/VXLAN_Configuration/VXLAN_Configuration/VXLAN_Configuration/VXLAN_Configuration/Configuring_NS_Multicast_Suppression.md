Configuring NS Multicast Suppression
====================================

Configuring NS Multicast Suppression

#### Prerequisites

Before configuring NS multicast suppression, you have completed one of the following tasks:

* [Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1072.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](dc_vrp_vxlan_cfg_1066.html)


#### Context

**Background**

On an IPv6 overlay network, IPv6 host neighbor discovery is implemented through NS multicast. After receiving an NS message for IPv6 address resolution, a gateway uses multicast to forward the message in its BD. If many NS messages are received within a certain period and they all need to be forwarded, a significant amount of VXLAN network resources will be consumed, degrading normal service operation. To address this issue, you can configure NS multicast suppression. After this function is enabled, the gateway checks whether it can obtain the destination user information when receiving an NS message. If so, it performs proxy ND or multicast-to-unicast processing to reduce or suppress NS message flooding.

**Related Concepts**

ND is a group of messages and processes that identify relationships between neighboring nodes. IPv6 ND provides similar functions as the ARP and ICMP router discovery in IPv4, as well as some additional functions.

After a node is configured with an IPv6 address, it checks whether the address is available and if it conflicts with any other addresses. For a node serving as a host, a network device must notify it of the packet's optimal next hop address to a destination. For a node serving as a network device, it must advertise its IPv6 address and address prefix, along with other configuration parameters to instruct hosts to configure parameters. When forwarding IPv6 packets, a node must know the link layer addresses and check the availability of neighboring nodes. IPv6 ND provides four types of ICMPv6 messages:

* Router Solicitation (RS): After a host starts, it sends an RS message to a network device, and the device replies with an RA message.
* Router Advertisement (RA): A network device periodically advertises RA messages that contain prefix and identifier information.
* Neighbor Solicitation (NS): An IPv6 node sends NS messages to obtain the link-layer addresses of neighbors, check the reachability of neighbors, and detect duplicate addresses.
* Neighbor advertisement (NA): An IPv6 host sends an NA message in response to an NS message. An IPv6 node also sends an NA message when the link-layer topology changes.

**Application Scenarios**

In a BGP EVPN-based VXLAN scenario with distributed or centralized VXLAN gateways and an IPv6 overlay network, you can configure NS multicast suppression to reduce or suppress NS message flooding, reducing the network pressure and ensuring normal operation of user services.

**Implementation**

The basic principle of NS multicast suppression is as follows: A VXLAN gateway collects local IPv6 host information, generates an ND table (containing outbound interface information) or proxy ND table, and floods the entries using BGP EVPN routes (ND or IRBv6 routes). After receiving the entries, other gateways generate a proxy ND table. As such, after a gateway receives an NS message, it searches its local proxy ND table. If corresponding IPv6 host information is found, the gateway directly performs proxy ND or multicast-to-unicast processing.

The following uses the network shown in [Figure 1](#EN-US_TASK_0000001176743965__fig_dc_fd_vxlan_004101) to describe the implementation of NS multicast suppression.

![](../public_sys-resources/note_3.0-en-us.png) 

The implementation is similar in centralized and distributed gateway scenarios. In a centralized gateway scenario, the BGP EVPN routes for flooding ND entries or proxy ND entries can be the ND type only, whereas in a distributed gateway scenario, such BGP EVPN routes can be either the ND type or IRBv6 type. The following uses the distributed gateway scenario as an example.


**Figure 1** NS multicast suppression  
![](figure/en-us_image_0000001130784406.png)

1. Host1 goes online on Leaf1. If no Layer 3 gateway exists, enable Leaf1 to generate a proxy ND entry for Host1 in the BD and flood the entry through a BGP EVPN route. If a Layer 3 gateway exists, enable the function to generate an ND entry of Host1 and flood the ND entry through a BGP EVPN route.
2. Leaf2 receives the BGP EVPN route flooded by Leaf1, extracts IPv6 host information from the route, and generates a local proxy ND entry for Host1.
3. Host2 sends an NS multicast message to Leaf2 to request the MAC address of Host1.
4. Leaf2 searches the local proxy ND table based on the destination IPv6 address in the NS multicast message and finds the MAC address of Host1. It then either constructs a unicast NA message destined for Host2, or converts the NS multicast message into an NS unicast message for further forwarding, depending on the user configuration.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If the NS multicast message is converted into an NS unicast message for further forwarding, Host1 responds with a unicast NA message after receiving the NS message. After receiving the NA message, Host2 obtains the MAC address of Host1.

**Derivative Functions**

* **ND spoofing attack defense**
  
  NS multicast suppression can prevent ND spoofing attacks. In an ND spoofing attack, an attacker associates its MAC address with the IPv6 address of a host so that all traffic destined for the IPv6 address is sent to the attacker. After NS multicast suppression is enabled, an IPv6 address conflict alarm will be generated through proxy ND entry conflict detection to notify users of a possible ND spoofing attack.
  
  The following uses the network shown in [Figure 2](#EN-US_TASK_0000001176743965__fig_dc_fd_vxlan_004102) to describe how to prevent ND spoofing attacks.
  
  ![](../public_sys-resources/note_3.0-en-us.png) 
  
  The implementation is similar in centralized and distributed gateway scenarios. In a centralized gateway scenario, the BGP EVPN routes for flooding ND entries or proxy ND entries can be the ND type only, whereas in a distributed gateway scenario, such BGP EVPN routes can be either the ND type or IRBv6 type. The following uses the distributed gateway scenario as an example.
  
  
  **Figure 2** ND spoofing attack defense  
  ![](figure/en-us_image_0000001130784410.png)
  1. Host1 goes online on Leaf1. If no Layer 3 gateway exists, enable Leaf1 to generate a proxy ND entry for Host1 in the BD and flood the entry through a BGP EVPN route. If a Layer 3 gateway exists, enable the function to generate an ND entry of Host1 and flood the ND entry through a BGP EVPN route.
  2. Leaf2 receives the BGP EVPN route flooded by Leaf1, extracts IPv6 host information from the route, and generates a local proxy ND entry for Host1.
  3. An attacker goes online from Leaf2, which generates an ND entry of Host1 and floods the entry through an IRBv6 route. After receiving the route, Leaf1 extracts IPv6 host information and generates a local proxy ND entry for Host1.
  4. At this point, both Leaf1 and Leaf2 have the same IPv6 address in their local ND entries and proxy ND entries that are generated through BGP EVPN routes, causing them to perform neighbor unreachability detection (NUD).
  5. If Leaf1 and Leaf2 find that the MAC address corresponding to the same IPv6 address changes multiple times within a certain period, they trigger an IPv6 conflict alarm to alert users that ND spoofing attacks may have occurred.
* **IPv6 VM migration in a distributed gateway scenario**
  
  After NS multicast suppression is enabled in a distributed gateway scenario, IPv6 VMs can be migrated. The following uses the network shown in [Figure 3](#EN-US_TASK_0000001176743965__fig_dc_fd_vxlan_004103) to describe the implementation process of IPv6 VM migration.
  
  **Figure 3** IPv6 VM migration  
  ![](figure/en-us_image_0000001176744073.png)
  1. Host1 goes online on Leaf1. If no Layer 3 gateway exists, enable Leaf1 to generate a proxy ND entry for Host1 in the BD and flood the entry through a BGP EVPN route. If a Layer 3 gateway exists, enable the function to generate an ND entry of Host1 and flood the ND entry through a BGP EVPN route.
  2. Leaf2 receives the BGP EVPN route flooded by Leaf1, extracts IPv6 host information from the route, and generates a local proxy ND entry for Host1.
  3. Host1 is migrated from Leaf1 to Leaf2 and sends a gratuitous NA message.
  4. Leaf2 generates the ND entry of Host1 based on the gratuitous NA message and floods it through a BGP EVPN route. After receiving the route, Leaf1 extracts IPv6 host information and generates a local proxy ND entry for Host1.
  5. In a local ND entry, Host1 is a local host, and Leaf1 is the next hop. In a proxy ND entry, Host1 is a remote host, and Leaf2 is the next hop. This indicates that Host1 may be migrated. Consequently, NUD is triggered on Leaf1. Leaf1 then sends an NS message. Because Host1 has been migrated to Leaf2, Leaf1 cannot receive the NA message.
  6. Leaf1 detects that Host1 is unreachable and deletes its local ND entry. Then, Leaf1 uses BGP EVPN to instruct the remote node Leaf2 to delete the proxy ND entry that is synchronized when Host1 goes online from Leaf1.

Perform the following steps on any Layer 2 and Layer 3 VXLAN gateways:


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Enable NS multicast suppression.
   
   
   ```
   [ipv6 nd multicast-suppress](cmdqueryname=ipv6+nd+multicast-suppress) { proxy-reply [ unknown-options-unicast ] | unicast-forward } [ mismatch-discard ] enable
   ```
   
   By default, NS multicast suppression is disabled.
   
   After NS multicast suppression is enabled, when the device receives ND entries or proxy ND entries from other devices, it generates local proxy ND entries to perform proxy ND. In this command:
   
   * **proxy-reply** indicates that when the destination of an NS multicast message is not a local host but it matches a proxy ND entry on the local device, the device implements proxy ND by replying with an NA message.
   * **unknown-options-unicast** indicates that when the destination of an NS multicast message is not a local host but it matches a proxy ND entry on the local device, the device converts the multicast message to a unicast message if the message carries unrecognized options. If this keyword is not specified, a device ignores the unrecognized options in NS messages but still performs proxy ND.
   * **unicast-forward** indicates that when the destination of an NS multicast message is not a local host but it matches a proxy ND entry on the local device, the device converts the multicast message to a unicast message and forwards the unicast message.
   * **mismatch-discard** indicates that when the destination of an NS multicast message is not a local host and it does not match a proxy ND entry on the local device, the device discards the NS multicast message. If this keyword is not specified, a device uses multicast to forward the NS message. If this keyword is not specified, a device uses multicast to forward the NS message.
4. (Optional) Configure the R flag for NA messages when proxy ND is performed.
   
   
   ```
   [ipv6 nd multicast-suppress](cmdqueryname=ipv6+nd+multicast-suppress) { host | router }
   ```
   
   By default, the R flag carried in an NA message is a router flag.
   
   During interconnection with a non-Huawei device, if the proxy ND entries synchronized from the peer device to the local device through EVPN routes do not carry the R flag, the local device cannot determine whether an NA message it receives was sent by a router or a host. To allow the local device to make this determination, configure the R flag for NA messages.
5. (Optional) Configure the maximum number of dynamic proxy ND entries that can be learned in a BD.
   
   
   ```
   [ipv6 nd multicast-suppress dynamic limit](cmdqueryname=ipv6+nd+multicast-suppress+dynamic+limit) limit-value
   ```
   
   By default, a maximum of 256 dynamic proxy ND entries can be learned in a BD.
   
   If an attacker sends a large number of RA messages to attack a device, the device may learn many dynamic proxy ND entries within a short period, causing the CPU usage to sharply increase and consuming a large amount of memory resources. Running this command limits the maximum number of dynamic proxy ND entries that can be learned in a BD, effectively preventing overflow of dynamic proxy ND entries and ensuring proper device operation.
6. (Optional) Configure the aging time of dynamic proxy ND entries.
   
   
   ```
   [ipv6 nd multicast-suppress dynamic expire-time](cmdqueryname=ipv6+nd+multicast-suppress+dynamic+expire-time) expire-time-value
   ```
   
   By default, the aging time of dynamic proxy ND entries is 900 seconds.
   
   Each dynamic proxy ND entry has a life cycle, also known as its aging time. If an entry is not updated before its life cycle expires, it will be deleted from the proxy ND table. If the entry is updated before its life cycle expires, the aging time of the entry is recalculated. This command ensures timely update of dynamic proxy ND entries.
7. Enable EVPN-based flooding of ND entries or proxy ND entries.
   
   
   
   If no Layer 3 gateway exists, enable the function to flood the proxy ND table on a Layer 2 gateway to EVPN peers through EVPN routes.
   
   ```
   [ipv6 nd collect host enable](cmdqueryname=ipv6+nd+collect+host+enable)
   ```
   
   By default, a device does not flood proxy ND entries through EVPN routes.
   
   Other devices generate local proxy ND entries after receiving flooded proxy ND entries. As such, when these devices receive an NS message, they first search the local proxy ND table for a matching entry. If one is found, they directly perform proxy ND or convert the multicast message to a unicast message for forwarding.
   
   
   
   If a Layer 3 gateway exists, enable the function to flood the ND table on the Layer 3 gateway to EVPN peers through EVPN routes.
   
   ```
   [quit](cmdqueryname=quit)
   [interface vbdif](cmdqueryname=interface+vbdif) bd-id
   [ipv6 enable](cmdqueryname=ipv6+enable)
   [ipv6 nd collect host enable](cmdqueryname=ipv6+nd+collect+host+enable)
   ```
   
   By default, a device does not flood ND entries through EVPN routes.
   
   Other devices generate local proxy ND entries after receiving flooded ND entries. As such, when these devices receive an NS message, they first search the local proxy ND table for a matching entry. If one is found, they directly perform proxy ND or convert the multicast message to a unicast message for forwarding.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   If the [**ipv6 nd collect host enable**](cmdqueryname=ipv6+nd+collect+host+enable) command is run in both the BD view and VBDIF interface view, the device directly generates ND entries and floods them through EVPN routes. When the configuration on the VBDIF interface is deleted, the generated ND entries are converted into proxy ND entries and then flooded through EVPN routes. As such, if a VBDIF interface exists, you are advised to run the [**ipv6 nd collect host enable**](cmdqueryname=ipv6+nd+collect+host+enable) command in both the BD view and VBDIF interface view.
8. Configure BGP EVPN to advertise ND routes.
   
   
   ```
   [quit](cmdqueryname=quit)
   [bgp](cmdqueryname=bgp) as-number [ instance instance-name ]
   [l2vpn-family evpn](cmdqueryname=l2vpn-family+evpn)
   [peer](cmdqueryname=peer) { ipv4-address | group-name } advertise nd
   ```
   
   By default, a device does not advertise ND routes to its BGP EVPN peers.
   
   BGP EVPN peers advertise ND routes to flood ND entries or proxy ND entries so that the local IPv6 host information obtained by each peer can be synchronized to others. This function increases the effectiveness of NS multicast suppression.
9. (Optional) Configure the rate at which ND messages are sent. This rate indicates the number of ND messages allowed to be sent to the CPU per second.
   
   
   ```
   [quit](cmdqueryname=quit)
   [ipv6 nd](cmdqueryname=ipv6+nd) { rs | ra | ns | na } anti-attack rate-limit limit-number
   ```
   
   By default, 550 ND messages are sent to the CPU per second.
   
   If an attacker sends a large number of ND messages to a device within a short period, the device consumes many CPU resources to learn and respond to ND entries, affecting the processing of other services. Running this command resolves the problem. It enables the device to count the number of ND messages received per second and discard excess messages that exceed the configured limit.
10. (Optional) Configure the rate at which ND Miss messages are sent to the CPU. This rate indicates the number of ND Miss messages allowed to be sent to the CPU per second.
    
    
    ```
    [ipv6 nd miss anti-attack rate-limit](cmdqueryname=ipv6+nd+miss+anti-attack+rate-limit) limit-number
    ```
    
    By default, 550 ND Miss messages are sent to the CPU per second.
    
    When a device sends an IPv6 packet, an ND Miss message is generated if the MAC address corresponding to the destination IPv6 address of the sent packet does not exist. This consumes device resources and impacts the processing of other services. Running this command resolves the problem. It enables the device to process only the allowed number of ND Miss messages within a specified period, ensuring normal operation of other services.
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display ipv6 nd multicast-suppress bridge-domain**](cmdqueryname=display+ipv6+nd+multicast-suppress+bridge-domain) [ *bd-id* ] [ **verbose** ] command to check information about the proxy ND table in a BD.
* Run the [**display ipv6 nd packet statistics bridge-domain**](cmdqueryname=display+ipv6+nd+packet+statistics+bridge-domain) [ *bd-id* ] command to check the number of sent and received ND messages in a BD.
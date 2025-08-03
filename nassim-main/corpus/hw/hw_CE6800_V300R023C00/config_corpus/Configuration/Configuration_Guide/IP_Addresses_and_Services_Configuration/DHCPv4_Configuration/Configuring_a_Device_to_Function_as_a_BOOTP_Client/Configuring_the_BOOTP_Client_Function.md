Configuring the BOOTP Client Function
=====================================

Configuring the BOOTP Client Function

#### Context

After the BOOTP client function is configured on a device, the device can obtain configuration parameters such as an IPv4 address from a DHCPv4 server.

If the IPv4 address allocated by a DHCPv4 server to a device's interface is on the same network segment as the IPv4 address of another interface on the device, the interface does not use this address or apply for a new IPv4 address from the server. To enable the interface to apply for a new IPv4 address, run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands in sequence on the interface, or run the [**undo ip address bootp-alloc**](cmdqueryname=undo+ip+address+bootp-alloc) and [**ip address bootp-alloc**](cmdqueryname=ip+address+bootp-alloc) commands in sequence.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Configure the BOOTP client to obtain routing entries through DHCPv4.
   
   
   ```
   [ip route](cmdqueryname=ip+route) ip-address { mask | mask-length } interface-type interface-num dhcp [ preference-value ]
   ```
   
   By default, a BOOTP client does not obtain routing entries through DHCPv4.
   
   After the BOOTP client is configured to dynamically obtain routing entries through DHCPv4, the next hop address of a static route changes with the gateway address.
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Enable the BOOTP client function on the interface.
   
   
   ```
   [ip address bootp-alloc](cmdqueryname=ip+address+bootp-alloc) [ unicast ]
   ```
   
   By default, the BOOTP client function is disabled on an interface.
6. (Optional) Configure parameters for the BOOTP client as required.
   
   
   
   **Table 1** Configuring parameters for the BOOTP client
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure a hostname for the BOOTP client. | [**dhcp client hostname**](cmdqueryname=dhcp+client+hostname) *hostname* | The hostname of the client is filled in Option 12. To access a BOOTP client through a domain name, configure a hostname for the client. A domain name consists of a hostname and domain name suffix.  By default, no hostname is configured for a BOOTP client. |
   | Configure gateway detection on the BOOTP client. | [**dhcp client gateway-detect**](cmdqueryname=dhcp+client+gateway-detect) **period** *period* **retransmit** *retransmit* **timeout** *timeout* | After this function is enabled, the BOOTP client sends an ARP Request message to detect the gateway status after obtaining an IPv4 address. If the client receives no ARP Reply message within the detection period, it considers the gateway address incorrect or the gateway faulty and applies for a new IPv4 address.  By default, gateway detection is disabled on a BOOTP client. |
   | Configure the default route precedence obtained by the BOOTP client from the DHCPv4 server. | [**dhcp client default-route preference**](cmdqueryname=dhcp+client+default-route+preference) *preference-value* | When a device functions as a BOOTP client, you can configure the precedence of routing entries allocated by the DHCPv4 server so that the client dynamically updates its routing table.  By default, the default route precedence obtained by a BOOTP client from a DHCPv4 server is 60. |
   | Configure the abnormal packet detection function. | [**undo dhcp anti-attack check magic-cookie**](cmdqueryname=undo+dhcp+anti-attack+check+magic-cookie): configures the device not to check the magic cookie field in received DHCPv4 messages in the system, VLAN, or interface view.  [**undo dhcp anti-attack check udp-checksum**](cmdqueryname=undo+dhcp+anti-attack+check+udp-checksum): configures the device not to check the UDP header checksum in received DHCPv4 messages in the system, VLAN, or interface view.  **dhcp udp-checksum enable**: enables the device to carry the UDP header checksum in sent DHCPv4 messages in the system view. | By default, a device does not check the magic cookie field in DHCPv4 messages and directly forwards DHCPv4 messages with an incorrect magic cookie field value; instead, it checks the UDP header checksum in DHCPv4 messages and discards those with an incorrect UDP header checksum. The UDP header checksum carried in DHCP messages sent by a device is 0, and the peer device does not need to verify the checksum. |
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display dhcp client**](cmdqueryname=display+dhcp+client) [ **interface** *interface-type* *interface-number* ] command to check DHCPv4 client lease information.
* Run the [**display dhcp client statistics**](cmdqueryname=display+dhcp+client+statistics) [ **interface** *interface-type* *interface-number* ] command to check message statistics on the DHCPv4 client.
* Run the [**display dhcp statistics**](cmdqueryname=display+dhcp+statistics) command to check statistics about DHCPv4 messages sent and received by the device.
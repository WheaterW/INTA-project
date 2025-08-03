Configuring the DHCPv4 Client Function
======================================

Configuring the DHCPv4 Client Function

#### Context

After the DHCPv4 client function is configured on a device, the device can obtain configuration parameters such as an IPv4 address from a DHCPv4 server.

If the IPv4 address allocated by a DHCPv4 server to a device's interface is on the same network segment as the IPv4 address of another interface on the device, the interface does not use this address or apply for a new IPv4 address from the server. To enable the interface to apply for a new IPv4 address, run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands in sequence on the interface, or run the [**undo ip address dhcp-alloc**](cmdqueryname=undo+ip+address+dhcp-alloc) and [**ip address dhcp-alloc**](cmdqueryname=ip+address+dhcp-alloc) commands in sequence.

After the DHCPv4 client function is enabled on a device's interface, the interface cannot communicate with the DHCPv4 server when the device functions as a DHCPv4 relay agent.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Configure parameters for the DHCPv4 client as required.
   
   
   
   **Table 1** Configuring parameters for the DHCPv4 client
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure Option 60 in DHCPv4 request messages sent by the DHCPv4 client. | [**dhcp client class-id**](cmdqueryname=dhcp+client+class-id) *class-id* | Option 60 identifies a vendor type and can be configured in both the system and interface views. If the configuration is performed in both views, only the configuration in the interface view takes effect.  By default, the value of Option 60 is related to a device and is expressed as "huawei device model." |
   | Configure the DHCPv4 client to obtain routing entries through DHCPv4. | [**ip route**](cmdqueryname=ip+route) *ip-address* { *mask* | *mask-length* } *interface-type interface-num* **dhcp** [ *preference-value* ] | After this function is configured, the next hop address of a static route changes with the gateway address.  By default, a DHCPv4 client does not obtain routing entries through DHCPv4. |
   | Configure the abnormal packet detection function. | * [**undo dhcp anti-attack check magic-cookie**](cmdqueryname=undo+dhcp+anti-attack+check+magic-cookie): configures the device not to check the magic cookie field in received DHCPv4 messages in the system, VLAN, or interface view. * [**undo dhcp anti-attack check udp-checksum**](cmdqueryname=undo+dhcp+anti-attack+check+udp-checksum): configures the device not to check the UDP header checksum in received DHCPv4 messages in the system, VLAN, or interface view. * **[**dhcp anti-attack check duplicate option**](cmdqueryname=dhcp+anti-attack+check+duplicate+option)** [ *option-start* [ **to** *option-end* ] ] &<1-254>: enables the device to check and discard DHCPv4 messages with duplicate options in the system view. | By default, a device does not check the magic cookie field in DHCPv4 messages and directly forwards DHCPv4 messages with an incorrect magic cookie field value; a device checks the UDP header checksum in DHCPv4 messages and discards those with an incorrect UDP header checksum; and a device does not check DHCPv4 messages with duplicate options.  Before configuring the abnormal packet detection function, run the **[**dhcp enable**](cmdqueryname=dhcp+enable)** command to enable DHCPv4 on the device. |
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Enable the DHCPv4 client function on the interface.
   
   
   ```
   [ip address dhcp-alloc](cmdqueryname=ip+address+dhcp-alloc) [ unicast ]
   ```
   
   By default, the DHCPv4 client function is disabled on an interface.
6. (Optional) Configure parameters for the DHCPv4 client as required.
   
   
   
   **Table 2** Configuring parameters for the DHCPv4 client
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure attributes for the DHCPv4 client. | [**dhcp client hostname**](cmdqueryname=dhcp+client+hostname) *hostname*: configures a hostname for the DHCPv4 client.  [**dhcp client client-id**](cmdqueryname=dhcp+client+client-id) *client-id*: configures an identifier for the DHCPv4 client.  [**dhcp client class-id**](cmdqueryname=dhcp+client+class-id) *class-id*: configures Option 60 in DHCPv4 request messages sent by the DHCPv4 client. | The hostname of the client is filled in Option 12. To access a DHCPv4 client through a domain name, configure a hostname for the client. A domain name consists of a hostname and domain name suffix.  The identifier of a DHCPv4 client is filled in Option 61 to uniquely identify the client.  Option 60 identifies a vendor type and can be configured in both the system and interface views. If the configuration is performed in both views, only the configuration in the interface view takes effect.  By default, no hostname is configured for a DHCPv4 client, the identifier of a DHCPv4 client is its MAC address, and Option 60 is not configured. |
   | Configure an expected lease for the DHCPv4 client. | [**dhcp client expected-lease**](cmdqueryname=dhcp+client+expected-lease) *time-value*: configures an expected lease for the DHCPv4 client.  [**dhcp client renew**](cmdqueryname=dhcp+client+renew): renews the lease of the IPv4 address obtained by the DHCPv4 client. | By default, no expected lease is configured for a DHCPv4 client.  The [**dhcp client renew**](cmdqueryname=dhcp+client+renew) command can be normally run only after the DHCPv4 client function is enabled on an interface that has obtained an IPv4 address. |
   | Configure gateway detection on the DHCPv4 client. | [**dhcp client gateway-detect**](cmdqueryname=dhcp+client+gateway-detect) **period** *period* **retransmit** *retransmit* **timeout** *timeout* | After this function is enabled, the DHCPv4 client sends an ARP Request message to detect the gateway status after obtaining an IPv4 address. If the client receives no ARP Reply message within the detection period, it considers the gateway address incorrect or the gateway faulty and applies for a new IPv4 address.  By default, this function is disabled. |
   | Configure the default route precedence obtained by the DHCPv4 client from the server. | [**dhcp client default-route preference**](cmdqueryname=dhcp+client+default-route+preference) *preference-value* | By default, the default route precedence obtained by a DHCPv4 client from a DHCPv4 server is 60. |
   | Configure the option information requested by the DHCPv4 client. | [**dhcp client request option-list exclude**](cmdqueryname=dhcp+client+request+option-list+exclude) *option-code* &<1-8>: configures a list of default request options that are not carried in Option 55 of DHCPv4 request messages.  [**dhcp client request option-list**](cmdqueryname=dhcp+client+request+option-list) *option-code* &<1-15>: configures a list of request options that Option 55 in DHCPv4 request messages carries besides the default options. | Option 55 in DHCPv4 request messages is used to set the request option list. A DHCPv4 client uses this option to request specified configuration parameters from a DHCPv4 server. You can run the [**dhcp client request option-list exclude**](cmdqueryname=dhcp+client+request+option-list+exclude) command to set a list of default options that are excluded from Option 55. You can also run the [**dhcp client request option-list**](cmdqueryname=dhcp+client+request+option-list) command to set a list of other options that Option 55 carries besides the default options. The other options include options 4, 7, 17, 42, 43, 66, 67, 120, and 129.  By default, no option is excluded from the request list on a DHCPv4 client, and Option 55 in DHCPv4 request messages carries only the default request options. |
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display dhcp client**](cmdqueryname=display+dhcp+client) [ **interface** *interface-type* *interface-number* ] command to check DHCPv4 client lease information.
* Run the [**display dhcp client statistics**](cmdqueryname=display+dhcp+client+statistics) [ **interface** *interface-type* *interface-number* ] command to check message statistics on the DHCPv4 client.
* Run the [**display dhcp statistics**](cmdqueryname=display+dhcp+statistics) command to check statistics about DHCPv4 messages sent and received by the device.
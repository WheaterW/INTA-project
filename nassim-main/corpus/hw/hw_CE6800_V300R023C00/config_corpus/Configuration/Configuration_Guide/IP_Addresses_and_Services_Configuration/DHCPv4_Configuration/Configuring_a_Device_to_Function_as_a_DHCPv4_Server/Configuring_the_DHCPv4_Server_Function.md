Configuring the DHCPv4 Server Function
======================================

Configuring the DHCPv4 Server Function

#### Context

If a device is configured as a DHCPv4 server, you must enable the DHCPv4 server function for an address pool after enabling DHCPv4 on the device.

![](public_sys-resources/note_3.0-en-us.png) 

When configuring the DHCPv4 server function on a Multichassis Link Aggregation Group (M-LAG), you must configure this function on the two devices that constitute the M-LAG.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the DHCPv4 server function for an address pool.
   * Enable the global DHCPv4 server function.
     1. Configure a primary IPv4 address for an interface.
        ```
        [interface](cmdqueryname=interface) interface-type interface-number
        [undo portswitch](cmdqueryname=undo+portswitch)
        [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
        ```
        
        Determine whether to run the [**undo portswitch**](cmdqueryname=undo+portswitch) command to switch the interface working mode to Layer 3 based on the current interface working mode.
        
        By default, no primary IPv4 address is configured for an interface.
     2. (Optional) Configure a secondary IPv4 address for the interface.
        ```
        [interface](cmdqueryname=interface) interface-type interface-number
        [undo portswitch](cmdqueryname=undo+portswitch)
        [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } sub
        ```
        
        Determine whether to run the [**undo portswitch**](cmdqueryname=undo+portswitch) command to switch the interface working mode to Layer 3 based on the current interface working mode.
        
        By default, no secondary IPv4 address is configured for an interface.
        
        The device can select a global address pool based on the primary and secondary IPv4 addresses of the interface only in scenarios where the DHCPv4 server and clients are on the same network segment. The device uses the address pool for the primary IPv4 address first. If no address is available, the device uses the address pool for the secondary IPv4 address.
        
        After an IPv4 address is configured for an interface, when a client connected to the interface applies for an IPv4 address:
        + If the device and client are on the same network segment (that is, no relay agent is deployed), the device allocates an IPv4 address to the client from the address pool on the same network segment as the interface's primary IPv4 address. If the address pool for the primary IPv4 address is exhausted or no address pool is configured for the primary IPv4 address, the address pool for the secondary IPv4 address is used to allocate an address to the client. If no IPv4 address is configured for the interface or no address pool on the same network segment as the interface address exists, the client cannot obtain an IPv4 address.
        + If the device and client are on different network segments (that is, a relay agent is deployed), the device parses the IPv4 address specified by the giaddr field in a received DHCPv4 request message, and selects an address pool on the same network segment as the IPv4 address for IPv4 address allocation. If the IPv4 address does not match any address pool, the client cannot obtain an IPv4 address.
     3. Enable the DHCPv4 server function based on the global address pool on the interface.
        ```
        [dhcp select global](cmdqueryname=dhcp+select+global)
        ```
        
        This step is optional if a DHCPv4 relay agent exists between the device and client; this step is mandatory if no relay agent exists.
        
        By default, the DHCPv4 server function based on the global address pool is disabled on the interface.
   * Enable the interface-based DHCPv4 server function.
     1. Configure an IPv4 address for an interface.
        ```
        [interface](cmdqueryname=interface) interface-type interface-number
        [undo portswitch](cmdqueryname=undo+portswitch)
        [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
        ```
        
        Determine whether to run the [**undo portswitch**](cmdqueryname=undo+portswitch) command to switch the interface working mode to Layer 3 based on the current interface working mode.
        
        By default, no IPv4 address is configured for an interface.
     2. Enable the DHCPv4 server function on the interface to allocate an IPv4 address to a client from the interface address pool.
        ```
        [dhcp select interface](cmdqueryname=dhcp+select+interface)
        ```
        
        By default, the DHCPv4 server function based on the interface address pool is disabled on the interface.
        
        If the device functions as a DHCPv4 server to provide DHCPv4 services for clients connected to multiple interfaces, repeat this step on each interface to enable the DHCPv4 server function.
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. (Optional) Configure optional functions for the DHCPv4 server as required.
   
   
   
   **Table 1** Configuring optional functions for the DHCPv4 server
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure DHCPv4 data saving. | [**dhcp server database**](cmdqueryname=dhcp+server+database) **enable**: enables the device to save address allocation data.  [**dhcp server database**](cmdqueryname=dhcp+server+database) **write-delay** *interval*: configures an interval for saving data. | After these functions are configured, the device periodically saves address allocation data to a storage medium. After the device restarts, it can restore data from the storage medium promptly.  The **lease.txt** and **conflict.txt** files in the **dhcp** folder of the storage medium store address leases and conflicting addresses, respectively. The two files are overwritten periodically; therefore, you are advised to back up them to other locations.  The time displayed in the two files is the UTC time rather than the system time, and you do not need to pay attention to time zone information.  By default, DHCPv4 data saving is disabled. After DHCPv4 data saving is enabled, DHCPv4 data is saved every 3600s by default. |
   | Configure IPv4 address conflict detection. | [**dhcp server ping**](cmdqueryname=dhcp+server+ping) { **packet** *number* | **timeout** *milliseconds* } \*: configures the number of conflict detections during IPv4 address allocation and maximum waiting time for each conflict detection. | After this function is configured, the DHCPv4 server, before sending a DHCPOFFER message, sends an ICMP Echo request message with the source address being the IPv4 address of the DHCPv4 server and the destination address being the pre-allocated IPv4 address to detect conflicts for the allocated IPv4 address.  * If the DHCPv4 server receives no ICMP Echo reply message within the detection period (number of detections x maximum waiting time for each detection), this IPv4 address is not used. In this case, the DHCPv4 server allocates the IPv4 address to the client. * If the DHCPv4 server receives an ICMP Echo reply message within the detection period, this IPv4 address is being used. In this case, the DHCPv4 server lists this IPv4 address as a conflicting one and waits for the next DHCPv4 request message. Do not set a long IPv4 address conflict detection period. Otherwise, clients cannot obtain IPv4 addresses. You are advised to set the detection period to less than 8 seconds.  By default, a DHCPv4 server sends a maximum of two ping packets, and the maximum timeout period of each ping reply is 500 ms. |
   | Configure the DHCPv4 server to dynamically allocate IPv4 addresses to BOOTP clients. | [**dhcp server bootp**](cmdqueryname=dhcp+server+bootp): enables the DHCPv4 server to respond to BOOTP requests.  [**dhcp server bootp automatic**](cmdqueryname=dhcp+server+bootp+automatic): enables the DHCPv4 server to allocate IPv4 addresses to BOOTP clients. | By default, a DHCPv4 server is enabled to respond to BOOTP requests and dynamically allocate IPv4 addresses to BOOTP clients. |
   | Configure the abnormal packet detection function. | [**dhcp anti-attack check magic-cookie**](cmdqueryname=dhcp+anti-attack+check+magic-cookie): configures the device to check the magic cookie field in received DHCPv4 messages in the system, VLAN, or interface view.  [**undo dhcp anti-attack check udp-checksum**](cmdqueryname=undo+dhcp+anti-attack+check+udp-checksum): configures the device not to check the UDP header checksum in received DHCPv4 messages in the system, VLAN, or interface view.  **[**dhcp udp-checksum enable**](cmdqueryname=dhcp+udp-checksum+enable)**: enables the device to carry the UDP header checksum in sent DHCPv4 messages in the system view. | Devices from different vendors may use different DHCPv4 implementation mechanisms. If a device finds that the UDP header checksum or magic cookie field in a received DHCPv4 message fails the check, it discards the DHCPv4 message. As a result, DHCPv4 becomes unavailable. To resolve this issue, configure the device not to check the UDP header checksum or magic cookie field in received DHCPv4 messages. In this case, if DHCPv4 messages carry an incorrect UDP header checksum or magic cookie value, they can still be properly forwarded.  According to the protocol, if the UDP header checksum is 0, the peer device does not verify the checksum in DHCPv4 messages. If the peer device does not comply with the protocol, it still verifies the checksum even if the UDP header checksum in DHCPv4 messages sent by the local device is 0. In this case, you need to configure the local device to carry the UDP header checksum in DHCPv4 messages to be sent, so that the checksum can be verified by the peer device.  Any DHCPv4 device can be configured not to check the UDP header checksum or magic cookie field in received DHCPv4 messages.  Only a device functioning as a DHCPv4 server can be configured to carry the UDP header checksum in DHCPv4 messages to be sent.  After DHCPv4 is enabled on a device, the device checks the IP and UDP header checksums in received DHCPv4 messages by default. In addition, the function of checking the IP header checksum cannot be disabled.  By default, a device does not check the magic cookie field in DHCPv4 messages and directly forwards those with incorrect magic cookie field values; a device checks the UDP header checksum in DHCPv4 messages and discards those with incorrect checksums; the UDP header checksum carried in DHCPv4 messages sent by a device is 0, and the peer device does not verify the checksum. |
   | Force the DHCPv4 server to reply with a DHCPNAK message. | [**dhcp server force response**](cmdqueryname=dhcp+server+force+response) | During the two-message exchange of a DHCPv4 client, if the IPv4 address requested by the DHCPv4 client is within the address pool but the address pool does not have the lease record of the DHCPv4 client, for example, when a wireless user obtains an IPv4 address from another DHCPv4 server, the user roams to the current DHCPv4 server, and the original IPv4 address is in the address pool of the current DHCPv4 server; or when the address pool is reset or the client goes online again. In this case, after receiving a DHCPREQUEST message from the DHCPv4 client, the DHCPv4 server does not send a DHCPNAK message to the DHCPv4 client. The DHCPv4 client can apply for an IPv4 address to go online again through four steps only after the two-message exchange times out. As a result, the DHCPv4 client takes a long time to obtain an IPv4 address. After this function is configured, the DHCPv4 server is forced to reply with a DHCPNAK message. The DHCPv4 client can then quickly enter the four-message exchange and apply for a new IPv4 address.  By default, a DHCPv4 server is not forced to reply with a DHCPNAK message. |
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
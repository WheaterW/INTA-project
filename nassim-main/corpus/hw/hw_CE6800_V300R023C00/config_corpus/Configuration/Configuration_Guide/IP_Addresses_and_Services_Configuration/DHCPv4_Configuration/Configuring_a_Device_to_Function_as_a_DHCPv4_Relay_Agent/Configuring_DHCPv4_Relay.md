Configuring DHCPv4 Relay
========================

Configuring DHCPv4 Relay

#### Context

If a DHCPv4 server and client are on the same network segment, they can directly exchange DHCPv4 messages. In this case, no DHCPv4 relay agent is required. If a DHCPv4 server and client are on different network segments, a device must be configured as a DHCPv4 relay agent to forward DHCPv4 messages.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Configure the DHCPv4 relay agent not to check the DHCPv4 server identifier (Option 54) in a DHCPREQUEST message to be forwarded.
   
   
   ```
   [undo dhcp relay request server-match enable](cmdqueryname=undo+dhcp+relay+request+server-match+enable)
   ```
   
   By default, a DHCPv4 relay agent checks the DHCPv4 server identifier (Option 54) in a DHCPREQUEST message to be forwarded.
3. (Optional) Configure the DHCPv4 relay agent to forward all DHCPACK messages.
   
   
   ```
   [dhcp relay reply forward all enable](cmdqueryname=dhcp+relay+reply+forward+all+enable)
   ```
   
   By default, a DHCPv4 relay agent forwards only the first received DHCPACK message.
4. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
5. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
6. Configure an IPv4 address for the interface.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Generally, DHCPv4 relay is configured on a user-side gateway interface. In this case, the IPv4 address of the gateway interface must be on the same network segment as the address pool configured on the server. Otherwise, a DHCPv4 client cannot obtain an IPv4 address.
   
   
   
   * Configure an IPv4 address for the interface.
     ```
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
     ```
     
     By default, no IPv4 address is configured for an interface.
   * Configure the interface to borrow the IPv4 address of another interface.
     ```
     [ip address unnumbered interface](cmdqueryname=ip+address+unnumbered+interface) interface-type interface-number
     ```
     
     By default, an interface does not borrow the IPv4 address of another interface.
7. Enable DHCPv4 relay on the interface.
   
   
   ```
   [dhcp select relay](cmdqueryname=dhcp+select+relay)
   ```
   
   By default, DHCPv4 relay is disabled on an interface.
8. (Optional) In an inter-VPN scenario, enable the DHCPv4 relay interface to insert Option 82 into DHCPv4 messages.
   
   
   ```
   [dhcp option82](cmdqueryname=dhcp+option82) { vss-control | link-selection | server-id-override } insert enable
   ```
   
   
   
   By default, a DHCPv4 relay interface does not insert Option 82 into DHCPv4 messages.
   
   
   
   If a DHCPv4 client and server are located in different VPNs, you must run this command on the DHCPv4 relay agent. You can specify **vss-control**, **link-selection**, and **server-id-override** to insert Option 82's different suboptions into DHCPv4 messages, ensuring that clients can obtain IPv4 addresses.
   
   The **dhcp option82 link-selection insert enable** command takes precedence over the [**dhcp relay source-ip-address**](cmdqueryname=dhcp+relay+source-ip-address) and [**dhcp relay gateway**](cmdqueryname=dhcp+relay+gateway) commands.
9. (Optional) In an inter-VPN scenario, modify the information of the giaddr field.
   
   
   
   Configure the source interface of DHCPv4 relay messages, and use the primary IPv4 address of the interface to fill in the giaddr field.
   
   ```
   [dhcp relay giaddr source-interface](cmdqueryname=dhcp+relay+giaddr+source-interface) interface-type interface-num
   ```
   
   Or configure the device to use the primary IPv4 address of the outbound interface to fill in the giaddr field.
   
   ```
   [dhcp relay giaddr outgoing-interface-address](cmdqueryname=dhcp+relay+giaddr+outgoing-interface-address)
   ```
   
   By default, a device uses the IPv4 address of a DHCPv4 relay agent to fill in the giaddr field.
   
   The [**dhcp relay source-ip-address**](cmdqueryname=dhcp+relay+source-ip-address) and [**dhcp relay gateway**](cmdqueryname=dhcp+relay+gateway) commands are mutually exclusive with the [**dhcp relay giaddr source-interface**](cmdqueryname=dhcp+relay+giaddr+source-interface) and [**dhcp relay giaddr outgoing-interface-address**](cmdqueryname=dhcp+relay+giaddr+outgoing-interface-address) commands.
   
   The [**dhcp relay giaddr source-interface**](cmdqueryname=dhcp+relay+giaddr+source-interface) *interface-type* *interface-num* command takes precedence over the [**dhcp relay giaddr outgoing-interface-address**](cmdqueryname=dhcp+relay+giaddr+outgoing-interface-address) command.
   
   In an inter-VPN scenario, if the DHCPv4 server supports the link-selection suboption of Option 82, you can perform this step to ensure that the DHCPv4 relay agent can search for a return route for reply messages based on the address specified by the giaddr field. If the DHCPv4 server does not support the link-selection suboption, this step cannot be performed. However, you can run the [**dhcp relay giaddr source-interface**](cmdqueryname=dhcp+relay+giaddr+source-interface) *interface-type* *interface-num* command on the DHCPv4 relay agent, configure the IP address of the source interface as the address specified by the giaddr field, and bind the source interface to the VPN where the server resides. This ensures that the return route is reachable.
   
   This step cannot be performed in a non-inter-VPN scenario, as doing so causes user access failures.
10. (Optional) Configure a source address and gateway address for the DHCPv4 relay agent.
    * Configure a source address for the DHCPv4 relay agent. DHCPv4 request and reply messages may travel along different paths. If such a case occurs, the relay agent discards a reply message because it cannot find user information. As a result, the client cannot go online. To resolve this issue, you can change the source address of DHCPv4 messages. After receiving a DHCPv4 request message, the relay agent fills the source address in the Source Address field in the IP header of the message. When the DHCPv4 server replies with a message, it searches for a route based on this address.
      ```
      [dhcp relay source-ip-address](cmdqueryname=dhcp+relay+source-ip-address) ip-address
      ```
      
      By default, the source address of a DHCPv4 relay agent is the primary IPv4 address of a relay interface.
    * Configure a gateway address for the DHCPv4 relay agent. Generally, a gateway address can be set to the primary or secondary IPv4 address of an interface. If VRRP is enabled on an interface, you must perform this step to forcibly specify a gateway address.
      ```
      [dhcp relay gateway](cmdqueryname=dhcp+relay+gateway) ip-address
      ```
      
      By default, no gateway address is configured, and the primary IPv4 address of an interface is used as the gateway address of a DHCPv4 relay agent.
11. (Optional) Configure abnormal packet detection.
    * Configure the device to check the magic cookie field in received DHCPv4 messages in the system view.
      ```
      [quit](cmdqueryname=quit)
      [dhcp anti-attack check magic-cookie](cmdqueryname=dhcp+anti-attack+check+magic-cookie)
      ```
    * Configure the device to check the magic cookie field in received DHCPv4 messages in the VLAN view.
      ```
      [quit](cmdqueryname=quit)
      [vlan](cmdqueryname=vlan) vlan-id
      [dhcp anti-attack check magic-cookie](cmdqueryname=dhcp+anti-attack+check+magic-cookie)
      ```
    * Configure the device to check the magic cookie field in received DHCPv4 messages in the interface view.
      ```
      [dhcp anti-attack check magic-cookie](cmdqueryname=dhcp+anti-attack+check+magic-cookie)
      ```
    * Configure the device not to check the UDP header checksum in received DHCPv4 messages in the system view.
      ```
      [quit](cmdqueryname=quit)
      undo [dhcp anti-attack check udp-checksum](cmdqueryname=dhcp+anti-attack+check+udp-checksum)
      ```
    * Configure the device not to check the UDP header checksum in received DHCPv4 messages in the VLAN view.
      ```
      [quit](cmdqueryname=quit)
      [vlan](cmdqueryname=vlan) vlan-id
      undo [dhcp anti-attack check udp-checksum](cmdqueryname=dhcp+anti-attack+check+udp-checksum)
      ```
    * Configure the device not to check the UDP header checksum in received DHCPv4 messages in the interface view.
      ```
      undo [dhcp anti-attack check udp-checksum](cmdqueryname=dhcp+anti-attack+check+udp-checksum)
      ```
    * Configure the device to carry the UDP header checksum in sent DHCPv4 messages in the system view.
      ```
      [quit](cmdqueryname=quit)
      [dhcp udp-checksum enable](cmdqueryname=dhcp+udp-checksum+enable)
      ```
    
    
    
    By default, a device does not check the magic cookie field in DHCPv4 messages and directly forwards those with incorrect magic cookie field values; a device checks the UDP header checksum in DHCPv4 messages and discards those with incorrect checksums.
12. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```
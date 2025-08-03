Configuring DHCP Relay
======================

After a DHCP relay agent is configured, it can forward DHCP Request messages from DHCP clients to the DHCP server on a different network segment.

#### Context

If the DHCP clients and DHCP server reside on different network segments, configure DHCP relay on an interface to forward DHCP Request messages from the DHCP clients to the DHCP server so that the clients can dynamically obtain IP addresses from the DHCP server.

When multiple clients are connected to the DHCP relay agent and multiple interfaces on the DHCP relay agent function as gateways, each gateway uses a public IP address, which wastes resources. If the relay interface on a routing device uses an unnumbered address as the gateway address, public IP address resources can be saved.

If a relay interface uses an unnumbered IP address, the DHCP relay agent performs the following operations to ensure DHCP message forwarding:

* The DHCP relay agent generates a user table for the users who go online from the relay interface and saves information, such as users' MAC addresses, online interface, and belonging VLAN.
* Upon receipt of a response message from the server, the DHCP relay agent searches the user table based on the chaddr field for the corresponding online interface and forwards the response message from this interface.

* In addition, after receiving the response message from the server, the DHCP relay agent generates two entries. In this way, when forwarding network-to-user traffic, the DHCP relay agent can find host routes based on the destination IP addresses (IP addresses assigned to users) and locate the outbound interfaces (user access interfaces) for DHCP response messages. Based on the ARP entries, the relay agent can obtain the MAC addresses of users.
  + ARP entry used to notify the ARP module of adding online users
  + Entry used to notify the route management module of delivering the user's host routes

#### Procedure

* Configure basic DHCP relay functions on a common interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**dhcp enable**](cmdqueryname=dhcp+enable)
     
     
     
     DHCP is enabled globally.
  3. (Optional) Run [**dhcp-server packet-distribute giaddr**](cmdqueryname=dhcp-server+packet-distribute+giaddr)
     
     
     
     The relay agent is enabled to distribute reply messages based on the GIADDR field value.
     
     
     
     In a scenario where a DHCP client applies for IP addresses from the DHCP server through a DHCP relay agent, if the DHCP client uses the same MAC address but different sub-interfaces to request for IP addresses in different network segments through the BRAS and DHCP relay agent, the DHCP relay agent may send return messages to the BAS user upon receipt of DHCP reply messages from the DHCP server. This is because the MAC address of the BRAS is the same as that of the DHCP relay agent. As a result, the DHCP relay user fails to go online. To address this problem, run the [**dhcp-server packet-distribute giaddr**](cmdqueryname=dhcp-server+packet-distribute+giaddr) command to enable the DHCP relay agent to determine whether to distribute the DHCP reply messages received from the DHCP server to the BAS user or DHCP relay user based on the GIADDR field value.
  4. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view is displayed.
  5. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
     
     
     
     The primary IP address is configured for the interface.
  6. (Optional) Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } **sub**
     
     
     
     The secondary IP address is configured for the interface.
  7. Run [**dhcp select relay**](cmdqueryname=dhcp+select+relay)
     
     
     
     DHCP relay is enabled on the interface.
  8. Run [**ip relay address**](cmdqueryname=ip+relay+address) *ip-address* [ **dhcp-option** { *code\_60* [ *option-text* ] | *code\_1to59* | *code\_61to254* } ]
     
     
     
     A DHCP server address is associated with the relay interface based on a DHCP option or Option 60.
  9. (Optional) Run [**ip relay giaddr**](cmdqueryname=ip+relay+giaddr) *ip-address* [ **dhcp-option** { *code\_60* [ *option-text* ] | *code\_1to59* | *code\_61to254* } ]
     
     
     
     A DHCP relay gateway address is configured for the interface.
  10. (Optional) Run [**dhcp relay source-ip-address**](cmdqueryname=dhcp+relay+source-ip-address) *ip-address* [ **dhcp-option** { *code\_60* [ *option-text* ] | *code\_1to59* | *code\_61to254* } ]
      
      
      
      A DHCP relay source IP address is configured for the interface.
  11. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
  12. (Optional) Run **[**dhcp rate-limit**](cmdqueryname=dhcp+rate-limit)** { **disable** | *rateLimitValue* }
      
      
      
      Global rate limiting is disabled for DHCP messages or a rate limit is configured for DHCP messages.
  13. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure basic DHCP relay functions on an unnumbered interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**dhcp enable**](cmdqueryname=dhcp+enable)
     
     
     
     DHCP is enabled globally.
  3. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The unnumbered interface view is displayed.
     
     
     
     Currently, an unnumbered interface can be an Ethernet physical interface, Ethernet physical sub-interface, VLANIF interface, and Ethernet trunk sub-interface.
  4. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
     
     
     
     The primary IP address of the interface is configured.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The interface view in which DHCP relay is to be enabled is displayed.
  7. Run [**ip address unnumbered**](cmdqueryname=ip+address+unnumbered) **interface** *interface-type interface-number*
     
     
     
     The unnumbered IP address of the relay interface is configured.
     
     
     
     The interface specified by the **interface** *interface-type interface-number* parameter must be the same as the unnumbered interface specified in Step 3.
  8. Run [**dhcp select relay**](cmdqueryname=dhcp+select+relay)
     
     
     
     DHCP relay is enabled on the interface.
  9. Run [**ip relay address**](cmdqueryname=ip+relay+address) *ip-address* [ **dhcp-option** { *code\_60* [ *option-text* ] | *code\_1to59* | *code\_61to254* } ]
     
     
     
     A DHCP server address is associated with the relay interface based on a DHCP option or Option 60.
  10. (Optional) Run [**ip relay giaddr**](cmdqueryname=ip+relay+giaddr) *ip-address* [ **dhcp-option** { *code\_60* [ *option-text* ] | *code\_1to59* | *code\_61to254* } ]
      
      
      
      A DHCP relay gateway address is configured for the interface.
  11. (Optional) Run [**dhcp relay source-ip-address**](cmdqueryname=dhcp+relay+source-ip-address) *ip-address* [ **dhcp-option** { *code\_60* [ *option-text* ] | *code\_1to59* | *code\_61to254* } ]
      
      
      
      A DHCP relay source IP address is configured for the interface.
  12. (Optional) Run [**dhcp option82 subscriber-id insert enable**](cmdqueryname=dhcp+option82+subscriber-id+insert+enable) **self-define** *self-define-value*
      
      
      
      The function to insert the Option 82 Subscriber-ID into DHCP request messages is enabled.
  13. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
  14. (Optional) Run **[**dhcp rate-limit**](cmdqueryname=dhcp+rate-limit)** { **disable** | *rateLimitValue* }
      
      
      
      Global rate limiting is disabled for DHCP messages or a rate limit is configured for DHCP messages.
  15. (Optional) Run [**dhcp relay arp user-detect interval**](cmdqueryname=dhcp+relay+arp+user-detect+interval) *interval*
      
      
      
      The ARP probe time for the DHCP relay user table is configured.
  16. (Optional) Perform the following steps as required:
      
      
      + To enable the DHCP relay agent to store user entries, run the [**dhcp relay unnumbered table autosave**](cmdqueryname=dhcp+relay+unnumbered+table+autosave) command.
        
        When DHCP relay users go online in address unnumbered scenarios, device faults may result in data loss. To prevent such loss, you can enable the DHCP relay agent to store user entries. In this case, the system generates a backup file **dhcpr\_user.dat** in the **/home/dhcp** directory.
      + To configure an interval at which the DHCP relay agent stores user entries, run the [**dhcp relay unnumbered table write-delay**](cmdqueryname=dhcp+relay+unnumbered+table+write-delay) *interval-value* command.
  17. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.

#### Follow-up Procedure

* (Optional) Run [**dhcp dscp-outbound**](cmdqueryname=dhcp+dscp-outbound) *dscp*
  
  The differentiated services code point (DSCP) value is set for DHCP messages.
* (Optional) Run [**dhcp ip-ttl**](cmdqueryname=dhcp+ip-ttl) *ttl-value*
  
  The time to live (TTL) value is set for DHCP messages.
* (Optional) Run [**dhcp relay reply broadcast-always**](cmdqueryname=dhcp+relay+reply+broadcast-always)
  
  The DHCP relay agent is enabled to broadcast response messages upon receipt of client requests.
* (Optional) Run [**dhcp option-82 ignore-hostname-match**](cmdqueryname=dhcp+option-82+ignore-hostname-match)
  
  The device is configured to ignore the host name matching check when parsing the Option 82 field.
  
  If dot1q or QinQ VLAN tag termination sub-interfaces are configured for user access and the messages exchanged between a client and a server are transmitted through different upstream and downstream paths, you can configure an upstream DHCP relay agent to insert the Option 82 field carrying user VLAN information to messages and configure a downstream DHCP relay agent to ignore the host name matching check so that users can successfully go online. However, the host name carried in the Option 82 is the host name of the upstream relay agent. Therefore, the downstream relay agent may fail to parse the Option 82 because the host name carried in the Option 82 is different from the host name of the local device. In this case, you need to configure the downstream relay agent to ignore the host name matching check, so that the user VLAN information can be correctly parsed from the Option 82.
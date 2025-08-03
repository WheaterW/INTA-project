Configuring IP Address Assignment
=================================

IP address assignment includes specifying such basic information as a gateway address and address segments, as well as configuring static binding.

#### Prerequisites

DHCP server packet receiving has been enabled using the [**dhcp server enable**](cmdqueryname=dhcp+server+enable) command on an interface if the interface needs to be used as a DHCP server.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* If multiple interfaces need to be used as DHCP servers, for security purposes, you are advised to preferentially run the [**dhcp server enable**](cmdqueryname=dhcp+server+enable) command on the interfaces to enable DHCP server packet receiving. If high security is not required, you run the [**dhcp server request-packet all-interface enable**](cmdqueryname=dhcp+server+request-packet+all-interface+enable) command in the system view to enable DHCP server packet receiving for all interfaces.
* If DHCP server packet receiving is not enabled, a DHCP server does not process DHCP request messages.


#### Context

After an address pool is created on the DHCP server, a gateway address and an address segment need to be specified, with the IP addresses in the address segment belonging to the gateway address segment. By default, all IP addresses in the address segment can be assigned to DHCP clients. If the NetBIOS server and DNS server reside in the address segment, fixed IP addresses need to be bound to the servers. Before such binding, the two IP addresses need to be removed from the address segment so that they will not be dynamically assigned to other DHCP clients.


#### Procedure

1. Configure the basic functions of IP address assignment.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. (Optional) Run **[**dhcp rate-limit**](cmdqueryname=dhcp+rate-limit)** { **disable** | *rateLimitValue* }
      
      
      
      Global rate limiting is disabled for DHCP messages or a rate limit is configured for DHCP messages.
   3. Run [**ip pool**](cmdqueryname=ip+pool) *ip-pool-name* [ **server** ]
      
      
      
      An address pool is created, and the address pool view is displayed.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      During first-time address pool creation, the **server** parameter must be specified. In the address pool view that is displayed after an address pool is created, the **server** parameter does not need to be specified.
   4. Run [**gateway**](cmdqueryname=gateway) *ip-address* { *mask* | *mask-length* }
      
      
      
      The gateway IP address and subnet mask of the address pool are configured.
      
      
      
      If a DHCP client requests an IP address from the DHCP server, the DHCP server notifies the DHCP client of the gateway address and subnet mask using Option 3 and Option 1.
   5. Run [**section**](cmdqueryname=section) *section-index* *start-ip-address* [ *end-ip-address* ]
      
      
      
      An address segment is configured for the address pool.
   6. (Optional) Run [**option router disable**](cmdqueryname=option+router+disable)
      
      
      
      The function of sending the gateway address to DHCP clients is disabled.
      
      When a carrier has high requirements on network security and does not want carriers to get aware of the gateway address, this command can be used to prohibit the DHCP server from sending DHCP clients Option 3 that contains the gateway address.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      After the DHCP is disabled from sending the gateway address, run the [**option33 route**](cmdqueryname=option33+route) command to allow DHCP clients to obtain the target route using Option 33.
   7. (Optional) Run [**option force-reply**](cmdqueryname=option+force-reply) { *option-code* } &<1-16>
      
      
      
      The DHCP option forcibly replied to a DHCP client by a DHCP server is configured.
      
      The DHCP server does not respond if the DHCP packets received from a DHCP client do not contain some DHCP option information. However, if such option information as option 6 (carrying the DNS server address) is not contained in DHCP packets, the DHCP client fails to be connected. To address the problem, such DHCP options need to be forcibly replied to a client by a DHCP server.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If the [**option router disable**](cmdqueryname=option+router+disable) command is used to disable the sending of Option 3 (gateway address) in addition to the [**option force-reply**](cmdqueryname=option+force-reply), the configuration of the [**option router disable**](cmdqueryname=option+router+disable) command takes effect preferentially due to a higher priority.
2. (Optional) Configure the static address assignment function.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ip pool**](cmdqueryname=ip+pool) *ip-pool-name* **server**
      
      
      
      An address pool is created, and its view is displayed.
   3. Run [**excluded-ip-address**](cmdqueryname=excluded-ip-address) *start-ip-address* [ *end-ip-address* ]
      
      
      
      The range of IP addresses that cannot be dynamically assigned in an address pool is specified.
      
      
      
      In network planning, some IP addresses need to be assigned to specified hosts, such as the DNS and WWW servers, for long-term use. In this case, you can run this command to configure the range of IP addresses that do not participate in automatic IP address assignment. Repeat this command as needed to specify multiple ranges of IP addresses.
   4. Run [**static-bind**](cmdqueryname=static-bind) **ip-address** *ip-address* **mac-address** *mac-address*
      
      
      
      The static address assignment function is configured.
      
      
      
      Fixed IP addresses need to be assigned to specified clients, such as the WWW server. In this case, you can bind an available IP address in an address pool with the MAC address of a client.
3. (Optional) Configure IP address assignment based on Option 60.
   1. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
   2. Run [**dhcp server base-option60 enable**](cmdqueryname=dhcp+server+base-option60+enable)
      
      
      
      The DHCP server is enabled to assign IP addresses based on Option 60.
      
      
      
      If no relay agent exists between the DHCP server and DHCP clients, configure the DHCP server to assign IP addresses to DHCP clients in different network segments or VPNs based on the Option 60 information carried in packets sent by the DHCP clients.
   3. Run [**ip pool**](cmdqueryname=ip+pool) *ip-pool-name* [ **server** ]
      
      
      
      The address pool view is displayed.
   4. Run [**client-option60**](cmdqueryname=client-option60) *option60-text*
      
      
      
      The Option 60 information is configured in the server address pool.
      
      
      
      If the *option60-text* parameter configured for a server address pool matches the Option 60 information carried in the packets sent by DHCP clients, the DHCP server assigns IP addresses from the address pool. Otherwise, the DHCP server assigns IP addresses based on the gateway address.
4. (Optional) Run [**dhcp reply**](cmdqueryname=dhcp+reply) { **unicast-always** | **broadcast-always** }
   
   
   
   The type of the packets sent by the DHCP server as a reply is specified.
5. (Optional) Run [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name*
   
   
   
   A VPN instance is configured for the address pool.
   
   
   
   If a VPN has the DHCP service, the address pool created on the DHCP server needs to be bound to a VPN instance.
6. (Optional) Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. (Optional) Run [**dhcp server identifier dest-ip**](cmdqueryname=dhcp+server+identifier+dest-ip)
   
   
   
   The DHCP server is enabled to use the destination IP address in the packet forwarded by the DHCP relay as the server identifier.
   
   
   
   This command is used when a DHCP client is connected to a DHCP relay (first PE) over a VPN and the DHCP relay sends a DHCP request to the DHCP server (second PE). The DHCP server assigns an IP address to the DHCP client over the VPN. The server IP address specified by the DHCP server is generally the IP address of a non-public interface on the DHCP server, but the DHCP request is received by a public interface on the DHCP server. By default, the DHCP server uses the inbound interface IP address in the DHCP request (public interface IP address) as the server identifier. As a result, the DHCP client fails to extend the lease. To address this problem, run the dhcp server identifier dest-ip command to enable the DHCP server to use the destination IP address in the packet forwarded by the DHCP relay as the server identifier.
8. (Optional) Run [**dhcp server option82 link-selection enable**](cmdqueryname=dhcp+server+option82+link-selection+enable)
   
   
   
   The DHCP server is enabled to assign IP addresses based on the Option 82 suboption Link Selection.
9. (Optional) Run [**dhcp server option82 server-id-override enable**](cmdqueryname=dhcp+server+option82+server-id-override+enable)
   
   
   
   The DHCP server is enabled to fill the Option 82 suboption Server Identifier Override in Option 54.
10. (Optional) Run [**dhcp server ping**](cmdqueryname=dhcp+server+ping) { **packets** *packet-number* | **timeout** *timeout-interval* }
    
    
    
    The maximum number of ping packets that a DHCP server sends and the maximum timeout period of each ping reply are set.
    
    
    
    Before assigning an IP address to a DHCP client, the DHCP server must ping the IP address to check whether this IP address is being used. This prevents address conflicts.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
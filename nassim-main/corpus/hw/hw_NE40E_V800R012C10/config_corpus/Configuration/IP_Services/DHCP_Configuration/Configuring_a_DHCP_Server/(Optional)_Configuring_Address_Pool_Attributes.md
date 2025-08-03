(Optional) Configuring Address Pool Attributes
==============================================

Configuring address pool attributes includes specifying an IP address lease, configuring the application server address and customized items. The address pool attributes are contained in option information that is sent by the DHCP server to clients.

#### Prerequisites

DHCP server packet receiving has been enabled using the [**dhcp server enable**](cmdqueryname=dhcp+server+enable) command on an interface if the interface needs to be used as a DHCP server.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* If multiple interfaces need to be used as DHCP servers, for security purposes, you are advised to preferentially run the [**dhcp server enable**](cmdqueryname=dhcp+server+enable) command on the interfaces to enable DHCP server packet receiving. If high security is not required, you run the [**dhcp server request-packet all-interface enable**](cmdqueryname=dhcp+server+request-packet+all-interface+enable) command in the system view to enable DHCP server packet receiving for all interfaces.
* If DHCP server packet receiving is not enabled, a DHCP server does not process DHCP request messages.


#### Procedure

* Configure an address lease.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip pool**](cmdqueryname=ip+pool) *ip-pool-name* **server**
     
     
     
     The address pool view is displayed.
  3. Run [**lease**](cmdqueryname=lease) *days* [ *hours* [ *minutes* ] ]
     
     
     
     An address lease is configured.
     
     
     
     A DHCP server can assign a specific lease to IP addresses in each address pool. All addresses in the same address pool must have the same lease.
  4. Run [**renewal-time**](cmdqueryname=renewal-time) *days* [ *hours* [ *minutes* ] ]
     
     
     
     The renewal time of IP addresses is specified.
  5. Run [**rebinding-time**](cmdqueryname=rebinding-time) *days* [ *hours* [ *minutes* ] ]
     
     
     
     The rebinding time of IP addresses is specified.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure well-known options.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip pool**](cmdqueryname=ip+pool) *ip-pool-name* **server**
     
     
     
     The address pool view is displayed.
  3. Run [**sip-server**](cmdqueryname=sip-server) { { **ip-address** *ip-address* } &<1-2> | { **list** *server-name* } &<1-2> }
     
     
     
     The IP address or name of the SIP server is configured.
     
     
     
     The establishment of multimedia sessions between DHCP clients requires a SIP server to complete user locating, authentication, and authorization.
     
     The DHCP server notifies DHCP clients of the SIP server address through Option 120.
  4. Run [**netbios-name-server**](cmdqueryname=netbios-name-server) *ip-address* &<1-8>
     
     
     
     The NetBIOS server address is configured.
     
     
     
     For Microsoft DHCP clients, the NetBIOS server needs to be used to resolve a domain name to an IP address.
     
     The DHCP server notifies DHCP clients of the NetBIOS server address through Option 44.
  5. Run [**netbios-type**](cmdqueryname=netbios-type) { **b-node** | **h-node** | **m-node** | **p-node** }
     
     
     
     The NetBIOS node type is specified.
  6. Run [**dns-server**](cmdqueryname=dns-server) *ip-address* &<1-8>
     
     
     
     A DNS server address is specified.
     
     
     
     Before a host accesses the Internet, the DNS server needs to be used to resolve a domain name to an IP address.
     
     The DHCP server notifies DHCP clients of the DNS server address through Option 6.
  7. Run [**dns-suffix**](cmdqueryname=dns-suffix) *suffix-name*
     
     
     
     A DNS suffix is specified.
     
     
     
     A DHCP client adds a DNS suffix to the domain name and sends it to the DNS server for domain name resolution.
     
     The DHCP server sends DHCP clients the domain name suffix through Option 15.
  8. Run [**domain-search-list**](cmdqueryname=domain-search-list) *domain-name*
     
     
     
     A search domain name is specified.
     
     
     
     When the first-time domain name resolution for a DHCP client fails, the search domain name needs to be added for another resolution.
     
     The DHCP server sends DHCP clients the search domain name through Option 119.
  9. Run [**option33 route**](cmdqueryname=option33+route) *dest-ip* *gateway*
     
     
     
     A user route is configured.
     
     
     
     After the [**option router disable**](cmdqueryname=option+router+disable) command is executed to disable the DHCP server from sending the gateway address, a user route can be configured to allow DHCP clients to obtain routes towards the target network.
  10. Run [**option121**](cmdqueryname=option121) **ip-address** { *ip-address* *mask-length* *gateway-address* } &<1-8>
      
      
      
      A classless static route that a DHCP server assigns to a DHCP client is specified.
  11. Run [**dhcp option125**](cmdqueryname=dhcp+option125) [ **enterprise-code** *enterprise-code* ] *option125-string*
      
      
      
      The enterprise code and string of Option 125 are specified.
  12. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure private options.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ip pool**](cmdqueryname=ip+pool) *ip-pool-name* **server**
     
     
     
     The address pool view is displayed.
  3. Run [**option**](cmdqueryname=option) *code* { **ip** { *ip-address* } &<1-2> | **string** *ascii-string* | **hex** *hex-string* | **cipher** *cipher-text* }
     
     
     
     DHCP sub-options are configured.
     
     
     
     This command can define well-known options except for options 3, 6, 15, 44, 46, 50-55, 57-59, 61, 82, and 119. For configuration details, refer to standard protocols.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) Customizing the following well-known options is not recommended:
     + If both this command and the [**dhcp option125**](cmdqueryname=dhcp+option125) command customize Option 125, the configuration of the latter command takes effect.
     + If both this command and the [**option33 route**](cmdqueryname=option33+route) command customize Option 33, the configuration of the latter command takes effect.
     + If both this command and the [**option121**](cmdqueryname=option121) command customize Option 121, the configuration of the latter command takes effect.
  4. Run [**dhcp client-option**](cmdqueryname=dhcp+client-option) *client-code* *client-string* **reply-option** *reply-code* { **suboption** *reply-sub-code* { **ip** *ip-address* | **string** *ascii-string* | **hex** *hex-string* } } &<1-16>
     
     
     
     An option that will be sent as a reply to a user request is specified.
     
     
     
     Currently, an option will be sent as a reply only to a user request that contains Option 60.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
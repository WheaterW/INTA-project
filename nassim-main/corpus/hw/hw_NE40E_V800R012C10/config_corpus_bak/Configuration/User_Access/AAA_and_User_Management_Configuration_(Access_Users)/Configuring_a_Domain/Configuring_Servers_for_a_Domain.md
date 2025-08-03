Configuring Servers for a Domain
================================

You can configure servers, such as RADIUS and DNS servers, for a domain as required.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. (Optional) Run [**radius-server llid-first-authentication group**](cmdqueryname=radius-server+llid-first-authentication+group) *group-name*
   
   
   
   A RADIUS server group for the first LLID authentication is configured.
5. Configure a web authentication server.
   1. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
      
      
      
      A RADIUS server group is specified for the domain.
   2. Run [**web-server**](cmdqueryname=web-server) { **url** *url* [ **slave** ] | **url-parameter** | *ip-address* [ *ipv6âaddress* ] [ **slave** ] | **mode** { **get** | **post** } | **redirect-key** { **mscg-ip** *mscg-ip-key* | **mscg-name** *mscg-name-key* | **user-ip-address** *user-ip-key* | **user-location** *user-location-key* } | **user-first-url-key** { *key-name* | **default-name** } | { *ip-address* [ *ipv6âaddress* ] | **url** *url* } **bind web-auth-server** *ip-address* [ **vpn-instance** *vpn-instance* ] **slave** }
      
      
      
      A mandatory web authentication server is specified for the domain.
   3. (Optional) Run [**web-server**](cmdqueryname=web-server) **redirect-key** **subscription-id** *subscription-id*
      
      
      
      The device is enabled to add the Option 82 information to the URL string in a redirection packet to be sent to a user.
6. Configure a DNS server.
   1. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
      
      
      
      A RADIUS server group is specified for the domain.
   2. Run [**dns**](cmdqueryname=dns) { **primary-ip** |**second-ip** } *ip-address*
      
      
      
      The primary or secondary DNS server is specified for the domain.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If IP addresses are automatically allocated from the BAS address pool, the DNS server can be configured in both the domain view and the address pool view, but the configuration in the domain view takes precedence.
      
      The IP address of the DNS server for user access can be delivered by the RADIUS server, configured in the AAA domain view, or configured in the address pool view. The DNS server address configured in the AAA domain view has a higher priority than that configured in the address pool view but has a lower priority than that delivered by the RADIUS server.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
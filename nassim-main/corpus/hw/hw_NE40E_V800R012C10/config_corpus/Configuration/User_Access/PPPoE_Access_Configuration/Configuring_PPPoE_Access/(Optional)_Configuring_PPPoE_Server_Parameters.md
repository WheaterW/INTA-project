(Optional) Configuring PPPoE Server Parameters
==============================================

PPPoE server parameters can be configured as needed for
negotiation between a PPPoE server and client.

#### Context

PPPoE uses the client/server model. A PPPoE client initiates
a connection request to a PPPoE server. After a session is established,
the PPPoE server provides access control and authentication for the
PPPoE client. To help clients identify PPPoE servers, configure a
name, service name, and service name matching mode for each PPPoE
server. To allow successful PPPoE negotiation between Huawei and non-Huawei
devices, configure conditions for sending PADM or PADN packets and a delimiter between MOTM items.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface virtual-template**](cmdqueryname=interface+virtual-template) *virtual-template-number*
   
   
   
   A VT is created and its view is displayed, or the view of
   an existing VT is displayed.
3. Run [**pppoe-server ac-name**](cmdqueryname=pppoe-server+ac-name) *ac-name*
   
   
   
   A name is configured for the PPPoE server.
4. Run [**pppoe-server service-name-parameter**](cmdqueryname=pppoe-server+service-name-parameter) *service-name-parameter*
   
   
   
   A service name is configured for the PPPoE server.
5. Run [**pppoe-server service-name-type**](cmdqueryname=pppoe-server+service-name-type) **exact-match**
   
   
   
   A service name matching mode is configured.
6. Run [**pppoe-server send**](cmdqueryname=pppoe-server+send) { **padm** | **padn** } [ **ipcp** | **ip6cp** | { **first** | **last** | **all** } **ncp** ]
   
   
   
   Conditions for sending PADM or PADN packets are configured.
7. Run [**pppoe-server motm item delimiter**](cmdqueryname=pppoe-server+motm+item+delimiter) *delimiter*
   
   
   
   A delimiter between MOTM items is configured.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. Run [**pppoe-server send padt always**](cmdqueryname=pppoe-server+send+padt+always)
   
   
   
   Delayed PADT packet transmission is enabled.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
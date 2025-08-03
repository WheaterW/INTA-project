Specifying Candidate PCE Servers for a PCE Client
=================================================

One or more candidate PCE servers can be specified to compute paths for a PCE client. If multiple such servers are specified, they work in backup mode, improving network reliability.

#### Usage Scenario

PCEP involves two PCE roles â PCE server and PCE client. To specify a candidate PCE server for a PCE client, you need to run the [**connect-server**](cmdqueryname=connect-server) command. A PCE client supports multiple candidate PCE servers.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   The PCE client view is displayed.
3. Run [**connect-server**](cmdqueryname=connect-server) *ip-address*
   
   
   
   A candidate PCE server is configured for the PCE client, and the PCE server connection view is displayed.
   
   
   
   The *ip-address* parameter specifies the source IP address of the PCE server. You can repeat this step to configure multiple candidate PCE servers for backup purposes.
4. (Optional) Run [**preference**](cmdqueryname=preference) *preference*
   
   
   
   A preference is configured for the candidate PCE server.
   
   
   
   The value of *preference* is an integer ranging from 0 to 7. A larger value indicates a higher preference.
   
   You can configure multiple candidate PCE servers for a PCE client and specify different preferences for these servers. The candidate PCE server with the highest preference is preferentially selected for path computation.
   
   If no preference is specified, the default value 0 is used to indicate the lowest preference. If multiple PCE servers have the same preference, the PCE server with the smallest IP address is preferentially selected for path computation.
5. (Optional) Run [**source-interface**](cmdqueryname=source-interface) *port-type* *port-num*
   
   
   
   A source IP address is configured for the PCEP session.
   
   
   
   By default, the PCEP session is established using the MPLS LSR-ID as the source IP address. In scenarios where the MPLS LSR-ID is unreachable, you can run this command to borrow the IP address of another local interface as the source IP address.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
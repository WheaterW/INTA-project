Configuring PCEP Delegation
===========================

This section describes how to establish a PCEP session between the PCC and PCE so that the PCC can send path computation requests to the PCE and receive SR-MPLS TE Policy information from the PCE.

#### Context

If the PCC has delegated the control permission to the PCE, the PCE recomputes a path when network information (e.g., topology information) or ODN template information changes. The PCE sends a PCUpd message to deliver information about the recomputed path to the PCC and uses the PLSP-ID reported by the PCC as an identifier. After receiving the PCUpd message delivered by the PCE, the PCC (headend) updates the path.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pce-client**](cmdqueryname=pce-client)
   
   
   
   The device is configured as a PCE client, and the PCE client view is displayed.
3. Run [**capability segment-routing**](cmdqueryname=capability+segment-routing)
   
   
   
   The PCE client is enabled to process SR-MPLS TE Policies.
4. Run [**connect-server**](cmdqueryname=connect-server) *ip-address*
   
   
   
   A candidate PCE server is configured for the PCE client, and the PCE server connection view is displayed.
   
   
   
   The *ip-address* parameter specifies the source IP address of the PCE server. You can repeat this step to configure multiple candidate servers for backup purposes.
5. (Optional) Run [**preference**](cmdqueryname=preference) *preference*
   
   
   
   A preference is configured for the candidate PCE server.
   
   
   
   The value of *preference* is an integer ranging from 0 to 7. A larger value indicates a higher preference.
   
   You can configure multiple candidate PCE servers for a PCE client and specify different preferences for these servers. The candidate PCE server with the highest preference is preferentially selected for path computation.
   
   If no preference is specified, the default value 0 is used to indicate the lowest preference. If multiple PCE servers have the same preference, the PCE server with the smallest IP address is preferentially selected for path computation.
6. (Optional) Run [**source-interface**](cmdqueryname=source-interface) *port-type* *port-num*
   
   
   
   A source IP address is configured for the PCEP session.
   
   
   
   By default, the PCEP session is established using the MPLS LSR-ID as the source IP address. In scenarios where the MPLS LSR-ID is unreachable, you can run this command to borrow the IP address of another local interface as the source IP address.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Follow-up Procedure

For more PCEP-related configurations, see [Configuring PCEP to Trigger SR-MPLS TE Policy Establishment](dc_vrp_pcep_cfg_0022.html).
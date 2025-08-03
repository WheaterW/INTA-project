(Optional) Configuring an LSR ID for a Remote LDP session
=========================================================

To isolate services, configure an LSR ID for each remote LDP session.

#### Context

A remote LDP session can be established between two indirectly connected LSRs or two adjacent LSRs. Both a local LDP session and a remote LDP session can be established between two LSRs. When a local LDP session and a remote LDP session are established between two LSRs, the configurations that both the local and remote LDP sessions support must be the same. The L2VPN/L3VPN services that pass through the LSPs between the two LSRs cannot be isolated from each other. To address this problem, you can specify a local LSR ID for each LDP session.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp remote-peer**](cmdqueryname=mpls+ldp+remote-peer) *remote-peer-name*
   
   
   
   The remote MPLS-LDP peer view is displayed.
3. Run [**mpls ldp local-lsr-id**](cmdqueryname=mpls+ldp+local-lsr-id) *interface-type* *interface-number*
   
   
   
   The primary IP address of a specified interface is used as a local LSR ID for the current LDP session.
   
   If both a local and remote LDP sessions are to be established between an LSR pair, LSR IDs configured for the two sessions must be the same. Otherwise, only the LDP session that finds the adjacency first can be established.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Execution of this command resets the current remote LDP session. The reset remote LSP session uses the new LSR ID.
Configuring an LDP LSP on an IPv4 Network
=========================================

An LDP LSP is configured on an IPv4/MPLS backbone network to forward IPv6 packets.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls lsr-id**](cmdqueryname=mpls+lsr-id) *lsr-id*
   
   
   
   An LSR ID is configured.
3. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled and the MPLS view is displayed.
4. (Optional) Run [**lsp-trigger**](cmdqueryname=lsp-trigger+all+host+ip-prefix+none) { **all** | **host** | **ip-prefix** *ip-prefix-name* | **none** }
   
   
   
   An LSP triggering policy is configured.
   
   
   
   Currently, the NE40E automatically distributes labels to host routes with 32-bit masks. This step is required if labels need to be distributed to other types of routes or only to specified routes.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   LDP is enabled.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
9. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   MPLS is enabled on the interface.
10. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
    
    
    
    LDP is enabled on the interface.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
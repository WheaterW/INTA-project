Configuring an LDP Entropy Label on the Ingress of an LSP
=========================================================

An LDP entropy label can be configured on the ingress of an LSP to implement load balancing.

#### Context

The growth of user networks worsens the load imbalance on transit nodes. To address this problem, the entropy label capability can be configured on the ingress of an LSP. After an LDP tunnel with the entropy label capability is negotiated using LDP, forwarding entries can carry the flag that supports the entropy label capability to implement load balancing.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**entropy-label enable**](cmdqueryname=entropy-label+enable)
   
   
   
   An LDP entropy label capability is enabled on the ingress of an LSP.
4. (Optional) To configure LDP to negotiate the entropy label capability only based on the primary LSP, perform the following steps:
   1. Run the [**ipv4-family**](cmdqueryname=ipv4-family) command to enter the MPLS-LDP-IPv4 view.
   2. Run the [**entropy-label negotiate primary-lsp-only**](cmdqueryname=entropy-label+negotiate+primary-lsp-only+ip-prefix) [ **ip-prefix** *ip-prefix-name* ] command to configure LDP to negotiate the entropy label capability only based on the primary LSP.
      
      
      
      If there are primary and backup paths, you can perform this step on the ingress or transit node of an LSP to prevent an LDP tunnel entropy label negotiation failure.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
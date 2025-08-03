Configuring a Mode for BIER-MPLS to Process and Adjust TTLs
===========================================================

This section describes how to configure a mode for BIER-MPLS to process TTLs and adjust the TTL value.

#### Context

The header of each BIER tunnel packet has a 4-byte MPLS label. You can configure BIER-MPLS to process TTLs in pipe mode and adjust the TTL value in pipe mode on the ingress of a BIER tunnel as required.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bier**](cmdqueryname=bier)
   
   
   
   The BIER view is displayed.
3. Run [**sub-domain**](cmdqueryname=sub-domain) *sub-domain-val*
   
   
   
   The BIER sub-domain view is displayed.
4. Run [**bier pipe-mode ttl**](cmdqueryname=bier+pipe-mode+ttl) *ttl-value*
   
   
   
   BIER-MPLS is configured to process TTLs in pipe mode, and the TTL value in pipe mode is adjusted.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
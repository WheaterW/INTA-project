(Optional) Configuring User Authentication on the LNS
=====================================================

Generally, access L2TP users are authenticated on a LAC and do not need to be authenticated on an LNS again. However, if the LNS does not trust the LAC, the users need to be authenticated again on the LNS after the connections between the users and the LNS are established.

#### Context

Authentication on an LNS involves mandatory PPP LCP re-negotiation and CHAP authentication.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
   
   
   
   An L2TP group is created, and its view is displayed.
3. Run [**mandatory-lcp**](cmdqueryname=mandatory-lcp) [ **on-mismatch** [ **strict** ] ]
   
   
   
   Mandatory LCP re-negotiation is performed.
4. Run [**mandatory-chap**](cmdqueryname=mandatory-chap)
   
   
   
   Mandatory CHAP authentication is performed.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
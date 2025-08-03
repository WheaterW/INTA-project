Configuring SRv6 TE Policy Status Advertisement to BGP-LS
=========================================================

Configure a forwarder to advertise SRv6 TE Policy status to BGP-LS. BGP-LS can then advertise the status to peers.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
   
   
   
   SRv6 is enabled, and the SRv6 view is displayed.
3. Run [**srv6-te-policy bgp-ls enable**](cmdqueryname=srv6-te-policy+bgp-ls+enable)
   
   
   
   The forwarder is enabled to advertise SRv6 TE Policy status to BGP-LS.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
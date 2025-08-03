Configuring OSPFv3 to Report Network Topology Information to BGP-LS
===================================================================

After OSPFv3 topology information is advertised to BGP-LS, BGP-LS reports the information to a controller, which implements path planning.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   OSPFv3 is enabled, and the OSPFv3 view is displayed.
3. Run [**bgp-ls enable**](cmdqueryname=bgp-ls+enable)
   
   
   
   The OSPFv3 process is enabled to advertise topology information.
4. Run [**bgp-ls identifier**](cmdqueryname=bgp-ls+identifier) [ *identifier-value* ]
   
   
   
   OSPFv3 topology advertisement is configured, and a topology ID is specified.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
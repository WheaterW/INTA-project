Configuring OSPFv3 Sham Hello
=============================

With OSPFv3 sham hello, device can exchange Hello and LSU and LSAck packets to maintain OSPFv3 neighbor relationships, which strengthens the neighbor detection mechanism.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
   
   
   
   The OSPFv3 view is displayed.
3. Run [**sham-hello enable**](cmdqueryname=sham-hello+enable)
   
   
   
   OSPFv3 sham hello is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
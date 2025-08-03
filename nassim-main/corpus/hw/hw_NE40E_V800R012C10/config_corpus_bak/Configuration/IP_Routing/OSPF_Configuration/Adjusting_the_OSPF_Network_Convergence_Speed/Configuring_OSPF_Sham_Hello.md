Configuring OSPF Sham Hello
===========================

With OSPF sham hello, device can exchange Hello and LSU and LSAck packets to maintain OSPF neighbor relationships, which strengthens the neighbor detection mechanism.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**sham-hello enable**](cmdqueryname=sham-hello+enable)
   
   
   
   OSPF sham hello is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
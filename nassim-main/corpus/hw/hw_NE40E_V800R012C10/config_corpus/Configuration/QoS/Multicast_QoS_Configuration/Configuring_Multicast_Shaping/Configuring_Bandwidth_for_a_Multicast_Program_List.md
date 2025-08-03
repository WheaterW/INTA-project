Configuring Bandwidth for a Multicast Program List
==================================================

You can perform multicast shaping on specific multicast programs by setting the CIR and PIR.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast shaping**](cmdqueryname=multicast+shaping)
   
   
   
   The multicast shaping view is displayed.
3. Run [**multicast-list**](cmdqueryname=multicast-list) { **name** *list-name* | **list-index** *start-index* [ *end-index* ] } **cir** *cir-value* [ **pir** *pir-value* ] [ **queue-length** *queue-length* ] [ **car-mode** ]
   
   
   
   Bandwidth is configured for the multicast program list.
   
   
   
   The **car-mode** parameter is not supported on the NE40E-M2E/NE40E-M2F/NE40E-M2H.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
Configuring an OSPF Interface to Automatically Adjust the Link Cost
===================================================================

Configuring an OSPF interface to automatically adjust the link cost based on link quality facilitates route selection control and improves network reliability.

#### Context

A bit error refers to the deviation between a bit that is sent and the bit that is received. The bit error rate (BER) refers to the number of bit errors divided by the total number of bits transferred during a studied time interval. During data transmission, a high BER will degrade or even interrupt services in extreme cases.

To prevent this problem, configure OSPF interfaces to automatically adjust link costs based on link quality so that unreliable links are not used by the optimal routes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
   
   
   
   OSPF is enabled on the interface.
4. Run [**ospf link-quality**](cmdqueryname=ospf+link-quality) **low** **incr-cost** { *cost* | **max-reachable** }
   
   
   
   The OSPF interface is configured to automatically adjust the link cost based on link quality.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The *cost* parameter specifies the link cost adjustment value. After this parameter is specified:
   
   * If the link quality changes to **low**, the link cost equals the original link cost plus the adjustment value. The maximum link cost allowed is 65535.
   * If the link quality recovers from **low**, the original link cost applies.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
Configuring an OSPFv3 Interface to Automatically Adjust the Link Cost
=====================================================================

Configuring an OSPFv3 interface to automatically adjust the link cost based on link quality facilitates route selection control and improves network reliability.

#### Context

A bit error refers to the deviation between a bit that is sent and the bit that is received. The bit error rate (BER) refers to the number of bit errors divided by the total number of bits transferred during a studied time interval. During data transmission, a high BER will degrade or even interrupt services in extreme cases.

To prevent this problem, configure OSPFv3 interfaces to automatically adjust link costs based on link quality so that unreliable links are not used by the optimal routes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled on the interface.
4. Run [**ospfv3**](cmdqueryname=ospfv3) *process-id* **area** *area-id* [ **instance** *instance-id* ]
   
   
   
   OSPFv3 is enabled on the interface.
5. Run [**ospfv3 link-quality**](cmdqueryname=ospfv3+link-quality) **low** **incr-cost** { *cost* | **max-reachable** } [ **instance** *instance-id* ]
   
   
   
   The OSPFv3 interface is enabled to automatically adjust the link cost based on link quality.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The *cost* parameter specifies the link cost adjustment value. After this parameter is specified:
   
   * If the link quality changes from good to low, the link cost equals the original link cost plus the adjustment value. The maximum link cost allowed is 65535.
   * If the link quality changes from low to good, the original link cost applies.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
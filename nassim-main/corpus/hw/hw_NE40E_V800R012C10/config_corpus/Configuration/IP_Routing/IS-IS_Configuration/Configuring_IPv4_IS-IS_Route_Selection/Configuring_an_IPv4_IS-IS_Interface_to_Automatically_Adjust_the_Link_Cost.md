Configuring an IPv4 IS-IS Interface to Automatically Adjust the Link Cost
=========================================================================

Configuring an IS-IS interface to automatically adjust the link cost based on link quality facilitates route selection control and improves network reliability.

#### Context

A bit error refers to the deviation between a bit that is sent and the bit that is received. The bit error rate (BER) refers to the number of bit errors divided by the total number of bits transferred during a studied time interval. During data transmission, a high BER may degrade or even interrupt services.

To prevent this problem, configure IS-IS interfaces to automatically adjust link costs based on link quality so that unreliable links are not used by the optimal routes.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**isis enable**](cmdqueryname=isis+enable) [ *process-id* ]
   
   
   
   IS-IS is enabled on the interface.
4. Run [**isis link-quality**](cmdqueryname=isis+link-quality) **low** **incr-cost** { *cost-value* | **max-reachable** }
   
   
   
   The IS-IS interface is configured to automatically adjust the link cost based on link quality.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) The *cost* parameter specifies the link cost adjustment value. After this parameter is specified:
   * If the link quality changes to **low**, the link cost equals the sum of the original link cost and the incremental cost. If the sum exceeds the maximum link cost allowed, the maximum link cost allowed is used.
     + The maximum link cost is 63, if the cost style is narrow, narrow-compatible, or compatible.
     + The maximum link cost is 16777214, if the cost style is wide or wide-compatible.
   * When the link quality recovers from **low**, the link cost of the interface is restored to the original value (the one before *cost* was added).
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
Configuring an IPv6 IS-IS Interface to Automatically Adjust the Link Cost
=========================================================================

Configuring an IPv6 IS-IS interface to automatically adjust the link cost based on link quality facilitates route selection control and improves network reliability.

#### Context

A bit error refers to the deviation between a bit that is sent and the bit that is received. The bit error rate (BER) refers to the number of bit errors divided by the total number of bits transferred during a studied time interval. During data transmission, a high BER may degrade or even interrupt services.

To prevent this problem, configure IPv6 IS-IS interfaces to automatically adjust link costs based on link quality so that unreliable links are not used by the optimal routes.


#### Procedure

* Perform the following steps for a conventional IS-IS process:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable) **topology** **ipv6**
     
     
     
     IPv6 is enabled for the IS-IS process.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  6. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
     
     
     
     IPv6 is enabled on the interface.
  7. Run [**isis ipv6 enable**](cmdqueryname=isis+ipv6+enable) [ *process-id* ]
     
     
     
     IPv6 IS-IS is enabled on the interface, and the specified process ID is associated with the interface.
  8. Run [**isis**](cmdqueryname=isis) **ipv6** **link-quality** **low** **incr-cost** { *cost-value* | **max-reachable** }
     
     
     
     The IPv6 IS-IS interface is enabled to automatically adjust the link cost based on link quality.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) The *cost* parameter specifies the link cost adjustment value. After this parameter is specified:
     + If the link quality changes from good to low, the link cost equals the original link cost plus the adjustment value. If the new link cost exceeds the maximum link cost allowed, the maximum link cost allowed applies:
       - The maximum link cost is 63, if the cost style is **narrow**, **narrow-compatible**, or **compatible**.
       - The maximum link cost is 16777214, if the cost style is **wide** or **wide-compatible**.
     + If the link quality changes from low to good, the original link cost applies.
  9. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Perform the following steps for an IS-IS multi-instance process:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
     
     
     
     The IS-IS view is displayed.
  3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable) **topology** **ipv6**
     
     
     
     IPv6 is enabled for the IS-IS process.
  4. Run [**multi-instance enable iid**](cmdqueryname=multi-instance+enable+iid) *iid-value*
     
     
     
     The conventional IS-IS process is configured as an IS-IS multi-instance process.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the system view.
  6. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  7. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
     
     
     
     IPv6 is enabled on the interface.
  8. Run [**isis ipv6 enable**](cmdqueryname=isis+ipv6+enable) [ *process-id* ]
     
     
     
     IPv6 IS-IS is enabled on the interface, and the specified process ID is associated with the interface.
  9. Run [**isis**](cmdqueryname=isis) [ **process-id** *process-id* ] **ipv6** **link-quality** **low** **incr-cost** { *cost-value* | **max-reachable** }
     
     
     
     The IPv6 IS-IS interface is enabled to automatically adjust the link cost based on link quality.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) The *cost* parameter specifies the link cost adjustment value. After this parameter is specified:
     + If the link quality changes from good to low, the link cost equals the original link cost plus the adjustment value. If the new link cost exceeds the maximum link cost allowed, the maximum link cost allowed applies:
       - The maximum link cost is 63, if the cost style is **narrow**, **narrow-compatible**, or **compatible**.
       - The maximum link cost is 16777214, if the cost style is **wide** or **wide-compatible**.
     + If the link quality changes from low to good, the original link cost applies.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
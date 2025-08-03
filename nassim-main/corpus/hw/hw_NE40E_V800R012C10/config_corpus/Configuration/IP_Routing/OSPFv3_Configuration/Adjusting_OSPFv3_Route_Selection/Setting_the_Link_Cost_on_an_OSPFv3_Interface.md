Setting the Link Cost on an OSPFv3 Interface
============================================

OSPFv3 can automatically calculate the link cost for an interface based on the interface bandwidth. You can also set the link cost for the interface.

#### Context

You can control the route cost by setting different link costs for OSPFv3 interfaces.

Perform the following steps on the router that runs OSPFv3:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospfv3 cost**](cmdqueryname=ospfv3+cost)*value* [ **instance***instanceId* ]
   
   
   
   The link cost is set on the OSPFv3 interface.
   
   
   
   If you do not set the cost of an OSPFv3 interface using the [**ospfv3 cost**](cmdqueryname=ospfv3+cost) *cost* command, OSPFv3 automatically calculates the cost for the interface based on the interface bandwidth. The calculation formula is as follows: Cost of the interface = Bandwidth reference value/Interface bandwidth. The integer of the calculated result is the cost of the interface. If the calculated result is smaller than 1, the cost value is 1. Changing the bandwidth reference value can change the cost of an interface.
   
   Perform the following steps to change the bandwidth reference value:
   
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
      
      
      
      OSPFv3 is enabled, and the OSPFv3 view is displayed.
   3. Run [**bandwidth-reference**](cmdqueryname=bandwidth-reference) *value*
      
      
      
      The bandwidth reference value is set.
   4. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
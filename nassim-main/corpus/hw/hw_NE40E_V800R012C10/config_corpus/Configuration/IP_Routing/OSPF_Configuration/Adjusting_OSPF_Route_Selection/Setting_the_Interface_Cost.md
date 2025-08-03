Setting the Interface Cost
==========================

You can adjust and optimize route selection by setting the OSPF interface cost.

#### Context

After the OSPF interface costs are set, the interface with a smaller cost value preferentially transmits routing information. This helps select the optimal route.

The OSPF interface cost can be set or calculated based on the interface bandwidth.

External factors may affect the physical bandwidth of links and change the physical bandwidth of interfaces, which in turn affects network performance. To address this problem, you can run the [**bandwidth**](cmdqueryname=bandwidth) *bandwidth* command in the interface view to set configuration bandwidth for the interface, and then run the [**bandwidth-config enable**](cmdqueryname=bandwidth-config+enable) command to enable the device to calculate the cost for the OSPF interface based on the configuration bandwidth of the interface.


#### Procedure

* Manually configure a cost for an OSPF interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ospf cost**](cmdqueryname=ospf+cost) *value*
     
     
     
     A cost is configured for the OSPF interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure bandwidth-based automatic OSPF interface cost calculation.
  
  
  
  The calculation formula is as follows: **Interface cost = Bandwidth reference value/Interface bandwidth**. The integer of the calculation result is used as the cost of the interface. If the result is less than 1, the cost is 1.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Perform the following operations as required:
  
  + To use the bandwidth reference value to determine the interface cost, run the [**bandwidth-reference**](cmdqueryname=bandwidth-reference) command.
  + To use the interface bandwidth to determine the interface cost, run the [**bandwidth**](cmdqueryname=bandwidth) command to set configuration bandwidth for an interface, and then run the [**bandwidth-config enable**](cmdqueryname=bandwidth-config+enable) command to enable the device to calculate the cost for the OSPF interface based on the configuration bandwidth of the interface.
  + To use both the bandwidth reference value and interface bandwidth to determine the interface cost, run the preceding three commands.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**bandwidth**](cmdqueryname=bandwidth) *bandwidth*
     
     
     
     Configuration bandwidth is configured for the interface.
  4. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit the interface view.
  5. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
     
     
     
     The OSPF view is displayed.
  6. Run [**bandwidth-reference**](cmdqueryname=bandwidth-reference) *value*
     
     
     
     A bandwidth reference value is set.
  7. Run [**bandwidth-config enable**](cmdqueryname=bandwidth-config+enable)
     
     
     
     Configuration bandwidth of each OSPF interface is allowed to participate in cost calculation for the interface.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + If the [**bandwidth**](cmdqueryname=bandwidth) command is not run, the cost of an OSPF interface is calculated based on the physical bandwidth of the interface.
     + If the [**bandwidth-config enable**](cmdqueryname=bandwidth-config+enable) command is not run, the cost of an OSPF interface is calculated based on the physical bandwidth of the interface.
  8. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Associate the remaining bandwidth of an OSPF interface with the link cost.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Associate the remaining bandwidth of an OSPF interface with the link cost.
     
     
     
     Perform the following operations as needed:
     
     + To associate the remaining bandwidth of an OSPF interface with the link cost, run the [**ospf**](cmdqueryname=ospf) **cost** *value* { **higher-bandwidth** *higher-bandwidth-value* **cost** *better-cost-value* | **lower-bandwidth** *lower-bandwidth-value* **cost** *worse-cost-value* } \* command.
     + To associate the remaining bandwidth of an OSPF multi-area adjacency interface with the link cost, run the [**ospf**](cmdqueryname=ospf) **cost** *costvalue* { **higher-bandwidth** *higher-bandwidth-value* **cost** *better-cost-value* | **lower-bandwidth** *lower-bandwidth-value* **cost** *worse-cost-value* } \* **multi-area** { *area-id-integer* | *area-id-ipv4* } command.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
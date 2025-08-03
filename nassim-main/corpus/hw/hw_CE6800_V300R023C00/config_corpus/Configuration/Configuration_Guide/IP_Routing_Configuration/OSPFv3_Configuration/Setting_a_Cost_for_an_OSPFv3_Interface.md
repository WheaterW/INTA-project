Setting a Cost for an OSPFv3 Interface
======================================

Setting a Cost for an OSPFv3 Interface

#### Prerequisites

Before setting a cost for an OSPFv3 interface, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

OSPFv3 can automatically calculate the link cost for an interface according to the interface bandwidth. You can also set a cost for the interface by using a specific command, and control the route cost by setting different link costs for OSPFv3 interfaces.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Set a cost for the OSPFv3 interface.
   
   
   ```
   [ospfv3 cost](cmdqueryname=ospfv3+cost) value [ instance instanceId ]
   ```
   
   By default, the link cost of an OSPFv3 interface is 1.
   
   If no cost is configured for an OSPFv3 interface, OSPFv3 can automatically calculate a cost for the interface based on the interface bandwidth. This is calculated as follows: Interface cost = Bandwidth reference value/Interface bandwidth. The resulting integer is used as the interface cost. If the result is smaller than 1, the cost is 1. In this case, changing the bandwidth reference value can change the cost of the interface.
   
   To change the bandwidth reference value, perform the following operations:
   
   1. Enter the system view.
      ```
      [system-view](cmdqueryname=system-view)
      ```
   2. Enter the OSPFv3 view.
      ```
      [ospfv3](cmdqueryname=ospfv3) [ process-id ]
      ```
   3. Set a bandwidth reference value.
      ```
      [bandwidth-reference](cmdqueryname=bandwidth-reference) value
      ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **no-peer** | **area** *area-id* ] [ *interface-type* *interface-number* ] command to check OSPFv3 interface information. The **Cost** field in the command output shows the cost.
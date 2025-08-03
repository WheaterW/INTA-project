Setting the Network Type to P2P
===============================

Setting the Network Type to P2P

#### Prerequisites

Before setting the network type to P2P, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

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
4. Set the network type of the OSPFv3 interface to P2P.
   
   
   ```
   [ospfv3 network-type](cmdqueryname=ospfv3+network-type) p2p [ instance instance-id ]
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **no-peer** | **area** *area-id* ] [ *interface-type* *interface-number* ] command to check OSPFv3 interface information.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **peer** command to check information about OSPFv3 neighbors.
Setting the Network Type to P2MP
================================

Setting the Network Type to P2MP

#### Prerequisites

Before setting the network type to P2MP, you have completed the following task:

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
4. Set the network type of the OSPFv3 interface to P2MP.
   
   
   ```
   [ospfv3 network-type](cmdqueryname=ospfv3+network-type) { broadcast | nbma | p2mp [ non-broadcast ] | p2p } [ instance instance-id ]
   ```
   
   **p2mp** [ **non-broadcast** ] must be configured. The P2MP network type must be forcibly changed from another network type. The details are as follows:
   
   * For an interface with the NBMA network type, if the network is not fully meshed, change the network type of the interface to P2MP. By doing this, two indirectly connected devices can communicate through a third device that can directly reach both devices. After the network type of the interface is changed to P2MP, there is no need to manually specify a neighbor.
   * If only two devices run OSPFv3 on the same network segment, changing the network type of the interface to P2MP is recommended.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **no-peer** | **area** *area-id* ] [ *interface-type* *interface-number* ] command to check OSPFv3 interface information.
* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **peer** command to check information about OSPFv3 neighbors.
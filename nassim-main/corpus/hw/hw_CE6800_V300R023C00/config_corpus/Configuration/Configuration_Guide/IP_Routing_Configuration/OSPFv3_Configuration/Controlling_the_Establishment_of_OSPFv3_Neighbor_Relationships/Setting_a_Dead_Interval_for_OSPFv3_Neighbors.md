Setting a Dead Interval for OSPFv3 Neighbors
============================================

Setting a Dead Interval for OSPFv3 Neighbors

#### Prerequisites

Before setting a Dead interval for OSPFv3 neighbors, you have completed the following task:

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
4. Set a Dead interval for OSPFv3 neighbors.
   
   
   ```
   [ospfv3 timer dead](cmdqueryname=ospfv3+timer+dead) interval [ instance instance-id ]
   ```
   
   By default, the Dead interval is four times the length of the Hello interval on the same interface.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   A Dead interval that is shorter than 10 seconds may disconnect the involved OSPFv3 neighbor relationship. To prevent this issue, a minimum of 10 seconds takes effect if the value of **dead** *interval* is less than 10 seconds. To ensure that a Dead interval shorter than 10 seconds takes effect, enable the conservative mode by specifying **conservative** in the [**ospfv3 timer hello**](cmdqueryname=ospfv3+timer+hello) command.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **area** *area-id* ] [ *interface-type* *interface-number* ] command to check OSPFv3 interface information. The **Dead** field in the command output indicates the Dead interval for OSPFv3 neighbors.
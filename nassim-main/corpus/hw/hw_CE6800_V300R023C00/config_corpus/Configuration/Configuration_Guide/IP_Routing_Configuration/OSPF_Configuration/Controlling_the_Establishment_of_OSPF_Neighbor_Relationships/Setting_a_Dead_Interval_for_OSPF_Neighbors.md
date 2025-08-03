Setting a Dead Interval for OSPF Neighbors
==========================================

Setting a Dead Interval for OSPF Neighbors

#### Prerequisites

Before setting a Dead interval for OSPF neighbors, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

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
4. Set a Dead interval for OSPF neighbors.
   
   
   ```
   [ospf timer dead](cmdqueryname=ospf+timer+dead) interval
   ```
   
   By default, the Dead interval on a P2P or broadcast interface is 40 seconds, whereas that on a P2MP or NBMA interface is 120 seconds; the Dead interval is four times the length of the Hello interval on the same interface.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   A Dead interval that is shorter than 10 seconds may disconnect the involved OSPF neighbor relationship. To prevent this issue, a minimum of 10 seconds takes effect if the value of **dead** *interval* is less than 10 seconds. To ensure that a Dead interval shorter than 10 seconds takes effect, enable the conservative mode by specifying **conservative** in the [**ospf timer hello**](cmdqueryname=ospf+timer+hello) command.
   
   Changing the network type will restore both the Hello interval and Dead interval to their default values.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** [ **all** | **no-peer** | *interface-type* *interface-number* ] [ **verbose** ] command to check OSPF interface information. The **Dead** field in the command output indicates the Dead interval for OSPF neighbors.
* Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **brief** command to check brief OSPF information. The **Dead** field in the command output indicates the Dead interval for OSPF neighbors.
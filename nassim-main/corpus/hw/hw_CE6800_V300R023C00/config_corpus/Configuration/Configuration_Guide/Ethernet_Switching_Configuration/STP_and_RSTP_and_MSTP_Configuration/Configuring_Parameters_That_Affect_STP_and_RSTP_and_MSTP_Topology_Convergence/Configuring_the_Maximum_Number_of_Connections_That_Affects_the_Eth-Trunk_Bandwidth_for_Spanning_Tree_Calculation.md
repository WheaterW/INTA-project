Configuring the Maximum Number of Connections That Affects the Eth-Trunk Bandwidth for Spanning Tree Calculation
================================================================================================================

Configuring the Maximum Number of Connections That Affects the Eth-Trunk Bandwidth for Spanning Tree Calculation

#### Context

The path cost is an important metric used in spanning tree calculation. Changing path costs triggers spanning tree recalculation. The interface bandwidth affects the path cost, so you can change the interface bandwidth to affect spanning tree calculation.

In [Figure 1](#EN-US_TASK_0000001345318777__fig151951930195417), DeviceA and DeviceB are connected through Eth-Trunks, among which Eth-Trunk 1 and Eth-Trunk 2 have three and two active member links, respectively. If each member link has the same bandwidth and DeviceA has been elected as the root bridge, then:

* Eth-Trunk 1 has a higher bandwidth than Eth-Trunk 2. After spanning tree calculation, Eth-Trunk 1 and Eth-Trunk 2 on DeviceB will be elected as the root port and an alternate port, respectively.
* If the maximum number of connections for Eth-Trunk 1 is set to 1, the path cost for Eth-Trunk 1 will be larger than Eth-Trunk 2. The spanning tree will then be recalculated, after which, Eth-Trunk 1 and Eth-Trunk 2 on DeviceB will become an alternate port and the root port, respectively.

**Figure 1** Configuring the maximum number of connections that affects the Eth-Trunk bandwidth  
![](figure/en-us_image_0000001345318853.png)

The maximum number of connections only affects the path cost for interfaces that participate in spanning tree calculation, and not the actual link bandwidth. The actual link bandwidth for traffic forwarding on an Eth-Trunk interface depends on the number of active member interfaces in the Eth-Trunk interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the Eth-Trunk interface view.
   
   
   ```
   [interface](cmdqueryname=interface) eth-trunk trunk-id
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Set the maximum number of connections that affects the Eth-Trunk bandwidth for spanning tree calculation.
   
   
   ```
   [max bandwidth-affected-linknumber](cmdqueryname=max+bandwidth-affected-linknumber) link-number
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display this**](cmdqueryname=display+this) command in the Eth-Trunk view to check the configuration.
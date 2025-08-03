Configuring Interface-based VLAN Assignment
===========================================

Configuring Interface-based VLAN Assignment

#### Prerequisites

Before configuring interface-based VLAN assignment, you have completed the following task:

* Create a VLAN. For details, see [Creating and Deleting a VLAN](vrp_vlan_cfg_0013.html).


#### Context

Interface-based VLAN assignment is the easiest and most effective method for assigning VLANs. After you add an interface to a VLAN, the interface can only forward packets from that VLAN. This limits broadcast packets to a single VLAN, as hosts in the same VLAN can directly communicate with each other at Layer 2, while those in different VLANs cannot. Before starting this operation, you need to know the interface type, default VLAN, and mode in which interfaces process tagged or untagged packets. For details, see [Understanding VLANs](vrp_vlan_cfg_0003.html).


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the Ethernet interface to be added to a VLAN.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure the attribute for the Layer 2 Ethernet interface.
   
   
   ```
   [port link-type](cmdqueryname=port+link-type) { access | hybrid | trunk }
   ```
5. Add the interface to a VLAN.
   
   
   * For an access interface, choose either of the following methods:Configure the default VLAN for the access interface and add the interface to the default VLAN.
     ```
     [port default vlan](cmdqueryname=port+default+vlan) vlan-id
     ```
     
     To configure the default VLAN for multiple interfaces and add these interfaces to the default VLAN in batches, run the following command in the VLAN view:
     
     ```
     [port](cmdqueryname=port) interface-type { interface-number1 [ to interface-number2 ] } &<1-10>
     ```
   * For a trunk interface, add it to specified VLANs in tagged mode.
     ```
     [port trunk allow-pass vlan](cmdqueryname=port+trunk+allow-pass+vlan) { { vlan-id1 [ to vlan-id2 ] } &<1-40> | all }
     ```
     
     To change the default VLAN of a trunk interface, run the [**port trunk pvid vlan**](cmdqueryname=port+trunk+pvid+vlan)*vlan-id* command in the interface view.
   * For a hybrid interface, add it to a VLAN in either untagged or tagged mode.Add the hybrid interface to a specified VLAN in untagged mode.
     ```
     [port hybrid untagged vlan](cmdqueryname=port+hybrid+untagged+vlan) { { vlan-id1 [ to vlan-id2 ] } &<1-10> | all }
     ```
     
     Add the hybrid interface to a specified VLAN in tagged mode.
     ```
     [port hybrid tagged vlan](cmdqueryname=port+hybrid+tagged+vlan) { { vlan-id1 [ to vlan-id2 ] } &<1-10> | all }
     ```
     
     To change the default VLAN of a hybrid interface, run the [**port hybrid pvid vlan**](cmdqueryname=port+hybrid+pvid+vlan)*vlan-id* command in the interface view.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display vlan**](cmdqueryname=display+vlan) *vlan-id1* [ **verbose** | **to** *vlan-id2* ] command to check information about specified VLANs.
* Run the [**display vlan**](cmdqueryname=display+vlan) [ **summary** ] command to check the summary of all VLANs.
* Run the [**display vlan vlan-name**](cmdqueryname=display+vlan+vlan-name) *vlan-name* command to check information about a specified VLAN.
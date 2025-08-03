Creating and Deleting a VLAN
============================

Creating and Deleting a VLAN

#### Context

As VLAN 1 is the default VLAN, it cannot be deleted and does not need to be created.


#### Procedure

* **Creating a VLAN**
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a VLAN and enter the VLAN view. If the VLAN has been created, the VLAN view is displayed. 
     
     
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     ```
  3. (Optional) Configure a description for the VLAN.
     
     
     ```
     [description](cmdqueryname=description+%28VLAN+view%29) description
     ```
     
     By default, the description of a VLAN contains the VLAN ID. For example, the description of VLAN 2 is VLAN 0002.
  4. (Optional) Configure a name for the VLAN.
     
     
     ```
     [name](cmdqueryname=name) vlan-name
     ```
     
     By default, a VLAN does not have a name.
     
     After a name is configured for the VLAN, you can run the [**vlan vlan-name**](cmdqueryname=vlan+vlan-name) *vlan-name* command in the system view to enter the view of this VLAN.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* **Creating VLANs in Batches**
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create VLANs in batches.
     
     
     ```
     [vlan batch](cmdqueryname=vlan+batch) { vlan-id1 [ to vlan-id2 ] } &<1-10>
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  To configure the same services in multiple VLANs in a batch, first configure a VLAN range. Run the [**vlan range**](cmdqueryname=vlan+range) { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> command in the system view to create a VLAN range and enter the VLAN-Range view. Then, configure services in the VLAN-Range view and commit the configurations. The service configurations of all member VLANs will be saved in the configuration file.
* **Deleting a VLAN**
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Delete a VLAN.
     
     
     ```
     [undo vlan](cmdqueryname=undo+vlan) vlan-id
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* **Deleting VLANs in Batches**
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Delete VLANs in batches.
     
     
     ```
     [undo vlan batch](cmdqueryname=undo+vlan+batch) { vlan-id1 [ to vlan-id2 ] } &<1-10>
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```

#### Verifying the Configuration

* Run the [**display vlan**](cmdqueryname=display+vlan) [ **summary** ] command to check the summary of all VLANs.
* Run the [**display default-parameter vlan**](cmdqueryname=display+default-parameter+vlan) *vlan-id* command to check the default configuration of a VLAN.
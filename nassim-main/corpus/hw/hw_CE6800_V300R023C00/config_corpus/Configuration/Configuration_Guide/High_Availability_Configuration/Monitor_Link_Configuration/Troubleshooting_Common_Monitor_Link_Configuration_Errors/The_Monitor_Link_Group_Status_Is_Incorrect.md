The Monitor Link Group Status Is Incorrect
==========================================

The Monitor Link Group Status Is Incorrect

#### Fault Symptom

A Monitor Link group remains in the Down state.


#### Procedure

1. Run the [**display monitor-link group**](cmdqueryname=display+monitor-link+group) **group-id** command to check whether the member interface status is normal.
   
   
   ```
   [display monitor-link group](cmdqueryname=display+monitor-link+group) group-id
   ```
   * If **DOWN** is displayed in the **State** field of a member interface, rectify the interface fault.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     An uplink interface down event may be caused by a link failure, a unidirectional OAM connectivity failure, or an OAM connection setup failure.
   * If **UP** is displayed in the **State** field of a member interface, go to Step 2.
2. Run the [**display current-configuration**](cmdqueryname=display+current-configuration) **interface** command in the member interface view to check whether the member interface is added to a service VLAN.
   
   
   ```
   [display current-configuration](cmdqueryname=display+current-configuration) interface interface-type interface-number
   ```
   
   If the member interface is not added to a service VLAN, add the interface to a service VLAN.
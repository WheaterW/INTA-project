A VLANIF Interface Fails to Be Created
======================================

A VLANIF Interface Fails to Be Created

#### Fault Symptom

When a user attempts to create a VLANIF interface on a device, an error message is displayed, indicating that the VLANIF interface fails to be created.

#### Possible Causes

* The number of created VLANIF interfaces has reached the upper limit.
* A VLANIF interface cannot be created for the target VLAN.


#### Procedure

* Check whether the number of created VLANIF interfaces has reached the upper limit.
  1. Check the VLANIF interface configuration.
     
     
     ```
     [display interface brief](cmdqueryname=display+interface+brief)
     ```
     
     
     
     The **Interface** field in the command output specifies the number of created VLANIF interfaces.
  2. Check whether the number of created VLANIF interfaces has reached the upper limit.
  3. Delete unwanted VLANIF interfaces.
     
     
     ```
     [undo interface](cmdqueryname=undo+interface) vlanif vlan-id
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Check whether the VLANIF interface cannot be created for the target VLAN.
  1. Check the VLAN type.
     
     
     ```
     [display vlan summary](cmdqueryname=display+vlan+summary)
     ```
  2. Create a VLANIF interface for another VLAN.
     
     
     ```
     [interface](cmdqueryname=interface) vlanif vlan-id
     ```
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
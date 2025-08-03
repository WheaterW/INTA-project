Deleting an ACL.
================

Deleting an ACL.

#### Context

When the usage of ACL resources on a device reaches the maximum, you can deploy a new ACL only after deleting unnecessary ACL configurations.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Delete an ACL using either of the following methods:
   
   
   ```
   [undo acl](cmdqueryname=undo+acl+number+all) { [ number ] acl-number | all }
   ```
   ```
   [undo acl](cmdqueryname=undo+acl+name) name acl-name
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Before deleting an ACL, ensure that it is not referenced by any service module.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
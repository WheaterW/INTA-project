Deleting an ACL6
================

Deleting an ACL6

#### Context

When the usage of ACL6 resources on a device reaches the maximum, you can deploy new ACL6s only after deleting unnecessary ACL6 configurations.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Delete an ACL6 using either of the following methods:
   
   
   ```
   [undo acl ipv6](cmdqueryname=undo+acl+ipv6+number+all) { [ number ] acl6-number | all } 
   [undo acl ipv6](cmdqueryname=undo+acl+ipv6+name) name acl6-name
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Before deleting an ACL6, ensure that it is not referenced by any service module.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
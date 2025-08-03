Modifying an ACL
================

Modifying an ACL

#### Context

You can add and delete ACL rules as required. However, it is recommended not to directly modify existing rules. This is because modified rules may conflict with and replace other rules, leading to unexpected results. In this manner, the ACL rules may fail to achieve the expected effect.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Run either of the following commands to enter the view of an ACL to be modified:
   
   
   ```
   [acl](cmdqueryname=acl+number) [ number ] acl-number
   ```
   ```
   [acl name](cmdqueryname=acl+name) acl-name
   ```
3. Configure new rules and delete unused rules.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If an existing rule is edited and the edited content conflicts with the original one, the edited content takes effect.
   
   When you update ACL rules on a device, the device delivers the old and new rules together, and then deletes the old rules. Therefore, sufficient ACL resources are required on the device for successful rule update. For example, if three rules are configured in ACL 3001, to add another rule, ensure that there are at least four ACL resources available.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
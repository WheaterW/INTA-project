Modifying an ACL6
=================

Modifying an ACL6

#### Context

You can add and delete ACL6 rules as required. However, it is recommended not to directly modify existing rules. This is because modified rules may conflict with and replace other rules, leading to unexpected results. In this manner, the ACL6 rules may fail to achieve the expected effect.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Run either of the following commands to enter the view of an ACL6 to be modified:
   
   
   ```
   [acl ipv6](cmdqueryname=acl+ipv6+number) [ number ] acl6-number
   ```
   ```
   [acl ipv6 name](cmdqueryname=acl+ipv6+name) acl6-name
   ```
3. Configure new rules and delete unused rules.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If an existing rule is edited and the edited content conflicts with the original one, the edited content takes effect.
   
   When you update ACL6 rules on a device, the device delivers the old and new rules together, and then deletes the old rules. Therefore, sufficient ACL6 resources are required on the device for successful rule update. For example, if three rules are configured in ACL6 3001, to add another rule, ensure that there are at least four ACL6 resources available.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
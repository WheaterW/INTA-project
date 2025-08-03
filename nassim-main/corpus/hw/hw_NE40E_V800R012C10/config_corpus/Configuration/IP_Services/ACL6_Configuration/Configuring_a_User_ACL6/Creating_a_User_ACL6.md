Creating a User ACL6
====================

You can create a user ACL6 and configure parameters for the ACL6.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Run **acl url** { **refresh interval** *interval* | **expire time** *expire-time* }
   
   
   
   A domain name update interval and aging time are configured.
3. Run [**acl ipv6**](cmdqueryname=acl+ipv6+name+ucl+number+match-order+auto+config) { **name** *ucl-acl6-name* **ucl** | **number** *ucl-acl6-number* } [ **match-order** { **auto** | **config** } ]
   
   
   
   A user ACL6 is created.
   
   The user ACL6 number ranges from 6000 to 9999.
4. (Optional) Run [**step**](cmdqueryname=step) *step*
   
   
   
   An ACL6 step is set.
   
   
   
   You can use an ACL6 step to maintain ACL6 rules and add new ACL6 rules conveniently. ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Assume that a user has created four rules numbered from 1 to 4 in an ACL6. The user can reconfigure the ACL6 step, for example, as 2 by running the **step 2** command in the ACL6 view. The original rule numbers 1, 2, 3, and 4 are renumbered as 2, 4, 6, and 8, respectively. After that, the user can run the [**rule 3 xxxx**](cmdqueryname=rule+3+xxxx) command to add a rule numbered 3 between the renumbered rules 2 and 4.
5. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   The ACL6 description is configured.
   
   The [**description**](cmdqueryname=description) command configures a description for an ACL6 in any of the following situations:
   
   * A large number of ACL6s are configured, and their functions are difficult to identify.
   * An ACL6 is used at a long interval, and its function may be left forgotten.
   * Names of named ACL6s cannot fully explain the ACL6s' functions.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
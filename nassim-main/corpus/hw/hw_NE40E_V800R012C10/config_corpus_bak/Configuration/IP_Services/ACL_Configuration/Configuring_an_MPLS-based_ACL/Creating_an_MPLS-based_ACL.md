Creating an MPLS-based ACL
==========================

You can create an MPLS-based ACL and configure parameters for the ACL.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**acl**](cmdqueryname=acl+name+mpls+mpls+number+number) { **name** *mpls-acl-name* { **mpls** | [ **mpls** ] **number** *mpls-acl-number* } | [ **number** ] *mpls-acl-number* }
   
   
   
   An MPLS-based ACL is created.
   
   The MPLS-based ACL number ranges from 10000 to 10999.
3. (Optional) Run [**step**](cmdqueryname=step) *step*
   
   
   
   An ACL increment is set.
   
   
   
   You can use an ACL increment to maintain ACL rules and add new ACL rules conveniently. ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Assume that a user has created four rules numbered from 1 to 4 in an ACL. The user can reconfigure the ACL increment, for example, to 2 by running the **step 2** command in the ACL view. The original rule numbers 1, 2, 3, and 4 are renumbered as 2, 4, 6, and 8, respectively. After that, the user can run the [**rule 3**](cmdqueryname=rule+3) command to add a rule numbered 3 between the renumbered rules 2 and 4.
4. (Optional) Run [**description**](cmdqueryname=description) *text*
   
   
   
   The ACL description is configured.
   
   The [**description**](cmdqueryname=description) command configures a description for an ACL in any of the following situations:
   
   * A large number of ACLs are configured, and their functions are difficult to identify.
   * An ACL is used at a long interval, and its function may be left forgotten.
   * Names of named ACLs cannot fully explain the ACLs' functions.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
(Optional) Configuring Command Line-based Reauthorization
=========================================================

(Optional) Configuring Command Line-based Reauthorization

#### Context

If the user group of an online user needs to be changed but the dynamic authorization server is down, enable command line-based reauthorization. This function allows you to run commands to change the user group and reauthorize the user.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Generally, ACLs are used to control user access authorities, and ACL rules are configured based on user groups. Therefore, to change a user's access authority, you can change its user group. For example, ACL rules are configured to allow user group 1 to access only the internal network and user group 2 to access both internal and external networks. When user A in user group 1 goes online, user A can access the internal network only. To allow user A to access both internal and external networks, reauthorize user A by changing its user group to user group 2.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**reauthorize enable**](cmdqueryname=reauthorize+enable)
   
   
   
   Command line-based reauthorization is enabled.
3. Run [**reauthorize**](cmdqueryname=reauthorize) **user-name** *username* **user-group** *user-group-name*
   
   
   
   The user group of a specified user is changed.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
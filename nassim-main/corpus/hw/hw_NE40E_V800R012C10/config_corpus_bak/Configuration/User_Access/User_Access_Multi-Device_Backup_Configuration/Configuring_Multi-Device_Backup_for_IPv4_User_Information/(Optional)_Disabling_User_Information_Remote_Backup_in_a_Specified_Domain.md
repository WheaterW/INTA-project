(Optional) Disabling User Information Remote Backup in a Specified Domain
=========================================================================

User information remote backup can be disabled for users
who get online from a specified domain as required.

#### Context

User information remote backup is enabled by default for
users who get online through an AAA domain. To disable this function,
run the [**undo peer-backup enable**](cmdqueryname=undo+peer-backup+enable) command. Information
about authenticated users will then not be backed up even if hot backup
is enabled on a user
access interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The AAA domain view is displayed.
4. Run [**undo peer-backup enable**](cmdqueryname=undo+peer-backup+enable)
   
   
   
   User information remote backup is disabled for users getting
   online from the specified
   domain.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The user information remote backup configuration
   cannot be modified in the view of an AAA domain where users have logged
   in. To be specific, if user information remote backup configuration
   is disabled, the [**peer-backup enable**](cmdqueryname=peer-backup+enable) command or its undo form cannot be run
   to change the existing user information remote backup configuration
   in the domain with logged-in users.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
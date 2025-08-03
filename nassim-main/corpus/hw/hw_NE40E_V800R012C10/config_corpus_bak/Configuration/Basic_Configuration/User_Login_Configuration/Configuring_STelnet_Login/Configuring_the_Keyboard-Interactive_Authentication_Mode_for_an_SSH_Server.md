Configuring the Keyboard-Interactive Authentication Mode for an SSH Server
==========================================================================

If an SSH user logs in to a device using password card authentication, keyboard-interactive authentication must be enabled for this user.

#### Context

If an SSH user logs in to a device using password card authentication, keyboard-interactive authentication must be enabled for this user. To enable keyboard-interactive authentication, run the **ssh server authentication-type****keyboard-interactive****enable** command.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ssh server authentication-type keyboard-interactive enable**](cmdqueryname=ssh+server+authentication-type+keyboard-interactive+enable)
   
   
   
   Keyboard-interactive authentication is enabled for the SSH server.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
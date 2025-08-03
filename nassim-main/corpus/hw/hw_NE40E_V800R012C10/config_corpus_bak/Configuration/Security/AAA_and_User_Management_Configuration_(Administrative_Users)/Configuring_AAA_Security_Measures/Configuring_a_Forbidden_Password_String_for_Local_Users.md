Configuring a Forbidden Password String for Local Users
=======================================================

To improve local account security, specify character strings
that are not allowed in passwords.

#### Context

Simple passwords can be easily compromised. To avoid security
problems caused by simple passwords, you can specify character strings
that are not allowed in passwords.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**security password**](cmdqueryname=security+password)
   
   
   
   The password security
   view is displayed.
3. Run [**rule admin**](cmdqueryname=rule+admin)
   
   
   
   The rules management view is displayed.
4. Run [**forbidden word**](cmdqueryname=forbidden+word) *word*
   
   
   
   A forbidden password string
   is configured.
   
   
   
   After a forbidden password string is configured, new passwords
   cannot contain this string, regardless of case.
   
   The [**forbidden word**](cmdqueryname=forbidden+word) command takes effect only with local users' passwords. After
   the [**forbidden word**](cmdqueryname=forbidden+word) command is executed, a newly configured or modified password
   cannot contain any forbidden password string. Otherwise, the configuration
   fails. If an existing password contains a forbidden password string,
   the system will prompt the user to change the password. The user,
   however, can continue to use the password.
   
   A device supports
   a maximum of 32 password configuration rules. Each rule can specify
   only one forbidden password string. The same forbidden password string
   can be specified in different rules.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
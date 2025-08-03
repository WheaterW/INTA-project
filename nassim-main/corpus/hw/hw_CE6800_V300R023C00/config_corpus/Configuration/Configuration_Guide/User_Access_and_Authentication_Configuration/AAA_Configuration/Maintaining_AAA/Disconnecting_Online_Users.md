Disconnecting Online Users
==========================

Disconnecting Online Users

#### Context

You can disconnect online users by specifying the user name, domain name, or access interface. This is required if a user's AAA configuration is modified, because the new configuration takes effect only after the user is disconnected. It may also be necessary if the number of online users reaches the maximum value or online users are unauthorized users.

![](public_sys-resources/note_3.0-en-us.png) 

If the AAA configuration of an online user is deleted, the online user may be disconnected.



#### Procedure

* Run the **display access-user** command in any view to check information about online users.
* Run the [**cut access-user**](cmdqueryname=cut+access-user) command in the AAA view to disconnect one or more sessions to log out online users.
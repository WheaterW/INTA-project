(Optional) Configuring the IP Address Locking Function
======================================================

To improve device security and protect user passwords against attacks, configure the FTP-based IP address locking function.

#### Context

After a user fails to log in to a device using FTP, the number of FTP login failures is recorded for the IP address. If the number of login failures within a specified period reaches the threshold, the IP address is locked, and all users who log in through this IP address cannot set up an FTP connection with this device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**undo ftp server ip-block disable**](cmdqueryname=undo+ftp+server+ip-block+disable)
   
   
   
   The client IP address locking function is enabled on the device that functions as an FTP server.
3. Run [**ftp server ip-block failed-times**](cmdqueryname=ftp+server+ip-block+failed-times) *failed-times* **period** *period*
   
   
   
   The maximum number of consecutive authentication failures and an authentication period are configured for client IP address locking.
4. Run [**ftp server ip-block reactive**](cmdqueryname=ftp+server+ip-block+reactive) *reactive-period*
   
   
   
   A period after which the system automatically unlocks a user is specified.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   The user view is displayed.
7. Run [**activate ftp server ip-block ip-address**](cmdqueryname=activate+ftp+server+ip-block+ip-address) *ip-address* [ **vpn-instance** *vpn-name* ]
   
   
   
   The IP address of a user that fails the authentication is unlocked.
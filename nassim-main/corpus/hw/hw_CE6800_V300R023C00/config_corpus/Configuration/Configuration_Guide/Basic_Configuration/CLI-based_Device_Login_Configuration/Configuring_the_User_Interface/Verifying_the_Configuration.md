Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display users**](cmdqueryname=display+users) [ **all** ] command to check information about users who have logged in to a device through the user interfaces.
* Run the [**display user-interface**](cmdqueryname=display+user-interface) **console** *ui-number* [ **summary** ] command to check information of the console user interface.
* Run the [**display user-interface maximum-vty**](cmdqueryname=display+user-interface+maximum-vty) command to check the maximum number of VTY user interfaces.
* Run the [**display user-interface**](cmdqueryname=display+user-interface) **vty** *ui-number1* [ **summary** ] command to check information of the VTY user interface.
* Run the [**display ssh server ip-block all**](cmdqueryname=display+ssh+server+ip-block+all) command to view all client IP addresses that fail authentication.
* Run the [**display ssh server ip-block list**](cmdqueryname=display+ssh+server+ip-block+list) command to view client IP addresses that are locked out due to authentication failure.
* Run the [**display vty ip-block list**](cmdqueryname=display+vty+ip-block+list) command to check the list of IP addresses that are blocked due to authentication failures.
* Run the [**display vty ip-block all**](cmdqueryname=display+vty+ip-block+all) command to check all IP addresses that fail to be authenticated.
* Run the [**display vty mode**](cmdqueryname=display+vty+mode) command to check the VTY mode.
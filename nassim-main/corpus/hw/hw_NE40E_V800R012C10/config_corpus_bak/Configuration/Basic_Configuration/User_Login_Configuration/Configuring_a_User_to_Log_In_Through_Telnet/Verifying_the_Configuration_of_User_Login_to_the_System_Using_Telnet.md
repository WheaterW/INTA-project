Verifying the Configuration of User Login to the System Using Telnet
====================================================================

After using Telnet to log in to a device, you can view information about the current user interface, every user interface, and established TCP connections.

#### Prerequisites

Telnet login has been configured.


#### Procedure

* Run the [**display users**](cmdqueryname=display+users) [ **all** ] command to check information about user interfaces.
* Run the [**display tcp status**](cmdqueryname=display+tcp+status) command to check established TCP connections.
* Run the [**display telnet server status**](cmdqueryname=display+telnet+server+status) command to check the status and configurations of the Telnet server.
* After configuring whitelist session-CAR for Telnet, you can verify the configuration.
  
  
  + For IPv4, run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **telnet** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for Telnet on a specified interface board.
    
    To view new statistics, run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car) **telnet** **statistics** **slot** *slot-id* command to clear the existing statistics about whitelist session-CAR for Telnet on a specified interface board, and then run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **telnet** **statistics** **slot** *slot-id* command.
  + For IPv6, run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car) **telnetv6** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for Telnet on a specified interface board.
    
    To view new statistics, run the [**reset cpu-defend whitelist-v6 session-car**](cmdqueryname=reset+cpu-defend+whitelist-v6+session-car) **telnetv6** **statistics** **slot** *slot-id* command to clear the existing statistics about whitelist session-CAR for Telnet on a specified interface board, and then run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car) **telnetv6** **statistics** **slot** *slot-id* command.
* Run the [**display vty ip-block all**](cmdqueryname=display+vty+ip-block+all) command to check all IP addresses that fail to be authenticated.
* Run the [**display vty ip-block list**](cmdqueryname=display+vty+ip-block+list) command to check the list of IP addresses that are blocked due to authentication failures.
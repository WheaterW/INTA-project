Verifying the Configuration of User Login to the System Using STelnet
=====================================================================

After using STelnet to log in to a device, verify the configuration.

#### Prerequisites

STelnet login has been configured.


#### Procedure

* Run the [**display ssh user-information**](cmdqueryname=display+ssh+user-information) *username* command on the SSH server to check information about SSH users.
* Run the [**display ssh server**](cmdqueryname=display+ssh+server) **status** command on the SSH server to check its configuration.
* Run the [**display ssh server**](cmdqueryname=display+ssh+server) **session** command on the SSH server to check information about sessions between the SSH server and SSH clients.
* After configuring whitelist session-CAR for SSH, you can verify the configuration.
  
  
  + For IPv4, run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **ssh** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for SSH on a specified interface board.
    
    To view new statistics, run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car) **ssh** **statistics** **slot** *slot-id* command to clear the existing statistics about whitelist session-CAR for SSH on a specified interface board, and then run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **ssh** **statistics** **slot** *slot-id* command.
  + For IPv6, run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car) **sshv6** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for SSH on a specified interface board.
    
    To view new statistics, run the [**reset cpu-defend whitelist-v6 session-car**](cmdqueryname=reset+cpu-defend+whitelist-v6+session-car) **sshv6** **statistics** **slot** *slot-id* command to clear the existing statistics about whitelist session-CAR for SSH on a specified interface board, and then run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car) **sshv6** **statistics** **slot** *slot-id* command.
Verifying the Configuration of SFTP-based File Operations
=========================================================

After completing the configuration of SFTP-based file operations, view information about SSH users and the configuration of the SSH server.

#### Prerequisites

The configuration of SFTP-based file operations is complete.


#### Procedure

* Run the [**display ssh user-information**](cmdqueryname=display+ssh+user-information) *username* command on the SSH server to check information about SSH users.
* Run the [**display ssh server**](cmdqueryname=display+ssh+server) **status** command to view the configuration of the SSH server.
* Run the [**display ssh server**](cmdqueryname=display+ssh+server) **session** command on the SSH server to check information about sessions between the SSH server and SSH clients.
* After configuring whitelist session-CAR for SSH, you can verify the configuration.
  
  
  + For IPv4, run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **ssh** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for SSH on a specified interface board.
    
    To view new statistics, run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car) **ssh** **statistics** **slot** *slot-id* command to clear the existing statistics about whitelist session-CAR for SSH on a specified interface board, and then run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **ssh** **statistics** **slot** *slot-id* command.
  + For IPv6, run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car) **sshv6** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for SSH on a specified interface board.
    
    To view new statistics, run the [**reset cpu-defend whitelist-v6 session-car**](cmdqueryname=reset+cpu-defend+whitelist-v6+session-car) **sshv6** **statistics** **slot** *slot-id* command to clear the existing statistics about whitelist session-CAR for SSH on a specified interface board, and then run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car) **sshv6** **statistics** **slot** *slot-id* command.
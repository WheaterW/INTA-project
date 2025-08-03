Verifying the Configuration of Using FTP to Operate Files
=========================================================

After completing the configuration of using FTP to operate files, you can view the configuration and status of the FTP server as well as information about logged-in FTP users.

#### Prerequisites

The configurations of file operation by using FTP are complete.


#### Procedure

* Run the [**display ftp-server**](cmdqueryname=display+ftp-server) command to check the configuration and status of the FTP server.
* Run the [**display ftp-users**](cmdqueryname=display+ftp-users) command to check information about logged-in FTP users.
* After configuring whitelist session-CAR for FTP, you can verify the configuration.
  
  
  + For IPv4, run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **ftp** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for FTP on a specified interface board.
    
    To view new statistics, run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car) **ftp** **statistics** **slot** *slot-id* command to clear the existing statistics about whitelist session-CAR for FTP on a specified interface board, and then run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car) **ftp** **statistics** **slot** *slot-id* command.
  + For IPv6, run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car) **ftpv6** **statistics** **slot** *slot-id* command to check statistics about whitelist session-CAR for FTP on a specified interface board.
    
    To view new statistics, run the [**reset cpu-defend whitelist-v6 session-car**](cmdqueryname=reset+cpu-defend+whitelist-v6+session-car) **ftpv6** **statistics** **slot** *slot-id* command to clear the existing statistics about whitelist session-CAR for FTP on a specified interface board, and then run the [**display cpu-defend whitelist-v6 session-car**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car) **ftpv6** **statistics** **slot** *slot-id* command.
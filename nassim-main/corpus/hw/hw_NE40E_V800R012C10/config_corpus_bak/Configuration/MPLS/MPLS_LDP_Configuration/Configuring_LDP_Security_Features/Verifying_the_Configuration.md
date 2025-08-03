Verifying the Configuration
===========================

After configuring LDP security features, you can view the configurations of LDP MD5 authentication, LDP GTSM, and LDP keychain authentication.

#### Prerequisites

LDP security features have been configured.


#### Procedure

* Run the [**display mpls ldp session**](cmdqueryname=display+mpls+ldp+session+verbose) **verbose** command to check the configurations of LDP MD5 authentication and LDP keychain authentication.
* Run the [**display gtsm statistics**](cmdqueryname=display+gtsm+statistics+all) { *slot-id* | **all** } command to check GTSM statistics.
* Run the [**display cpu-defend whitelist session-car**](cmdqueryname=display+cpu-defend+whitelist+session-car+ldp-tcp+ldp-udp-local) { **ldp-tcp** | **ldp-udp-local** | **ldp-udp-remote** } **statistics** **slot** *slot-id* command to check the statistics about whitelist session-CAR for LDP on a specified interface board.
  
  
  
  To facilitate the query of statistics in a new period, run the [**reset cpu-defend whitelist session-car**](cmdqueryname=reset+cpu-defend+whitelist+session-car+ldp-tcp+ldp-udp-local) { **ldp-tcp** | **ldp-udp-local** | **ldp-udp-remote** } **statistics** **slot** *slot-id* command to clear the existing statistics about whitelist session-CAR for LDP on a specified interface board. Then, check the statistics after a certain period.
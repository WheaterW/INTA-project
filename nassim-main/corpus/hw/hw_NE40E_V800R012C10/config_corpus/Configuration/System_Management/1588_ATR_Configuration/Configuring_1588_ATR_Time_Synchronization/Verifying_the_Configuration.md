Verifying the Configuration
===========================

After configuring 1588 ATR on the Router that functions as a server or client in hop-by-hop mode, verify the configuration.

#### Procedure

* Run the [**display ptp-adaptive all**](cmdqueryname=display+ptp-adaptive+all) command to check all configurations of the 1588 ATR module on the server or client in hop-by-hop mode.
* Run the [**display ptp-adaptive config**](cmdqueryname=display+ptp-adaptive+config) command to check 1588 ATR related configurations on the server or client in hop-by-hop mode.
* Run the [**display ptp-adaptive client**](cmdqueryname=display+ptp-adaptive+client) [ *client-id* ] command to check detailed information and packet statistics about the client from which the 1588 ATR server receives a negotiation request.
* Run the [**display ptp-adaptive**](cmdqueryname=display+ptp-adaptive) **master-only-vport** [ *mvport-id* ] command to check configurations of the master-only-vport on the T-BC as well as the information about the connected client.
* Run the [**display ptp-adaptive**](cmdqueryname=display+ptp-adaptive) **vport** [ *vport-id* ] command to check configurations of the vport on the T-BC as well as the status information.
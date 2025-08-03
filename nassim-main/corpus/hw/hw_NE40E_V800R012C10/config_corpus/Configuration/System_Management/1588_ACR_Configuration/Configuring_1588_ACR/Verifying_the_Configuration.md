Verifying the Configuration
===========================

After configuring 1588 ACR on the Router, verify the configuration.

#### Procedure

* When the device functions as a client:
  1. Run the [**display ptp-adaptive all**](cmdqueryname=display+ptp-adaptive+all) command to check all 1588 ACR configurations on the client.
  2. Run the [**display ptp-adaptive**](cmdqueryname=display+ptp-adaptive) **server** [ *server-id* ] command to check detailed information about a clock server that is connected to the 1588 ACR enabled client and statistics about packets exchanged between the client and server.
* When the device functions as a server:
  1. Run the [**display ptp-adaptive all**](cmdqueryname=display+ptp-adaptive+all) command to check all 1588 ACR configurations on the server.
  2. Run the [**display ptp-adaptive**](cmdqueryname=display+ptp-adaptive) **client** [ *client-id* ] command to check detailed information about a clock client that is connected to the 1588 ACR server and statistics about packets exchanged between the client and server.
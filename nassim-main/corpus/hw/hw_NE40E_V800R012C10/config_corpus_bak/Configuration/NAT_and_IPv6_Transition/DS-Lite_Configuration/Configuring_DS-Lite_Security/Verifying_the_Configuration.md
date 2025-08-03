Verifying the Configuration
===========================

After configuring the DS-Lite security functions, you can run **display** commands to verify the configuration.

#### Prerequisites

All DS-Lite security functions have been configured.


#### Procedure

* Run the [**display nat flow-defend**](cmdqueryname=display+nat+flow-defend) command to check the configured rate at which the first packet is sent to create a flow for a user.
* Run the [**display nat user-information**](cmdqueryname=display+nat+user-information) command to check DS-Lite user information.
* Run the [**display nat flow-defend reverse-blacklist**](cmdqueryname=display+nat+flow-defend+reverse-blacklist) command to check entries in a reverse first-packet blacklist on the CPU of a service board.
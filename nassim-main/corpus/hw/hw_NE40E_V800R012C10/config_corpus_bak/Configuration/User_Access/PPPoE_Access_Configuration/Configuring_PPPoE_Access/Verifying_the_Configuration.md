Verifying the Configuration
===========================

After configuring the PPPoE access service, check the PPPoE access configurations.

#### Procedure

* Run the [**display access-user**](cmdqueryname=display+access-user) command to check information about online users.
* Run the [**display bas-interface**](cmdqueryname=display+bas-interface) command to check service information on the BAS interface.
* Run the [**display pppoe statistics**](cmdqueryname=display+pppoe+statistics) command to check PPPoE packet statistics.
* Run the [**display pppoe statistics online-fail-record**](cmdqueryname=display+pppoe+statistics+online-fail-record) command to check statistics about PPPoE user login failures due to the limit on the number of access users (configured using the **access-ip-limit** command).
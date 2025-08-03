Verifying the Configuration
===========================

After WRED is configured, verify the configuration.

#### Procedure

* Run the [**display port-wred configuration**](cmdqueryname=display+port-wred+configuration) [ **verbose** [ *port-wred-name* ] ] command to check the parameters configured for WRED profiles.
* Run the [**display port-queue configuration interface**](cmdqueryname=display+port-queue+configuration+interface) *interface-type* *interface-number* **outbound** command to check the detailed configuration of port queues.
* Run the [**display port-queue statistics**](cmdqueryname=display+port-queue+statistics) [ **slot** *slot-id* | **interface** *interface-type* *interface-number* ] [ *cos-value* ] **outbound** [ **default** ] command to check port queue statistics.
* Run the [**display port-queue statistics slot**](cmdqueryname=display+port-queue+statistics+slot) *slot-id* [ *cos-value* ] **outbound** **bind** **mtunnel** command to check port queue statistics on the MTunnel interface of distributed multicast VPN.
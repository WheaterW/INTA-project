Verifying the PFC Configuration
===============================

Verifying the PFC Configuration

#### Procedure

* Run the [**display dcb**](cmdqueryname=display+dcb) [ **interface** { **interface-name** | *interface-type* **interface-num** } ] command to check the DCB configuration and negotiation status. (Not supported by the CE6885-LL (low latency mode).)
* Run the [**display dcb pfc-profile**](cmdqueryname=display+dcb+pfc-profile) [ **profilename** ] command to check the PFC profile configuration.
* Run the [**display dcb pfc buffer**](cmdqueryname=display+dcb+pfc+buffer) [ **interface** { **interface-name** | *interface-type* **interface-num** } ] command to check PFC backpressure parameter settings.
* Run the [**display dcb pfc deadlock trigger status**](cmdqueryname=display+dcb+pfc+deadlock+trigger+status) [ **interface** { **interface-name** | *interface-type* **interface-num** } ] command to check the PFC deadlock detection status on an interface.
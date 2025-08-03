Monitoring the DCB Running Status
=================================

Monitoring the DCB Running Status

#### Context

During routine maintenance, you can run the following commands in any view to monitor the DCB running status.


#### Procedure

* Run the [**display dcb**](cmdqueryname=display+dcb) [ **interface** { **interface-name** | *interface-type* **interface-num** } ] command to check the DCB configuration and negotiation status. (Not supported by the CE6885-LL (low latency mode).)
* Run the [**display dcb pfc-profile**](cmdqueryname=display+dcb+pfc-profile) [ *profile-name* ] command to check the PFC profile configuration.
* Run the [**display dcb ets-profile**](cmdqueryname=display+dcb+ets-profile) [ *profile-name* ] command to check the ETS profile configuration. (Not supported by the CE6885-LL (low latency mode).)
* Run the [**display dcb app-profile**](cmdqueryname=display+dcb+app-profile) [ *profile-name* ]command to check the App profile configuration. (Not supported by the CE6885-LL (low latency mode).)
* Run the [**display dcb pfc**](cmdqueryname=display+dcb+pfc) [ **interface** { **interface-name** | *interface-type* **interface-num** } ] command to check statistics on PFC frames on an interface.
* Run the [**display dcb fail-record**](cmdqueryname=display+dcb+fail-record) [ **interface** { **interface-name** | *interface-type* **interface-num** } ] command to check DCB negotiation failure records on an interface. (Not supported by the CE6885-LL (low latency mode).)
* Run the [**display dcb status**](cmdqueryname=display+dcb+status) [ **interface** { **interface-name** | *interface-type* **interface-num** } ] **verbose** command to check the DCB configuration on the local and remote devices. (Not supported by the CE6885-LL (low latency mode).)
* Run the [**display qos headroom-usage**](cmdqueryname=display+qos+headroom-usage) [ **slot** *slot-id* | **interface** { **interface-name** | *interface-type* **interface-num** } ] command to check the headroom buffer usage. (Supported only by the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.)
* Run the **[**display dcb pfc time**](cmdqueryname=display+dcb+pfc+time)** [ **interface** { *interface-name* | *interface-type interface-num* } ] command to check the backpressure duration on a PFC-enabled interface. (Supported only by the CE6855-48XS8CQ, CE6863E-48S8CQ, CE6885, CE6885-LL, CE6885-SAN, CE6885-T, CE8851-32CQ4BQ, CE8855.)
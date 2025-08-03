Verifying the Configuration
===========================

After configuring the TWAMP Light statistics collection function, verify the configurations.

#### Prerequisites

You have configured the TWAMP Light statistics collection function.


#### Procedure

* Run the [**display twamp-light**](cmdqueryname=display+twamp-light) [ **link-bundle** ] **test-session** [ **verbose** | *session-id* ] command to check the real-time statistics about a specified TWAMP Light test session.
* Run the [**display twamp-light statistic-type**](cmdqueryname=display+twamp-light+statistic-type) { **twoway-delay** | **twoway-loss** } **test-session** *session-id* [ **link-bundle-member** { *ifType* *ifNum* | *ifName* } ] [ **summary** ] command to check two-way delay or two-way packet loss statistics about a specified TWAMP Light test session.
* Run the [**display twamp-light statistic-type**](cmdqueryname=display+twamp-light+statistic-type) **oneway-delay** **test-session** *session-id* command to check one-way delay statistics about a specified TWAMP Light test session.
* Run the [**display twamp-light responder**](cmdqueryname=display+twamp-light+responder) [ **link-bundle** ] **test-session** [ **verbose** | *session-id* ] command to check real-time session information on the TWAMP Light Responder.
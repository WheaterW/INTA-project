Verifying the Configuration
===========================

After configuring STAMP, you can check STAMP session information.

#### Prerequisites

STAMP has been configured.


#### Procedure

* Run the [**display stamp**](cmdqueryname=display+stamp)[ **ipv4** | **ipv6** ] **test-session** [ **verbose** | **interface** { *ifName* | *ifType**ifNum* } ] command to check real-time information about STAMP sessions.
* Run the [**display stamp**](cmdqueryname=display+stamp) [ **ipv4** | **ipv6** ] **responder****test-session** [ **verbose** | **interface** { *ifName* | *ifType**ifNum* } ] command to check real-time session information on the Session-Reflector.
* Run the [**display stamp**](cmdqueryname=display+stamp)[ **ipv4** | **ipv6** ] **interface** {{ *interface-type**interface-number* | *interface-name* } | **all** } command to check brief information about STAMP sessions on an interface.
* Run the [**display stamp**](cmdqueryname=display+stamp) { **ipv4** | **ipv6** } **statistic-type****twoway-loss** ****interface**** { *interface-type**interface-number* | *interface-name* } command to check two-way packet loss statistics of STAMP sessions on an interface.
* Run the [**display stamp**](cmdqueryname=display+stamp) { **ipv4** | **ipv6** } **statistic-type****twoway-delay** ****interface**** { *interface-type**interface-number* | *interface-name* } command to check two-way delay statistics of STAMP sessions on an interface.
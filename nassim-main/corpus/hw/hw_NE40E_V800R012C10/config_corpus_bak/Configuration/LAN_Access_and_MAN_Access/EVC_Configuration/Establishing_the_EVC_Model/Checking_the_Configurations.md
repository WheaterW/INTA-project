Checking the Configurations
===========================

After establishing an EVC model, you can view the bridge domain configurations, including information about traffic encapsulation types and behaviors configured on an EVC Layer 2 sub-interface.

#### Prerequisites

The EVC model has been configured.


#### Procedure

* Run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) [ **binding-info** | [ *bd-id* [ **brief** | **verbose** | **binding-info** ] ] ] command to check bridge domain configurations.
* Run the [**display ethernet uni information**](cmdqueryname=display+ethernet+uni+information) [ **interface** *interface-type interface-number* ] command to check encapsulation types and behaviors configured on an EVC Layer 2 sub-interface.
Verifying the Configuration
===========================

After configuring bit-error-triggered IGP route switching, verify the configurations.

#### Prerequisites

Bit-error-triggered IGP route switching has been configured.


#### Procedure

* Run the [**display isis interface**](cmdqueryname=display+isis+interface) **verbose** or [**display ospf interface**](cmdqueryname=display+ospf+interface) **verbose** command to check the link quality information of all IS-IS or OSPF interfaces and whether the link costs have been adjusted based on link quality.
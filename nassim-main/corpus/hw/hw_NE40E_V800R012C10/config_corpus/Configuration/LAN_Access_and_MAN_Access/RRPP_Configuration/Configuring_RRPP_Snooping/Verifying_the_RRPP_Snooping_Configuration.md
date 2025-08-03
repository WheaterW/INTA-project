Verifying the RRPP Snooping Configuration
=========================================

After the basic RRPP Snooping functions are successfully configured, you can view the interface enabled with RRPP Snooping and the names of the virtual switch instances (VSIs) that are associated with RRPP Snooping.

#### Context

RRPP snooping function has been configured.


#### Procedure

* Run the [**display rrpp snooping enable**](cmdqueryname=display+rrpp+snooping+enable) { **all** | **interface** *{interface-name | interface-type interface-number*} } command to check the interface enabled with RRPP snooping.
* Run the [**display rrpp snooping vsi**](cmdqueryname=display+rrpp+snooping+vsi) { **all** | **interface** *{interface-type interface-number | interface-name}* } command to check the VSI associated with RRPP snooping.
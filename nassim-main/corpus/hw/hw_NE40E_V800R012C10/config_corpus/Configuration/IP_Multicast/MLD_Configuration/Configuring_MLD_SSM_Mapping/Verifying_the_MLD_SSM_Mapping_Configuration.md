Verifying the MLD SSM Mapping Configuration
===========================================

After configuring MLD Source-Specific Multicast (SSM) mapping, verify the configurations, including multicast groups configured with SSM mapping, SSM mapping rules of a specific multicast group, and SSM mapping status.

#### Prerequisites

MLD SSM mapping has been configured.


#### Procedure

* Run the [**display mld interface**](cmdqueryname=display+mld+interface) [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] command to check the configurations and operating status of MLD on an interface.
* Run the [**display mld group**](cmdqueryname=display+mld+group) [ *ipv6-group-address* | **interface** *interface-type* *interface-number* ] \* **ssm-mapping** [ **verbose** ] command to check details about MLD groups configured with SSM mapping.
* Run the [**display mld ssm-mapping**](cmdqueryname=display+mld+ssm-mapping) **group** [ *ipv6-group-address* ] command to check SSM mapping rules of a specified MLD group.
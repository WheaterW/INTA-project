Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display mld interface**](cmdqueryname=display+mld+interface) [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] command to check the configurations and operating status of MLD on interfaces.
* Run the [**display mld group**](cmdqueryname=display+mld+group) [ *ipv6-group-address* | **interface** { *interface-type* *interface-number* | *interface-name* } ] \* **ssm-mapping** [ **verbose** ] command to check information about MLD groups configured with SSM mapping.
* Run the [**display mld ssm-mapping**](cmdqueryname=display+mld+ssm-mapping) **group** [ *ipv6-group-address* ] command to check SSM mapping rules of a specified MLD group.
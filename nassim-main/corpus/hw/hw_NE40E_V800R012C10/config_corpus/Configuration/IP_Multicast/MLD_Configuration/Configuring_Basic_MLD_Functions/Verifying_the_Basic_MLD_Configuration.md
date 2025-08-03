Verifying the Basic MLD Configuration
=====================================

After configuring basic MLD functions, verify the MLD configurations, MLD operating status, and information about MLD group members.

#### Prerequisites

Basic MLD functions have been configured.


#### Procedure

* Run the [**display mld interface**](cmdqueryname=display+mld+interface) [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] command to view the configurations and operating status of MLD on an interface.
* Run the [**display mld group**](cmdqueryname=display+mld+group) [ *ipv6-group-address* | **interface** *interface-type* *interface-number* ] \* [ **static** ] [ **verbose** ] command to check information about MLD group members.
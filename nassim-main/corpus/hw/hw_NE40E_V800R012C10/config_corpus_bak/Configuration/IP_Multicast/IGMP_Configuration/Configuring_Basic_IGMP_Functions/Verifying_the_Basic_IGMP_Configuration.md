Verifying the Basic IGMP Configuration
======================================

After configuring basic IGMP functions, verify the IGMP configuration, IGMP operating status, and information about IGMP group members.

#### Prerequisites

Basic IGMP functions have been configured.


#### Procedure

* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **interface** [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] command to check the configurations and operating status of IGMP on an interface.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **group** [ *group-address* | **interface** *interface-type* *interface-number* ] \* [ **static** ] [ **verbose** ] command to check information about IGMP group members.
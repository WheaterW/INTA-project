Monitoring the Operating Status of IGMP
=======================================

To monitor the IGMP operating status, check information about IGMP groups, Source-Specific Multicast (SSM) mapping, IGMP-enabled interfaces, and IGMP routing tables.

#### Context

Run the following commands in any view to check the IGMP operating status.


#### Procedure

* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **group** [ *group-address* | **interface** *interface-type* *interface-number* ] \* [ **static** ] [ **verbose** ] command to check IGMP group information on an interface.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **group** [ *group-address* | **interface** *interface-type* *interface-number* ] \* **ssm-mapping** [ **verbose** ] command to check IGMP groups configured with SSM mapping.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **interface** [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] command to check the configurations and operating status of IGMP on an interface.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **ssm-mapping** **group** [ *group-address* ] command to check SSM mapping rules of a specified group.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **control-message counters** [ **interface** *interface-type* *interface-number* ] [ **message-type** { **query** | **report** } ] command to check statistics about IGMP control messages on a specific or all interfaces.
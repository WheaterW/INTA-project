Verifying the IGMP SSM Mapping Configuration
============================================

After configuring IGMP SSM mapping, verify the configuration, including multicast groups configured with SSM mapping, SSM mapping rules of a specific multicast group, and SSM mapping status.

#### Prerequisites

IGMP SSM mapping has been configured.


#### Procedure

* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **interface** [ *interface-type* *interface-number* | **up** | **down** ] [ **verbose** ] command to check the configurations and operating status of IGMP on an interface.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **group** [ *group-address* | **interface** *interface-type* *interface-number* ] \* **ssm-mapping** [ **verbose** ] command to check details about IGMP groups configured with SSM mapping.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **ssm-mapping** **group** [ *group-address* ] command to check SSM mapping rules of a specified IGMP group.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **ssm-mapping** **interface** [ *interface-type* *interface-number* ] command to check whether the SSM mapping function is enabled on an interface.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **dns-ssm-mapping** [ **group** *group-address* ] command to view information about DNS-based SSM mapping.
* Run the [**display ssm-mapping policy**](cmdqueryname=display+ssm-mapping+policy) *SsmMapPlcName* **group** *group-address* command to check the mapping rules of the SSM mapping policy configured on the device.
Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **group** [ *group-address* | **interface** *{ interface-type interface-number | interface-name }* ] \* **ssm-mapping** [ **verbose** ] command to check information about multicast groups configured with SSM mapping.
* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **ssm-mapping** **group** [ *group-address* ] command to check the SSM mapping rules of a specified group address.
* Run the [**display ssm-mapping policy**](cmdqueryname=display+ssm-mapping+policy) *SsmMapPlcName* [ **group** *group-address* ] command to check the mapping rules of the SSM mapping policy configured on the device.
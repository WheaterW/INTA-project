Verifying the Configuration
===========================

After configuring an mVRRP6 group, verify the binding between the common VRRP6 and mVRRP6 groups and verify the configurations.

#### Prerequisites

An mVRRP6 group has been configured.


#### Procedure

* Run the [**display vrrp6 admin-vrrp6**](cmdqueryname=display+vrrp6+admin-vrrp6) command to check the configuration and status information about all mVRRP6 groups configured on the device.
* Run the [**display vrrp6 binding admin-vrrp6**](cmdqueryname=display+vrrp6+binding+admin-vrrp6) [ **interface** *interface-type1* *interface-number1* ] [ **vrid** *virtual-router-id1* ] [ **member-vrrp** [ **interface** *interface-type2* *interface-number2* ] ] [ **vrid** *virtual-router-id2* ] command to check the binding between the mVRRP6 and common VRRP6 groups.
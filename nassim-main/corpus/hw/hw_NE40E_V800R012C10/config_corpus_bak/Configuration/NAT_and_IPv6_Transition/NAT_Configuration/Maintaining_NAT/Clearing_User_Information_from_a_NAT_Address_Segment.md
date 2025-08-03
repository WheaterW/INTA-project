Clearing User Information from a NAT Address Segment
====================================================

This section describes how to use the **reset** command to clear user information from a locked NAT address segment.

#### Context

When an address segment is locked, the users who have gone online from this address segment need to be logged out so that the locked address segment can be reclaimed.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only [dedicated boards](dc_ne_nat_feature_0008.html#EN-US_CONCEPT_0172359138__li1033371595) support this configuration.


![](../../../../public_sys-resources/notice_3.0-en-us.png) 

After user information of a NAT address segment is cleared, users on the NAT address segment will be logged out. Exercise caution when you perform this operation.



#### Procedure

* Run the [**reset nat user nat-ip-pool section**](cmdqueryname=reset+nat+user+nat-ip-pool+section) command to clear the user information from the address segment in a global address pool.
* Run the [**reset nat user address-group section**](cmdqueryname=reset+nat+user+address-group+section) command to clear the user information from the address segment in an address pool of a specified NAT instance.
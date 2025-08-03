Deleting Join Information of Multicast Groups
=============================================

If multicast group join information of a user is not needed, run the [**reset multicast group-ip**](cmdqueryname=reset+multicast+group-ip) command to delete it. After the command is run and then the user receives Query messages again, the device is triggered to restore the multicast group join information of the user.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

After the join information of a multicast group is deleted, services of this group will be interrupted.

If a large amount of join information is deleted, multicast route flapping may occur.



#### Procedure

* To delete join information of multicast groups, run the following commands in the user view:
  
  
  + [**reset multicast group-ip**](cmdqueryname=reset+multicast+group-ip) { *group-ipv4-address* | *group-ipv6-address* | **all** } { **user-id** *user-id* | **user-ip** { *user-ipv4-address* | *user-ipv6-address* } }
  + [**reset multicast group-ip**](cmdqueryname=reset+multicast+group-ip) { *group-ipv4-address* | *group-ipv6-address* | **all** } **user-ip** *user-ipv4-address* **vpn-instance** *vpn-instance-name*
  + [**reset multicast group-ip**](cmdqueryname=reset+multicast+group-ip) { *group-ipv4-address* | *group-ipv6-address* | **all** } **out-interface** *interface-type interface-number* [ **vpn-instance** *vpn-instance-name* ]
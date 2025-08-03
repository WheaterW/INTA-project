Enabling Port Load Balancing in a Public NAT Address Pool
=========================================================

To prevent user services from being compromised due to high port usage within a public address pool, the port load balancing is enabled for public NAT address pools. With this function enabled, new online users preferentially select public IP addresses with lower port usage, which leads to even use of ports within a public address pool.

#### Context

When a user attempts to get online, it selects a public address pool mapped to private network information based on a NAT traffic conversion policy. A public IP address is randomly selected from the public address pool. This process ensures that public IP addresses are evenly assigned to users. In dynamic port allocation scenarios, if a user dynamically applies for a great number of public ports, high usage of the ports mapped to a public IP address results in the insufficient number of ports assigned to other users within the same public network, which compromises services of the other users.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration is supported only on the CX600-M2K and CX600-M2K-B.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

This function is supported only on the [dedicated boards](dc_ne_nat_feature_0008.html).



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* **id** *id*
   
   
   
   The NAT instance view is displayed.
3. Run [**nat port-usage load-balance enable**](cmdqueryname=nat+port-usage+load-balance+enable)
   
   
   
   Port load balancing in a public NAT address pool is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
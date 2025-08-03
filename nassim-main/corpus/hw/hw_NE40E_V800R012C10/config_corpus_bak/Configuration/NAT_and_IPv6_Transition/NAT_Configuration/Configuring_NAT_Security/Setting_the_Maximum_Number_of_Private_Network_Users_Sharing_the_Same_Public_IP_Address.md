Setting the Maximum Number of Private Network Users Sharing the Same Public IP Address
======================================================================================

In PAT mode, multiple uses can use the same public IP address for access. However, excessive users may lead to network congestion. To address this issue, you can set the maximum number of private network users sharing the same public IP address.

#### Context

This configuration is applicable to the dynamic port allocation and per-port allocation modes where multiple users use the same public IP address for access. In these two modes, a public IP address can be used by a large number of users. If the number of sessions of these users is large, user traffic may fail to be forwarded. Therefore, the number of online users using a single public IP address needs to be limited.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only [dedicated boards](dc_ne_nat_feature_0008.html#EN-US_CONCEPT_0172359138__li1033371595) support this function.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance) *instance-name* **id** *id*
   
   
   
   The NAT instance view is displayed.
3. Run [**nat ip access-user limit**](cmdqueryname=nat+ip+access-user+limit) *max-number*
   
   
   
   The maximum number of allowed private network users sharing the same public IP address is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
Setting the Maximum Number of Private Network Users Who Use Public IP addresses Translated by NAT64 to Get Online
=================================================================================================================

If a device working in PAT mode creates a large number of NAT sessions for each of users sharing a public IP address, user traffic may fail to be forwarded. To prevent the problem, set the maximum number of private network users who can get online using the same public IP address.

#### Context

The limit on the number of private network users sharing a public IP address is primarily used when dynamic port range allocation or per-port allocation is used on a device working in PAT mode. When dynamic port range allocation or per-port allocation is used, without a port range specified, if a device creates a large number of NAT sessions for private network users sharing a public IP address, user traffic may fail to be forwarded. As a result, the number of users who attempt to use a single public IP address to get online is reduced.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only dedicated boards support this configuration.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* **id** *id*
   
   
   
   The NAT64 instance view is displayed.
3. Run [**nat64 ip access-user limit**](cmdqueryname=nat64+ip+access-user+limit) *max-number*
   
   
   
   The maximum number of private network users who can get online using the same NAT64 public IP address is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
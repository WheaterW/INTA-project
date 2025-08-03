Setting the Maximum Number of Private Network Users Sharing the Same Public IP Address
======================================================================================

In PAT mode, multiple uses can use the same public IP address for access. However, excessive users may lead to network congestion. To address this issue, you can set the maximum number of private network users sharing the same public IP address.

#### Context

This configuration is applicable to the dynamic port allocation and per-port allocation modes where multiple users use the same public IP address for access. In these two modes, a public IP address can be used by a large number of users. If the number of sessions of these users is large, user traffic may fail to be forwarded. Therefore, the number of online users using a single public IP address needs to be limited.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* **id** *id*
   
   
   
   The DS-Lite instance view is displayed.
3. Run [**ds-lite ip access-user limit**](cmdqueryname=ds-lite+ip+access-user+limit) *max-number*
   
   
   
   The maximum number of private network users sharing the same public IP address is set.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
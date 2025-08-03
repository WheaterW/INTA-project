(Optional) Configuring EDSG Service Traffic to Match a User Group
=================================================================

This section describes how to configure EDSG service traffic to match a user group in load-balancing scenarios.

#### Context

In load-balancing scenarios, after user traffic matches EDSG services, it must continue to match a user group for service selection.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**service-policy**](cmdqueryname=service-policy) **name** *policy-name* **edsg**
   
   
   
   The EDSG service policy view is displayed.
3. Run [**traffic match user-group**](cmdqueryname=traffic+match+user-group) [ **inbound** | **outbound** ]
   
   
   
   EDSG service traffic is configured to match a user group.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For DS-Lite users, the EDSG service matches the inner IPv4 address of the tunnel.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
Configuring Port Forwarding
===========================

When the IP addresses of internal servers frequently change, you can configure the port forwarding service to dynamically associate each internal server with a public IP address and port.

#### Context

The IP addresses of internal servers may frequently change. To prevent frequent manual modification of the NAT configurations, you can deploy the port forwarding function to dynamically associate each internal server with a public IP address and port.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance+id) *instance-name* [ **id** *id* ]
   
   
   
   The DS-Lite instance view is displayed.
3. Run [**port-forwarding**](cmdqueryname=port-forwarding+address-group+port-scope) **address-group** *addr-grp-name* **port-scope** *start-port-value* *end-port-value*
   
   
   
   The DS-Lite address pool and port range are configured to be dynamically associated with internal servers.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The [**port-forwarding address-group**](cmdqueryname=port-forwarding+address-group) command configures only the port range of the port forwarding service. Port forwarding rules, however, are issued by a RADIUS server when a user gets online.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
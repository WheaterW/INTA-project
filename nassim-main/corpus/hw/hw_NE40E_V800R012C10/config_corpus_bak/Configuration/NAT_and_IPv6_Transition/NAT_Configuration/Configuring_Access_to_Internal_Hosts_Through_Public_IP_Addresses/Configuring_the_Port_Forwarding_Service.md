Configuring the Port Forwarding Service
=======================================

If the IP addresses of internal servers frequently change, you can configure the port forwarding service to dynamically associate each internal server with a public IP address and a public port.

#### Context

The IP addresses of internal servers may frequently change. To avoid frequent manual modifications of the configurations of internal NAT servers, you can deploy the port forwarding function to dynamically associate each internal server with a public IP address and a public port.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only the NE40E-M2K and NE40E-M2K-B support this configuration.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**nat instance**](cmdqueryname=nat+instance+id) *instance-name* [ **id** *id* ]
   
   
   
   The NAT instance view is displayed.
3. Run [**port-forwarding**](cmdqueryname=port-forwarding+address-group+port-scope) **address-group** *addr-grp-name* **port-scope** *start-port-value* *end-port-value*
   
   
   
   The NAT address pool and port range are dynamically associated with internal servers.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This command configures only the port range of the port forwarding service. The port forwarding rules, however, are issued by a RADIUS server when a user goes online.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
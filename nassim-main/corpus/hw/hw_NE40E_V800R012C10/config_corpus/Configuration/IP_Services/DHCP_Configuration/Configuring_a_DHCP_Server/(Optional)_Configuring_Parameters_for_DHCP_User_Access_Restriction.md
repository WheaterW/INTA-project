(Optional) Configuring Parameters for DHCP User Access Restriction
==================================================================

(Optional) Configuring Parameters for DHCP User Access Restriction

#### Prerequisites

DHCP server packet receiving has been enabled using the [**dhcp server enable**](cmdqueryname=dhcp+server+enable) command on an interface if the interface needs to be used as a DHCP server.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* If multiple interfaces need to be used as DHCP servers, for security purposes, you are advised to preferentially run the [**dhcp server enable**](cmdqueryname=dhcp+server+enable) command on the interfaces to enable DHCP server packet receiving. If high security is not required, you run the [**dhcp server request-packet all-interface enable**](cmdqueryname=dhcp+server+request-packet+all-interface+enable) command in the system view to enable DHCP server packet receiving for all interfaces.
* If DHCP server packet receiving is not enabled, a DHCP server does not process DHCP request messages.


#### Context

If a large number of invalid connection request packets exist on a network, the network may be overloaded and even authorized users may not go online. By default, after DHCP user access restriction is enabled, if the number of connection request packets from a DHCP user exceeds 10 within 180 seconds, the user is suppressed for 300 seconds. If the default parameter configuration for DHCP user access restriction does not meet service requirements, you can adjust it.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp user chasten request-packets**](cmdqueryname=dhcp+user+chasten+request-packets) *reqPktNum* **check-period** *checkPer* **restrain-period** *restrainPer*
   
   
   
   Parameters are configured for DHCP user access restriction.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   DHCP user access restriction is disabled by default. If a large number of invalid connection request packets exist on a network, you can run the [**undo dhcp user chasten disable**](cmdqueryname=undo+dhcp+user+chasten+disable) command to enable DHCP user access restriction.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
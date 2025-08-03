Defining a VPN-based QoS Profile and Configuring Scheduling Parameters
======================================================================

You can define the Flow Queue (FQ) profile, FQ mapping object, service profile, and user group queue in a QoS profile.

#### Context

Perform the following configurations on the Router.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name*
   
   
   
   A VPN-based QoS profile is defined and the QoS profile view is displayed.
3. Run [**mpls-hqos flow-queue**](cmdqueryname=mpls-hqos+flow-queue) *flow-queue-name* [ **flow-mapping** *mapping-name* | **service-template** *template-name* | **user-group-queue** *group-queue-name* ] \*
   
   
   
   FQ scheduling parameters for VPN are configured in the QoS profile.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The service profile specified in this command must be a globally configured one rather than a board-specific one.
   
   This command is mutually exclusive with the [**car**](cmdqueryname=car) and [**user-queue**](cmdqueryname=user-queue) commands in the QoS profile view.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
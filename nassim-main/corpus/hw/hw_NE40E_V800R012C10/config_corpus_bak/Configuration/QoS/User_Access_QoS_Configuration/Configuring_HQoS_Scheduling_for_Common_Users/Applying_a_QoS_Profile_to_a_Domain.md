Applying a QoS Profile to a Domain
==================================

You can define a QoS profile and then apply it to the AAA domain to perform QoS scheduling for access user traffic.

#### Context

Applying a QoS profile to an interface functions differently from applying a QoS profile to a domain. The parameters about the bandwidth allocated to family users are obtained through the QoS profile applied to the interface while the parameters about the bandwidth allocated based on service types are obtained through the QoS profile applied to the domain.

The system performs traffic scheduling on common online users in a domain by directly adopting the parameters in the QoS profile applied to the domain. For family users, however, the system adopts only the parameters in the [**car**](cmdqueryname=car) command that is configured in the view of the QoS profile applied to the domain for traffic rate limiting.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) If the [**user-queue**](cmdqueryname=user-queue) command is run in a QoS profile to bind a flow queue in 4-CoS mode, perform the following configurations before applying the QoS profile because no user-queue resources support the 4-CoS mode by default.
   1. Run [**slot**](cmdqueryname=slot) *slot-id*
      
      
      
      The slot view is displayed.
   2. Run [**qos user-queue resource 4cos**](cmdqueryname=qos+user-queue+resource+4cos) *4cos-size*
      
      
      
      The specification of user-queue resources supporting the 4-CoS mode is specified.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
4. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   An AAA domain is created and its view is displayed.
   
   
   
   Here, *domain-name* specifies the domain to which the service needs to be mapped.
5. Run [**qos-profile**](cmdqueryname=qos-profile) *profile-name* { **inbound** | **outbound** } ****lns-gts****
   
   
   
   The QoS profile is applied to the domain.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The **lns-gts** parameter can be used only when a QoS profile is bound to L2TP users on an LNS.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the AAA view.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. (Optional) When a user accesses the device through an Eth-Trunk interface and the Eth-Trunk member interfaces reside on different forwarding or traffic management modules, to prevent the bandwidth of the Eth-Trunk interface from doubling, perform the following operations to configure the total bandwidth to be allocated among Eth-Trunk member interfaces based on weights.
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The Eth-Trunk interface view is displayed.
   2. Perform either of the following operations based on the user access type:
      
      
      * For common access users, run the [**qos subscriber-access member-link-scheduler distribute**](cmdqueryname=qos+subscriber-access+member-link-scheduler+distribute) **inbound** command to allocate the bandwidth to trunk member interfaces based on weights.
      * For private line access users, run the [**qos leased-line-access member-link-scheduler distribute**](cmdqueryname=qos+leased-line-access+member-link-scheduler+distribute) { **inbound** | **outbound** } command to allocate the bandwidth to trunk member interfaces based on weights.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
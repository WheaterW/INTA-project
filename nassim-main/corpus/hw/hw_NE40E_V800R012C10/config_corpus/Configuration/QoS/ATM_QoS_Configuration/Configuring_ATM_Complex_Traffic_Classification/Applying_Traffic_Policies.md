Applying Traffic Policies
=========================

Class-based traffic policies take effect only after they are applied to interfaces.

#### Context

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run one of the following commands as required.
   
   
   * To enter the ATM interface (or sub-interface) view, run:
     
     ```
     [interface](cmdqueryname=interface) atm interface-number [.sub-interface ]
     ```
   * To enter the VE interface view, run:
     
     ```
     [interface](cmdqueryname=interface) virtual-ethernet interface-number
     ```
3. Run [**traffic-policy**](cmdqueryname=traffic-policy) *policy-name* { **inbound** | **outbound** }
   
   
   
   A traffic policy is applied to the interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * After a traffic policy is applied to an interface, you cannot modify the **shared** or **unshared** mode of the traffic policy. Before modifying the **shared** or **unshared** mode of a traffic policy, you must cancel the application of the traffic policy from the interface.
   * A traffic policy with the **shared** attribute: For a traffic policy that is applied to different interfaces, the statistics displayed for an individual interface is the sum of the statistics of all interfaces to which the traffic policy is applied. Therefore, the original data for each individual interface is not identifiable.
   * A traffic policy with the **unshared** attribute: You can identify the statistics of a traffic policy according to the interface where the traffic policy is applied.
   * The inbound and outbound attributes can be identified in traffic statistics, no matter a policy is of the **shared** attribute or the **unshared** attribute.
   * An ATM interface configured with ATM transparent cell transport services does not support the ATM complex traffic classification or this command.
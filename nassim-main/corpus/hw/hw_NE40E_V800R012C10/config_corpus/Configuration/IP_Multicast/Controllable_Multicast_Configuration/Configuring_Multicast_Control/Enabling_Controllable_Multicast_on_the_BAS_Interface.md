Enabling Controllable Multicast on the BAS Interface
====================================================

After controllable multicast is enabled on an interface, the interface controls the users' rights to access the multicast groups based on multicast configurations in the AAA view.

#### Context

Perform the following steps on the Router:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Before enabling controllable multicast on the interface, you must enable IGMP.

This feature is supported only on the Admin-VS.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   The bas interface is created.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the interface view.
5. Run [**igmp enable**](cmdqueryname=igmp+enable)
   
   
   
   IGMP is enabled on the interface.
6. Run [**multicast authorization-enable**](cmdqueryname=multicast+authorization-enable)
   
   
   
   Controllable multicast is enabled.
   
   
   
   After controllable multicast is enabled on the interface, the interface controls the authorities of users to join related multicast groups according to the configuration of multicast services in the AAA view.
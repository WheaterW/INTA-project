Configuring Neighbor Relationship Flapping Suppression on an OSPF Multi-Area Adjacency Interface
================================================================================================

Neighbor relationship flapping suppression can be configured on an OSPF multi-area adjacency interface to delay OSPF neighbor relationship reestablishment or set the link cost to the maximum value in case of neighbor relationship flapping.

#### Usage Scenario

If an interface carrying OSPF services frequently alternates between up and down, frequent neighbor relationship flapping will occur. During the flapping, OSPF frequently sends Hello packets to reestablish the neighbor relationship, synchronizes LSDBs, and recalculates routes. In this process, a large number of packets are exchanged, adversely affecting neighbor relationship stability, OSPF services, and other OSPF-dependent services, such as LDP and BGP. OSPF neighbor relationship flapping suppression can address this problem by delaying OSPF neighbor relationship reestablishment or preventing service traffic from passing through flapping links.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The following steps are optional, and choose them as required.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
   
   
   
   To disable the function globally, run the [**suppress-flapping peer disable**](cmdqueryname=suppress-flapping+peer+disable) command.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ospf enable**](cmdqueryname=ospf+enable) [ *process-id* ] **area** *area-id*
   
   
   
   OSPF is enabled on the interface.
4. Run [**ospf enable multi-area**](cmdqueryname=ospf+enable+multi-area) *area-id*
   
   
   
   OSPF is enabled on the multi-area adjacency interface.
5. (Optional) Run [**ospf suppress-flapping peer disable multi-area**](cmdqueryname=ospf+suppress-flapping+peer+disable+multi-area) *area-id*
   
   
   
   OSPF neighbor relationship flapping suppression on a multi-area adjacency interface is disabled.
   
   
   
   To disable OSPF neighbor relationship flapping suppression from one of the interfaces, run this command.
6. Run [**ospf suppress-flapping peer hold-down**](cmdqueryname=ospf+suppress-flapping+peer+hold-down) *interval* **multi-area** *area-id*
   
   
   
   The Hold-down mode and its duration are configured for the multi-area adjacency interface.
   
   
   
   OSPF neighbor relationship flapping suppression operates in Hold-down or Hold-max-cost mode.
   
   * Hold-down mode: In the case of frequent flooding and topology changes during neighbor relationship establishment, interfaces prevent neighbor relationship reestablishment during the suppression period, which reduces LSDB synchronization attempts and packet exchanges.
   * Hold-max-cost mode: If the traffic forwarding path changes frequently, interfaces use 65535 (maximum value) as the cost of the flapping link during the suppression period. This prevents traffic from passing through the flapping link.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     To change the value of Max-cost for OSPF links, run the [**maximum-link-cost**](cmdqueryname=maximum-link-cost) *cost* command.
   
   The Hold-down mode and Hold-max-cost mode can be both used. When both modes are configured, the device first enters the Hold-down mode. After exiting the Hold-down mode, the device enters the Hold-max-cost mode.
   
   To disable the Hold-max-cost mode, run the [**ospf suppress-flapping peer hold-max-cost disable multi-area**](cmdqueryname=ospf+suppress-flapping+peer+hold-max-cost+disable+multi-area) command.
7. Run [**ospf suppress-flapping peer**](cmdqueryname=ospf+suppress-flapping+peer) { **detecting-interval** *detecting-interval* | **threshold** *threshold* | **resume-interval** *resume-interval* } \* **multi-area** *area-id*
   
   
   
   Detection parameters are configured for OSPF neighbor relationship flapping suppression on the multi-area adjacency interface.
   
   
   
   * Configure a threshold for exiting OSPF neighbor relationship flapping suppression.
     
     If the interval between two successive neighbor relationship state changes from Full to a non-Full state is longer than the *resume-interval*, the flapping\_count is reset.
   * If OSPF neighbor relationship flapping suppression works in Hold-max-cost mode, the value of *resume-interval* indicates the duration of this mode.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The value of *resume-interval* must be greater than that of *detecting-interval*.
   
   
   You can configure detection parameters for OSPF neighbor relationship flapping suppression on specific interfaces according to network conditions. However, using the default values of these parameters is recommended.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   The user view is displayed.
10. Run [**reset ospf**](cmdqueryname=reset+ospf) *process-id* **suppress-flapping peer** [ *interface-name* [ **all-areas** | **area** *area-id* ] | *interface-type* *interface-number* [ **all-areas** | **area** *area-id* ] ] [ **notify-peer** ]
    
    
    
    The OSPF multi-area adjacency interface is configured to exit neighbor relationship flapping suppression.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    The interface exits flapping suppression in the following scenarios:
    
    * The suppression timer expires.
    * The corresponding OSPF process is reset.
    * An OSPF neighbor is reset using the [**reset ospf peer**](cmdqueryname=reset+ospf+peer) command.
    * OSPF neighbor relationship flapping suppression is disabled globally using the [**suppress-flapping peer disable (OSPF)**](cmdqueryname=suppress-flapping+peer+disable+%28OSPF%29) command.
    * The [**reset ospf suppress-flapping peer**](cmdqueryname=reset+ospf+suppress-flapping+peer) command is run.
11. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
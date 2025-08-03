Configuring OSPF Neighbor Relationship Flapping Suppression
===========================================================

OSPF neighbor relationship flapping suppression works by delaying OSPF neighbor relationship reestablishment or setting the link cost to the maximum value.

#### Usage Scenario

If an interface carrying OSPF services frequently alternates between up and down, frequent neighbor relationship flapping will occur. During the flapping, OSPF frequently sends Hello packets to reestablish the neighbor relationship, synchronizes LSDBs, and recalculates routes. In this process, a large number of packets are exchanged, adversely affecting neighbor relationship stability, OSPF services, and other OSPF-dependent services, such as LDP and BGP. OSPF neighbor relationship flapping suppression can address this problem by delaying OSPF neighbor relationship reestablishment or preventing service traffic from passing through flapping links.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The following steps are optional, and choose them as required.



#### Pre-configuration Tasks

Before configuring OSPF neighbor relationship flapping suppression, complete the following tasks:

* Configure an IP address for each interface to ensure that neighboring routers are reachable at the network layer.
* [Configure basic OSPF functions.](dc_vrp_ospf_cfg_0003.html)

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Disable OSPF neighbor relationship flapping suppression globally.
   
   
   1. Run the [**ospf**](cmdqueryname=ospf) [ *process-id* | **router-id** *router-id* ]\* command to enter the OSPF view.
   2. Run the [**suppress-flapping peer disable**](cmdqueryname=suppress-flapping+peer+disable) command to disable OSPF neighbor relationship flapping suppression.
   3. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   
   
   
   To disable the function globally, perform this step.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. (Optional) Run [**suppress-flapping peer disable**](cmdqueryname=suppress-flapping+peer+disable)
   
   
   
   OSPF neighbor relationship flapping suppression is disabled on the interface.
   
   
   
   To disable the function on one of the interfaces, perform this step.
5. Configure an OSPF neighbor relationship flapping suppression mode, which can be Hold-down or Hold-max-cost mode.
   
   
   * Hold-down mode:
     
     To configure the Hold-down mode and set its duration, run the [**ospf suppress-flapping peer hold-down**](cmdqueryname=ospf+suppress-flapping+peer+hold-down) *interval* command.
     
     If flooding and topology changes frequently occur during OSPF neighbor relationship establishment, you can configure the Hold-down mode to prevent OSPF neighbor relationship reestablishment within a period of time. This prevents frequent LSDB synchronization and a large number of packets from being exchanged.
   * Hold-max-cost mode:
     
     If user service traffic is frequently switched, you can configure OSPF neighbor relationship flapping suppression to work in Hold-max-cost mode. In this mode, the link cost is set to the maximum value (Max-cost) within a period of time, preventing user service traffic from passing through flapping links.
     
     1. (Optional) Set the maximum cost for OSPF links.
        
        If OSPF neighbor relationship flapping suppression works in Hold-max-cost mode, the device sets the link cost to the maximum value (Max-cost) within a period of time, preventing service traffic from passing through flapping links.
        
        If the value needs to be modified, perform this step.
        1. Run [**quit**](cmdqueryname=quit)
           
           Return to the system view.
        2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
           
           The OSPF view is displayed.
        3. Run [**maximum-link-cost**](cmdqueryname=maximum-link-cost) *cost*
           
           The maximum cost of OSPF is changed.
        4. Run [**quit**](cmdqueryname=quit)
           
           Return to the system view.
        5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
           
           The interface view is displayed.
     2. (Optional) Run [**ospf suppress-flapping peer hold-max-cost disable**](cmdqueryname=ospf+suppress-flapping+peer+hold-max-cost+disable)
        
        The Hold-max-cost neighbor relationship flapping suppression mode is disabled.
        
        To disable the Hold-max-cost neighbor relationship flapping suppression mode, perform this step.
   
   
   
   Flapping suppression can also work first in Hold-down mode and then in Hold-max-cost mode.
6. Run [**ospf suppress-flapping peer**](cmdqueryname=ospf+suppress-flapping+peer) { **detecting-interval** *detecting-interval* | **threshold** *threshold* | **resume-interval** *resume-interval* }\*
   
   
   
   Detection parameters are configured for OSPF neighbor relationship flapping suppression.
   
   
   
   * Specify an interval for exiting OSPF neighbor relationship flapping suppression.
     
     If the interval between two successive neighbor relationship states (changing from Full to a non-Full state) is longer than the *resume-interval*, the flapping\_count is reset.
   * If OSPF neighbor relationship flapping suppression works in Hold-max-cost mode, the value of *resume-interval* indicates the duration of this mode.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The value of *resume-interval* must be greater than that of *detecting-interval*.
   
   
   
   You can configure detection parameters for OSPF neighbor relationship flapping suppression on specific interfaces according to network conditions. However, using the default values of these parameters is recommended.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   The user view is displayed.
10. Run [**reset ospf**](cmdqueryname=reset+ospf) *process-id* **suppress-flapping** **peer** [ *interface-type* *interface-number* ] [ **notify-peer** ]
    
    
    
    Interfaces are forced to exit OSPF neighbor relationship flapping suppression.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    Interfaces exit flapping suppression in the following scenarios:
    
    * The suppression timer expires.
    * The corresponding OSPF process is reset.
    * An OSPF neighbor is reset using the [**reset ospf peer**](cmdqueryname=reset+ospf+peer) command.
    * OSPF neighbor relationship flapping suppression is disabled globally using the [**suppress-flapping peer disable**](cmdqueryname=suppress-flapping+peer+disable) command in the OSPF view.
    * The [**reset ospf suppress-flapping peer**](cmdqueryname=reset+ospf+suppress-flapping+peer) command is run.

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** *interfaceType* *interfaceNum* **verbose** command to check the status of OSPF neighbor relationship flapping suppression.
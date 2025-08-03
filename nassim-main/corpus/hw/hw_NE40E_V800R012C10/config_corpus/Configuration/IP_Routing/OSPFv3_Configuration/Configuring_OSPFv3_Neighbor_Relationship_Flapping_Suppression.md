Configuring OSPFv3 Neighbor Relationship Flapping Suppression
=============================================================

OSPFv3 neighbor relationship flapping suppression works by delaying OSPFv3 neighbor relationship reestablishment or setting the link cost to the maximum value.

#### Usage Scenario

If an interface carrying OSPFv3 services alternates between up and down, OSPFv3 neighbor relationship flapping occurs on the interface. During the flapping, OSPFv3 frequently sends Hello packets to reestablish the neighbor relationship, synchronizes LSDBs, and recalculates routes. In this process, a large number of packets are exchanged, adversely affecting neighbor relationship stability, OSPFv3 services, and other OSPFv3-dependent services. OSPFv3 neighbor relationship flapping suppression can address this problem by delaying OSPFv3 neighbor relationship reestablishment or preventing service traffic from passing through flapping links.


#### Pre-configuration Tasks

Before configuring OSPFv3 neighbor relationship flapping suppression, complete the following tasks:

* Configure an IP address for each interface to ensure that neighboring devices are reachable at the network layer.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. (Optional) Disable OSPFv3 neighbor relationship flapping suppression globally.
   
   
   1. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
      
      The OSPFv3 view is displayed.
   2. Run [**suppress-flapping peer disable**](cmdqueryname=suppress-flapping+peer+disable)
      
      OSPFv3 neighbor relationship flapping suppression is disabled.
   3. Run [**quit**](cmdqueryname=quit)
      
      Return to the system view.
   
   
   
   To disable the function globally, perform this step.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. (Optional) Run [**ospfv3 suppress-flapping peer disable**](cmdqueryname=ospfv3+suppress-flapping+peer+disable)
   
   
   
   OSPFv3 neighbor relationship flapping suppression is disabled on the interface.
   
   
   
   To disable the function on one of the interfaces, perform this step.
5. Configure an OSPFv3 neighbor relationship flapping suppression mode, which can be Hold-down or Hold-max-cost mode.
   
   
   * Hold-down mode:
     
     Run the [**ospfv3 suppress-flapping peer hold-down**](cmdqueryname=ospfv3+suppress-flapping+peer+hold-down) *interval* [ **instance** *instance-id* ] command to configure the Hold-down mode and set its duration.
     
     If flooding and topology changes frequently occur during OSPFv3 neighbor relationship establishment, you can configure the Hold-down mode to prevent OSPFv3 neighbor relationship reestablishment within a period of time. This prevents frequent LSDB synchronization and a large number of packets from being exchanged.
   * Hold-max-cost mode:If user service traffic is frequently switched, you can configure OSPFv3 neighbor relationship flapping suppression to work in Hold-max-cost mode. In this mode, the link cost is set to the maximum value (Max-cost) within a period of time, preventing user service traffic from passing through flapping links.
     1. (Optional) Set the maximum cost for OSPFv3 links. If the value needs to be modified, perform this step.
        1. Run [**quit**](cmdqueryname=quit)
           
           Return to the system view.
        2. Run [**ospfv3**](cmdqueryname=ospfv3) [ *process-id* ]
           
           The OSPFv3 view is displayed.
        3. Run [**maximum-link-cost**](cmdqueryname=maximum-link-cost) *cost*
           
           The maximum cost of OSPFv3 is set.
        4. Run [**quit**](cmdqueryname=quit)
           
           Return to the system view.
        5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
           
           The interface view is displayed.
     2. (Optional) Run [**ospfv3 suppress-flapping peer hold-max-cost disable**](cmdqueryname=ospfv3+suppress-flapping+peer+hold-max-cost+disable) [ **instance** *instance-id* ]
        
        The Hold-max-cost neighbor relationship flapping mode is disabled.
        
        To disable the Hold-max-cost neighbor relationship flapping suppression mode, perform this step.
   
   
   
   Flapping suppression can also work first in Hold-down mode and then in Hold-max-cost mode.
6. (Optional) Run [**ospfv3 suppress-flapping peer**](cmdqueryname=ospfv3+suppress-flapping+peer) { **detecting-interval** *detecting-interval* | **threshold** *threshold* | **resume-interval** *resume-interval* }\* [ **instance** *instance-id* ]
   
   
   
   Detection parameters are configured for OSPFv3 neighbor relationship flapping suppression.
   
   
   
   Each OSPFv3 interface on which OSPFv3 neighbor relationship flapping suppression is enabled starts a flapping counter. If the interval between two successive neighbor status changes from Full to a non-Full state is shorter than *detecting-interval*, a valid flapping\_event is recorded, and the flapping\_count is incremented by 1.
   
   When the flapping\_count reaches or exceeds *threshold*, flapping suppression takes effect.
   
   If the interval between two successive neighbor status changes from Full to a non-Full state is longer than *resume-interval*, the flapping\_count is reset.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The value of *resume-interval* must be greater than that of *detecting-interval*.
   
   You can configure detection parameters for OSPFv3 neighbor relationship flapping suppression on specific interfaces according to network conditions. However, using the default values of these parameters is recommended.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the user view.
10. (Optional) Run [**reset ospfv3**](cmdqueryname=reset+ospfv3) *process-id* **suppress-flapping peer** [ *interface-type interface-number* ] [ **notify-peer** ]
    
    
    
    The OSPFv3 interface is configured to exit neighbor relationship flapping suppression.
    
    
    
    To exit neighbor relationship flapping suppression in advance after the fault that causes OSPFv3 neighbor relationship flapping is rectified, perform this step.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) Interfaces exit flapping suppression in the following scenarios:
    * The suppression timer expires.
    * The corresponding OSPFv3 process is reset.
    * An OSPFv3 neighbor relationship is reset using the [**reset ospfv3 peer**](cmdqueryname=reset+ospfv3+peer) command.
    * OSPFv3 neighbor relationship flapping suppression is disabled globally using the [**suppress-flapping peer disable**](cmdqueryname=suppress-flapping+peer+disable) command in the OSPFv3 view.
    * The [**reset ospfv3 suppress-flapping peer**](cmdqueryname=reset+ospfv3+suppress-flapping+peer) command is run to exit flapping suppression.

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **no-peer** | **area** *area-id* ] [ *interface-type* *interface-number* ] command to check the status of OSPFv3 neighbor relationship flapping suppression.
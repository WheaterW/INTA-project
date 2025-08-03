Configuring IS-IS Neighbor Relationship Flapping Suppression
============================================================

IS-IS neighbor relationship flapping suppression works by delaying IS-IS neighbor relationship reestablishment or setting the link cost to the maximum value.

#### Usage Scenario

If the status of an interface carrying IS-IS services alternates between up and down, the neighbor relationship frequently flaps. During the flapping, IS-IS reestablishes the neighbor relationship and recalculates routes. In this process, a large number of packets are exchanged, adversely affecting neighbor relationship stability, IS-IS services, and other IS-IS-dependent services, such as LDP and BGP. IS-IS neighbor relationship flapping suppression can address this problem by either delaying IS-IS neighbor relationship reestablishment, or setting the link cost to the maximum value to prevent service traffic from passing through flapping links.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The following steps are optional, choose them as required.



#### Pre-configuration Tasks

Before configuring IS-IS neighbor relationship flapping suppression, complete the following tasks:

* Configure an IP address for each interface to ensure that neighboring routers are reachable at the network layer.
* [Configuring Basic IPv4 IS-IS Functions](dc_vrp_isis_cfg_1000.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
   
   
   
   To disable the function globally, run the [**suppress-flapping peer disable**](cmdqueryname=suppress-flapping+peer+disable) command.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   
   
   To disable IS-IS neighbor relationship flapping suppression from one of the interfaces, run the [**isis suppress-flapping peer disable**](cmdqueryname=isis+suppress-flapping+peer+disable) command.
3. Run [**isis suppress-flapping peer hold-down**](cmdqueryname=isis+suppress-flapping+peer+hold-down) *interval*
   
   
   
   The Hold-down mode is configured, and its duration is set.
   
   
   
   IS-IS neighbor relationship flapping suppression works in either Hold-down or Hold-max-cost mode.
   
   * Hold-down mode: In the case of frequent flooding and topology changes during neighbor relationship establishment, interfaces prevent neighbor relationship reestablishment during Hold-down suppression, which minimizes synchronization attempts and packet exchanges.
   * Hold-max-cost mode: If the traffic forwarding path changes frequently, interfaces use the maximum value (16777214 for the wide mode and 63 for the narrow mode) as the cost of the flapping link during Hold-max-cost suppression, which prevents traffic from passing through the flapping link.
   
   Flapping suppression can also work first in Hold-down mode and then in Hold-max-cost mode.
   
   To disable this mode, run the [**isis suppress-flapping peer hold-max-cost**](cmdqueryname=isis+suppress-flapping+peer+hold-max-cost) **disable** command.
4. Run [**isis suppress-flapping peer**](cmdqueryname=isis+suppress-flapping+peer) { **detecting-interval** *detecting-interval* | **threshold** *threshold* | **resume-interval** *resume-interval* } \*
   
   
   
   Detection parameters are configured for IS-IS neighbor relationship flapping suppression.
   
   
   
   Each IS-IS interface on which IS-IS neighbor relationship flapping suppression is enabled starts a flapping counter. If the interval between two successive times when the neighbor state is ExStart or Down is shorter than or equal to *detecting-interval*, a valid flapping\_event is recorded, and the flapping\_count increases by 1. When the flapping\_count reaches or exceeds *threshold*, flapping suppression takes effect. If the interval between two successive times when the neighbor state is ExStart or Down is longer than or equal to *resume-interval*, the flapping\_count is reset.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The value of *resume-interval* must be greater than that of *detecting-interval*.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the user view.
7. Run [**reset isis**](cmdqueryname=reset+isis) *process-id* **suppress-flapping peer** [ **interface** { *interface-name* | *interfaceType* *interfaceNum* } ] [ **notify-peer** ]
   
   
   
   The interface exits the neighbor flapping suppression.
   
   
   
   Interfaces exit from flapping suppression in the following scenarios:
   * The suppression timer expires.
   * The corresponding IS-IS process is reset.
   * An IS-IS neighbor is reset using the [**reset isis peer**](cmdqueryname=reset+isis+peer) command.
   * IS-IS neighbor relationship flapping suppression is disabled globally using the [**suppress-flapping peer disable**](cmdqueryname=suppress-flapping+peer+disable) command.
   * The [**reset isis suppress-flapping peer**](cmdqueryname=reset+isis+suppress-flapping+peer) command is run to forcibly exit flapping suppression.
   * The [**reset isis**](cmdqueryname=reset+isis) *process-id* **suppress-flapping peer** [ **interface** *interface-type* *interface-number* ] **notify-peer** command is run on the peer device to forcibly exit flapping suppression.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display isis**](cmdqueryname=display+isis) [ *process-id* ] **interface** *interfaceType* *interfaceNum* **verbose** command to check the status of IS-IS neighbor relationship flapping suppression.
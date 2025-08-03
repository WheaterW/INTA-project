Configuring OSPFv3 Neighbor Relationship Flapping Suppression
=============================================================

Configuring OSPFv3 Neighbor Relationship Flapping Suppression

#### Prerequisites

Before configuring OSPFv3 neighbor relationship flapping suppression, you have completed the following task:

* [Configure basic OSPFv3 functions](vrp_ospfv3_cfg_0009.html).

#### Context

If an interface carrying OSPFv3 services frequently alternates between up and down, OSPFv3 neighbor relationship flapping will occur on the interface. In this case, OSPFv3 frequently sends Hello packets to re-establish neighbor relationships, synchronizes LSDBs, and recalculates routes. As a result, a large number of packets are exchanged, compromising the stability of existing neighbor relationships, OSPFv3 services, and other OSPFv3-dependent services. To overcome this problem, OSPFv3 neighbor relationship flapping suppression can delay the OSPFv3 neighbor relationship from being re-established or prevent service traffic from passing through flapping links.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Disable OSPFv3 neighbor relationship flapping suppression globally.
   
   
   ```
   [ospfv3](cmdqueryname=ospfv3) [ process-id ]
   [suppress-flapping peer disable](cmdqueryname=suppress-flapping+peer+disable+%28OSPFv3+view%29)
   [quit](cmdqueryname=quit)
   ```
   
   By default, OSPFv3 neighbor relationship flapping suppression is enabled globally. This function is enabled on each interface in the current OSPFv3 process. To disable this function globally, perform this step.
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Enable the Hold-down mode and set a corresponding duration.
   
   
   ```
   [ospfv3 suppress-flapping peer hold-down](cmdqueryname=ospfv3+suppress-flapping+peer+hold-down) interval [ instance instance-id ]
   ```
   
   Flapping suppression is classified as Hold-down mode or Hold-max-cost mode:
   
   * Hold-down mode: In the case of frequent flooding and topology changes during neighbor relationship establishment, interfaces prevent neighbor relationship re-establishment during Hold-down suppression, which minimizes LSDB synchronization attempts and packet exchanges.
   * Hold-max-cost mode: If the traffic forwarding path changes frequently, interfaces use 65535 (maximum value) as the cost of the flapping link during Hold-max-cost suppression, which prevents traffic from passing through the flapping link.![](../public_sys-resources/note_3.0-en-us.png) 
     
     You can run the [**maximum-link-cost**](cmdqueryname=maximum-link-cost%28ospfv3%29) *cost* command in the OSPFv3 view to change the maximum cost for OSPFv3 links.
   
   By default, the Hold-max-cost mode takes effect. If both modes are enabled, flapping suppression initially works in Hold-down mode (until its duration expires) and then in Hold-max-cost mode.
6. (Optional) Disable the Hold-max-cost mode.
   
   
   ```
   [ospfv3 suppress-flapping peer hold-max-cost disable](cmdqueryname=ospfv3+suppress-flapping+peer+hold-max-cost+disable) [ instance instance-id ]
   ```
7. (Optional) Configure detection parameters for OSPFv3 neighbor relationship flapping suppression.
   
   
   ```
   [ospfv3 suppress-flapping peer](cmdqueryname=ospfv3+suppress-flapping+peer) { detecting-interval detecting-interval | threshold threshold | resume-interval resume-interval } * [ instance instance-id ]
   ```
   
   An OSPFv3 interface with neighbor relationship flapping suppression enabled starts a flapping counter. If the interval between two successive neighbor relationship states (changing from Full to a non-Full state) is shorter than the **detecting-interval**, a valid flapping\_event is recorded, and the flapping\_count is incremented by 1. When the flapping\_count reaches or exceeds the **threshold**, flapping suppression takes effect. If the interval between two successive neighbor relationship states (changing from Full to a non-Full state) is longer than the **resume-interval**, the flapping\_count is reset.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   The value of *resume-interval* must be greater than that of *detecting-interval*.
   
   You can configure detection parameters for OSPFv3 neighbor relationship flapping suppression on specific interfaces according to network conditions. However, using the default values of these parameters is recommended. By default, the detection interval for OSPFv3 neighbor relationship flapping suppression is 60 seconds, the suppression threshold is 10, and the interval for exiting flapping suppression is 120 seconds.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
9. (Optional) Configure the specified OSPFv3 interface to exit neighbor relationship flapping suppression.
   
   
   ```
   [quit](cmdqueryname=quit)
   [quit](cmdqueryname=quit)
   [reset ospfv3](cmdqueryname=reset+ospfv3) process-id suppress-flapping peer [ interface-type interface-number ] [ notify-peer ]
   ```
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) Interfaces exit flapping suppression in the following scenarios:
   * The suppression timer expires.
   * The corresponding OSPFv3 process is reset.
   * An OSPFv3 neighbor relationship is reset using the [**reset ospfv3 peer**](cmdqueryname=reset+ospfv3+peer) command.
   * OSPFv3 neighbor relationship flapping suppression is disabled globally using the [**suppress-flapping peer disable**](cmdqueryname=suppress-flapping+peer+disable) command in the OSPFv3 view.

#### Verifying the Configuration

Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **interface** [ **no-peer** | **area** *area-id* ] [ *interface-type* *interface-number* ] command to check the status of OSPFv3 neighbor relationship flapping suppression.

**Suppress flapping peer** in the command output indicates the current suppression mode (Hold-down), when flapping suppression started, and the remaining time before flapping suppression exits.
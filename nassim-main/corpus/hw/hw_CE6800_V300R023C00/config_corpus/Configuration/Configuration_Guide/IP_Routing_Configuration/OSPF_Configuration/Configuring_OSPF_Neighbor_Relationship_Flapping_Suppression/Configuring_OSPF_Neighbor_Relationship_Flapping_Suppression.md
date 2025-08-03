Configuring OSPF Neighbor Relationship Flapping Suppression
===========================================================

Configuring OSPF Neighbor Relationship Flapping Suppression

#### Prerequisites

Before configuring OSPF neighbor relationship flapping suppression, you have completed the following task:

* [Configure basic OSPF functions](vrp_ospf_cfg_0010.html).

#### Context

If an interface carrying OSPF services frequently alternates between up and down, OSPF neighbor relationship flapping will occur on the interface. In this case, OSPF frequently sends Hello packets to re-establish neighbor relationships, synchronizes LSDBs, and recalculates routes. As a result, a large number of packets are exchanged, compromising the stability of existing neighbor relationships, OSPF services, and other OSPF-dependent services. To overcome this problem, OSPF neighbor relationship flapping suppression can delay the OSPF neighbor relationship from being re-established or prevent service traffic from passing through flapping links.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Disable OSPF neighbor relationship flapping suppression globally.
   
   
   ```
   [ospf](cmdqueryname=ospf) [ process-id ]
   [suppress-flapping peer disable](cmdqueryname=suppress-flapping+peer+disable)
   [quit](cmdqueryname=quit)
   ```
   
   By default, OSPF neighbor relationship flapping suppression is enabled globally. This function is enabled on each interface in the current OSPF process. To disable this function globally, perform this step.
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
   [ospf suppress-flapping peer hold-down](cmdqueryname=ospf+suppress-flapping+peer+hold-down) interval
   ```
   
   Flapping suppression is classified as Hold-down mode or Hold-max-cost mode:
   
   * Hold-down mode: In the case of frequent flooding and topology changes during neighbor relationship establishment, interfaces prevent neighbor relationship re-establishment during Hold-down suppression, which minimizes LSDB synchronization attempts and packet exchanges.
   * Hold-max-cost mode: If the traffic forwarding path changes frequently, interfaces use 65535 (maximum value) as the cost of the flapping link during Hold-max-cost suppression, which prevents traffic from passing through the flapping link.
   
   By default, the Hold-max-cost mode takes effect. If both modes are enabled, flapping suppression initially works in Hold-down mode (until its duration expires) and then in Hold-max-cost mode.
6. (Optional) Disable the Hold-max-cost mode.
   
   
   ```
   [ospf suppress-flapping peer hold-max-cost disable](cmdqueryname=ospf+suppress-flapping+peer+hold-max-cost+disable)
   ```
7. (Optional) Configure detection parameters for OSPF neighbor relationship flapping suppression.
   
   
   ```
   [ospf suppress-flapping peer](cmdqueryname=ospf+suppress-flapping+peer) { detecting-interval detecting-interval | threshold threshold | resume-interval resume-interval } *
   ```
   
   Parameters in this command are described as follows:
   
   * **detecting-interval**: indicates the detection interval for OSPF neighbor relationship flapping suppression. An OSPF interface with OSPF neighbor relationship flapping suppression enabled starts a flapping counter. If the interval between two successive neighbor relationship states (changing from Full to a non-Full state) is shorter than the *detecting-interval*, a valid flapping\_event is recorded, and the flapping\_count is incremented by 1.
   * **threshold**: indicates the threshold for OSPF neighbor relationship flapping suppression. When the flapping\_count reaches or exceeds the *threshold*, flapping suppression occurs.
   * **resume-interval**: indicates the interval for exiting OSPF neighbor relationship flapping suppression. If the interval between two successive neighbor relationship states (changing from Full to a non-Full state) is longer than the *resume-interval*, the flapping\_count is reset. If OSPF neighbor relationship flapping suppression works in Hold-max-cost mode, the value of *resume-interval* indicates the duration of this mode.
   * The value of *resume-interval* must be greater than that of *detecting-interval*.
   
   You can configure detection parameters for OSPF neighbor relationship flapping suppression on specific interfaces according to network conditions. However, using the default values of these parameters is recommended. By default, the detection interval for OSPF neighbor relationship flapping suppression is 60 seconds, the suppression threshold is 10, and the interval for exiting flapping suppression is 120 seconds.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
9. (Optional) Configure the specified OSPF interface to exit neighbor relationship flapping suppression.
   
   
   ```
   [quit](cmdqueryname=quit)
   [quit](cmdqueryname=quit)
   [reset ospf](cmdqueryname=reset+ospf+suppress-flapping+peer) process-id suppress-flapping peer [ interface-type interface-number ] [ notify-peer ]
   ```
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   Interfaces exit flapping suppression in the following scenarios:
   
   * The suppression timer expires.
   * The corresponding OSPF process is reset.
   * An OSPF neighbor relationship is reset using the [**reset ospf peer**](cmdqueryname=reset+ospf+peer) command.
   * OSPF neighbor relationship flapping suppression is disabled globally using the [**suppress-flapping peer disable**](cmdqueryname=suppress-flapping+peer+disable) command in the OSPF view.

#### Verifying the Configuration

Run the [**display ospf**](cmdqueryname=display+ospf) [ *process-id* ] **interface** *interface-type* *interface-number* **verbose** command to check the status of OSPF neighbor relationship flapping suppression. **Suppress flapping peer** in the command output indicates the current suppression mode, when flapping suppression started, and the remaining time before flapping suppression exits.
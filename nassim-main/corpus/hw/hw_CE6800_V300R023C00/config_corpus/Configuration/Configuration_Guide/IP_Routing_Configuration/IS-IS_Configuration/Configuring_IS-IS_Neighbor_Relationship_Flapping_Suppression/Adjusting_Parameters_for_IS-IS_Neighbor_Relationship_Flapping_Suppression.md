Adjusting Parameters for IS-IS Neighbor Relationship Flapping Suppression
=========================================================================

Adjusting Parameters for IS-IS Neighbor Relationship Flapping Suppression

#### Prerequisites

Before adjusting parameters for IS-IS neighbor relationship flapping suppression, you have completed the following task:

* [Configure basic IS-IS functions](vrp_isis_ipv4_cfg_0011.html).

#### Context

If an IS-IS interface alternates between up and down, IS-IS neighbor relationship flapping occurs on the interface. During the flapping, IS-IS frequently sends IIHs to reestablish the neighbor relationship, synchronizes LSDBs, and recalculates routes. In this process, a large number of packets are exchanged, impacting neighbor relationship stability, IS-IS services, and IS-IS-dependent services. IS-IS neighbor relationship flapping suppression can address this problem by either delaying IS-IS neighbor relationship reestablishment, or setting the link cost to the maximum value to prevent service traffic from passing through flapping links.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Set the flapping suppression mode to Hold-down.
   
   
   ```
   [isis suppress-flapping peer hold-down](cmdqueryname=isis+suppress-flapping+peer+hold-down) interval
   ```
   
   
   
   IS-IS neighbor relationship flapping suppression works in either Hold-down or Hold-max-cost mode.
   
   * Hold-down mode: If frequent flooding and network topology changes occur during neighbor relationship establishment, interfaces prevent neighbor relationship reestablishment during Hold-down suppression to minimize LSDB synchronization attempts and packet exchanges.
   * Hold-max-cost mode: If the traffic forwarding path frequently changes, interfaces use the maximum cost of the flapping link during the suppression period to prevent traffic from passing through the flapping link.
   
   If both modes are enabled, flapping suppression first works in Hold-down mode and then in Hold-max-cost mode.
   
   By default, the Hold-max-cost mode takes effect.
   
   To disable the Hold-max-cost mode, run the [**isis suppress-flapping peer hold-max-cost**](cmdqueryname=isis+suppress-flapping+peer+hold-max-cost) **disable** command.
5. Configure detection parameters for IS-IS neighbor relationship flapping suppression.
   
   
   ```
   [isis suppress-flapping peer](cmdqueryname=isis+suppress-flapping+peer) { detecting-interval detecting-interval | threshold threshold | resume-interval resume-interval }
   ```
   
   
   
   Each IS-IS interface maintains a flapping counter. If the interval between two successive neighbor state changes from Up to Initial or Down is less than or equal to the *detecting-interval*, a valid flapping\_event is recorded, and the flapping\_count increases by 1. When the flapping\_count reaches or exceeds the *threshold*, flapping suppression takes effect. If the interval between two successive neighbor state changes from Up to Initial or Down is greater than or equal to the *resume-interval*, neighbor relationship flapping suppression exits, and the flapping\_count is set to 0.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   The value of *resume-interval* must be greater than that of *detecting-interval*.
   
   You can configure detection parameters as required. However, using the default detection parameters is recommended. By default, the detection interval for IS-IS neighbor relationship flapping suppression is 60s, the suppression threshold is 10, and the interval for exiting suppression is 120s.
6. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

* Run the [**display isis**](cmdqueryname=display+isis) [ *process-id* ] **interface** *interface-type* *interface-number* **verbose** command to check the status of IS-IS neighbor relationship flapping suppression.
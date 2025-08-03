Configuring the Control-Flap Function
=====================================

This section describes how to configure the control-flap function.

#### Usage Scenario

The flapping of routing protocols, MPLS, and other protocols caused by the frequent change of the interface status may influence the stability of the whole network. To resolve this problem, you can configure the control-flap function.

The function controls the frequency of interface status alternations between up and down, which minimizes the impact on device and network stability.

For related concepts and fundamentals, see [Interface Flapping Control](dc_vrp_ifm_cfg_0030.html#EN-US_CONCEPT_0172362528__section_dc_vrp_ifm_cfg_003004).


#### Pre-configuration Tasks

Before configuring the control-flap function, configure the physical attributes for the Router interfaces.


#### Procedure

* Configure the control-flap function.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The null interface and loopback interface do not support the control-flap function.
  3. Run [**control-flap**](cmdqueryname=control-flap) [ *suppress* *reuse* *ceiling* *decay-ok* *decay-ng* ]
     
     
     
     The control-flap function is enabled on the interface.
     
     
     
     The value of *suppress* is 1000 times the suppress threshold of the interface. It ranges from 1 to 20000. The default value is 2000. The value of *suppress* must be greater than the value of *reuse* and smaller than the value of *ceiling*.
     
     The value of *reuse* is 1000 times the reuse threshold of the interface. It ranges from 1 to 20000. The default value is 750. The value of *reuse* must be smaller than the value of *suppress*.
     
     The value of *ceiling* is 1000 times the suppress penalty value of the interface. It ranges from 1001 to 20000. The default value is 6000. The value of *ceiling* must be greater than the value of *suppress*.
     
     The value of *decay-ok* is the time taken to decay the penalty value to half when the interface is Up. It ranges from 1 to 900 seconds. The default value is 54 seconds.
     
     The value of *decay-ng* is the time taken to decay the penalty value to half when the interface is Down. It ranges from 1 to 900 seconds. The default value is 54 seconds.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure status flapping suppression on a physical interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of an interface is displayed.
  3. Run [**damp-interface enable**](cmdqueryname=damp-interface+enable)
     
     
     
     Status flapping suppression is enabled on the interface.
  4. (Optional) Run [**damp-interface level**](cmdqueryname=damp-interface+level) { **light** | **middle** | **heavy** | **manual** { *half-life-period* *suppress* *reuse* *max-suppress-time* } }
     
     
     
     A suppression level is configured for status flapping suppression.
     
     
     
     + **light**: If light suppression is configured, the system triggers suppression only when an interface's status flaps frequently and rapidly. The light suppression level is the default setting and applies to flappings that have the maximum impact on the system.
     + **heavy**: If heavy suppression is configured, the system triggers suppression when detecting an interface's status begins to flap, even if the flapping is not severe. At the heavy suppression level, an interface is prone to be suppressed. This level applies to services that are sensitive to flappings. Enabling heavy suppression prevents service interruptions or resource waste caused by interface flappings.
     + **middle**: Intensity of middle suppression is between the light and heavy levels.
     + **manual**: If light, middle, or heavy suppression cannot meet your requirement, you can specify *manual*.
  5. (Optional) Run [**damp-interface mode tx-off**](cmdqueryname=damp-interface+mode+tx-off)
     
     
     
     The interface is disabled from sending signals if it is under status flapping suppression.
     
     
     
     If an interface is under status flapping suppression, the interface can be disabled from sending signals, so that the remote interface can detect that the local interface is unavailable.
     
     If the local interface is disabled from sending signals, the remote interface considers it Down.
     
     If status flapping suppression on the local interface is canceled, this interface automatically begins to send signals to the remote interface. The remote interface then considers this interface Up.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

Run the [**display control-flap**](cmdqueryname=display+control-flap) **interface** *interface-type interface-number* command to check the previous configuration.

Run the [**display damp-interface**](cmdqueryname=display+damp-interface) [ **interface** *interface-type* *interface-number* ] command to check the status and statistics about status flapping suppression on the interface.
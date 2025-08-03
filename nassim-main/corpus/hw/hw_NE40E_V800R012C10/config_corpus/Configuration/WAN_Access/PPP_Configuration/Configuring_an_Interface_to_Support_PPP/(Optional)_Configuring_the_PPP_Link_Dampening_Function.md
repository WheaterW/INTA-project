(Optional) Configuring the PPP Link Dampening Function
======================================================

To prevent frequent PPP link flapping from causing flapping of the link and network layers, configure the PPP link dampening function.

#### Context

Optical fiber flapping on a physical interface causes PPP link to alternate between Up and Down frequently. This results in unstable link or network layers. To prevent the link or network layer flapping from causing PPP link frequent alternating between Up and Down, configure the PPP link dampening function.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This feature is supported only by the NE40E-M2E, NE40E-M2F, NE40E-M2H.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ppp dampening level**](cmdqueryname=ppp+dampening+level) { **light** | **middle** | **heavy** | **manual** { **half-life-period** *half-life-period* **suppress-value** *suppress-value* **reuse-value** *reuse-value* **max-suppress-time** *max-suppress-time* } }
   
   
   
   The PPP link dampening level is configured.
   
   
   
   When the PPP link dampening function is enabled, run the [**ppp dampening level**](cmdqueryname=ppp+dampening+level) command to configure a light, middle, or heavy dampening level based on PPP link dampening requirements, or configure *suppress-value* manually.
   
   * light: If light PPP link dampening is configured, dampening procedure will be triggered only when the PPP link flaps frequently and rapidly.
   * middle: If middle PPP link dampening is configured, intensity of PPP link dampening is between the light and heavy.
   * heavy: If heavy PPP link dampening is configured, dampening will be triggered even if link flapping is not severe. That is, the link is vulnerable to dampening.
   * manual: If PPP link dampening is configured manually, you can configure a PPP link dampening level based on sensitivity of flapping.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
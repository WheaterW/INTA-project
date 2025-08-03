(Optional) Configuring HDLC Link Dampening Function
===================================================

To prevent frequent HDLC flapping from flapping of the link or network layers, configure the HDLC link dampening function.

#### Context

Optical fiber flapping on a physical interface causes HDLC link to flap between Up and Down frequently. This results in unstable link or network layers. To prevent HDLC flapping from causing flapping of link or network layers, configure the HDLC link dampening function.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This feature is supported only by the NE40E-M2E, NE40E-M2F, NE40E-M2H.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**hdlc dampening level**](cmdqueryname=hdlc+dampening+level) { **light** | **middle** | **heavy** | **manual** { **half-life-period** *half-life-period* **suppress-threshold** *suppress-threshold* **reuse-threshold** *reuse-threshold* **max-suppress-time** *max-suppress-time* } }
   
   
   
   The HDLC link dampening level is configured.
3. (Optional) Run the [**hdlc dampening disable**](cmdqueryname=hdlc+dampening+disable) command to disable the HDLC link dampening.
   
   
   
   If you do not want to use the HDLC link dampening function, run the [**hdlc dampening disable**](cmdqueryname=hdlc+dampening+disable) command to disable the function.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
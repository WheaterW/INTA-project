(Optional) Enabling the Optical Module Laser
============================================

After enabling the optical module laser, you can check whether the link failure is cleared.

#### Context

If the optical module is configured to disable the laser automatically, the laser is not immediately re-enabled when the link failure is cleared. However, maintenance engineers can enable the optical module laser manually to check whether services have recovered.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **interface-type interface-number** or [**controller**](cmdqueryname=controller) *interface-type* *interface-number*
   
   
   
   The corresponding interface view is displayed.
3. Run [**laser turn-on**](cmdqueryname=laser+turn-on) [ **duration** *duration-value* ]
   
   
   
   The optical module laser is enabled, and the duration for which the optical module laser will be temporarily enabled is configured.
   
   
   
   The duration takes effect only after the [**laser autoshutdown enable**](cmdqueryname=laser+autoshutdown+enable) command is run.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
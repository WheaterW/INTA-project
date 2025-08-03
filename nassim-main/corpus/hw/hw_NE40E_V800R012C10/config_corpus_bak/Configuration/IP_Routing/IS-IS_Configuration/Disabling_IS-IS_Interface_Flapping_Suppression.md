Disabling IS-IS Interface Flapping Suppression
==============================================

IS-IS interface flapping suppression is globally enabled by default. If this function is not needed, you can disable it.

#### Usage Scenario

If IS-IS interfaces frequently alternate between up and down, the interfaces will flap, and protocol packets will be frequently exchanged, affecting IS-IS services and other services relying on IS-IS. Interface flapping suppression can address this issue. This function allows a device to delay interface state changes to up. If this function is not needed, you can disable it.


#### Pre-configuration Tasks

Before configuring IS-IS interface flapping suppression, [configure basic IS-IS functions](dc_vrp_isis_cfg_1000.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis suppress-flapping interface disable**](cmdqueryname=isis+suppress-flapping+interface+disable)
   
   
   
   IS-IS interface flapping suppression is disabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configuration

Run the [**display current-configuration configuration isis**](cmdqueryname=display+current-configuration+configuration+isis) command to check the status of IS-IS interface flapping suppression.
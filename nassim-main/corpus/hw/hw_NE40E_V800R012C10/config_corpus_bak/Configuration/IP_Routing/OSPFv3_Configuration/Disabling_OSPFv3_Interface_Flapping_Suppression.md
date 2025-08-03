Disabling OSPFv3 Interface Flapping Suppression
===============================================

OSPFv3 interface flapping suppression is globally enabled by default. If this function is not needed, you can disable it.

#### Usage Scenario

If OSPFv3 interfaces frequently alternate between up and down, the interfaces will flap, and protocol packets will be frequently exchanged, affecting OSPFv3 services and other services relying on OSPFv3. Interface flapping suppression can address this issue. This function allows a device to delay interface state changes to up. If this function is not needed, you can disable it.


#### Pre-configuration Tasks

Before configuring OSPFv3 interface flapping suppression, [configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3 suppress-flapping interface disable**](cmdqueryname=ospfv3+suppress-flapping+interface+disable)
   
   
   
   OSPFv3 interface flapping suppression is disabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configuration

Run the [**display current-configuration configuration ospfv3**](cmdqueryname=display+current-configuration+configuration+ospfv3) command to check the status of OSPFv3 interface flapping suppression.
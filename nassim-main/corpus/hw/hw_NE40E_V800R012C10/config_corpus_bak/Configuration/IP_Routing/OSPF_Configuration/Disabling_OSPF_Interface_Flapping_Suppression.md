Disabling OSPF Interface Flapping Suppression
=============================================

OSPF interface flapping suppression is globally enabled by default. If this function is not needed, you can disable it.

#### Usage Scenario

If OSPF interfaces frequently alternate between up and down, the interfaces will flap, and protocol packets will be frequently exchanged, affecting OSPF services and other services relying on OSPF. Interface flapping suppression can address this issue. This function allows a device to delay interface state changes to up. If this function is not needed, you can disable it.


#### Pre-configuration Tasks

Before configuring OSPF interface flapping suppression, [configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf suppress-flapping interface disable**](cmdqueryname=ospf+suppress-flapping+interface+disable)
   
   
   
   OSPF interface flapping suppression is disabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configuration

Run the [**display current-configuration configuration ospf**](cmdqueryname=display+current-configuration+configuration+ospf) command to check the status of OSPF interface flapping suppression.
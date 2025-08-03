Configuring Global Padding
==========================

This section describes how to configure global padding.

#### Usage Scenario

1. By default, port padding is enabled for all MAC modules.
2. If there are a large number of outbound packets containing less than 42 bytes, the highest forwarding performance of some MAC modules can be achieved only when global padding is enabled for the subcards.
3. By default, global padding is disabled.

In VS mode, this configuration task is supported only by the admin VS.


#### Pre-configuration Tasks

None


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**set mac-padding enable**](cmdqueryname=set+mac-padding+enable)
   
   
   
   The padding function is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring global padding, check the configurations.

Run the [**display this**](cmdqueryname=display+this) command to check whether the function is successfully configured.
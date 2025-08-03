Configuring Global Layer 2 Multicast CAC
========================================

Global Layer 2 multicast CAC configurations are performed to limit the global multicast bandwidth.

#### Context

Global Layer 2 multicast CAC configurations take effect on an entire device. After Layer 2 multicast CAC is configured globally, the bandwidth of each multicast group (including multicast groups in VSIs) is limited.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2-multicast-channel**](cmdqueryname=l2-multicast-channel)
   
   
   
   The global channel view is displayed.
3. (Optional) Run [**unspecified-channel deny**](cmdqueryname=unspecified-channel+deny)
   
   
   
   The device is enabled to filter out multicast data for groups undefined in a global channel.
   
   
   
   After this command is run, the device permits only multicast data for groups defined in a global channel and denies all multicast data for groups undefined in a global channel.
4. Run [**channel**](cmdqueryname=channel) *channel-name* **type** { **asm** | **ssm** }
   
   
   
   A global channel is created.
5. Run [**group**](cmdqueryname=group) *group-address* { *group-mask-length* | *group-mask* } [ **per-bandwidth** *bandwidth* ]
   
   
   
   Multicast groups are specified for the channel. If **per-bandwidth** *bandwidth* is set, the bandwidth is limited to a specific value for each multicast group in the global channel. If this parameter is not set, the bandwidth is not limited for any multicast group in the global channel.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit from the channel view.
8. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit from the global channel view.
Configuring the Maximum Number of Invalid Layer 2 Multicast Protocol Packets Allowed on a Multicast Device
==========================================================================================================

Configuring the maximum number of invalid Layer 2 multicast protocol packets allowed on a multicast device helps to locate and rectify faults.

#### Usage Scenario

If forwarding entries cannot be created on a multicast network, configure the maximum number of invalid Layer 2 multicast protocol packets allowed on a multicast device. Then, you can locate and rectify the fault based on statistics and detailed information about invalid Layer 2 multicast protocol packets.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2-multicast invalid-packet**](cmdqueryname=l2-multicast+invalid-packet) **igmp-snooping** **max-count** *max-number*
   
   
   
   The maximum number of invalid Layer 2 multicast protocol packets allowed on a multicast device is specified.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) [**| include**](cmdqueryname=%7C+include)  [**l2-multicast invalid-packet**](cmdqueryname=l2-multicast+invalid-packet) command to check the maximum number of invalid Layer 2 multicast protocol messages that can be stored on the device.

```
<HUAWEI> display current-configuration | include l2-multicast invalid-packet
 l2-multicast invalid-packet igmp max-count 20
```

After the maximum number of invalid Layer 2 multicast protocol messages that a device can store is set, you can run the [**display igmp-snooping invalid-packet**](cmdqueryname=display+igmp-snooping+invalid-packet) { **vlan** [ *vlan-id* ] | **vsi** [ *vsi-name* ] } **message-type** { **leave** | **query** | **report** | **hello** } \* command to check statistics about invalid Layer 2 multicast protocol messages that the device stores.

After the maximum number of invalid Layer 2 multicast protocol messages that a device can store is set, you can run the [**display igmp-snooping invalid-packet**](cmdqueryname=display+igmp-snooping+invalid-packet) [ *packet-number* ] **verbose** command to check details about invalid Layer 2 multicast protocol messages that the device stores.
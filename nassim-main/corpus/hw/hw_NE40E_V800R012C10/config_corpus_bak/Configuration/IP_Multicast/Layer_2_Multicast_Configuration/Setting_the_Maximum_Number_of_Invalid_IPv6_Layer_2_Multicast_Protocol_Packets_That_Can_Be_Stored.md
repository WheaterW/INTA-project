Setting the Maximum Number of Invalid IPv6 Layer 2 Multicast Protocol Packets That Can Be Stored
================================================================================================

Set the maximum number of invalid IPv6 Layer 2 multicast protocol packets that can be stored. Then, you can effectively locate and rectify faults based on the information about the limited number of invalid messages.

#### Usage Scenario

If forwarding entries cannot be created on a multicast network, set the maximum number of invalid IPv6 Layer 2 multicast protocol messages that can be stored. Then, you can effectively locate and rectify faults based on statistics and detailed information about invalid Layer 2 multicast protocol messages.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2-multicast invalid-packet mld-snooping**](cmdqueryname=l2-multicast+invalid-packet+mld-snooping) **max-count** *max-number* The maximum number of invalid IPv6 Layer 2 multicast protocol messages that can be stored on the device is set.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) [**| include**](cmdqueryname=%7C+include)  [**l2-multicast invalid-packet mld-snooping**](cmdqueryname=l2-multicast+invalid-packet+mld-snooping) command to check the maximum number of invalid Layer 2 multicast protocol messages that can be stored.

```
<HUAWEI> display current-configuration | include l2-multicast invalid-packet mld-snooping
 l2-multicast invalid-packet mld max-count 20
```
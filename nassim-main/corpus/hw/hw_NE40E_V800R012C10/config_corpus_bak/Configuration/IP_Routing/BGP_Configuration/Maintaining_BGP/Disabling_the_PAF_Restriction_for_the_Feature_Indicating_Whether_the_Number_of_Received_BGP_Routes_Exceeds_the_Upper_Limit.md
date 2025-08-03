Disabling the PAF Restriction for the Feature Indicating Whether the Number of Received BGP Routes Exceeds the Upper Limit
==========================================================================================================================

You can disable the PAF restriction for the feature indicating whether the number of routes received from all peers in a BGP address family exceeds the upper limit. This configuration allows a device to continue to receive routes even after the number exceeds the upper limit.

#### Usage Scenario

By default, the PAF restriction is enabled for the feature indicating whether the number of routes received from all peers in a BGP address family exceeds the upper limit. With the PAF restriction, if the number of received routes exceeds 80% of the upper limit, a threshold alarm is generated. If the number exceeds the upper limit, a threshold-crossing alarm is generated, and the excess routes are discarded. To enable the local device to continue to receive routes even after the number exceeds the upper limit, run the **bgp paf feature off** command to disable the PAF restriction for this feature.

![](../../../../public_sys-resources/caution_3.0-en-us.png) 

Currently, only the PAF restriction on the number of routes received from peers in a BGP address family can be removed. If the PAF restriction is removed, the device can still learn routes after the specification is exceeded. This may consume excessive memory and affect other services. In addition, memory exhaustion may cause the device to reset. Therefore, removing the PAF restriction is not recommended.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp paf feature**](cmdqueryname=bgp+paf+feature+off) *featureName* **off**
   
   
   
   The PAF restriction is removed on a specified BGP feature.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
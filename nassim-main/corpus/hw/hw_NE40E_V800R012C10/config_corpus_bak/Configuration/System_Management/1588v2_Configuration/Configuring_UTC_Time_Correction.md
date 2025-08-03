Configuring UTC Time Correction
===============================

This section describes how to configure UTC time correction. This function helps ensure time signal accuracy on a 1588v2 network and a fix offset between the UTC and TAI time.

#### Context

Universal Coordinated Time (UTC) is Greenwich Mean Time (GMT), which is displayed on a device. TAI is short for international atomic time. There is a fixed offset between the TAI and UTC. The international time organization periodically releases the offset.

When a 1588v2 device tracks an external BITS clock source, the device uses the offset provided by this source by default. If the external BITS clock source is lost, the 1588v2 device uses the previous offset, which may change. An offset change causes inaccurate time signals on the 1588v2 network.

You can manually configure the offset between the UTC time and TAI time on a Router. You only need to configure it on the Grandmaster Clock on the 1588v2 network. The time on other 1588v2 devices is synchronized from that on the Grandmaster Clock.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ptp utc-offset**](cmdqueryname=ptp+utc-offset) *utc-offset*
   
   
   
   An accumulative offset between the UTC and TAI time is set.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the following command to check the previous configuration.

Run the [**display ptp utc**](cmdqueryname=display+ptp+utc) command to check the UTC time.

```
<HUAWEI> display ptp utc
```
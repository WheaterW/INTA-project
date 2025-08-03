Configuring a Default Invalid VLAN ID in the Calling-Station-Id Attribute
=========================================================================

To ensure interconnection between a Huawei device and a non-Huawei device, you can configure a default invalid VLAN ID in the Calling-Station-Id attribute for the Huawei device.

#### Context

By default, a Huawei device uses 4096 as the default invalid VLAN ID. However, a non-Huawei device may use 0 as the default invalid VLAN ID. To allow a Huawei device to communicate with a non-Huawei device that uses 0 as the default invalid VLAN ID, change the default invalid VLAN ID of the Huawei device to 0.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2tp calling-station-id vlan-0-invalid**](cmdqueryname=l2tp+calling-station-id+vlan-0-invalid)
   
   
   
   0 is configured as the default invalid VLAN ID in the Calling-Station-Id attribute delivered from an L2TP user (LAC) to the LNS.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
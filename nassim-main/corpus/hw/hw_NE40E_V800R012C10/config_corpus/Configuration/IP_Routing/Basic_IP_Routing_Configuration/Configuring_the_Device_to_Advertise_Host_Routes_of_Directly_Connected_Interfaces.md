Configuring the Device to Advertise Host Routes of Directly Connected Interfaces
================================================================================

You can configure a device to advertise the host routes of directly connected interfaces after the routes are imported by routing protocols.

#### Usage Scenario

By default, after a routing protocol imports host routes of directly connected interfaces, the routing protocol stores them in the routing table but does not advertise them. You can configure the device to advertise host routes of directly connected interfaces as required.


#### Pre-configuration Tasks

None


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip direct-routing-table local-host-route advertise enable**](cmdqueryname=ip+direct-routing-table+local-host-route+advertise+enable) or [**ipv6 direct-routing-table local-host-route advertise enable**](cmdqueryname=ipv6+direct-routing-table+local-host-route+advertise+enable)
   
   
   
   The device is configured to advertise host routes of directly connected interfaces.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring the device to advertise host routes of directly connected interfaces, run the [**display current-configuration**](cmdqueryname=display+current-configuration) command in the system view. The command output shows that this function has been enabled.
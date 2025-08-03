Configuring the Device to Advertise Host Routes of Directly Connected Interfaces
================================================================================

Configuring the Device to Advertise Host Routes of Directly Connected Interfaces

#### Context

By default, after a routing protocol imports host routes of directly connected interfaces, the routing protocol stores them in the routing table but does not advertise them. You can configure the device to advertise host routes of directly connected interfaces as required.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to advertise host routes of directly connected interfaces.
   
   
   * Configure the device to advertise IPv4 host routes of directly connected interfaces.
     ```
     [ip direct-routing-table local-host-route advertise enable](cmdqueryname=ip+direct-routing-table+local-host-route+advertise+enable)
     ```
   * Configure the device to advertise IPv6 host routes of directly connected interfaces.
     ```
     [ipv6 direct-routing-table local-host-route advertise enable](cmdqueryname=ipv6+direct-routing-table+local-host-route+advertise+enable)
     ```
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     The CE6885-LL in low latency mode does not support this command.
   
   
   
   By default, a device is not configured to advertise host routes of directly connected interfaces.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) command to check the configuration.
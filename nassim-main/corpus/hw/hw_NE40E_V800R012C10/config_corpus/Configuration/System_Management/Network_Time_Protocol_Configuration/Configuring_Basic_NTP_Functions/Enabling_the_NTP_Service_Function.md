Enabling the NTP Service Function
=================================

This section describes how to use NTP IPv4 or IPv6 services.

#### Context

After NTP-related commands are configured on a device, the device automatically disables the NTP server function to prevent external devices from synchronizing their clocks with the device's clock. In addition, the device also generates the [**ntp-service**](cmdqueryname=ntp-service) [ **ipv6** ] **server** **disable** commands in its configuration file. If you want to use the device as an NTP server, enable the NTP server function on the device.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**undo ntp-service**](cmdqueryname=undo+ntp-service) [ **ipv6** ] **server** **disable**
   
   
   
   The NTP server function is enabled on the device.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
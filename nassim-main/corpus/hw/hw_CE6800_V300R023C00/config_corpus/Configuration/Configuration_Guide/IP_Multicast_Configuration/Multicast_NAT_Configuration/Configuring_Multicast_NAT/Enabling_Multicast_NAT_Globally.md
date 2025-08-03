Enabling Multicast NAT Globally
===============================

Enabling Multicast NAT Globally

#### Context

Before configuring multicast NAT, you must enable it globally. Otherwise, the multicast NAT configuration does not take effect.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable multicast NAT globally.
   
   
   ```
   [multicast-nat enable](cmdqueryname=multicast-nat+enable)
   ```
3. (Optional) Disable the function of reducing the TTL value of multicast packets so that the TTL value of multicast packets does not decrease by 1 when the packets pass through the device.
   
   
   ```
   [multicast-nat ttl-decrease disable](cmdqueryname=multicast-nat+ttl-decrease+disable)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
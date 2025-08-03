(Optional) Configuring Suppression of Dynamic IGMP Snooping Joining
===================================================================

(Optional) Configuring Suppression of Dynamic IGMP Snooping Joining

#### Context

By default, the device forwards received Report/Leave messages carrying static group addresses to upstream devices. If an upstream Layer 3 device is a non-Huawei device and has static multicast groups configured on user-side interfaces and multicast users are not allowed to dynamically join or leave multicast groups, you can configure suppression of dynamic IGMP snooping joining on the current device. This function prevents the current device from forwarding IGMP Report/Leave messages carrying static group addresses to the upstream device.


#### Procedure

1. Enter the system view.
   
   
   ```
   system-view
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Configure suppression of dynamic IGMP snooping joining.
   
   
   ```
   [igmp snooping static-group suppress-dynamic-join](cmdqueryname=igmp+snooping+static-group+suppress-dynamic-join)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
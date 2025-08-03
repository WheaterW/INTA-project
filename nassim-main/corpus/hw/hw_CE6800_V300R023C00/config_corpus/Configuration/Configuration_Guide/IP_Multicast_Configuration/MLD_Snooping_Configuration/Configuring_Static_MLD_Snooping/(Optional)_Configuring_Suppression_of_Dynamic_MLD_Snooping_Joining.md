(Optional) Configuring Suppression of Dynamic MLD Snooping Joining
==================================================================

(Optional) Configuring Suppression of Dynamic MLD Snooping Joining

#### Context

If an upstream Layer 3 device is a non-Huawei device and has static multicast groups configured on user-side interfaces and multicast users are not allowed to dynamically join or leave multicast groups, you can configure suppression of dynamic MLD snooping joining on the current device. This function prevents the current device from forwarding Report and Done messages carrying static group addresses to the upstream device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Configure suppression of dynamic MLD snooping joining.
   
   
   ```
   [mld snooping static-group suppress-dynamic-join](cmdqueryname=mld+snooping+static-group+suppress-dynamic-join)
   ```
   
   By default, the device forwards received Report and Done messages carrying static group addresses to the upstream device.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
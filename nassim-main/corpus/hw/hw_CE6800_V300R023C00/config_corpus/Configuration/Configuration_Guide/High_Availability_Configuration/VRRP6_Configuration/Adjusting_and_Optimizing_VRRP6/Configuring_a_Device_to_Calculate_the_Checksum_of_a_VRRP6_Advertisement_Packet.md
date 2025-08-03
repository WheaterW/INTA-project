Configuring a Device to Calculate the Checksum of a VRRP6 Advertisement Packet
==============================================================================

Configuring a Device to Calculate the Checksum of a VRRP6 Advertisement Packet

#### Context

After receiving a VRRP6 Advertisement packet, a Huawei device calculates the packet's checksum based on the content including the IPv6 pseudo header. However, a non-Huawei device may calculate the packet's checksum based on the content excluding the IPv6 pseudo header. As a result, VRRP6 negotiation between the Huawei and non-Huawei devices may fail. To resolve this issue, configure the Huawei device to calculate the checksum of a VRRP6 Advertisement packet based on the content excluding the IPv6 pseudo header.


#### Procedure

1. Enter the system view.
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to calculate the checksum of a VRRP6 Advertisement packet based on the content excluding the IPv6 pseudo header.
   ```
   [vrrp6 checksum exclude pseudo-header](cmdqueryname=vrrp6+checksum+exclude+pseudo-header)
   ```
   
   By default, a device calculates the checksum of a VRRP6 Advertisement packet based on the content including the IPv6 pseudo header.
3. Commit the configuration.
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display vrrp6**](cmdqueryname=display+vrrp6) { **interface** *interface-type* *interface-number* [ *virtual-router-id* ] | *virtual-router-id* } **verbose** command to check detailed VRRP6 group information.
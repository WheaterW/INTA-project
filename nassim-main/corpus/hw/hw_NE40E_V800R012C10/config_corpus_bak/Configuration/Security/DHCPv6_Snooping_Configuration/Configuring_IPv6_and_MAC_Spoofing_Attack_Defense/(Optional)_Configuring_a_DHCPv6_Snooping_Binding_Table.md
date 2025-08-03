(Optional) Configuring a DHCPv6 Snooping Binding Table
======================================================

After DHCPv6 snooping is enabled, dynamic DHCPv6 snooping binding entries are automatically generated when users go online. Static DHCPv6 snooping binding entries need to be manually configured.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Both the static IPv6 addresses and the IPv6 addresses statically assigned to users refer to the IPv6 addresses manually configured on clients. Static users are those who use static IPv6 addresses.

If the IPv6 addresses assigned to users are static IPv6 addresses, you can configure static binding entries for these addresses to prevent unauthorized users from embezzling the static IPv6 addresses. If there are a large number of static IPv6 users, static binding entries must be configured for each static IPv6 address; otherwise, unauthorized users who attempt to embezzle static IPv6 addresses cannot be isolated.

Dynamic entries in a DHCPv6 snooping binding table do not need to be configured. Instead, they are automatically generated after DHCPv6 snooping is enabled. Static entries, however, need to be configured using commands.

* For the IPv6 address dynamically assigned to a user, the device automatically learns the user's MAC address and generates a binding entry. In this case, no binding entry needs to be configured.
* For the IPv6 address statically assigned to a user, the device cannot automatically generate a binding entry. Therefore, you need to manually configure a binding entry for the user.

If no binding entries are created for static users, the following situations may occur:

* All static users can access the DHCPv6 server normally. This is the default setting for the device.
* No static user can access the DHCPv6 server.

If an interface enabled with the packet check function receives an IPv6 packet, the interface matches the source IPv6 address and source MAC address of the IPv6 packet against the DHCPv6 snooping binding table to check the MAC address, IPv6 address, interface information, and VLAN ID. If no entry is matched, the packet is discarded. If an entry is completely matched, the packet is properly forwarded.


#### Procedure

* Configure a static DHCPv6 snooping binding entry on an interface.
  1. Run the **system-view** command to enter the system view.
  2. Run the **interface** *interface-type* *interface-number* command to enter the interface view.
  3. Run the **dhcpv6 snooping bind-table static** { **ipv6-address** *ipv6-address* [ **mac-address** *mac-address* ] | **ipv6-prefix** *ipv6-prefix-mask* } [ **vlan** *vlan-id* [ **ce-vlan** *ce-vlanid* ] ] command to configure a static entry for the mapping between the IPv6 address, MAC address, and VLAN ID.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Back up the DHCPv6 snooping binding table.
  1. Run the **system-view** command to enter the system view.
  2. Run the [**dhcpv6 snooping bind-table autosave enable**](cmdqueryname=dhcpv6+snooping+bind-table+autosave+enable) command to back up the DHCPv6 snooping binding table.
     
     Once configured, the system backs up the binding entries in a specified backup path at an interval of 30 minutes or after 4096 entries are dynamically generated.
  3. (Optional) Run the **dhcpv6 snooping database authentication-mode** command to configure a file integrity check mode for the binding table.
  4. Run the **commit** command to commit the configuration.
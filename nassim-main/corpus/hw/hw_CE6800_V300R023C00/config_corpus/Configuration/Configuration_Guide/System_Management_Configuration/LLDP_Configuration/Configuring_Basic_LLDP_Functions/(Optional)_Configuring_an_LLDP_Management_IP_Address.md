(Optional) Configuring an LLDP Management IP Address
====================================================

(Optional) Configuring an LLDP Management IP Address

#### Context

The LLDP management IP address is carried in the Management Address TLV field in LLDP frames. It is used by the NMS to identify a device, and this helps to detect network topology and facilitate network management.

You can use any of the following methods to configure an LLDP management IP address:

* On IPv4 networks:
  + Run the [**lldp management-address**](cmdqueryname=lldp+management-address) command to configure an LLDP management IPv4 address.
  + Run the [**lldp management-address bind**](cmdqueryname=lldp+management-address+bind) command to bind the final LLDP management IP address to an interface so that the device preferentially uses the interface's IPv4 address as the final management IPv4 address.
* On IPv6 networks:
  + Run the [**lldp management-address ipv6**](cmdqueryname=lldp+management-address+ipv6) command to configure an LLDP management IPv6 address.
  + Run the [**lldp management-address ipv6 bind**](cmdqueryname=lldp+management-address+ipv6+bind) command to bind the final LLDP management IPv6 address to an interface so that the device preferentially uses the interface's IPv6 address as the final management IPv6 address.
  + Run the [**lldp management-address interface-mode**](cmdqueryname=lldp+management-address+interface-mode) command to enable the interface mode for management addresses. In interface mode, the interface address carried in the Management Address TLV field in LLDP packets is used as the management IP address.

The LLDP management IP address is selected based on the following principles:

1. If a management IP address is configured using the [**lldp management-address**](cmdqueryname=lldp+management-address) or **lldp management-address ipv6** command but the binding between the management IP address and an interface is not configured, the configured management IP address has the highest priority and is preferentially selected as the management IP address.
2. If no management IP address is configured using the [**lldp management-address**](cmdqueryname=lldp+management-address) or **lldp management-address ipv6** command, but the management IP address is bound to an interface, the device uses the interface's IP address as the management IP address.
3. If no management IP address has been configured using the [**lldp management-address**](cmdqueryname=lldp+management-address) or **lldp management-address ipv6** command and the binding between the management IP address and an interface is not configured, the device searches the IP address list and automatically specifies an IP address as the management IP address. If no default IP address is available, the device uses the bridge MAC address as the management IP address.![](public_sys-resources/note_3.0-en-us.png) 
   
   The device searches IP addresses of the following interfaces in sequence for the LLDP management address: loopback interface, management network interface , and VLANIF interface. The device selects the smallest IP address of the same type of interface as the LLDP management address.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure an LLDP management IP address using any of the following methods:
   
   
   * Configure an LLDP management IPv4 address.
     ```
     [lldp management-address](cmdqueryname=lldp+management-address) ip-address
     ```
   * Configure an LLDP management IPv6 address.
     ```
     [lldp management-address ipv6](cmdqueryname=lldp+management-address+ipv6) IPv6address
     ```
     
     The CE6885-LL supports this configuration only in standard forwarding mode.
   
   
   * Bind the LLDP management IPv4 address to an interface.
     ```
     [lldp management-address bind](cmdqueryname=lldp+management-address+bind) interface interface-type interface-number
     ```
   * Bind the LLDP management IPv6 address to an interface.
     ```
     [lldp management-address ipv6 bind](cmdqueryname=lldp+management-address+ipv6+bind) interface interface-type interface-number
     ```
     
     The CE6885-LL supports this configuration only in standard forwarding mode.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
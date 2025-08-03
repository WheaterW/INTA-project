Configuring an IPv6 Multicast Boundary
======================================

Configuring an IPv6 Multicast Boundary

#### Context

A multicast boundary configured for a multicast group on a multicast device's interface specifies the scope for multicast packet forwarding.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the IPv6 multicast function.
   
   
   ```
   [multicast ipv6 routing-enable](cmdqueryname=multicast+ipv6+routing-enable)
   ```
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the working mode of the interface from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
5. Configure an IPv6 multicast boundary.
   
   
   ```
   [multicast ipv6 boundary](cmdqueryname=multicast+ipv6+boundary) ipv6-group-address ipv6-group-mask-length
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display multicast ipv6**](cmdqueryname=display+multicast+ipv6) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] **boundary** [ *ipv6-group-address* [ *ipv6-group-mask-length* ] ] [ **interface** *{interface-type interface-number*  | *interface-name*} ] command to check information about the multicast boundary configured on an interface.
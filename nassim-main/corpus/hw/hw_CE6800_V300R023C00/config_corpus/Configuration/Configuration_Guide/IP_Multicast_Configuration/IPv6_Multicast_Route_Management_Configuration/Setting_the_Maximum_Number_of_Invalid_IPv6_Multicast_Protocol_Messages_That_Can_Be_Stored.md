Setting the Maximum Number of Invalid IPv6 Multicast Protocol Messages That Can Be Stored
=========================================================================================

Setting the Maximum Number of Invalid IPv6 Multicast Protocol Messages That Can Be Stored

#### Context

If forwarding entries cannot be created on a multicast network, you can set the maximum number of invalid multicast protocol messages that can be stored on a multicast device and run the corresponding display command to check statistics and details about these messages. The command output helps you analyze these invalid messages and troubleshoot the faults.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the maximum number of invalid IPv6 multicast protocol messages that can be stored on the device.
   
   
   ```
   [multicast ipv6 invalid-packet](cmdqueryname=multicast+ipv6+invalid-packet) { mld | pim } max-count max-number
   ```
   
   By default, a device can store a maximum of 10 invalid messages for each multicast protocol.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After the configuration is complete, run the following commands to check statistics about invalid IPv6 multicast protocol messages received by the device:

* Run the [**display mld**](cmdqueryname=display+mld) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] [**invalid-packet**](cmdqueryname=invalid-packet) [ **interface** *interface-type interface-number* | *interface-name* | **message-type** { **done** | **query** | **report** } ] \* command to check statistics about invalid MLD messages received by the device.
* Run the [**display pim ipv6**](cmdqueryname=display+pim+ipv6) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] [**invalid-packet**](cmdqueryname=invalid-packet) [ **interface** { *interface-type interface-number* | *interface-name* } | **message-type** { **assert** | **bsr** | **hello** | **join-prune** } ] \* command to check statistics about invalid IPv6 PIM messages received in all instances or the public network instance.

Run the following commands to check detailed information about a specified number of invalid IPv6 multicast protocol messages received by the device:

* Run the [**display mld invalid-packet**](cmdqueryname=display+mld+invalid-packet) [ *packet-number* ] **verbose** command to check detailed information about a specified number of invalid MLD messages received by the device.
* Run the [**display pim ipv6 invalid-packet**](cmdqueryname=display+pim+ipv6+invalid-packet) [ *packet-number* ] **verbose** command to check detailed information about a specified number of invalid IPv6 PIM messages received by the device.
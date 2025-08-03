Setting the Maximum Number of Invalid IPv4 Multicast Protocol Messages That Can Be Stored
=========================================================================================

Setting the Maximum Number of Invalid IPv4 Multicast Protocol Messages That Can Be Stored

#### Context

If forwarding entries cannot be created or Multicast Source Discovery Protocol (MSDP) peer relationships cannot be established on a multicast network, you can set the maximum number of invalid multicast protocol messages that can be stored on a multicast device and run the corresponding display command to check statistics and details about these messages. The command output helps you analyze these invalid messages and troubleshoot the faults.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Set the maximum number of invalid multicast protocol messages that can be stored on the device.
   
   
   ```
   [multicast invalid-packet](cmdqueryname=multicast+invalid-packet) { igmp | msdp | pim } max-count max-number
   ```
   
   By default, a device can store a maximum of 10 invalid messages for each multicast protocol.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After the configuration is complete, run the following command to check information about invalid multicast protocol messages stored on the device:

* Run the [**display current-configuration**](cmdqueryname=display+current-configuration) | [**include multicast invalid-packet**](cmdqueryname=include+multicast+invalid-packet) command to check the effective maximum number of invalid multicast protocol messages on the device.

Run the following commands to check statistics about invalid multicast protocol messages received by the device:

* Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] [**invalid-packet**](cmdqueryname=invalid-packet) [ **interface** *interface-type interface-number* | *interface-name* | **message-type** { **leave** | **query** | **report** } ] \* command to check statistics about invalid IGMP messages received by the device.
* Run the [**display msdp**](cmdqueryname=display+msdp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] [**invalid-packet**](cmdqueryname=invalid-packet) [ **peer** *peer-address* | **message-type** { **keepalive** | **notification** | **sa-request** | **sa-response** | **source-active** } ] \* command to check statistics about invalid MSDP messages received by the device.
* Run the [**display pim**](cmdqueryname=display+pim) [ **vpn-instance** *vpn-instance-name* | **all-instance** ] [**invalid-packet**](cmdqueryname=invalid-packet) [ **interface** { *interface-type interface-number* | *interface-name* } | **message-type** { **assert** | **bsr** | [**crp**](cmdqueryname=crp) | **hello** | **join-prune** | **announcement** | **discovery** | [**register**](cmdqueryname=register) | [**register-stop**](cmdqueryname=register-stop) } ] \* command to check statistics about invalid PIM messages received by all instances or the public network instance of the device.

Run the following commands to check detailed information about a specified number of invalid multicast protocol messages received by the device:

* Run the [**display igmp invalid-packet**](cmdqueryname=display+igmp+invalid-packet) [ *packet-number* ] **verbose** command to check detailed information about a specified number of invalid IGMP messages received by the device.
* Run the [**display msdp invalid-packet**](cmdqueryname=display+msdp+invalid-packet) [ *packet-number* ] **verbose** command to check detailed information about a specified number of invalid MSDP messages received by the device.
* Run the [**display pim invalid-packet**](cmdqueryname=display+pim+invalid-packet) [ *packet-number* ] **verbose** command to check detailed information about a specified number of invalid PIM messages received by the device.
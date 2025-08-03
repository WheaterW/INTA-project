Configuring the Maximum Number of Invalid IPv6 Multicast Protocol Packets that a Device Can Store
=================================================================================================

This section describes how to configure the maximum number of invalid IPv6 multicast protocol packets that a device can store. This configuration helps locate and rectify faults.

#### Usage Scenario

If multicast forwarding entries cannot be established on a network, you can configure the maximum number of invalid IPv6 multicast protocol packets that the devices can store. Then you can check statistics and detailed information about invalid multicast protocol packets using related commands to troubleshoot problems.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast ipv6 invalid-packet**](cmdqueryname=multicast+ipv6+invalid-packet) { **mld** | **pim** } **max-count** *max-number*
   
   
   
   The maximum number of invalid IPv6 multicast protocol packets that the device can store is configured.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configuration

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) [**| include multicast ipv6 invalid-packet**](cmdqueryname=%7C+include+multicast+ipv6+invalid-packet) command to check the maximum number of invalid IPv6 multicast protocol packets that the device can store.

To check statistics about invalid IPv6 multicast protocol packets that the device stores, perform the following operations:

* Run the [**display mld invalid-packet**](cmdqueryname=display+mld+invalid-packet) [ **interface** *interface-type interface-number* | **message-type** { **done** | **query** | **report** } ] \* command to check statistics about invalid multicast listener discovery (MLD) packets that the device stores.
* Run the [**display pim ipv6 invalid-packet**](cmdqueryname=display+pim+ipv6+invalid-packet) [ **interface** *interface-type interface-number* | **message-type** { **assert** | **bsr** | **hello** | **join-prune** | **graft** | **graft-ack** | **state-refresh** } ] \* command to check statistics about invalid IPv6 Protocol Independent Multicast (PIM) packets that the device stores.

To check details about invalid IPv6 multicast protocol packets that the device stores, perform the following operations:

* Run the [**display mld invalid-packet**](cmdqueryname=display+mld+invalid-packet) [ *packet-number* ] **verbose** command to check details about invalid MLD packets that the device stores.
* Run the [**display pim ipv6 invalid-packet**](cmdqueryname=display+pim+ipv6+invalid-packet) [ *packet-number* ] **verbose** command to check details about invalid IPv6 PIM packets that the device stores.
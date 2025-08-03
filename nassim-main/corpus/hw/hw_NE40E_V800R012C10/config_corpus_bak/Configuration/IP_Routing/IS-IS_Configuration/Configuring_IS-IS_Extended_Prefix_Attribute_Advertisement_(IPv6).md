Configuring IS-IS Extended Prefix Attribute Advertisement (IPv6)
================================================================

After IS-IS extended prefix advertisement is configured, route origin information can be advertised to the LSDB so that the device can determine the origin of received routes.

#### Usage Scenario

IS-IS defines a type of extended prefix attribute (IPv4/IPv6 Extended Reachability Attribute) sub-TLVs. These sub-TLVs are used to describe the origin of advertised routes and can be advertised in IPv4, IPv6, and locator TLVs. Based on the advertised sub-TLVs, the device can determine whether the received routes are inter-domain routes or host routes.

The extended prefix attribute flag (IPv4/IPv6 Extended Reachability Attribute Flags) is a part of the extended prefix attribute sub-TLV. You can run a command to determine whether this flag is advertised.


#### Pre-configuration Tasks

Before configuring IS-IS extended prefix attribute advertisement, complete the following tasks:

* Configure the link layer protocol on interfaces.
* Configure addresses for interfaces to ensure that neighboring devices are reachable at the network layer.
* [Configure basic IPv6 IS-IS functions](dc_vrp_isis_cfg_1023.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   An IS-IS process is created, and its view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable) [ **topology** { **compatible** [ **enable-mt-spf** ] | **ipv6** | **standard** } ]
   
   
   
   IPv6 is enabled for the IS-IS process.
4. Run [**advertise prefix-attributes flags**](cmdqueryname=advertise+prefix-attributes+flags)
   
   
   
   The IPv6 IS-IS process is enabled to advertise the extended prefix attribute flag.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
6. (Optional) Set the N flag of the extended prefix attribute on a loopback interface in the IPv6 IS-IS process to 0.
   
   
   
   By default, if a loopback interface's route with a 128-bit subnet mask is a host route, the extended prefix N flag is set to 1. To set the extended prefix N flag to 0, perform this step.
   
   1. Run the [**interface**](cmdqueryname=interface) **Loopback** *interface-number* command to enter the loopback interface view.
   2. Run the [**ipv6 enable**](cmdqueryname=ipv6+enable) command to enable IPv6 on the loopback interface.
   3. Run the [**isis ipv6 enable**](cmdqueryname=isis+ipv6+enable) [ *process-id* ] command to enable IPv6 IS-IS on the interface.
   4. Run the [**isis**](cmdqueryname=isis) [ **process-id** *process-id-value* ] [**ipv6 prefix-attributes node-disable**](cmdqueryname=ipv6+prefix-attributes+node-disable) command to set the N flag of the extended prefix attribute on the loopback interface in the IPv6 IS-IS process to 0.
   5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, run the [**display isis lsdb verbose**](cmdqueryname=display+isis+lsdb+verbose) command to view information about the extended prefix attribute flag.
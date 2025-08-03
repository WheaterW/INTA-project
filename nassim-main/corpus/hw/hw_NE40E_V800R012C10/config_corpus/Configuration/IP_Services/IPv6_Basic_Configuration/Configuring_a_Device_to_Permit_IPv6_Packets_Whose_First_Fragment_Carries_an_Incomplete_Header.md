Configuring a Device to Permit IPv6 Packets Whose First Fragment Carries an Incomplete Header
=============================================================================================

After IPv6 is enabled on a device, the device does not permit IPv6 packets whose first fragment carries an incomplete header by default. To use IPv6 packets whose first fragment carries an incomplete header in special scenarios, configure the device to permit such IPv6 packets.

#### Prerequisites

Before configuring a device to permit IPv6 packets whose first fragment carries an incomplete header, [enable IPv6](dc_vrp_ipv6_cfg_0004.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure the device to permit IPv6 packets whose first fragment carries an incomplete header in the system or interface view.
   
   
   * To configure the device to permit IPv6 packets whose first fragment carries an incomplete header in the system view, run the [**ipv6 security permit incomplete-first-fragment**](cmdqueryname=ipv6+security+permit+incomplete-first-fragment) command.
   * To configure the device to permit IPv6 packets whose first fragment carries an incomplete header in the interface view, perform the following steps:
     1. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the interface view.
     2. Run the [**ipv6 security permit incomplete-first-fragment**](cmdqueryname=ipv6+security+permit+incomplete-first-fragment) command to configure the device to permit IPv6 packets whose first fragment carries an incomplete header on the interface.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
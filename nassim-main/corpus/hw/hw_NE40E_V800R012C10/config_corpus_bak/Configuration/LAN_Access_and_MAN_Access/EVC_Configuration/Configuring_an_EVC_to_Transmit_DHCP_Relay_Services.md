Configuring an EVC to Transmit DHCP Relay Services
==================================================

To allow user terminals in a BD to automatically apply for IP addresses from a DHCP server, configure the DHCP relay function on the VBDIF interface.

#### Usage Scenario

In an EVC model, a VBDIF interface can be deployed to allow Layer 2 traffic to access Layer 3. To allow user terminals in a BD to automatically obtain IP addresses through DHCP, configure the DHCP relay function on the VBDIF interface and specify the IP address of the DHCP server on the Layer 3 network.

#### Pre-configuration Tasks

Before configuring an EVC to transmit DHCP relay services, complete the following tasks:

1. [Establishing the EVC Model](dc_vrp_evc_cfg_0003.html)
2. [Configuring VBDIF Interfaces to Implement Layer 3 Communication](dc_vrp_evc_cfg_0023.html)


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface vbdif**](cmdqueryname=interface+vbdif) *bd-id*
   
   
   
   The VBDIF interface view is displayed.
3. Run [**dhcp select relay**](cmdqueryname=dhcp+select+relay)
   
   
   
   The DHCP relay function is enabled.
4. Run [**ip relay address**](cmdqueryname=ip+relay+address) *ip-address* [ **dhcp-option** { *code\_60* [ *option-text* ] | *code\_1to59* | *code\_61to254* } ]
   
   
   
   A DHCP server IP address associated with an Option is configured on the DHCP relay interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After configuring an EVC to transmit DHCP relay services, check the configurations.

1. Run the [**display dhcp relay address**](cmdqueryname=display+dhcp+relay+address) { **all** | **interface** *interface-type* *interface-number* } command to check the IP addresses of the DHCP relay agent and DHCP server.
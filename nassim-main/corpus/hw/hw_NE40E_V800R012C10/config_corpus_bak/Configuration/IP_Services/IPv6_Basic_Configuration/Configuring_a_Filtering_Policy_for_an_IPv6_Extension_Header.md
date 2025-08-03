Configuring a Filtering Policy for an IPv6 Extension Header
===========================================================

You can configure a filtering policy for an IPv6 extension header to filter packets.

#### Prerequisites

Before configuring a filtering policy for an IPv6 extension header in the interface view, enable the IPv6 function (for details, see [Enabling IPv6](dc_vrp_ipv6_cfg_0004.html)).


#### Context

To prevent the system from being attacked by specific packets, run the **ipv6 extension-header** command to configure a filtering policy (deny or permit) for an extension header in the packets. The methods of configuring filtering policies for different types of extended headers are as follows:

* If the extension header is Hop-by-Hop or Destination Options, you can configure a filtering policy for all options or a specified one in the header.
* If the extension header is Routing, you can configure a filtering policy for all routing types or a specified one in the header.
* If the extension header is Fragment, Encapsulation Security Payload, or Authentication, you can configure a filtering policy directly for the header because it carries neither options nor routing types.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a filtering policy for an IPv6 extension header in the system or interface view.
   
   
   * To configure a filtering policy for an IPv6 extension header in the system view, perform the following steps as needed:
     + Run the [**ipv6 extension-header**](cmdqueryname=ipv6+extension-header+hop-by-hop+destination+option-code+all) { **hop-by-hop** | **destination** } **option-code** { **all** | *optcodevalue* } { **deny** | **permit** } command to configure a filtering policy for the IPv6 Hop-by-Hop Options or Destination Options header.
     + Run the [**ipv6 extension-header routing routing-type**](cmdqueryname=ipv6+extension-header+routing+routing-type+all+deny+permit) { **all** | *routing-number* } { **deny** | **permit** } command to configure a filtering policy for the IPv6 Routing header.
     + Run the [**ipv6 extension-header**](cmdqueryname=ipv6+extension-header+fragment+esp+ah+deny+permit) { **fragment** | **esp** | **ah** } { **deny** | **permit** } command to configure a filtering policy for the IPv6 Fragment, Encapsulating Security Payload, or Authentication header.
   
   
   * To configure a filtering policy for an IPv6 extension header in the interface view, perform the following steps:
     1. Run the [**interface**](cmdqueryname=interface) *interface-type interface-number* command to enter the interface view.
     2. Run the [**ipv6 enable**](cmdqueryname=ipv6+enable) command to enable the IPv6 function.
     3. Perform the following steps as needed:
        + Run the [**ipv6 extension-header**](cmdqueryname=ipv6+extension-header+hop-by-hop+destination+option-code+all) { **hop-by-hop** | **destination** } **option-code** { **all** | *optcodevalue* } { **deny** | **permit** } command to configure a filtering policy for the IPv6 Hop-by-Hop Options or Destination Options header.
        + Run the [**ipv6 extension-header routing routing-type**](cmdqueryname=ipv6+extension-header+routing+routing-type+all+deny+permit) { **all** | *routing-number* } { **deny** | **permit** } command to configure a filtering policy for the IPv6 Routing header.
        + Run the [**ipv6 extension-header**](cmdqueryname=ipv6+extension-header+fragment+esp+ah+deny+permit) { **fragment** | **esp** | **ah** } { **deny** | **permit** } command to configure a filtering policy for the IPv6 Fragment, Encapsulating Security Payload, or Authentication header.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   A filtering policy configured for an IPv6 extension header in the interface view takes precedence over that in the system view.
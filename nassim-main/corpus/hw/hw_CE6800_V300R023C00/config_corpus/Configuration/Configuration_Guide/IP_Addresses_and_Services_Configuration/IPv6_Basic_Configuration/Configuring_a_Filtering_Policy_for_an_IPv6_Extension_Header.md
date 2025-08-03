Configuring a Filtering Policy for an IPv6 Extension Header
===========================================================

Configuring a Filtering Policy for an IPv6 Extension Header

#### Context

If the system needs to filter IPv6 packets, configure a filtering policy (deny or permit) for an extension header in the packets.

* If the extension header is Hop-by-Hop or Destination Options, you can configure a filtering policy for all options or a specified one in the header.
* If the extension header is Routing, you can configure a filtering policy for all routing types or a specified one in the header.
* If the extension header is Fragment, Encapsulation Security Payload, or Authentication, you can configure a filtering policy directly for the header because it carries neither options nor routing types.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure a filtering policy for an IPv6 extension header as required.
   
   
   
   **Table 1** Configuring a filtering policy for an IPv6 extension header
   | Operation | Global Deployment | Interface Deployment |
   | --- | --- | --- |
   | Configure a filtering policy for the Hop-by-Hop and Destination Options headers. | [**ipv6 extension-header**](cmdqueryname=ipv6+extension-header+hop-by-hop+destination+option-code+all) { **hop-by-hop** | **destination** } **option-code** { **all** | *optcodevalue* } { **deny** | **permit** } | [**interface**](cmdqueryname=interface) *interface-type interface-number*  [**undo portswitch**](cmdqueryname=undo+portswitch)  [**ipv6 enable**](cmdqueryname=ipv6+enable)  [**ipv6 extension-header**](cmdqueryname=ipv6+extension-header+hop-by-hop+destination+option-code+all) { **hop-by-hop** | **destination** } **option-code** { **all** | *optcodevalue* } { **deny** | **permit** } |
   | Configure a filtering policy for the Routing header. | [**ipv6 extension-header routing routing-type**](cmdqueryname=ipv6+extension-header+routing+routing-type+all+deny+permit) { **all** | *routing-number* } { **deny** | **permit** } | [**interface**](cmdqueryname=interface) *interface-type interface-number*  [**undo portswitch**](cmdqueryname=undo+portswitch)  [**ipv6 enable**](cmdqueryname=ipv6+enable)  [**ipv6 extension-header routing routing-type**](cmdqueryname=ipv6+extension-header+routing+routing-type+all+deny+permit) { **all** | *routing-number* } { **deny** | **permit** } |
   | Configure a filtering policy for the IPv6 Fragment, Encapsulating Security Payload, and Authentication headers. | [**ipv6 extension-header**](cmdqueryname=ipv6+extension-header+fragment+esp+ah+deny+permit) { **fragment** | **esp** | **ah** } { **deny** | **permit** } | [**interface**](cmdqueryname=interface) *interface-type interface-number*  [**undo portswitch**](cmdqueryname=undo+portswitch)  [**ipv6 enable**](cmdqueryname=ipv6+enable)  [**ipv6 extension-header**](cmdqueryname=ipv6+extension-header+fragment+esp+ah+deny+permit) { **fragment** | **esp** | **ah** } { **deny** | **permit** } |
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   A filtering policy configured for an IPv6 extension header in the interface view takes precedence over that in the system view.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
Configuring a Rate Limit for Receiving ND Messages
==================================================

Configuring_a_Rate_Limit_for_Receiving_ND_Messages

#### Context

If a device is attacked, it receives a large number of ND or ND Miss messages within a short period. As a result, the device consumes many CPU resources to learn and respond to ND entries, affecting the processing of other services. To resolve this issue, configure a rate limit for receiving ND messages. After the configuration is complete, the device counts the number of ND messages received per period. If the number exceeds the configured limit, the device does not process excess ND messages.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure a rate limit for receiving ND messages in the system or interface view.
   
   
   * In the system view, perform any of the following operations as needed:
     + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit**](cmdqueryname=anti-attack+rate-limit) *limit-number* command to configure a rate limit for receiving ND messages, that is, the number of ND messages that can be processed per second.
     + Run the [**ipv6 nd miss anti-attack rate-limit**](cmdqueryname=ipv6+nd+miss+anti-attack+rate-limit) *limit-number* command to configure a rate limit for receiving ND Miss messages, that is, the number of ND Miss messages that can be processed per second.
     + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit source-mac**](cmdqueryname=anti-attack+rate-limit+source-mac) *mac-address* [**maximum**](cmdqueryname=maximum) *max-value* command to configure a rate limit for receiving ND messages based on a specified source MAC address, that is, the number of ND messages that can be processed per second based on a specified source MAC address.
     + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit source-mac all**](cmdqueryname=anti-attack+rate-limit+source-mac+all) [**maximum**](cmdqueryname=maximum) *max-value* command to configure a rate limit for receiving ND messages based on any source MAC address, that is, the number of ND messages that can be processed per second based on any source MAC address.
     + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit source-ip**](cmdqueryname=anti-attack+rate-limit+source-ip) *ipv6-address* [**maximum**](cmdqueryname=maximum) *max-value* command to configure a rate limit for receiving ND messages based on a specified source IPv6 address, that is, the number of ND messages that can be processed per second based on a specified source IPv6 address.
     + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit source-ip all**](cmdqueryname=anti-attack+rate-limit+source-ip+all) [**maximum**](cmdqueryname=maximum) *max-value* command to configure a rate limit for receiving ND messages based on any source IPv6 address, that is, the number of ND messages that can be processed per second based on any source IPv6 address.
     + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { **ns** | **na** | **rs** | **ra** } **anti-attack** **rate-limit** **destination-ip** *ipv6-address* **maximum** *max-value* command to configure a rate limit for receiving ND messages based on a specified destination IPv6 address, that is, the number of ND messages that can be processed per second based on a specified destination IPv6 address.
     + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { **ns** | **na** } **anti-attack** **rate-limit** **target-ip** *ipv6-address* **maximum** *max-value* command to configure a rate limit for receiving ND messages based on a specified target IPv6 address, that is, the number of ND messages that can be processed per second based on a specified target IPv6 address.
     + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { **ns** | **na** | **rs** | **ra** } **anti-attack** **rate-limit** **destination-ip** **all** **maximum** *max-value* command to configure a rate limit for receiving ND messages based on any destination IPv6 address, that is, the number of ND messages that can be processed per second based on any destination IPv6 address.
     + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { **ns** | **na** } **anti-attack** **rate-limit** **target-ip** **all** **maximum** *max-value* command to configure a rate limit for receiving ND messages based on any target IPv6 address, that is, the number of ND messages that can be processed per second based on any target IPv6 address.
     + Run the [**ipv6 nd miss anti-attack rate-limit source-ip**](cmdqueryname=ipv6+nd+miss+anti-attack+rate-limit+source-ip) *ipv6-address* **maximum** *max-value* command to configure a rate limit for receiving ND Miss messages based on a specified source IPv6 address, that is, the number of ND Miss messages that can be processed per second based on a specified source IPv6 address.
     + Run the [**ipv6 nd miss anti-attack rate-limit source-ip all maximum**](cmdqueryname=ipv6+nd+miss+anti-attack+rate-limit+source-ip+all+maximum) *max-value* command to configure a rate limit for receiving ND Miss messages based on any source IPv6 address, that is, the number of ND Miss messages that can be processed per second based on any source IPv6 address.
   * In the interface view, perform the following steps:
     1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
     2. Run the [**ipv6 enable**](cmdqueryname=ipv6+enable) command to enable the IPv6 function for the interface.
     3. Perform any of the following operations as needed:
        + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit**](cmdqueryname=anti-attack+rate-limit) *limit* command to configure a rate limit for receiving ND messages, that is, the number of ND messages that can be processed per second.
        + Run the [**ipv6 nd miss anti-attack rate-limit**](cmdqueryname=ipv6+nd+miss+anti-attack+rate-limit) *limit* command to configure a rate limit for receiving ND Miss messages, that is, the number of ND Miss messages that can be processed per second.
        + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**na**](cmdqueryname=na) | [**ns**](cmdqueryname=ns) | [**ra**](cmdqueryname=ra) | [**rs**](cmdqueryname=rs) } [**anti-attack rate-limit source-ip**](cmdqueryname=anti-attack+rate-limit+source-ip) *ipv6-address* [**maximum**](cmdqueryname=maximum) *max-value* command to configure a rate limit for receiving ND messages based on a specified source IPv6 address, that is, the number of ND messages that can be processed per second based on a specified source IPv6 address.
        + Run the [**ipv6 nd miss anti-attack rate-limit source-ip**](cmdqueryname=ipv6+nd+miss+anti-attack+rate-limit+source-ip) *ipv6-address* **maximum** *max-value* command to configure a rate limit for receiving ND Miss messages based on a specified source IPv6 address, that is, the number of ND Miss messages that can be processed per second based on a specified source IPv6 address.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
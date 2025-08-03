Configuring a Rate Limit for Sending ND Messages
================================================

Configuring a Rate Limit for Sending ND Messages

#### Context

If a device is attacked, it receives a large number of ND or ND Miss messages within a short period. As a result, the device consumes many CPU resources to learn and respond to ND entries, affecting the processing of other services. To resolve this issue, configure a rate limit for sending ND messages. After the configuration is complete, the device counts the number of ND messages sent per period. If the number exceeds the configured limit, the device delays scheduling or ignores excess ND messages.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The priorities of rate limits for sending ND messages are as follows: rate limit for sending ND multicast messages configured in the interface view > rate limit for sending ND messages configured in the interface view > rate limit for sending ND multicast messages configured in the system view > rate limit for sending ND messages configured in the system view



#### Procedure

* In the system view, perform the following steps:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Perform either of the following operations as needed:
     
     
     + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**rs**](cmdqueryname=rs) | [**ra**](cmdqueryname=ra) | [**ns**](cmdqueryname=ns) | [**na**](cmdqueryname=na) } [**send rate-limit**](cmdqueryname=send+rate-limit) *rate-limit* command to configure a rate limit for sending ND messages.
     + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**rs**](cmdqueryname=rs) | [**ra**](cmdqueryname=ra) | [**ns**](cmdqueryname=ns) | [**na**](cmdqueryname=na) } [**send multicast rate-limit**](cmdqueryname=send+multicast+rate-limit) *rate-limit* command to configure a rate limit for sending ND multicast messages.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* In the interface view, perform the following steps:
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
     
     
     
     IPv6 is enabled for the interface.
  4. Perform either of the following operations as needed:
     
     
     + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**rs**](cmdqueryname=rs) | [**ra**](cmdqueryname=ra) | [**ns**](cmdqueryname=ns) | [**na**](cmdqueryname=na) } [**send rate-limit**](cmdqueryname=send+rate-limit) *rate-limit* command to configure a rate limit for sending ND messages on the interface.
     + Run the [**ipv6 nd**](cmdqueryname=ipv6+nd) { [**rs**](cmdqueryname=rs) | [**ra**](cmdqueryname=ra) | [**ns**](cmdqueryname=ns) | [**na**](cmdqueryname=na) } [**send multicast rate-limit**](cmdqueryname=send+multicast+rate-limit) *rate-limit* command to configure a rate limit for sending ND multicast messages on the interface.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
(Optional) Configuring Generation of ND Entries Upon Receipt of NA Messages
===========================================================================

The generation of ND entries upon receipt of NA messages enhances network reliability.

#### Context

By default, a device performs the following operations upon receipt of valid NS/NA messages:

* When an interface with ND entries receives valid NS messages, the values of ND entries are updated. In contrast, when an interface without ND entries receives valid NS messages, ND entries are generated on the interface.
* When an interface with ND entries receives valid NA messages, the values of ND entries are updated. In contrast, when an interface without ND entries receives valid NA messages, the NA messages are discarded.

When an interface has no ND entries, to ensure the device does not discard valid NA messages resulting in packet loss, configure the device to generate ND entries on the interface upon receipt of NA messages.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
   
   
   
   IPv6 is enabled for the interface.
4. Run either of the following commands:
   * To configure the device to generate an ND entry after receiving a valid NA message from an interface if no ND entry exists on the interface, run the [**ipv6 nd na glean**](cmdqueryname=ipv6+nd+na+glean) command.
   * To enable NA message attack defense, run the [**ipv6 nd na anti-attack enable**](cmdqueryname=ipv6+nd+na+anti-attack+enable) command. After this command is run, only the NA messages in response to the NS messages that the device sends are sent to the CPU for processing, and ND entries are generated.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the [**ipv6 nd na glean**](cmdqueryname=ipv6+nd+na+glean) command is run, the NA messages received by the CPU contain the NA messages in response to the NS messages that the device sends and the gratuitous NA messages that the peer sends. If the [**ipv6 nd na anti-attack enable**](cmdqueryname=ipv6+nd+na+anti-attack+enable) command is run, the NA messages received by the CPU contain only the NA messages in response to the NS messages that the device sends.
   
   The [**ipv6 nd na glean**](cmdqueryname=ipv6+nd+na+glean) and [**ipv6 nd na anti-attack enable**](cmdqueryname=ipv6+nd+na+anti-attack+enable) commands cannot be used together. If NA message attack defense is enabled on an interface, the device discards the gratuitous NA messages sent by the peer. As a result, the [**ipv6 nd na glean**](cmdqueryname=ipv6+nd+na+glean) command fails to take effect.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
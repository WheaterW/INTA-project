Configuring Generation of ND Entries Upon Receipt of NA Messages
================================================================

Configuring Generation of ND Entries Upon Receipt of NA Messages

#### Context

By default, a device performs the following operations upon receipt of valid NS/NA messages:

* When an interface with ND entries receives valid NS messages, the values of ND entries are updated. In contrast, when an interface without ND entries receives valid NS messages, ND entries are generated on the interface.
* When an interface with ND entries receives valid NA messages, the values of ND entries are updated. In contrast, when an interface without ND entries receives valid NA messages, the NA messages are discarded.

When an interface has no ND entries, to ensure the device does not discard valid NA messages resulting in packet loss, configure the device to generate ND entries on the interface upon receipt of NA messages.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
4. Enable IPv6.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
5. Configure the device to generate ND entries on the interface upon receipt of valid NA messages if no ND entry exists on the interface.
   
   
   ```
   [ipv6 nd na glean](cmdqueryname=ipv6+nd+na+glean)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
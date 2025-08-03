Enabling IPv6
=============

Enabling IPv6

#### Prerequisites

Before configuring IPv6 addresses for interfaces, you have completed the following tasks:

* Connect interfaces and configure physical parameters for the interfaces to ensure that the physical status of the interfaces is up.
* Configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is up.

#### Context

You can perform IPv6-related configurations on an interface only after IPv6 is enabled in the interface view.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of an interface on which IPv6 is to be enabled.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
4. Enable IPv6 on the interface.
   
   
   ```
   [ipv6 enable](cmdqueryname=ipv6+enable)
   ```
5. Exit the interface view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
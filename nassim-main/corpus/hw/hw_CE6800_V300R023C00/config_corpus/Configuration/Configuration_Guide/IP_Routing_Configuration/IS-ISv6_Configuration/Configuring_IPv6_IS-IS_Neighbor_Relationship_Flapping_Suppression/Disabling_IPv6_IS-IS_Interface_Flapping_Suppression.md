Disabling IPv6 IS-IS Interface Flapping Suppression
===================================================

Disabling IPv6 IS-IS Interface Flapping Suppression

#### Context

If an interface that carries IPv6 IS-IS services frequently alternates between up and down, interface flapping occurs, and protocol packets will be frequently exchanged. As a result, IPv6 IS-IS services and other services that rely on IPv6 IS-IS will be negatively affected. IPv6 IS-IS interface flapping suppression can address this issue by allowing a device to delay interface state changes to up. You are advised to disable this function if it is not needed.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable IPv6 IS-IS interface flapping suppression.
   
   
   ```
   [isis suppress-flapping interface disable](cmdqueryname=isis+suppress-flapping+interface+disable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
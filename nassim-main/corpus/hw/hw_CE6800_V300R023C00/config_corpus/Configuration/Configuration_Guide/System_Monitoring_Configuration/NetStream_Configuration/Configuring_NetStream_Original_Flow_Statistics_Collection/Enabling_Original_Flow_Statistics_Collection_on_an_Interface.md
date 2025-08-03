Enabling Original Flow Statistics Collection on an Interface
============================================================

Enabling Original Flow Statistics Collection on an Interface

#### Context

Original flow statistics can be exported only after the original flow statistics collection function is enabled on an interface.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Switch the NetStream mode.
   
   
   ```
   assign forward enp netstream enable
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   This command is supported only on the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S.
   
   By default, the NetStream flow table of a small size is supported on the CE6820H, CE6820H-K, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820S. After the NetStream mode is switched, the NetStream flow table of a large size is supported and the configuration takes effect after the device restarts.
3. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Perform the following configurations based on your site requirements:
   * Enable IPv4 original flow statistics collection on the interface.
     ```
     [netstream](cmdqueryname=netstream) { inbound | outbound } ip
     ```
     
     By default, IPv4 original flow statistics collection is disabled on an interface.
   * Enable IPv6 original flow statistics collection on the interface.
     ```
     [netstream](cmdqueryname=netstream) { inbound | outbound } ipv6
     ```
     
     By default, IPv6 original flow statistics collection is disabled on an interface.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
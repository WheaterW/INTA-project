(Optional) Enabling Bogus DHCP Server Detection
===============================================

After bogus Dynamic Host Configuration Protocol (DHCP)
server detection is enabled, the system generates logs about DHCP
servers.

#### Context

Before enabling bogus DHCP server detection, ensure that
DHCP snooping is enabled globally for the interface. Otherwise, the
detection function does not take effect.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dhcp snooping server record**](cmdqueryname=dhcp+snooping+server+record)
   
   
   
   Bogus DHCP server detection is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
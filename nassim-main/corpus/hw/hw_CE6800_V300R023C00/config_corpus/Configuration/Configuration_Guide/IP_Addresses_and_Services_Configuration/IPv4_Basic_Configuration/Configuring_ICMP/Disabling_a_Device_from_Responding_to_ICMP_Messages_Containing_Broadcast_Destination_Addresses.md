Disabling a Device from Responding to ICMP Messages Containing Broadcast Destination Addresses
==============================================================================================

Disabling a Device from Responding to ICMP Messages Containing Broadcast Destination Addresses

#### Prerequisites

Before disabling a device from responding to ICMP messages containing broadcast destination addresses, configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is up.


#### Context

Attackers often use ICMP messages containing broadcast destination addresses to attack a device. This increases network loads and degrades device performance.

To address this issue, disable the device from responding to such ICMP messages.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Disable the device from responding to ICMP messages containing broadcast destination addresses.
   
   
   ```
   [icmp broadcast-address echo disable](cmdqueryname=icmp+broadcast-address+echo+disable)
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
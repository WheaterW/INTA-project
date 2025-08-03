Configuring a Loopback Interface as an RP
=========================================

Configuring a Loopback Interface as an RP

#### Prerequisites

Before configuring anycast RP, you have completed the following tasks:

* Configure a unicast routing protocol to ensure that unicast routes are reachable.
* Enable multicast routing on all devices and enable PIM-SM on all involved interfaces.
* Divide the network into multiple PIM-SM domains without configuring RPs.

#### Context

Before configuring anycast RP on multiple devices in a PIM-SM domain, specify a loopback interface on each device and assign the same IP address to each interface. After an RP is configured, advertise the RP interface address through unicast routes to ensure that each device on the network has a reachable route to the RP address.

Configure the loopback interfaces as static RPs or C-RPs to participate in dynamic RP election.

* To use static RPs, configure a static RP on all devices in a PIM-SM domain.
* To use C-RPs, you are only required to configure a C-RP on the device where anycast RP is to be set up.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the loopback interface view.
   
   
   ```
   [interface](cmdqueryname=interface) loopback interface-number
   ```
   
   As multiple RPs that use the same IP address exist on a network, configuring loopback interfaces as RPs is recommended.
3. Configure an IP address for the loopback interface, that is, the RP address.
   
   
   ```
   [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
   ```
4. (Optional) Enable PIM-SM on the RP interface.
   
   
   ```
   [pim sm](cmdqueryname=pim+sm)
   ```
   
   
   
   You need to run this command on the interface before configuring a C-RP. This command is not required if a static RP is configured.
5. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Enter the PIM view.
   
   
   ```
   [pim](cmdqueryname=pim) [ vpn-instance vpn-instance-name ] 
   ```
7. Configure the loopback interface as an RP.
   * Configure a static RP.
     ```
     [static-rp](cmdqueryname=static-rp) rp-address
     ```
   * Configure a C-RP.![](public_sys-resources/note_3.0-en-us.png) 
     
     When configuring a C-RP, you need to configure a C-BSR and BSR boundaries. When configuring MSDP anycast RP, ensure that the C-BSR and C-RP addresses are different.
     
     ```
     [c-rp](cmdqueryname=c-rp) loopback interface-number
     ```
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
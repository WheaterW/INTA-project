Configuring PIM
===============

Configuring PIM

#### Context

IPv4 Layer 3 multicast over VXLAN uses VPN PIM as the multicast routing protocol. VXLAN gateways establish C-multicast routing tables to guide multicast data forwarding.

Perform the following steps on each of the PEs functioning as VXLAN gateways:


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VBDIF interface view.
   
   
   ```
   [interface vbdif](cmdqueryname=interface+vbdif) bd-id
   ```
   
   Ensure that the VBDIF interfaces on gateways have been bound to an L3VPN instance when deploying VXLAN in distributed gateway mode.
3. Enable PIM-SM.
   
   
   ```
   [pim sm](cmdqueryname=pim+sm)
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

Configure VPN PIM-related functions as needed. Note that PIM configurations are performed in the VPN instance PIM view whereas interface-specific configurations are performed in the VBDIF interface view. For details, see [PIM Configuration](vrp_pim_cfg_0000.html). The following configuration tasks are not supported:

* Configuring PIM-DM
* Configuring BFD for IPv4 PIM

When PIM-SM is configured in the ASM model, RPs can be deployed in either of the following modes:

* Deploy RPs for the VXLAN overlay network on VTEPs. You are advised to use loopback interface IP addresses as RP IP addresses and configure the same RP address for all VTEPs.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  If the IP address of a VTEP is set to the IP address of a loopback interface, the loopback interface address used by the RP must be different from the VTEP IP address because the loopback interface used by the RP must be bound to a VPN instance.
* Deploy RPs on other nodes. In this case, all VTEPs must have reachable VPN routes to the RPs.
(Optional) Configuring Proxy ARP
================================

When users communicate with each other for the first time, they send ARP request packets, which are broadcast on the Layer 2 network. To reduce the number of broadcast ARP packets, configure proxy ARP.

#### Context

Upon receipt of an ARP request packet, a device broadcasts the packet in the local BD. If the device receives a large number of ARP request packets within a certain period of time and broadcasts the packets, these packets consume many EVPN MPLS network resources, causing network congestion. As a result, network performance deteriorates, affecting user services.

To resolve this problem, configure proxy ARP on the device. Proxy ARP adheres to the following basic rules: The device listens to received ARP packets and generates ARP snooping entries to record source user information, including the source IP and MAC addresses, and inbound interfaces of the packets. After receiving an ARP request packet, the device preferentially responds to the request based on the information in the ARP snooping entry.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**l2vpn-family evpn**](cmdqueryname=l2vpn-family+evpn)
   
   
   
   The BGP EVPN address family view is displayed.
4. Run [**peer**](cmdqueryname=peer+advertise) { *ipv4-address* | *group-name* } **advertise** **arp**
   
   
   
   ARP route advertisement is configured.
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BGP view.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
7. (Optional) Run [**arp host ip-conflict-check**](cmdqueryname=arp+host+ip-conflict-check) **period** *period-value* **retry-times** *retry-times-value*
   
   
   
   The host IP address conflict check options are configured.
8. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The BD view is displayed.
9. Run [**arp l2-proxy enable**](cmdqueryname=arp+l2-proxy+enable)
   
   
   
   Proxy ARP is enabled.
10. (Optional) Run [**arp l2-proxy timeout**](cmdqueryname=arp+l2-proxy+timeout) *expire-time*
    
    
    
    An aging time is configured for ARP snooping entries.
    
    
    
    Each ARP snooping entry has a lifecycle, called aging time. An ARP snooping entry will be deleted if it is not updated before its aging time expires. If the device stores a large number of ARP snooping entries, the CPU resources are wasted, and ARP snooping entries for new users cannot be generated. To resolve this problem, perform this step to set an aging time, which allows ARP snooping entries to be updated regularly.
11. Perform the following operations as required:
    
    
    * If the device needs to carry Layer 2 services, run the [**arp collect host enable**](cmdqueryname=arp+collect+host+enable) command to enable EVPN MPLS to collect host information per BD.
    * If the device needs to carry Layer 3 services or carry both Layer 2 and Layer 3 services:
      
      1. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
      2. Run the [**interface**](cmdqueryname=interface) **vbdif** *bd-id* command to create a VBDIF interface and enter its view.
      3. Run the [**arp collect host enable**](cmdqueryname=arp+collect+host+enable) command to enable EVPN MPLS to collect host information per VBDIF interface.
12. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
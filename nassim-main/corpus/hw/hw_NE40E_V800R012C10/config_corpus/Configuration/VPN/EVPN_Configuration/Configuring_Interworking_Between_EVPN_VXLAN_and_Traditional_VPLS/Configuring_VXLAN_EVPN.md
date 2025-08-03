Configuring VXLAN EVPN
======================

Before enabling interconnection between PE1, PE2, and the EOR switch, configure basic EVPN and VXLAN functions on PE1 and PE2, and create EVPN instances and NVE interfaces.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**evpn vpn-instance**](cmdqueryname=evpn+vpn-instance) *vpn-instance-name* **bd-mode**
   
   
   
   A BD EVPN instance is created, and its view is displayed.
3. Run [**route-distinguisher**](cmdqueryname=route-distinguisher) *route-distinguisher*
   
   
   
   An RD is configured for the EVPN instance.
4. Run [**vpn-target**](cmdqueryname=vpn-target) *vpn-target* &<1-8> [ **both** | **export-extcommunity** | **import-extcommunity** ]
5. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the EVPN instance view.
6. Run [**interface nve**](cmdqueryname=interface+nve) *nve-number*
   
   
   
   The view of a Network Virtualization Edge (NVE) interface is displayed.
7. Run [**source**](cmdqueryname=source) *ip-address*
   
   
   
   An IP address is configured for the source virtual tunnel end point (VTEP).
8. Run [**vni**](cmdqueryname=vni) *vni-id* **head-end peer-list protocol bgp**
   
   
   
   An ingress replication list is configured.
9. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit from the NVE interface view.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
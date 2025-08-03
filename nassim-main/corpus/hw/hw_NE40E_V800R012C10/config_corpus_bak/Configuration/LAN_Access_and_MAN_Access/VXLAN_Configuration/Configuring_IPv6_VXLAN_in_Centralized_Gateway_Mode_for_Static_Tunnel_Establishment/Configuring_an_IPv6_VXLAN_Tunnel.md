Configuring an IPv6 VXLAN Tunnel
================================

VXLAN is a tunneling technology that uses MAC-in-UDP encapsulation to extend large Layer 2 networks. If an underlay network is an IPv6 network, you can configure an IPv6 VXLAN tunnel for a virtual network to access a large number of tenants.

#### Context

After you configure local and remote VNIs and VTEP IPv6 addresses, an IPv6 VXLAN tunnel is statically created. This configuration is simple, and no protocol configurations are involved. To ensure the proper forwarding of IPv6 VXLAN packets, IPv6 VXLAN tunnels must be configured on VXLAN gateways.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
   
   
   
   The BD view is displayed.
   
   
   
   *bd-id* specified in this command must be the same as *bd-id* specified in Step 2 in the service access point configuration.
3. Run [**vxlan vni**](cmdqueryname=vxlan+vni) *vni-id*
   
   
   
   A VNI is created and associated with the BD.
   
   
   
   To interconnect a VXLAN with a VPLS network, run the [**vxlan vni**](cmdqueryname=vxlan+vni) *vni-id* **split-horizon-mode** command on the edge device belonging to both networks to create a VNI, associate the VNI with a BD, and implement split horizon forwarding.
4. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view from the BD view.
5. Run [**interface nve**](cmdqueryname=interface+nve) *nve-number*
   
   
   
   An NVE interface is created, and the NVE interface view is displayed.
6. Run [**source**](cmdqueryname=source+%28NVE+interface+view%29+%28IPv6%29+) *ipv6-address*
   
   
   
   An IPv6 address is configured for the source VTEP.
   
   
   
   Either a physical or loopback interface address can be specified as the source VTEP's IPv6 address. Using a loopback interface address is recommended.
7. Run [**vni**](cmdqueryname=vni+head-end+peer-list+%28IPv6%29) *vni-id* **head-end peer-list** { *ipv6-address* } &<1-10>
   
   
   
   An IPv6 ingress replication list is configured.
   
   
   
   With this function, the ingress of an IPv6 VXLAN tunnel replicates and sends a copy of any received BUM packets to each VTEP in the ingress replication list (a collection of remote VTEP IPv6 addresses).
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Currently, BUM packets can be forwarded only through ingress replication. This means that non-Huawei devices must have ingress replication configured to establish IPv6 VXLAN tunnels with Huawei devices. If ingress replication is not configured, the tunnels fail to be established.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
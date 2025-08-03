(Optional) Configuring the Device to Sample MPLS IPv4 Packets
=============================================================

(Optional) Configuring the Device to Sample MPLS IPv4 Packets

#### Context

After NetStream is configured on an MPLS network, only the inner IP packets of MPLS packets are sampled by default. Depending on your requirements, you can configure the NetStream IPv4 original flow statistics collection function to sample the following type of information about MPLS IPv4 packets:

* Only inner IP packets of MPLS packets
* Only labels of MPLS packets
* Both inner IP packets and labels of MPLS packets

![](public_sys-resources/note_3.0-en-us.png) 

When NetStream is configured on an MPLS network, the version of exported NetStream packets must be V9, which does not need to be configured.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the type of MPLS IPv4 packet information to be sampled.
   
   
   ```
   [netstream mpls-aware](cmdqueryname=netstream+mpls-aware) { ip-only | label-and-ip | label-only } ip
   ```
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
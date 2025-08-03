(Optional) Configuring DOH Removal by the BIERv6 Penultimate Segment
====================================================================

If a BFER does not support the IPv6 DOH (indicating that it does not support BIERv6 forwarding), you can configure the function which allows the BIERv6 penultimate segment to remove the DOH that carries BIER options when sending packets.

#### Context

If you find that the boards on a BFER do not support BIERv6 forwarding during BIERv6 deployment, you can configure DOH removal by the BIERv6 penultimate segment. In this way, the BIERv6 penultimate segment removes the IPv6 DOH when sending IPv6 packets to the BFER. The BFER can then process the received packets without the IPv6 DOH.

DOH removal by the BIERv6 penultimate segment can be configured in either of the following modes:

* Configure this function on a BFER for a node that does not support BIERv6 forwarding.
* Configure this function through static BIFT mode on the node upstream of a node that does not support BIERv6 forwarding.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This configuration can be executed only when both the penultimate segment endpoint and the last segment endpoint both support DOH removal by the BIERv6 penultimate segment.



#### Procedure

* Enable DOH removal by the BIERv6 penultimate segment on a BFER.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bier**](cmdqueryname=bier)
     
     
     
     The BIER view is displayed.
  3. Run [**sub-domain**](cmdqueryname=sub-domain) *sub-domain-val* **ipv6**
     
     
     
     The sub-domain view is displayed.
  4. Run [**protocol**](cmdqueryname=protocol) *isis*
     
     
     
     The underlay protocol used to advertise BIERv6 information is configured.
  5. Run [**psp request**](cmdqueryname=psp+request)
     
     
     
     DOH removal by the BIERv6 penultimate segment is enabled.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the next hop has multiple BIERv6 traffic receivers, the previous-hop device replicates traffic into multiple copies, and the traffic is no longer transmitted through BIERv6 after this command is run.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure DOH removal by the BIERv6 penultimate segment through static BIFT mode on the node upstream of the node that does not support BIERv6 forwarding.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bier**](cmdqueryname=bier)
     
     
     
     The BIER view is displayed.
  3. Run [**sub-domain**](cmdqueryname=sub-domain) *sub-domain-val* **ipv6**
     
     
     
     The sub-domain view is displayed.
  4. Run [**protocol**](cmdqueryname=protocol) *static-bift*
     
     
     
     Static BIFT-based forwarding is enabled.
  5. Run [**bfr-neighbor**](cmdqueryname=bfr-neighbor) **end-bier** *ipv6-address* **bfr-id** *bfrid-start* **psp**
     
     
     
     The device is configured to remove the BIER DOH from the packets destined for a BFER and then directly forward the packets to the BFER.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
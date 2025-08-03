Specifying the TTL Mode for MPLS
================================

MPLS nodes process TTLs in either uniform or pipe mode.

#### Context

You can configure an MPLS TTL processing mode on the ingress PE or egress PE.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

After the TTL mode of an MPLS public network or VPN is changed, the new mode takes effect only for new MPLS LDP sessions. To make the change take effect for previously established MPLS LDP sessions, run the **reset mpls ldp** command to reestablish the sessions.



#### Procedure

* Set a TTL processing mode for MPLS LDP packets.
  
  
  
  Perform the following steps on the ingress:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls ldp ttl-mode**](cmdqueryname=mpls+ldp+ttl-mode+pipe+uniform) { **pipe** | **uniform** }
     
     
     
     An MPLS TTL processing mode is set.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set a TTL processing mode for MPLS TE packets.
  
  
  
  Perform the following steps on the ingress:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls te ttl-mode**](cmdqueryname=mpls+te+ttl-mode+pipe+uniform) { **pipe** | **uniform** }
     
     
     
     An MPLS TTL processing mode is set.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set a TTL processing mode for an MPLS SR.
  
  
  
  Perform the following steps on the ingress PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls sr ttl-mode**](cmdqueryname=mpls+sr+ttl-mode+pipe+uniform) { **pipe** | **uniform** }
     
     
     
     An MPLS TTL processing mode is set.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set a TTL processing mode for a BGP LSP egress.
  
  
  
  Perform the following steps on the egress PE:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. Run [**mpls bgp ttl-mode**](cmdqueryname=mpls+bgp+ttl-mode+pipe+uniform+egress) { **pipe** | **uniform** } **egress**
     
     
     
     A TTL processing mode is set for a BGP LSP egress.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  
  
  When IP packets in a VPN instance enter an MPLS tunnel, to configure the mode of processing the MPLS TTL carried in a private network label, run the [**ttl-mode**](cmdqueryname=ttl-mode) command. In addition, the [**mpls te ttl-mode**](cmdqueryname=mpls+te+ttl-mode) or [**mpls ldp ttl-mode**](cmdqueryname=mpls+ldp+ttl-mode) command configures the mode of processing the MPLS TTL in public network labels. The combinations of TTL processing modes are as follows:
  
  + The MPLS TTL processing modes for both the private network label and public network label are uniform.
    
    When an IP packet passes through an MPLS network, the IP TTL decreases by one on the ingress and is mapped to the MPLS TTL of the private network label. The MPLS TTL of the private network label is mapped to the MPLS TTL of the public network label. Then, the packet is processed in the standard TTL mode on the MPLS network. The egress removes the public network label, copies and pastes the MPLS TTL in the public network label to the MPLS TTL in the private network label, and removes the private network label. The egress then reduces the MPLS TTL by one and changes the IP TTL to a smaller value of the MPLS TTL and IP TTL. [Figure 1](#EN-US_TASK_0172368024__fig19685125215162) illustrates such an MPLS TTL processing mode.
    
    **Figure 1** MPLS TTL processing mode 1  
    ![](figure/en-us_image_0178301723.png)
  + The MPLS TTL processing mode for the private network label is pipe, and that for the public network label is uniform.
    
    When an IP packet passes through an MPLS network, the ingress reduces the IP TTL and copies and pastes the MPLS TTL that is fixed at 255 in the private network label to the MPLS TTL in the public network label. Then, the packet is processed in the standard TTL mode on the MPLS network. The egress removes the public network label, copies and pastes the MPLS TTL to the MPLS TTL in the private network label, and removes the private network label. The IP TTL is reduced by one only by the egress. [Figure 2](#EN-US_TASK_0172368024__fig17428105982615) illustrates such an MPLS TTL processing mode.
    
    **Figure 2** MPLS TTL processing mode 2  
    ![](figure/en-us_image_0178303162.png)
  + The MPLS TTL processing mode for the private network label is uniform, and that for the public network label is pipe.
    
    When an IP packet passes through an MPLS network, the ingress reduces the IP TTL by one and copies and pastes the IP TTL to the MPLS TTL of the private network label. The MPLS TTL of the public network label is fixed at 255. Then, the packet is processed in the standard TTL mode on the MPLS network. The egress removes the public network label and private network label in sequence, reduces the MPLS TTL by one, and changes the IP TTL to a smaller value of the MPLS TTL and the IP TTL. [Figure 3](#EN-US_TASK_0172368024__fig151291418183119) illustrates such an MPLS TTL processing mode.
    
    **Figure 3** MPLS TTL processing mode 3  
    ![](figure/en-us_image_0178303287.png)
  + The MPLS TTL processing modes for both the private network label and public network label are pipe.
    
    When an IP packet passes through an MPLS network, the IP TTL decreases by one on the ingress. The MPLS TTLs in the private network label and public network label are fixed at 255. Then, the packet is processed in the standard TTL mode on the MPLS network. The egress removes the public network label and private network label in sequence. The IP TTL is reduced by one only by the egress. [Figure 4](#EN-US_TASK_0172368024__fig1124394953420) illustrates such an MPLS TTL processing mode.
    
    **Figure 4** MPLS TTL processing mode 4  
    ![](figure/en-us_image_0178303571.png)
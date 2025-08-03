Configuring Layer 2 Multicast CAC in a VSI Scenario
===================================================

Layer 2 multicast CAC configurations are performed in a VSI scenario to limit the multicast group number and bandwidth.

#### Context

On the network shown in [Figure 1](#EN-US_TASK_0172367906__fig_dc_vrp_l2mc_cfg_06101), PE1 is downlinked to a residential network and uplinked to PE2 through a VPLS network to access an IPTV server on the Internet. To ensure high PE1 performance, stable multicast data transmission on PE1, and good IPTV service experience, configure Layer 2 multicast CAC for specific VSIs on PE1. If all programs of a service provider are grouped into one or more VSI channels, Layer 2 multicast CAC can also be configured to limit the bandwidth to a specific value for each multicast group in a VSI channel.

**Figure 1** Configuring Layer 2 multicast CAC for a VSI  
![](images/fig_dc_vrp_l2mc_cfg_06101.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

* On this network, PE1 is a Layer 2 device on which VSI-based Layer 2 multicast CAC needs to be configured.
* Before configuring Layer 2 multicast CAC for a VSI, configure an LDP-based VSI.
* Before configuring Layer 2 multicast CAC for a sub-interface, configure the sub-interface as a dot1q termination sub-interface and bind the sub-interface to the LDP-based VSI.

Layer 2 multicast CAC configurations can be performed for a VSI channel and for a sub-interface in a VSI.


#### Procedure

* Configure Layer 2 multicast CAC for a VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
     
     
     
     A VSI is created, and the VSI view is displayed.
  3. Run [**l2-multicast limit max-entry**](cmdqueryname=l2-multicast+limit+max-entry) *count* [ **except** { *acl-number* | **acl-name** *acl-name* } ]
     
     
     
     A multicast group number limit is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  5. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit from the VSI view.
* Configure Layer 2 multicast CAC for a VSI channel.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**l2-multicast-channel**](cmdqueryname=l2-multicast-channel) **vsi** *vsi-name*
     
     
     
     The VSI channel view is displayed.
  3. Run [**channel**](cmdqueryname=channel) *channel-name* **type** { **asm** | **ssm** }
     
     
     
     A VSI channel is created.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A VSI channel name must be different from a global channel name.
  4. Run [**group**](cmdqueryname=group) *group-address* { *group-mask-length* | *group-mask* } [ **per-bandwidth** *bandwidth* ]
     
     
     
     Multicast groups are specified for the channel. If **per-bandwidth** **bandwidth** is set, the bandwidth is limited to a specific value for each multicast group in the VSI channel. If this parameter is not set, the bandwidth is not limited for any multicast group in the VSI channel.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + Multicast group addresses specified for VSI channels must be different from those specified for global channels.
     + A multicast group address can be specified only for one channel in the same VSI.
  5. (Optional) Run [**unspecified-channel deny**](cmdqueryname=unspecified-channel+deny)
     
     
     
     The device is enabled to filter out multicast data for groups undefined in a VSI channel.
     
     
     
     After this command is run, the device permits only multicast data for groups defined in a VSI channel and denies all multicast data for groups undefined in a VSI channel.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  7. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit from the channel view.
  8. Run [**quit**](cmdqueryname=quit)
     
     
     
     Exit from the VSI channel view.
* Configure Layer 2 multicast CAC for a sub-interface in a VSI.
  1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number.subnumber*
     
     
     
     The Eth-Trunk sub-interface view is displayed.
  2. Run [**l2-multicast limit**](cmdqueryname=l2-multicast+limit) [ **channel** *channel-name* ] **bandwidth** *bandwidth* **dot1q** { *vid1* [ **to** *vid2* ] } &<1-10>
     
     
     
     The bandwidth is limited to a specific value for the dot1q termination sub-interface.
  3. Run [**l2-multicast limit per-trunk-member bandwidth**](cmdqueryname=l2-multicast+limit+per-trunk-member+bandwidth) *bandwidth* **dot1q** **vid** { *vid1* [ **to** *vid2* ] } &<1-10>
     
     
     
     The bandwidth is limited to a specific value for each Eth-Trunk member interface.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
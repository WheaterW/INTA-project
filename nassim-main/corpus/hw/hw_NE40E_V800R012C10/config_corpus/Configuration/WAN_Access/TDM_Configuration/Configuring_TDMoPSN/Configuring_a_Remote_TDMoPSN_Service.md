Configuring a Remote TDMoPSN Service
====================================

TDMoPSN supports SVC and PWE3 PWs.

#### Context

At the edge of a PSN, PE1 on the user side is connected to CE1 in the downstream direction, and PE2 on the network side is connected to CE2 in the upstream direction. Both PEs require the following configurations, whereas devices inside the PSN do not.

Currently, the following types of PWs are supported:

* SVC
* PWE3

This section uses dynamic PWE3 as an example to describe the PW configuration process.

The configuration can be performed using either of the following two methods.


#### Procedure

* Create a PW using a PW template.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) command to enable MPLS L2VPN.
  3. Run the [**pw-template**](cmdqueryname=pw-template) *pwname* command to create a PW template and enter the PW template view.
  4. Run the [**peer-address**](cmdqueryname=peer-address) *ip-address* command to configure an IP address for the peer PE of the current PW.
  5. Run the [**tnl-policy**](cmdqueryname=tnl-policy) **tnlPolicyName** command to configure a tunnel selection policy for the PW template.
  6. (Optional) Run the [**jitter-buffer depth**](cmdqueryname=jitter-buffer+depth) *depth* command to configure a jitter buffer depth.
  7. (Optional) Run the [**tdm-encapsulation-number**](cmdqueryname=tdm-encapsulation-number) *tdmEncapNumber* command to configure the number of TDM frames encapsulated in CESoPSN or SAToP packets.
  8. (Optional) Run the [**rtp-header**](cmdqueryname=rtp-header) command to add the RTP header to transparently transmitted TDM frames.
  9. Run the [**quit**](cmdqueryname=quit) command to exit the PW template view.
  10. Run the [**interface serial**](cmdqueryname=interface+serial) *interface-number* command to enter the serial interface view.
  11. Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ [ **control-word** | **no-control-word** ] | **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **ip-interworking** | **ip-layer2** ] | [ **secondary** | **bypass** ] | **ignore-standby-state** | **tdm-encapsulation-number** *number* | **tdm-sequence-number** | **jitter-buffer** *depth* | **rtp-header** | **idle-code** *idle-code-value* ] \* command to create a dynamic PW.
  12. (Optional) Run the [**trap-threshold**](cmdqueryname=trap-threshold) { **ces-jtrovr-exc** | **ces-jtrudr-exc** | **ces-lospkt-exc** | **ces-malpkt-exc** | **ces-misorderpkt-exc** | **ces-straypkt-exc** } **trigger-threshold** *trigger-threshold* **resume-threshold** *resume-threshold* command to configure generation and clearance thresholds for CES service performance threshold-crossing alarms.
  13. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Create a PW in the interface view.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**mpls l2vpn**](cmdqueryname=mpls+l2vpn) command to enable MPLS L2VPN.
  3. Run the [**interface serial**](cmdqueryname=interface+serial) *interface-number* command to enter the serial interface view.
  4. Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc) { *ip-address* | **pw-template** *pw-template-name* } \* *vc-id* [ | **tunnel-policy** *policy-name* [ **endpoint** *endpoint-address* **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **jitter-buffer** *depth* ] | [ **tdm-encapsulation** *number* ] | [ **tdm-sequence-number** ] | [ **idle-code** *idle-code-value* ] | **rtp-header** | **ignore-standby-state** ] \* command to create a dynamic PW.
  5. (Optional) Run the [**trap-threshold**](cmdqueryname=trap-threshold) { **ces-jtrovr-exc** | **ces-jtrudr-exc** | **ces-lospkt-exc** | **ces-malpkt-exc** | **ces-misorderpkt-exc** | **ces-straypkt-exc** } **trigger-threshold** *trigger-threshold* **resume-threshold** *resume-threshold* command to configure generation and clearance thresholds for CES service performance threshold-crossing alarms.
  6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
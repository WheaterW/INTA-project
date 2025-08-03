(Optional) Configuring a Multicast Group Security Policy
========================================================

A multicast group policy can be configured to limit the range and number of multicast groups that some hosts can join or to add security messages to multicast data packets.

#### Context

A multicast group security policy provides the following functions:

* Restriction on multicast group models: There are two models of multicast groups: Any-Source Multicast (ASM) and Source-Specific Multicast (SSM). When IGMPv3 multicast services are deployed, you can configure a device to forward the data of only ASM or SSM groups in the VLAN/VSI.
* Limit on the multicast group address range: You can limit the range of multicast groups that user hosts are allowed to join on an interface or sub-interface or in a VLAN/VSI.
* Multicast protocol message security protection: This function is used to ensure protocol security. After this function is enabled on a device and the device receives an IGMP message from the VLAN or VSI, the device directly discards the message if it does not carry the Router Alert option in the IP header.
* Multicast protocol message filtering based on the source or destination IP address: An ACL can be configured to filter the source and destination IP addresses in IGMP Query, Report, or Leave messages, which prevents multicast service interruptions caused by forged IGMP Query, Report, or Leave messages.

The preceding functions are optional and can be configured in any order. Configure one or more functions as required. Default settings are recommended.

Before configuring a multicast group security policy, enable IGMP snooping both globally and in a specified VLAN/VSI.


#### Procedure

* Set a multicast group model.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Perform either of the following operations based on the VLAN or VPLS networking:
     
     
     + To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
     + To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
  3. Run [**igmp-snooping version**](cmdqueryname=igmp-snooping+version) **3**
     
     
     
     The version number of IGMP snooping is set to 3 in the VLAN or VSI.
  4. Run [**igmp-snooping**](cmdqueryname=igmp-snooping) { **ssm-only** | **asm-only** | **asm-ssm** }
     
     
     
     A multicast group type is set in the VLAN or VSI.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Limit the multicast address range in a VLAN or VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Perform either of the following operations based on the VLAN or VPLS networking:
     
     
     + To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
     + To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
  3. Run [**igmp-snooping group-policy**](cmdqueryname=igmp-snooping+group-policy) { *acl-number* | **acl-name** *acl-name* } [ **version** *number* ]
     
     
     
     The multicast group address range is limited in the VLAN or VSI. Interfaces in the the VLAN or VSI are allowed to join only multicast groups in the range defined by a specified ACL.
     
     By default, the multicast address range is not limited in the VLAN or VSI.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the range of multicast groups that hosts can join on a sub-interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) { **ethernet** | **gigabitethernet** |**eth-trunk**} *interface-number.subnumber*
     
     
     
     The sub-interface view is displayed.
  3. Run [**igmp-snooping group-policy**](cmdqueryname=igmp-snooping+group-policy) { *acl-number* | **acl-name** *acl-name* } [ **version** *number* ]
     
     
     
     The multicast group address range is limited on the sub-interface, and the sub-interface is allowed to join only multicast groups in the range defined by a specified ACL.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a security policy for multicast protocol messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Perform either of the following operations based on the VLAN or VPLS networking:
     
     
     + To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
     + To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
  3. Run [**igmp-snooping require-router-alert**](cmdqueryname=igmp-snooping+require-router-alert)
     
     
     
     The device is configured to accept only the IGMP messages that contain the Router Alert option in the IP header.
     
     
     
     If the IP header of an IGMP message received by the device does not contain the Router Alert option, the device discards the message.
  4. Run [**igmp-snooping send-router-alert**](cmdqueryname=igmp-snooping+send-router-alert)
     
     
     
     The device is configured to send IGMP messages that carry the Router Alert option in the IP header.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure multicast message filtering based on source or destination IP addresses.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Perform either of the following operations based on the VLAN or VPLS networking:
     
     
     + To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
     + To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* command.
  3. Perform either of the following operations to configure IGMP Query, Report, or Leave message filtering based on source or destination IP addresses.
     
     
     + Run the [**igmp-snooping query-ip-policy**](cmdqueryname=igmp-snooping+query-ip-policy) { *acl-number* | **acl-name** *acl-name* } command to configure IGMP Query message filtering based on source IP addresses.
       
       After the configuration is complete and the device receives forged IGMP Query messages from a user host, the device does not forward subsequent IGMP Report or Leave messages to the user host. This configuration prevents multicast service interruptions.
     + Run the [**igmp-snooping ip-policy**](cmdqueryname=igmp-snooping+ip-policy) { *acl-number* | **acl-name** *acl-name* } command to configure IGMP Report or Leave message filtering based on source or destination IP addresses.
       
       After the configuration is complete and the device receives forged IGMP Report or Leave messages from a user host, the device does not forward multicast traffic to the user host. This configuration prevents bandwidth resource waste.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
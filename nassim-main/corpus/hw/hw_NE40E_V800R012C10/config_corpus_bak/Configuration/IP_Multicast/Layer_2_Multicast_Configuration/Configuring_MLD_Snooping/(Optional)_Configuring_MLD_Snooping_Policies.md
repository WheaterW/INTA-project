(Optional) Configuring MLD Snooping Policies
============================================

To improve service security, configure MLD snooping policies on a Layer 2 multicast device to filter multicast messages or restrict the multicast group range that hosts can join.

#### Context

Configure MLD snooping policies to control the programs that users can join and improve the controllability and security of a Layer 2 multicast network. MLD snooping policies include:

* Restriction on multicast group models: There are two models of multicast groups: Any-Source Multicast (ASM) and Source-Specific Multicast (SSM). If MLDv2 is used, you can configure the device to forward only ASM or SSM group data in a VLAN or VSI.
* Restriction on multicast group addresses, including those on a sub-interface and in a VLAN or VSI. To allow hosts on an interface, a sub-interface, or in a VLAN or VSI to join only specified multicast groups, configure this function.
* Multicast protocol message security protection: This function is used to ensure protocol security. After this function is enabled on a device and the device receives an MLD message from the VLAN or VSI, the device directly discards the message if it does not carry the Router Alert option in the IP header.
* Multicast protocol message filtering based on the source or destination IP address: An ACL can be configured to filter the source and destination IP addresses in MLD Report messages, which prevents multicast service interruptions caused by forged MLD Report messages.

The preceding functions are optional and can be configured in any order. Configure one or more functions as required. Default settings are recommended.

Before configuring a multicast group security policy, enable MLD snooping both globally and in a specified VLAN or VSI.


#### Procedure

* Set a multicast group model.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Perform either of the following operations based on the VLAN or VPLS networking:
     
     
     + To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
     + To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
  3. Run [**mld-snooping version**](cmdqueryname=mld-snooping+version) **2**
     
     
     
     Version 2 is set for MLD snooping in the VLAN or VSI.
  4. Run [**mld-snooping**](cmdqueryname=mld-snooping) { **ssm-only** | **asm-only** | **asm-ssm** }
     
     
     
     A multicast group model is set in the VLAN or VSI.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Limit the multicast address range in a VLAN or VSI.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Perform either of the following operations based on the VLAN or VPLS networking:
     
     
     + To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
     + To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
  3. Run [**mld-snooping group-policy**](cmdqueryname=mld-snooping+group-policy) { *acl6-number* | **acl6-name** *acl6-name* } [ **version** *number* ]
     
     
     
     The range of multicast groups that ports in the VLAN or VSI can join is set. The ports in the VLAN or VSI can only dynamically join the multicast groups that match the specified ACL.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the range of multicast groups that hosts can join on a sub-interface.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number.subnumber*
     
     
     
     The sub-interface view is displayed.
  3. Run [**mld-snooping group-policy**](cmdqueryname=mld-snooping+group-policy) { *acl6-number* | **acl6-name** *acl6-name* } [ **version** *number* ]
     
     
     
     The range of multicast groups that hosts can join is set for the sub-interface. The sub-interface can only dynamically join the multicast groups that match the specified ACL.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a security policy for multicast protocol messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Perform either of the following operations based on the VLAN or VPLS networking:
     
     
     + To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
     + To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* [ **static** ] command.
  3. Run [**mld-snooping require-router-alert**](cmdqueryname=mld-snooping+require-router-alert)
     
     
     
     The device is configured to accept only the MLD messages that contain the Router Alert option in the IP header.
     
     
     
     If the IP header of an MLD message received by the device does not contain the Router Alert option, the device discards the message.
  4. Run [**mld-snooping send-router-alert**](cmdqueryname=mld-snooping+send-router-alert)
     
     
     
     The device is configured to send MLD messages with the Router-Alert option in the IP header.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure multicast message filtering based on source or destination IP addresses.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Perform either of the following operations based on the VLAN or VPLS networking:
     
     
     + To enter the VLAN view, run the [**vlan**](cmdqueryname=vlan) *vlan-id* command.
     + To enter the VSI view, run the [**vsi**](cmdqueryname=vsi) *vsi-name* command.
  3. Configure the device to filter MLD Report messages based on source or destination IP addresses.
     
     
     + Run the [**mld-snooping ip-policy**](cmdqueryname=mld-snooping+ip-policy) { *acl6-number* | **acl6-name** *acl6-name* } command to configure an MLD Report filtering policy.
       
       After the configuration is complete and the device receives forged MLD Report messages from a user host, the device does not forward multicast traffic to the network segment of the user host. This prevents bandwidth resource waste.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
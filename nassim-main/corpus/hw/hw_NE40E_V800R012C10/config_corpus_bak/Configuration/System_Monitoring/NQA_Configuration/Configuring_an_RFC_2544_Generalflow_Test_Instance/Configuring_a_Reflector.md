Configuring a Reflector
=======================

This section describes how to configure a reflector, which loops traffic to an initiator. You can set reflector parameters based on each scenario.

#### Context

On the network shown in [Figure 1](dc_vrp_nqa_cfg_0046.html#EN-US_TASK_0172373103__fig_dc_vrp_nqa_cfg_004601) of "Configuring an RFC 2544 Generalflow Test Instance", the following two roles are involved in a generalflow test:

* Initiator: sends simulated service traffic to a reflector.
* Reflector: loops the service traffic to the initiator.

The reflector can reflect all packets on a reflector interface or the packets matching filter criteria to the initiator. The filter criteria include a destination unicast MAC address or a port number.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure the reflector. The reflector settings vary according to usage scenarios.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The reflector ID must be unique on a local node.
   * The aging time can be set for a reflector.
   
   | Usage Scenario | Configuration Procedure | Configuration Note |
   | --- | --- | --- |
   | Any scenario in which a reflector loops all packets | [**nqa reflector**](cmdqueryname=nqa+reflector) *reflector-id* **interface** *interface-type interface-number* [ **exclusive** ] [ **exchange-port** ] | On the network shown in [Figure 1](dc_vrp_nqa_cfg_0046.html#EN-US_TASK_0172373103__fig_dc_vrp_nqa_cfg_004601) of "Configuring an RFC 2544 Generalflow Test Instance", UNI-B is used as a reflector interface. |
   | Layer 2 | [**nqa reflector**](cmdqueryname=nqa+reflector) *reflector-id* **interface** *interface-type interface-number* [ **mac** *mac-address* ] [ **pe-vid** *pe-vid* **ce-vid** *ce-vid* | **vlan** *vlan-id* ] [ **source-port** *source-port* ] [ **destination-port** *destination-port* ] [ **exchange-port** ] [ **agetime** *agetime* | **endtime** { *endtime* | *enddate* *endtime* } ] [ **share-mode** ] | On the network shown in [Figure 1](dc_vrp_nqa_cfg_0046.html#EN-US_TASK_0172373103__fig_dc_vrp_nqa_cfg_004601) of "Configuring an RFC 2544 Generalflow Test Instance", the MAC address of the reflector's UNI-B or a MAC address that has never been used is used as the MAC address. |
   | Layer 3 | [**nqa reflector**](cmdqueryname=nqa+reflector) *reflector-id* **interface** *interface-type interface-number* [ **ipv4** *ip-address* ] [ **pe-vid** *pe-vid* **ce-vid** *ce-vid* | **vlan** *vlan-id* ] [ **source-port** *source-port* ] [ **destination-port** *destination-port* ] [ **exchange-port** ] [ **agetime** *agetime* | **endtime** { *endtime* | *enddate* *endtime* } ] [ **share-mode** ]  NOTE:  * In a Layer 3 scenario, static ARP must be configured first using the [**arp static**](cmdqueryname=arp+static) *ip-address* *mac-address* command. * In a Layer 3 scenario, the outbound interface must be specified when static ARP is configured on the reflector. | On the network shown in [Figure 1](dc_vrp_nqa_cfg_0046.html#EN-US_TASK_0172373103__fig_dc_vrp_nqa_cfg_004601) of "Configuring an RFC 2544 Generalflow Test Instance", an IP address on the same network segment as the reflector's UNI-B is used as the IP address. |
   | IP and IP gateway | [**nqa reflector**](cmdqueryname=nqa+reflector) *reflector-id* **interface** *interface-type interface-number* [ **ipv4** *ip-address* | **mac** *mac-address* | **simulate-ip** **ipv4** *ip-address2* ] [ **pe-vid** *pe-vid* **ce-vid** *ce-vid* | **vlan** *vlan-id* ] [ **source-port** *source-port* ] [ **destination-port** *destination-port* ] [ **exchange-port** ] [ **agetime** *agetime* | **endtime** { *endtime* | *enddate* *endtime* } ] [ **share-mode** ]  NOTE:  In the IP and IP gateway scenario, need to run the [**arp static**](cmdqueryname=arp+static) *ip-address* *mac-address* command to configure a static ARP entry for the source IP address. | On the network shown in [Figure 1](dc_vrp_nqa_cfg_0046.html#EN-US_TASK_0172373103__fig_dc_vrp_nqa_cfg_004601) of "Configuring an RFC 2544 Generalflow Test Instance", an IP address on the same network segment as the reflector's UNI-B is used as the simulated IP address. |
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
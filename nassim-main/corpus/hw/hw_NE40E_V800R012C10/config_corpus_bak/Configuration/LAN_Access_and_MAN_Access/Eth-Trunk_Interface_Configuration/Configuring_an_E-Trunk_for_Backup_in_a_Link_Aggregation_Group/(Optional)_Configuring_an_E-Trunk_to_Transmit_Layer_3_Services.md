(Optional) Configuring an E-Trunk to Transmit Layer 3 Services
==============================================================

(Optional)_Configuring_an_E-Trunk_to_Transmit_Layer_3_Services

#### Context

When you configure IP addresses for Eth-Trunk interfaces connecting the CE and PEs to transmit Layer 3 services, the PEs' Eth-Trunk interface configurations must meet the following requirements:

* The same IP address must be configured for the PE Eth-Trunk interfaces.
* The same MAC address must be configured for the PE Eth-Trunk interfaces.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **eth-trunk** trunk-id [ .subnumber ]
   
   
   
   An Eth-Trunk interface or Eth-Trunk sub-interface is created.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the service interface is an Eth-Trunk sub-interface, run the [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id* command to specify the VLAN associated with the sub-interface.
3. Run [**ip address**](cmdqueryname=ip+address) *address-value* { *mask-value* | *mask-v4* } [ *sub* ]
   
   
   
   An IP address is configured for the interface on the device. Note that the interfaces on PE1 and PE2 must be configured with the same IP address.
4. Run [**mac-address**](cmdqueryname=mac-address) *mac*
   
   
   
   A MAC address is configured for the interface on the device. Note that the interfaces on PE1 and PE2 must be configured with the same MAC address.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
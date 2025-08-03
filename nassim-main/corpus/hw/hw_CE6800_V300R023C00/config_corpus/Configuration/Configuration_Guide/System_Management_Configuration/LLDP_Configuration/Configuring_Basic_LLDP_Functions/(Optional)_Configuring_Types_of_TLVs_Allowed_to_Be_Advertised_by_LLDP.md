(Optional) Configuring Types of TLVs Allowed to Be Advertised by LLDP
=====================================================================

(Optional) Configuring Types of TLVs Allowed to Be Advertised by LLDP

#### Context

TLVs that can be encapsulated in an LLDPDU include basic TLVs, TLVs defined by IEEE 802.1, TLVs defined by IEEE 802.3, DCBX TLVs, and identity TLVs.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Perform one or more of the following operations to configure the types of TLVs that can be advertised by LLDP based on device configuration requirements.
   
   
   * Configure the types of basic TLVs that can be advertised on an interface.
     ```
     undo [lldp tlv-disable basic-tlv](cmdqueryname=lldp+tlv-disable+basic-tlv) { all | management-address | port-description | system-capability | system-description | system-name }
     ```
   * Configure the types of TLVs defined by IEEE 802.1 that can be advertised on an interface.
     ```
     [lldp tlv-enable dot1-tlv](cmdqueryname=lldp+tlv-enable+dot1-tlv) { protocol-vlan-id vlan-id | vlan-name vlan-id | protocol-identity }
     ```
   
   
   * Configure the types of TLVs defined by IEEE 802.3 that can be advertised on an interface.
     ```
     undo [lldp tlv-disable dot3-tlv](cmdqueryname=lldp+tlv-disable+dot3-tlv) { all | link-aggregation | mac-physic | max-frame-size } 
     ```
4. Enable the interface to advertise LLDP packets carrying peer device identity TLVs.
   
   
   
   When a controller is used to automatically deploy network services, you can manually manage a device on the controller web UI. When multiple devices directly connected to the device go online, the controller cannot determine which configurations are to be delivered to which devices. You can configure the interfaces to advertise LLDP packets carrying peer device identity TLVs. The directly connected devices can receive the identity TLVs and notify the controller, which can then deliver corresponding network service configurations to the devices based on their identity TLVs.
   
   1. Configure the peer device identity TLV.
      ```
      [port identity](cmdqueryname=port+identity) identify-para
      ```
   2. Configure the LLDP packets advertised by the interface to carry the peer device identity TLV.
      ```
      [identity enable](cmdqueryname=identity+enable)
      ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
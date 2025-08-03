Configuring Protocol-based VLAN Assignment
==========================================

Configuring Protocol-based VLAN Assignment

#### Prerequisites

Before configuring protocol-based VLAN assignment, you have completed the following task:

* Create a VLAN. For details, see [Creating and Deleting a VLAN](vrp_vlan_cfg_0013.html).


#### Context

Protocol-based VLAN assignment reduces manual VLAN configuration workloads and allows users to easily join a VLAN, transfer from one VLAN to another, and exit from a VLAN. In protocol-based VLAN assignment mode, only untagged packets are processed. For tagged packets, only interface-based VLAN assignment mode is used.

When receiving an untagged frame, a device identifies the protocol profile of the frame and uses that information to determine the VLAN that the frame belongs to.

* If the protocol profile of the frame matches one of the protocol-based VLANs configured on the interface, the device adds the protocol-based VLAN tag to the frame.
* If the protocol profile of the frame does not match any protocol-based VLAN configured on the interface, the device tags the frame with the PVID of the interface.

![](public_sys-resources/note_3.0-en-us.png) 

An interface enabled with protocol-based VLAN assignment cannot process protocol packets that need to be sent to the CPU. As such, protocol-based VLAN assignment is recommended in Layer 2 transparent transmission scenarios.


![](public_sys-resources/note_3.0-en-us.png) 

This function is not supported by the CE6885-LL (low latency mode).



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLAN view.
   
   
   ```
   [vlan](cmdqueryname=vlan) vlan-id
   ```
3. Associate a protocol with the VLAN and specify the protocol profile.
   
   
   ```
   [protocol-vlan](cmdqueryname=protocol-vlan) [ protocol-index1 ] { at | ipv4 | ipv6 | ipx { ethernetii | llc | raw | snap } | mode { ethernetii-etype etype-id1 | llc { dsap dsapValue ssap ssapValue } | snap-etype etype-id1 } }
   ```
   
   
   * *protocol-index1* specifies the index of a protocol profile.
     
     A protocol profile is composed of the protocol type and encapsulation format, and a protocol profile corresponds to a protocol-based VLAN.
   * When specifying the source and destination service access points (specified by *dsap-id* and *ssap-id* respectively), note the following points:
     
     + *dsapValue* and *ssapValue* cannot both be set to 0xaa.
     + *dsapValue* and *ssapValue* cannot both be set to 0xe0, which indicates logical link control (LLC) encapsulation of Internet Packet Exchange (IPX) packets.
     + *dsapValue* and *ssapValue* cannot both be set to 0xff, which indicates raw encapsulation of IPX packets.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Enter the view of the Ethernet interface to be added to the VLAN.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
6. Switch the interface working mode to Layer 2.
   
   
   ```
   [portswitch](cmdqueryname=portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
7. Configure the attribute for the Layer 2 Ethernet interface.
   
   
   ```
   [port link-type](cmdqueryname=port+link-type) hybrid
   ```
8. Configure the hybrid interface to allow packets from the protocol-based VLANs to pass through.
   
   
   ```
   [port hybrid untagged vlan](cmdqueryname=port+hybrid+vlan) { { vlan-id1 [ to vlan-id2 ] } &<1-10> | all }
   ```
9. Associate the interface with the protocol-based VLAN.
   
   
   ```
   [protocol-vlan vlan](cmdqueryname=protocol-vlan+vlan) vlan-id { all | protocol-index1 [ to protocol-index2 ] } [ priority priority ]
   ```
   
   *vlan-id* must be a protocol-based VLAN ID.
10. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display protocol-vlan interface**](cmdqueryname=display+protocol-vlan+interface) { *interface-type* *interface-number* | **all** } command to check the protocol-based VLAN assignment configuration on a single interface or all interfaces.
* Run the **display protocol-vlan vlan** { *vlan-id1* [ **to** *vlan-id2* ] | **all** } command to check the protocols associated with VLANs and the indexes of the corresponding protocol profiles.
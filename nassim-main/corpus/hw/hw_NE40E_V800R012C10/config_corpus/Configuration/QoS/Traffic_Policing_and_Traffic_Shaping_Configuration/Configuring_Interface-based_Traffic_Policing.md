Configuring Interface-based Traffic Policing
============================================

Interface-based traffic policing implements unified interface-specific traffic control through CAR configuration.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Perform the following operations depending on the type of the interface on which traffic policing will be used:
   
   
   * On a Layer 3 interface:
     1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the Layer 3 interface view.
   
   
   * On a Layer 2 interface:
     1. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the Layer 3 interface view.
     2. Run the [**portswitch**](cmdqueryname=portswitch) command to switch to the Layer 2 interface view.
        
        Perform either of the following operations to add the Layer 2 interface to one or more VLANs:
        
        + To add the Layer 2 interface to a specified VLAN, run the [**port default vlan**](cmdqueryname=port+default+vlan) *vlan-id* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
          
          Before running this command, ensure that the specified VLAN has been created.
        + To add the Layer 2 interface to a range of VLANs, run the [**port trunk allow-pass**](cmdqueryname=port+trunk+allow-pass) **vlan** { { *vlan-id1* [ **to** *vlan-id2* ] } & <1-10> | **all** } command.
3. Run the [**qos car**](cmdqueryname=qos+car) { **cir-percentage** *cir-percentage-value* [ [**pir-percentage**](cmdqueryname=pir-percentage) *pir-percentage-value* ] } [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ] [ **green** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } | **yellow** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } | **red** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } ] \* { **inbound** | **outbound** } [ **color-aware** ] or [**qos car**](cmdqueryname=qos+car) { **cir** *cir-value* [ **pir** *pir-value* ] } [ **cbs** *cbs-value* [ **pbs** *pbs-value* ] ] [ **adjust** *adjust-value* ] [ **green** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } | **yellow** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } | **red** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } ] \* { **inbound** | **outbound** } [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] &<1-10> } ] [ **identifier** { **none** | **vid** | **ce-vid** | **vid-ce-vid** } ] [ **color-aware** ] command to configure CAR on the interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * The [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] & <1-10> } ] parameter is valid only for Layer 2 interfaces and is used to configure traffic policing for VLAN packets. If this command is run on a Layer 3 interface, you cannot specify a VLAN ID. If this command is run on a Layer 2 interface, you must specify a VLAN ID.
   * When an interface is configured with both interface-based CAR and MF classification-based CAR actions, the numbers of bytes and packets on which MF classification-based CAR actions are performed are not counted in the interface-based CAR statistics.
   * When both MF classification-based CAR and interface-based CAR are configured, MF classification-based CAR takes effect first, and then interface-based CAR. When both broadcast suppression and interface-based CAR are configured, interface-based CAR applies only to known unicast packets, and broadcast suppression applies to broadcast packets. When CAR is configured for both the packets sent to the CPU and the packets sent to an interface, the CAR statistics on the packets sent to the CPU take precedence over the CAR statistics on the packets sent to an interface.
   * Interface-based CAR cannot be configured on trunk member interfaces.
   * The **cir** and **pir** parameters are expressed in kbit/s, and the **cbs** and **pbs** parameters are expressed in bytes.
   * If the network traffic is simple, you can configure single-token-bucket traffic policing. In this case, specify the **cir** and **cbs** parameters.
   * If the network traffic is complex, you must configure dual-token-bucket traffic policing. In this case, specify the **cir**, **pir**, **cbs**, and **pbs** parameters.
4. (Optional) Run the [**qos qos-car member-link-scheduler distribute**](cmdqueryname=qos+qos-car+member-link-scheduler+distribute) command to configure weight-based traffic distribution among trunk member interfaces when interface CAR is applied to the trunk interface.
5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After completing the configuration, perform the following operations to check the configurations:

* Run the [**display interface**](cmdqueryname=display+interface) [ *interface-type* [ *interface-number* ] ] command to check the traffic information about an interface.
* Run the [**display car statistics interface**](cmdqueryname=display+car+statistics+interface) *interface-type* *interface-number* { **inbound** | **outbound** } command to check the CAR statistics about a Layer 3 interface in a specified direction.
* Run the [**display car statistics interface**](cmdqueryname=display+car+statistics+interface) *interface-type* *interface-number* **vlan** *vlan-id* { **inbound** | **outbound** } command to check the CAR statistics about a Layer 2 interface in a specified direction.
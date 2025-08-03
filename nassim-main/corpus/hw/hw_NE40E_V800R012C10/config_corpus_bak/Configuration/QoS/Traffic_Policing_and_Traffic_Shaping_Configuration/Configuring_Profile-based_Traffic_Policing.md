Configuring Profile-based Traffic Policing
==========================================

QoS profile-based traffic policing allows you to configure a CAR policy in a QoS profile and apply the QoS profile to an interface to control the traffic on this interface.

#### Procedure

* Configure traffic policing in a QoS profile.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**qos-profile**](cmdqueryname=qos-profile) *profile-name* command to create a QoS profile and enter its view.
  3. (Optional) Run the **[**description**](cmdqueryname=description)** **description-info** command to configure a description for the QoS profile.
  4. Run the [**car**](cmdqueryname=car) { **cir** *cir-value* [ **pir** *pir-value* ] | **cir** **cir-percentage** *cir-percentage-value* [ **pir** **pir-percentage** *pir-percentage-value* ] } [ [**cbs**](cmdqueryname=cbs) *cbs-value* [ **pbs** *pbs-value* ] ] [ **green** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } | **yellow** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } | **red** { **discard** | **pass** [ **service-class** *class* **color** *color* ] } ] \* [ **inbound** | **outbound** ] [ **color-aware** ] command to configure CAR in order to guarantee user traffic.
  5. (Optional) Run the [**broadcast-suppression**](cmdqueryname=broadcast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] [ **inbound** | **outbound** ] command to configure a rate limit for broadcast packets in the QoS profile.
  6. (Optional) Run the [**multicast-suppression**](cmdqueryname=multicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] [ **inbound** | **outbound** ] command to configure a rate limit for multicast packets in the QoS profile.
  7. (Optional) Run the [**unknown-unicast-suppression**](cmdqueryname=unknown-unicast-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] [ **inbound** | **outbound** ] command to configure a rate limit for unknown unicast packets in the QoS profile.
  8. (Optional) Run the [**bu-suppression**](cmdqueryname=bu-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] **inbound** command to configure an overall rate limit for broadcast and unknown unicast packets in the QoS profile.
  9. (Optional) Run the [**bum-suppression**](cmdqueryname=bum-suppression) **cir** *cir-value* [ **cbs** *cbs-value* ] **inbound** command to configure an overall rate limit for broadcast, unknown unicast, and multicast packets in the QoS profile.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The [**qos-profile**](cmdqueryname=qos-profile) command configuration on an interface is mutually exclusive with the CAR and traffic suppression configuration on this interface in the same direction.
* Apply the QoS profile.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
  3. Run any of the following commands to apply the QoS profile to a specific type of interface:
     
     
     + Run the [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name* { **inbound** | **outbound** } [ **identifier** **none** ] [ **group** *group-name* ] command to apply the QoS profile to an IP-Trunk interface or a dot1q sub-interface.
     + Run the [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name* { **inbound** | **outbound** } **vlan** *vlan-id-begin* [ **to** *vlan-id-end* ] [ **identifier** { **vlan-id** | **none** } ] [ **group** *group-name* ] command to apply the QoS profile to a Layer 2 interface or a dot1q VLAN tag termination sub-interface.
     + Run the [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name* { **inbound** | **outbound** } **pe-vid** *pe-vlan-id* **ce-vid** { *ce-vlan-id-begin* [ **to** *ce-vlan-id-end* ] } [ **identifier** { **pe-vid** | **ce-vid** | **pe-ce-vid** | **none** } ] [ **group** *group-name* ] command to apply the QoS profile to a QinQ VLAN tag termination sub-interface.
     + Run the [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name* { **inbound** | **outbound** } [ **identifier** { **none** | **vid** | **ce-vid** | **vid-ce-vid** } ] [ **group** *group-name* ] command to apply the QoS profile to an EVC Layer 2 sub-interface.
     + Run the [**qos-profile**](cmdqueryname=qos-profile) *qos-profile-name* { **inbound** | **outbound** } **vni** *vni-id* **source** *sourceip* **peer** *peerip* command to apply the QoS profile to an NVE interface.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After completing the configuration, perform the following operations to verify the configuration:

* Run the [**display qos-profile application**](cmdqueryname=display+qos-profile+application) { *qos-profile-name* } command to check the application information about a QoS profile.
* Run the [**display qos-profile configuration**](cmdqueryname=display+qos-profile+configuration) [ *qos-profile-name* ] command to check the configurations of a QoS profile.
* Run the [**monitor qos-profile statistics**](cmdqueryname=monitor+qos-profile+statistics) **interface** { *interface-name* | *interface-type* *interface-number* } [ **vlan** *vlan-id* | **pe-vid** *pe-vid* **ce-vid** *ce-vid* | **vid** *vid-id* | **ce-vid** *ce-vid* | **vid** *vid-id* **ce-vid** *ce-vid* ] { **inbound** | **outbound** } [ **interval** *seconds* [ **repeat** *repeat* ] ] command to monitor QoS profile statistics.
* Run the [**display traffic buffer usage slot**](cmdqueryname=display+traffic+buffer+usage+slot) *slot-id* command to check the current buffer usage.
  
  In VS mode, this command is supported only by the admin VS.
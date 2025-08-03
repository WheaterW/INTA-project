Binding a QoS Profile and a Service Identification Policy to a BAS Interface
============================================================================

You can apply a QoS profile to a type of user packets on an interface to perform HQoS for the user packets based on the scheduling parameters. You can also bind a service identification policy to the interface so that packets that meet specified conditions can be mapped to the domain for authentication.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Applying a QoS profile to an interface functions differently from applying a QoS profile to a domain. The parameters about the bandwidth allocated to family users are obtained through the QoS profile applied to the interface while the parameters about the bandwidth allocated based on service types are obtained through the QoS profile applied to the domain.

You can apply a QoS profile configured with CAR to the AAA domain for a single service of family users, and then to the interface for all family users.

When rate limiting is configured for all family users on the interface, CAR and user-queue cannot both take effect in the upstream direction. If both CAR and user-queue are configured, CAR takes effect in the upstream direction. CAR and user-queue can both take effect in the downstream direction.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**bas**](cmdqueryname=bas)
   
   
   
   The BAS interface view is displayed.
4. Configure a user access type and related attributes:
   
   
   * To set the access type to Layer 2 common users and configure related attributes, run the [**access-type**](cmdqueryname=access-type) **layer2-subscriber** [ **bas-interface-name** *bname* | **default-domain** { **pre-authentication** *predname* | **authentication** [ **force** | **replace** ] *dname* } \* | **accounting-copy** **radius-server** *rd-name* ] \* command.
   * To configure the access type and related attributes for Layer 3 common users, run the [**access-type**](cmdqueryname=access-type) **layer3-subscriber** [ **default-domain** { [ **pre-authentication** *predname* ] **authentication** [ **force** | **replace** ] *dname* }\* ] command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When setting the user access type on a BAS interface, you can set the service attributes of the access users at the same time or later.
     
     + To specify an IP address segment and an associated authentication domain name for Layer 3 common users, run the [**layer3-subscriber**](cmdqueryname=layer3-subscriber) { *start-ip-address* [ *end-ip-address* ] | *start-ipv6-address* [ *end-ipv6-address* ] | **delegation-prefix** *start-ipv6-address* [ *end-ipv6-address* ] [ *end-ip-address* ] *mask-length*} \* [ **vpn-instance** *instance-name* ] **domain-name** *domain-name* and [**layer3-subscriber ip-address any**](cmdqueryname=layer3-subscriber+ip-address+any) **domain-name** *domain-name* commands in the system view.
     + To specify an IPv4 address segment and an associated authentication domain name for Layer 3 static users using the mask mode, run the [**layer3-subscriber subnet-session**](cmdqueryname=layer3-subscriber+subnet-session) *start-ip-address* { *mask-address* | *mask-length* } [ **vpn-instance** *instance-name* ] **domain-name** *domain-name* command in the system view.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + The access type cannot be configured on an Ethernet interface that is added to an Eth-Trunk interface. You can configure the access type of such an Ethernet interface only on the associated Eth-Trunk interface.
     + When configuring static routes for Layer 3 users, specify the next hop as the user IP address and do not specify the outbound interface. Otherwise, network-to-user traffic may fail to be forwarded.
   
   
   * To set the access type and configure related attributes for Layer 2 or Layer 3 leased line users, run the [**access-type**](cmdqueryname=access-type) **layer2-leased-line** **user-name** *uname* **password** { **cipher** *password* | **simple** *password* } [ **bas-interface-name** *bname* | **default-domain** **authentication** *dname* | **accounting-copy** **radius-server** *rd-name* | **nas-port-type** { **async** | **sync** | **isdn-sync** | **isdn-async-v120** | **isdn-async-v110** | **virtual** | **piafs** | **hdlc** | **x.25** | **x.75** | **g.3-fax** | **sdsl** | **adsl-cap** | **adsl-dmt** | **idsl** | **ethernet** | **xdsl** | **cable** | **wireless-other** | **802.11** } ] \* or [**access-type**](cmdqueryname=access-type) **layer3-leased-line** { **user-name** *uname* | **user-name-template** } **password** { **cipher** *password* | **simple** *password* } [ **default-domain** **authentication** *dname* | **bas-interface-name** *bname* | **accounting-copy** **radius-server** *rd-name* | **nas-port-type** { **async** | **sync** | **isdn-sync** | **isdn-async-v120** | **isdn-async-v110** | **virtual** | **piafs** | **hdlc** | **x.25** | **x.75** | **g.3-fax** | **sdsl** | **adsl-cap** | **adsl-dmt** | **idsl** | **ethernet** | **xdsl** | **cable** | **wireless-other** | **802.11** } | **mac-address** *mac-address* | **client-id** *client-id* ] \* command.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If a BAS interface has an online user, you can change the access type of the BAS interface only when the online user is a leased line user.
   * After the access type is set to leased line access, the NE40E performs authentication on the leased line user immediately.
5. (Optional) Run [**user-bandwidth auto-adapt**](cmdqueryname=user-bandwidth+auto-adapt) { **enable** | **type1** }
   
   
   
   Automatic PIR bandwidth adjustment is configured for DHCPv4, DHCPv6, and PPPoE users.
6. (Optional) Run [**option82-identify include static-user**](cmdqueryname=option82-identify+include+static-user)
   
   
   
   Option 82 is inserted for static users so that static users can be identified using a QoS profile.
7. Choose the matched command line to apply QoS profiles based on types of user packets.
   
   
   * Run the [**qos-profile**](cmdqueryname=qos-profile) *profile-name* [ **inbound** | **outbound** ] [ **identifier** { **none** | **option82** | **access-line-id** | **pe-vid** | **ce-vid** | **pe-ce-vid** | **vlan-id**} ] [ **group** *group-name* ] [ **session-limit** *max-session-number* ] command to apply a QoS profile to Layer 3 user packets and specify a family user identification mode.
   * Run the [**qos-profile**](cmdqueryname=qos-profile) *profile-name* [ **inbound** | **outbound** ] **vlan** *vlan-id-begin* [ **to** *vlan-id-end* ] [ **identifier** { **vlan-id** | **none** | **option82** | **access-line-id** } ] [ **group** *group-name* ] [ **session-limit** *max-session-number* ] command to apply a QoS profile to VLAN user packets and specify a family user identification mode.
   * Run the [**qos-profile**](cmdqueryname=qos-profile) *profile-name* [ **inbound** | **outbound** ] **pe-vid** *pe-vlan-id* **ce-vid** *ce-vlan-id-begin* [ **to** *ce-vlan-id-end* ] [ **identifier** { **pe-vid** | **ce-vid** | **pe-ce-vid** | **none** | **option82** | **access-line-id** } ] [ **group** *group-name* ] [ **session-limit** *max-session-number* ] command to apply a QoS profile to QinQ user packets and specify a family user identification mode.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Each SQ can be mapped to only one GQ.
8. Run [**service-identify-policy**](cmdqueryname=service-identify-policy) *policy-name*
   
   
   
   A service identification policy is bound to the BAS interface.
9. (Optional) When a family user accesses the device through an Eth-Trunk interface and the Eth-Trunk member interfaces reside on different forwarding or traffic management modules, to prevent the bandwidth of the Eth-Trunk interface from doubling, run one of the following commands to configure the total bandwidth to be allocated among Eth-Trunk member interfaces based on weights.
   
   
   * For common access family users, run the [**qos subscriber-access member-link-scheduler distribute**](cmdqueryname=qos+subscriber-access+member-link-scheduler+distribute) **inbound** command to allocate the bandwidth to trunk member interfaces based on weights.
   * For private line access family users, run the [**qos leased-line-access member-link-scheduler distribute**](cmdqueryname=qos+leased-line-access+member-link-scheduler+distribute) { **inbound** | **outbound** } command to allocate the bandwidth to trunk member interfaces based on weights.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
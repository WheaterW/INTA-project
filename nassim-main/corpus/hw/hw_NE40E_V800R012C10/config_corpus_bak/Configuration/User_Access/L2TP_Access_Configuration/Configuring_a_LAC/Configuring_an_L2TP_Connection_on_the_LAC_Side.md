Configuring an L2TP Connection on the LAC Side
==============================================

Configuring an L2TP connection on the LAC side is the prerequisite for establishing an L2TP tunnel.

#### Context

When the LAC is interconnected with the LNS, the LAC must have a reachable route to the LNS. After a loopback interface is specified on the LNS, a route destined for the loopback interface must be configured on the LAC.

Perform the following steps on the NE40E:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l2tp-group**](cmdqueryname=l2tp-group) *group-name*
   
   
   
   An L2TP group is created and the L2TP group view is displayed.
3. Run [**tunnel name**](cmdqueryname=tunnel+name) *tunnel-name* [ **lns-ip** *lns-ip* ]
   
   
   
   The local tunnel name is configured.
   
   
   
   The tunnel name is used for tunnel negotiation between the LAC and LNS. The requirements for the tunnel name vary according to the tunnel authentication mode.
   
   * In local authentication mode, only the tunnel password, not the tunnel name, is needed for tunnel authentication on the LAC/LNS. The tunnel name is used by the LNS to select an L2TP group to respond to connection requests from the LAC. There are no specific requirements on the format of the tunnel name. You only need to ensure that the LAC tunnel name and LNS tunnel name configured on the LAC are the same. No tunnel name needs to be configured on the LNS. In local strict authentication mode, the LAC checks the validity of both the remote LNS tunnel name and password. If the remote LNS tunnel name and password are inconsistent with the LNS tunnel name and password delivered by the RADIUS server or the locally configured LNS tunnel name and password, the check fails and the tunnel fails to be established.
   * In remote authentication mode, the LAC/LNS takes the L2TP tunnel as a user; therefore, the format of the tunnel name is **username@domain**. During tunnel establishment, the LAC/LNS sends the username and password received from the peer to the AAA server for authentication. The corresponding username and password must be configured on the AAA server.
4. Run [**start l2tp**](cmdqueryname=start+l2tp) { **ip** *ip-address* [ [ **weight** *lns-weight* ] | [ **preference** *preference*-value ] | [ **remote** *lns-name* ] | [ **identifier-name** *identifiername* ] ] \* } &<1-8>
   
   
   
   An L2TP connection is configured on the LAC.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * When configuring an L2TP connection on the LAC, you need to specify the IP address and weight of the LNS. Each L2TP group can be configured with a maximum of eight LNSs.
   * After this configuration is performed, the L2TP group type is LAC.
   * The LNS IP address in this command is optional. If the LNS IP address is delivered by the RADIUS server, you do not need to specify the LNS IP address in this command. Otherwise, you must specify the LNS IP address.
   * The LNS weight is valid only in LNS load balancing mode. The LAC assigns user sessions to each LNS based on weights.
   * In non-load balancing mode, after multiple LNSs are configured, the LAC attempts to establish a connection with each LNS in the order in which the LNSs are configured, until an LNS responds to the connection request and a tunnel is established. The other LNSs then function as the backup LNSs.
   * The **preference** *preference* parameter specified in the [**start l2tp**](cmdqueryname=start+l2tp) command is valid only when the priority-based load balancing mode is configured for the LNSs. The LAC preferentially establishes a tunnel with the highest-priority LNS. If the LNS with the highest priority is unavailable, the LAC selects an LNS based on the LNS priorities in descending order. For the LNSs with the same priority, the NE40E establishes tunnels with them in equal cost load balancing mode.
   * If the LAC needs to check the validity of the LNS tunnel name, you need to specify the **remote** *lns-name* parameter in the [**start l2tp**](cmdqueryname=start+l2tp) command. In this case, strict L2TP tunnel authentication needs to be enabled using the [**tunnel authentication strict**](cmdqueryname=tunnel+authentication+strict) command in the L2TP group view.
5. (Optional) Run [**tunnel-per-user**](cmdqueryname=tunnel-per-user)
   
   
   
   An L2TP user is allowed to exclusively use an L2TP tunnel.
   
   
   
   Tunnels in an L2TP group can work in active/standby, weight-based load balancing, or priority-based load balancing mode. The three load balancing modes are mutually exclusive. If a tunnel has been established in an L2TP group, the configuration cannot be changed.
6. (Optional) Run [**lac mtu enable**](cmdqueryname=lac+mtu+enable)
   
   
   
   The MTU of the VT is allowed to take effect on the LAC.
7. (Optional) Run [**lac mss enable**](cmdqueryname=lac+mss+enable)
   
   
   
   The MSS of the VT is allowed to take effect on the LAC.
8. (Optional) Run [**tunnel load-sharing**](cmdqueryname=tunnel+load-sharing)
   
   
   
   LNS load balancing is enabled.
   
   
   
   Tunnels in an L2TP group can work in active/standby, weight-based load balancing, or priority-based load balancing mode. The three load balancing modes are mutually exclusive. If a tunnel has been established in an L2TP group, the configuration cannot be changed.
9. (Optional) Configure the LNS locking period.
   1. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   2. Run the [**l2tp aging**](cmdqueryname=l2tp+aging) *time* command to configure the LNS locking period.
      
      
      
      If the NE40E attempts to establish a tunnel with an LNS but the LNS does not work properly, the NE40E marks the LNS as unavailable and does not establish a tunnel with the LNS within a specified period of time (LNS locking period). The NE40E attempts to re-establish a tunnel with the LNS only after the LNS locking period elapses.
   3. Run the [**l2tp chasten lns-stopccn disable**](cmdqueryname=l2tp+chasten+lns-stopccn+disable) command to disable the device from locking the LNS IP address when receiving a STOPCCN message.
   4. Run the [**l2tp-group**](cmdqueryname=l2tp-group) *group-name* command to enter the L2TP group view.
10. (Optional) Run [**avp nas-port enable**](cmdqueryname=avp+nas-port+enable)
    
    
    
    The function to encapsulate NAS-PORT into the AVP100 attribute of the ICRQ messages to be sent to the LNS when a user goes online from the LAC is enabled.
11. (Optional) Run [**tunnel source**](cmdqueryname=tunnel+source) *interface-type* *interface-number*
    
    
    
    The tunnel source interface is configured.
    
    
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    When initiating a tunnel establishment request, the LAC needs to send the source address of the local tunnel to the LNS for communication with the LNS. To improve the reliability of the communication between the LAC and LNS, you can configure the tunnel source interface so that the LAC uses the IP address of the specified interface as the source address of the tunnel during tunnel establishment.
    
    The IP address of the tunnel source interface and the IP address of the source interface bound to the LNS cannot be the same as the tunnel source IP address of the RBS tunnel in dual-device hot backup scenarios.
12. (Optional) Run [**allow-address-change**](cmdqueryname=allow-address-change) { **setup-only** | **always** }
    
    
    
    The NE40E is configured to respond to the changes of the LNS's source IP address during tunnel establishment or hello detection for tunnels.
13. (Optional) Run [**tunnel window receive**](cmdqueryname=tunnel+window+receive) *window-size*
    
    
    
    The size of the L2TP receive window which is used to save out-of-order packets is configured.
14. (Optional) Run [**tunnel priority**](cmdqueryname=tunnel+priority)
    
    
    
    Priority-based load balancing for tunnels is configured.
    
    
    
    After the [**tunnel priority**](cmdqueryname=tunnel+priority) command is run, the NE40E preferentially establishes a tunnel with the highest-priority LNS. If the LNS with the highest priority is unavailable, the LAC selects an LNS based on the LNS priorities in descending order.
    
    For the LNSs with the same priority, the NE40E establishes tunnels with them in equal cost load balancing mode.
    
    Tunnels in an L2TP group can work in active/standby, weight-based load balancing, or priority-based load balancing mode. The three load balancing modes are mutually exclusive. If a tunnel has been established in an L2TP group, the configuration cannot be changed.
15. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
16. Run [**quit**](cmdqueryname=quit)
    
    
    
    The system view is displayed.
17. (Optional) Run the [**qos link-adjustment vendor redback**](cmdqueryname=qos+link-adjustment+vendor+redback) { **lns** | **lac** } \* [ **slot** *slot-id* ] command to configure user traffic compensation on the LAC so that the compensated user traffic statistics are collected in redback mode.
    
    
    
    In VS mode, this command is supported only by the admin VS.
    
    The compensation in redback mode is implemented as follows:
    
    | Layer 2 | LAC (UP) (Unit: Byte) | LAC (DOWN) (Unit: Byte) | LNS (UP) | LNS (DOWN) |
    | --- | --- | --- | --- | --- |
    | Compensation value (default) | * Double-tagged: 12 * Single-tagged: 16 * Without a VLAN: 20 | 4 | 6 | 4 |
    | Compensation value (CAR) | * Double-tagged: 12 * Single-tagged: -16 * Without a VLAN: -20 | -4 | 6 | -4 |
    | Compensation value (SQ) | * Double-tagged: -8 * Single-tagged: -12 * Without a VLAN: -16 | * Double-tagged: 24 * Single-tagged: 20 * Without a VLAN: 16 | 10 | 38 |
18. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.
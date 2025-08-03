(Optional) Configuring Negotiation Parameters for a RADIUS Server
=================================================================

(Optional)_Configuring_Negotiation_Parameters_for_a_RADIUS_Server

#### Context

A device must use the negotiated RADIUS parameters and message format to communicate with a RADIUS server.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure global negotiation parameters between the device and RADIUS server as required.
   
   
   
   **Table 1** Configuring global negotiation parameters between the device and RADIUS server
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure a mode for collecting statistics about RADIUS authentication request and response packets. | [**radius-server packet statistics algorithm**](cmdqueryname=radius-server+packet+statistics+algorithm) { **version1** | **version2** } | When a Huawei device interworks with a non-Huawei NMS, run this command to adjust the mode for collecting statistics about RADIUS authentication request and response packets. |
   | Configure the device to bind a RADIUS server group with the [**undo radius-server user-name domain-included**](cmdqueryname=radius-server+user-name%28RADIUS%E6%9C%8D%E5%8A%A1%E5%99%A8%E7%BB%84%E8%A7%86%E5%9B%BE%29) command configured to the default management domain or the domain with the [**adminuser-priority**](cmdqueryname=adminuser-priority) *level* command configured. | [**radius-server admin-user domain-exclude enable**](cmdqueryname=radius-server+admin-user+domain-exclude+enable) | If RADIUS authentication, authorization, and accounting need to be performed for an administrator but some RADIUS servers do not support the username format with a domain name, configure the device to delete the domain name in a username before sending it to the RADIUS server. In this case, the username of the administrator does not carry the domain name. Therefore, run this command to bind the administrator to the default administrative domain or the domain configured with the [**adminuser-priority**](cmdqueryname=adminuser-priority) *level* command after running the [**undo radius-server user-name domain-included**](cmdqueryname=undo+radius-server+user-name+domain-included) command. |
   | Configure the maximum number of pending packets that can be sent to the RADIUS server. | [**radius-server**](cmdqueryname=radius-server+pending-limit) { **accounting** | **authentication** } [*ip-address* [ **vpn-instance** *vpn-instance*  ] ] [ *port* ] **pending-limit** *pending-limit* | The processing capability of the RADIUS server is limited. To ensure that the device receives a response packet for each packet sent to the RADIUS server, run this command. |
   | Configure the limit on the rate at which packets are sent to the RADIUS server. | **[**radius-server**](cmdqueryname=radius-server)** { ****authentication**** | ****accounting**** } **ip-address** [ ****vpn-instance**** **vpn-instance-name** ] [ **port** ] ****speed-limit**** **send-packet-number** **second** | The processing capability of the RADIUS server is limited. To limit the rate at which the device sends packets to the RADIUS server, run this command.  If you do not know the processing capability of the RADIUS server and the number of service packets to be processed, you are advised to limit the number of pending packets instead of directly limiting the packet sending rate. |
3. Run [**radius-server group**](cmdqueryname=radius-server+group) *group-name*
   
   
   
   The RADIUS server group view is displayed.
4. Configure negotiation parameters between the device and RADIUS server group as required.
   
   
   
   **Table 2** Configuring negotiation parameters between the device and RADIUS server group
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the protocol version of the RADIUS server. | [**radius-server type**](cmdqueryname=radius-server+type) { **standard** | **plus10** | **plus11** } | RADIUS attributes vary with versions of the RADIUS protocol. |
   | Configure the username format supported by the RADIUS server. | [**radius-server user-name**](cmdqueryname=radius-server+user-name) { **domain-included** | **original** } | Run this command to configure whether the username sent from the device to the RADIUS server contains the domain name according to the type of the RADIUS server. |
   | Configure the device to replace the username generated on the device with that delivered by the RADIUS server. | [**radius-attribute apply user-name match user-type**](cmdqueryname=radius-attribute+apply+user-name+match+user-type) { **ipoe** | **pppoe** } | If the username generated on the device does not meet the naming requirements of the RADIUS server with which it communicates, run this command to configure the device to replace the original username with the username in the standard RADIUS No.1 attribute delivered by the RADIUS server. |
   | Configure the mode in which the RADIUS server delivers a tunnel password. | [**radius-attribute tunnel-password**](cmdqueryname=radius-attribute+tunnel-password) { **cipher** | **simple** } | Run this command to configure the mode used by the RADIUS server to deliver tunnel passwords. Both the RADIUS server and device must use the same mode. |
   | Configure the traffic unit for a RADIUS server. | [**radius-server traffic-unit**](cmdqueryname=radius-server+traffic-unit) { **byte** | **gbyte** | **kbyte** | **mbyte** } | This command is invalid for RADIUS servers that do not measure traffic by bytes and for those that use the standard RADIUS protocol. |
   | Configure the format of RADIUS packets used to inform the upstream device of the link ID. | [**radius-attribute agent-circuit-id format**](cmdqueryname=radius-attribute+agent-circuit-id+format) { **cn** | **tr-101** } | Run this command to configure the format of RADIUS packets used to inform the upstream device of the ID of the link through which the upstream device forwards traffic. |
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
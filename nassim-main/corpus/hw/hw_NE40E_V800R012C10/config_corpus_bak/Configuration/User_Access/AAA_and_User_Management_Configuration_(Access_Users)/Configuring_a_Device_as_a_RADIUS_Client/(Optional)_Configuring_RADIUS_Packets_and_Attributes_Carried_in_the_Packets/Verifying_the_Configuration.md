Verifying the Configuration
===========================

Verifying_the_Configuration

#### Prerequisites

The server template has been configured.


#### Context

After configuring a RADIUS server, you can view the server configurations, the supported RADIUS attributes, and statistics about RADIUS packets.


#### Procedure

* Run the [**display radius-server authorization configuration**](cmdqueryname=display+radius-server+authorization+configuration) command to check the configuration of the RADIUS authorization server.
* Run the [**display radius-server configuration**](cmdqueryname=display+radius-server+configuration) [ **group** *groupname* ] command to check the configuration of the RADIUS server group.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Configuring the [**ui-mode type1**](cmdqueryname=ui-mode+type1) command in the system view influences the output format of the display command.
* Run the [**display radius-attribute**](cmdqueryname=display+radius-attribute) [ **name** *attribute-name* | { **type** { **3gpp** | **cmcc** | **dsl** | **huawei** | **microsoft** | **redback** | **standard** | **cisco** } *attribute-number* } ] command to check the RADIUS attributes supported by the system.
* Run the [**display radius-attribute**](cmdqueryname=display+radius-attribute) [ **server-group** *server-group-name* **packet** { **access-request** | **access-accept** | **access-reject** | **accounting-request** | **accounting-response** | **coa-request** | **coa-ack** | **coa-nak** | **dm-request** | **dm-ack** | **dm-nak** | **accounting-on** | **accounting-off** } ] command to check the attributes carried in various packets in the RADIUS server group.
* Run the [**display radius-server packet**](cmdqueryname=display+radius-server+packet) { **ip-address** | **ipv6-address** } *ip-address* [ **vpn-instance** *vpn-instance* ] { **accounting** | **authentication** | **coa** | **dm** } command to check statistics about packets on the RADIUS server with a specified IP address.
* Run the [**display radius-attribute packet-count**](cmdqueryname=display+radius-attribute+packet-count) command to check the number of times an attribute occurs in a RADIUS packet.
* Run the [**display radius-client statistics**](cmdqueryname=display+radius-client+statistics) **client-ip** *client-ip-address* [ **vpn-instance** *vpn-instance-name* ] command to check statistics about RADIUS packets exchanged between the RADIUS client and proxy.
* Run the [**display aaa remote-download acl item**](cmdqueryname=display+aaa+remote-download+acl+item) [ **user-id** *user-id* | **classifier** *classifier-name* ] \* [ **verbose** ] command to check information about dynamic ACL C-B pairs delivered by the RADIUS server.
* Run the [**display aaa remote-download acl statistics**](cmdqueryname=display+aaa+remote-download+acl+statistics) **classifier** *classifier-name* [ **slot** *slot-id* ] command to check statistics about dynamic ACL C-B pairs delivered by the RADIUS server on a specific board.
* Run the [**display cpu-defend whitelist session-car radius statistics**](cmdqueryname=display+cpu-defend+whitelist+session-car+radius+statistics) **slot** *slot-id* command to check statistics about whitelist session-CAR for RADIUS sessions on a specified interface board.
* Run the [**display cpu-defend whitelist-v6 session-car radiusv6 statistics**](cmdqueryname=display+cpu-defend+whitelist-v6+session-car+radiusv6+statistics) **slot** *slot-id* command to check statistics about whitelist session-CAR for RADIUSv6 sessions on a specified interface board.
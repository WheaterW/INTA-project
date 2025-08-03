RADIUS CoA/DM
=============

The device supports the RADIUS Change of Authorization (CoA) and Disconnect Message (DM) functions.

* CoA provides a mechanism to change the rights of online users through RADIUS.
* DM provides a mechanism to disconnect users. When a user needs to be disconnected, the RADIUS server sends a DM packet to the device.

#### RADIUS CoA and DM Packets

[Table 1](#EN-US_CONCEPT_0000001513035594__tab-radius-3) describes types of CoA and DM packets.

**Table 1** RADIUS CoA and DM packets
| Packet Name | Description |
| --- | --- |
| CoA-Request | When an administrator needs to modify the rights of an online user (for example, prohibit the user from accessing a website), the RADIUS server sends this packet to the RADIUS client, requesting the client to modify the user rights. |
| CoA-ACK | If the RADIUS client successfully modifies the user rights, it returns this packet to the RADIUS server. |
| CoA-NAK | If the RADIUS client fails to modify the user rights, it returns this packet to the RADIUS server. |
| DM-Request | When an administrator needs to disconnect a user, the RADIUS server sends this packet to the RADIUS client, requesting the client to disconnect the user. |
| DM-ACK | If the RADIUS client has disconnected the user, it returns this packet to the RADIUS server. |
| DM-NAK | If the RADIUS client fails to disconnect the user, it returns this packet to the RADIUS server. |



#### Exchange Procedure

[Figure 1](#EN-US_CONCEPT_0000001513035594__fig_dc_fd_aaa_601901) shows the CoA exchange process.

**Figure 1** CoA exchange process  
![](figure/en-us_image_0000001563995929.png)

1. The RADIUS server sends a CoA-Request packet to the device according to service information, requesting the device to modify user authorization information. This packet can contain authorization information including ACLs.
2. Upon receiving the CoA-Request packet, the device checks whether the attributes in the packet match user information on the device to identify the user. If the match is successful, the device modifies authorization information of the user. Otherwise, the device retains the original authorization information of the user.
3. The device returns a CoA-ACK or CoA-NAK packet:
   * If authorization information is successfully modified, the device sends a CoA-ACK packet to the RADIUS server.
   * If authorization information fails to be modified, the device sends a CoA-NAK packet to the RADIUS server. If the user does not exist, the device does not respond.

[Figure 2](#EN-US_CONCEPT_0000001513035594__fig_dc_fd_aaa_601902) shows the DM exchange process.

**Figure 2** DM exchange process  
![](figure/en-us_image_0000001512676538.png)

1. The administrator disconnects a user on the RADIUS server. The RADIUS server sends a DM-Request packet to the device, requesting the device to disconnect the user.
2. Upon receiving the DM-Request packet, the device checks whether the attributes in the packet match user information on the device to identify the user. If the match is successful, the device instructs the user to go offline. Otherwise, the user remains online.
3. The device returns a DM-ACK or DM-NAK packet:
   
   * If the user successfully goes offline, the device sends a DM-ACK packet to the RADIUS server.
   * If the user remains online, the device sends a DM-NAK packet to the RADIUS server. If the user does not exist, the device does not respond.

In the CoA/DM process, the server sends a request packet to the device, which then sends a response packet. This process is different from the process in which authorization is performed for an online user or a user proactively goes offline. If the CoA/DM process is successful, the device returns an ACK packet. Otherwise, the device returns a NAK packet.


#### Session Identification

After the device receives a CoA-Request or DM-Request packet from the RADIUS server, it identifies the user based on some RADIUS attributes in the packet. The following RADIUS attributes can be used to identify users:

* Standard RADIUS attribute: User-Name (1)
* Standard RADIUS attribute: Acct-Session-ID (44)
* Standard RADIUS attribute: Framed-IP-Address (8)

The match methods are as follows:

* **any** method
  
  The device checks whether a RADIUS attribute matches user information on the device. It identifies the RADIUS attributes used by the users in the sequence listed: Acct-Session-ID (44) > Framed-IP-Address (8). The device then checks whether the first found attribute matches user information on the device. If the match is successful, the device responds with an ACK packet; otherwise, the device responds with a NAK packet.
* **all** method
  
  The device checks whether all RADIUS attributes match user information on the device. It identifies the following RADIUS attributes used by the users in the sequence listed: Acct-Session-ID (44), Framed-IP-Address (8), and User-Name (1). The device then checks whether all the preceding attributes in the request packet match user information on the device. If the match is successful, the device responds with an ACK packet; otherwise, the device responds with a NAK packet.

#### Error Codes

When RADIUS attributes in the CoA-Request or DM-Request packet from the RADIUS server fail to match user information on the device, the device describes the failure causes using the error codes in the CoA-NAK or DM-NAK packet. For details about the error codes, see [Table 2](#EN-US_CONCEPT_0000001513035594__coa-err) and [Table 3](#EN-US_CONCEPT_0000001513035594__dm-err).

**Table 2** Error codes in a CoA-NAK packet
| Name | Value | Description |
| --- | --- | --- |
| RD\_DM\_ERRCODE\_MISSING\_ATTRIBUTE | 402 | The request packet lacks key attributes, so the integrity check of RADIUS attributes fails. |
| RD\_DM\_ERRCODE\_INVALID\_REQUEST | 404 | Parsing the attributes in the request packet fails. |
| RD\_DM\_ERRCODE\_INVALID\_ATTRIBUTE\_VALUE | 407 | The request packet contains the attributes that are not supported by the device or do not exist, so the attribute check fails.  The authorization check involves VLAN, ACL, CAR, number of the ACL used for redirection, and whether Huawei RADIUS extended attributes RD\_hw\_URL\_Flag and RD\_hw\_Portal\_URL can be authorized to the interface-based authenticated user.  Possible errors are as follows:   * The authorized service scheme does not exist. * The authorized QoS profile does not exist or no user queue is configured in the QoS profile. * The authorized values of upstream and downstream priorities exceed the maximum values. * The ISP VLAN and outbound interface information are incorrectly parsed. * Reauthentication attributes and other attributes are authorized simultaneously. |
| RD\_DM\_ERRCODE\_SESSION\_CONTEXT\_NOT\_FOUND | 503 | The session request fails:   * Authorization for the current user is being processed. * The temporary RADIUS table cannot be requested. * User information does not match or no user is found. * The user is a non-RADIUS authenticated user. |
| RD\_DM\_ERRCODE\_RESOURCES\_UNAVAILABLE | 506 | This error code is used for other authorization failures. |


**Table 3** Error codes in a DM-NAK packet
| Name | Value | Description |
| --- | --- | --- |
| RD\_DM\_ERRCODE\_NAS\_IDENTIFICATION\_MISMATCH | 403 | The user information in the request packet does not match the user information on the device. |
| RD\_DM\_ERRCODE\_INVALID\_REQUEST | 404 | Parsing the attributes in the request packet fails. |
| RD\_DM\_ERRCODE\_SESSION\_CONTEXT\_NOT\_REMOVABLE | 504 | Failed to delete the user. |
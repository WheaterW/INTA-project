HWTACACS Packets
================

An HWTACACS client and an HWTACACS server communicate using HWTACACS packets sent over TCP/IP networks. Unlike RADIUS packets with the same format, HWTACACS packets (including [HWTACACS Authentication Packet](#EN-US_CONCEPT_0000001513035654__section_dc_fd_aaa_002002), [HWTACACS Authorization Packet](#EN-US_CONCEPT_0000001513035654__section_dc_fd_aaa_002003), and [HWTACACS Accounting Packet](#EN-US_CONCEPT_0000001513035654__section_dc_fd_aaa_002004)) are formatted differently. HWTACACS packets all share the same [HWTACACS Packet Header](#EN-US_CONCEPT_0000001513035654__section_dc_fd_aaa_002001).

#### HWTACACS Packet Header

HWTACACS defines a 12-byte header that appears in all HWTACACS packets. [Figure 1](#EN-US_CONCEPT_0000001513035654__fig_dc_fd_aaa_002001) shows the header.

**Figure 1** HWTACACS packet header  
![](figure/en-us_image_0000001512676638.png)

**Table 1** Fields in an HWTACACS packet header
| Field | Description |
| --- | --- |
| major version | Major HWTACACS version number. The current version is 0xc. |
| minor version | Minor HWTACACS version number. The current version is 0x0. |
| type | HWTACACS packet type:   * 0x01 (authentication) * 0x02 (authorization) * 0x03 (accounting) |
| seq\_no | Sequence number of the packet in a session. The sequence number of the first packet in a session is 1 and that of each subsequent packet increments by 1. The value ranges from 1 to 254. |
| flags | Encryption flag on the packet body. This field contains 8 bits, of which only the first bit has a valid value. The value 0 indicates that the packet body is encrypted, and the value 1 indicates that the packet body is not encrypted. |
| session\_id | ID of the HWTACACS session, which is the unique identifier of a session. |
| length | Total length of the HWTACACS packet body, excluding the packet header. |



#### HWTACACS Authentication Packet Format

HWTACACS defines three types of authentication packets:

* [Authentication Start](#EN-US_CONCEPT_0000001513035654__step_dc_fd_aaa_002002): indicates the type of authentication to be performed, and contains the user name and authentication data. This packet is only sent as the first packet in an HWTACACS authentication process.
* [Authentication Continue](#EN-US_CONCEPT_0000001513035654__step_dc_fd_aaa_002003): indicates that the authentication process has not ended. This packet is sent by a client when the client receives an Authentication Reply packet from the server.
* [Authentication Reply](#EN-US_CONCEPT_0000001513035654__step_dc_fd_aaa_002004): notifies the client of the current authentication status. When the server receives an Authentication Start or Authentication Continue packet from a client, the server sends this packet to the client.

The HWTACACS authentication packets have different formats.

* The following figure shows the HWTACACS Authentication Start packet body.
  
  **Figure 2** HWTACACS Authentication Start packet body  
  ![](figure/en-us_image_0000001513035826.png)
  
  **Table 2** Fields in an HWTACACS Authentication Start packet
  | Field | Description |
  | --- | --- |
  | action | Specific authentication action. Currently, only authentication login (0x01) and password change (0x02) are supported. |
  | priv\_lvl | Privilege level of a user. The value ranges from 0 to 15. |
  | authen\_type | Authentication type:  + 0x03 (CHAP authentication) + 0x02 (PAP authentication) + 0x01 (ASCII authentication) |
  | service | Type of the service requesting authentication. The value varies depending on the user type:  + PPP users: PPP(0x03) + Administrators: LOGIN(0x01) + Other users: NONE(0x00) |
  | user len | Length of the user name entered by a login user. |
  | port len | Length of the port field. |
  | rem\_addr len | rem\_addr field length. |
  | data len | Authentication data length. |
  | user | Name of the user requesting authentication. The maximum length is 129. |
  | port | Name of the user interface requesting authentication. The maximum length is 47.  + For administrators, this field indicates the user terminal interface, such as console0 and vty1. For example, the authen\_type of Telnet users is ASCII, service is LOGIN, and port is vtyx. + For other users, this field indicates the user access interface. |
  | rem\_addr | IP address of the login user. |
  | data | Authentication data. Different data is encapsulated depending on the values of the action and authen\_type fields. For example, when PAP authentication is used, the value of this field is PAP cleartext password. |
* The following figure shows the HWTACACS Authentication Continue packet body.
  
  **Figure 3** HWTACACS Authentication Continue packet body  
  ![](figure/en-us_image_0000001563875773.png)
  
  **Table 3** Fields in an HWTACACS Authentication Continue packet
  | Field | Description |
  | --- | --- |
  | user\_msg len | Length of the character string entered by a login user. |
  | data len | Authentication data length. |
  | flags | Authentication continue flag:  + 0: Authentication continues. + 1: Authentication has ended. |
  | user\_msg | Character string entered by a login user. This field carries the user login password to respond to the server\_msg field in the Authentication Reply packet. |
  | data | Authentication data. Different data is encapsulated depending on the values of the action and authen\_type fields. For example, when PAP authentication is used, the value of this field is PAP cleartext password. |
* The following figure shows the HWTACACS Authentication Reply packet body.
  
  **Figure 4** HWTACACS Authentication Reply packet body  
  ![](figure/en-us_image_0000001512676626.png)
  
  **Table 4** Fields in an HWTACACS Authentication Reply packet
  | Field | Description |
  | --- | --- |
  | status | Current authentication status:  + PASS (0x01): Authentication succeeds. + FAIL (0x02): Authentication fails. + GETDATA (0x03): Request user information. + GETUSER (0x04): Request user name. + GETPASS (0x05): Request password. + RESTART (0x06): Request reauthentication. + ERROR (0x07): The authentication packets received by the server have errors. + FOLLOW (0x21): The server requests reauthentication. |
  | flags | Whether the client displays the password entered by user in plain text. The value 1 indicates that the password is not displayed in plain text. |
  | server\_msg len | Length of the server\_msg field. |
  | data len | Authentication data length. |
  | server\_msg | Optional field. This field is sent by the server to the user to provide additional information. |
  | data | Authentication data, providing information to the client. |


#### HWTACACS Authorization Packet Format

HWTACACS defines two types of authorization packets:

* [Authorization Request](#EN-US_CONCEPT_0000001513035654__step_dc_fd_aaa_002005): contains a fixed set of fields that indicate how a user is authenticated or processed and a variable set of attributes that describe the information for which authorization is requested.
* [Authorization Response](#EN-US_CONCEPT_0000001513035654__step_dc_fd_aaa_002006): contains a variable set of attributes that can limit or change the client's action.

The HWTACACS authorization packets have different formats.

* The following figure shows the HWTACACS Authorization Request packet body.
  
  **Figure 5** HWTACACS Authorization Request packet body  
  ![](figure/en-us_image_0000001563875761.png)
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  The meanings of the following fields in the Authorization Request packet are the same as those in the Authentication Start packet: priv\_lvl, authen\_type, authen\_service, user len, port len, rem\_addr len, port, and rem\_addr.
  
  
  **Table 5** Fields in an HWTACACS Authorization Request packet
  | Field | Description |
  | --- | --- |
  | authen\_method | Authentication method used by the client to acquire user information:  + 0x00 (no authentication method configured) + 0x01 (non-authentication) + 0x05 (local authentication) + 0x06 (HWTACACS authentication) + 0x10 (RADIUS authentication) |
  | authen\_service | Type of the service requesting authentication. The value varies depending on the user type:  + PPP users: PPP(0x03) + Administrators: LOGIN(0x01) + Other users: NONE(0x00) |
  | arg\_cnt | Number of attributes carried in the Authorization Request packet. |
  | argN | Attribute of the Authorization Request packet:  + cmd: first argument in the command for authorization request. + cmd-arg: arguments in the command for authorization request. The format is fixed as cmd-arg=*command parameter*. The cmd-arg=<cr> is added at the end of the command line. The total length of cmd-arg=*command parameter* cannot exceed 255 bytes, and each command parameter cannot be longer than 247 bytes. |
* The following figure shows the HWTACACS Authorization Response packet body.
  
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  The meanings of the following fields are the same as those in the HWTACACS Authentication Reply packet: server\_msg len, data len, and server\_msg.
  
  
  **Figure 6** HWTACACS Authorization Response packet body  
  ![](figure/en-us_image_0000001513035782.png)
  
  **Table 6** Fields in an HWTACACS Authorization Response packet
  | Field | Description |
  | --- | --- |
  | status | Authorization status:  + 0x01 (authorization is successful) + 0x02 (the attributes in Authorization Request packets are modified by the TACACS server) + 0x10 (authorization fails) + 0x11 (an error occurs on the authorization server) + 0x21 (an authorization server is re-specified) |
  | arg\_cnt | Number of attributes carried in an Authorization Response packet. |
  | argN | Authorization attribute delivered by the HWTACACS authorization server. |


#### HWTACACS Accounting Packet Format

HWTACACS defines two types of accounting packets:

* [Accounting Request](#EN-US_CONCEPT_0000001513035654__step_dc_fd_aaa_002007): contains information used to provide accounting for a service provided to a user.
* [Accounting Response](#EN-US_CONCEPT_0000001513035654__step_dc_fd_aaa_002008): After receiving and recording an Accounting Request packet, the server returns this packet, indicating that accounting has completed and the record has been securely committed.

The HWTACACS accounting packets have different formats.

* The following figure shows the HWTACACS Accounting Request packet body.
  
  **Figure 7** HWTACACS Accounting Request packet body  
  ![](figure/en-us_image_0000001564115853.png)
  ![](public_sys-resources/note_3.0-en-us.png) 
  
  The meanings of the following fields in the Accounting Request packet are the same as those in the Authorization Request packet: authen\_method, priv\_lvl, authen\_type, user len, port len, rem\_addr len, port, and rem\_addr.
  
  
  **Table 7** Fields in an HWTACACS Accounting Request packet
  | Field | Description |
  | --- | --- |
  | flags | Accounting type:  + 0x02 (start accounting) + 0x04 (stop accounting) + 0x08 (interim accounting) |
  | authen\_service | Type of the service requesting authentication, which varies by user type:  + PPP users: PPP(0x03) + Administrators: LOGIN(0x01) + Other users: NONE(0x00) |
  | arg\_cnt | Number of attributes carried in the Accounting Request packet. |
  | argN | Attribute of the Accounting Request packet.  The command executed by a user is recorded in a recording scheme and transmitted to the server through this field. The field format is cmd=*command line*. The total length of the field cannot exceed 255 bytes, and each command line cannot exceed 251 bytes. If a command line exceeds 251 bytes, the device truncates the command line. |
* The following figure shows the HWTACACS Accounting Response packet body.
  
  **Figure 8** HWTACACS Accounting Response packet body  
  ![](figure/en-us_image_0000001513035786.png)
  
  **Table 8** Fields in an HWTACACS Accounting Response packet
  | Field | Description |
  | --- | --- |
  | server\_msg len | Length of the server\_msg field. |
  | data len | Length of the data field. |
  | status | Accounting status:  + 0x01 (accounting is successful) + 0x02 (accounting fails) + 0x03 (no response) + 0x21 (the server requests reaccounting) |
  | server\_msg | Information sent by the accounting server to the client. |
  | data | Information sent by the accounting server to the administrator. |
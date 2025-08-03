HWTACACS Attributes
===================

HWTACACS uses different attributes to define authorization and accounting to be performed. The attributes are carried by the argN field. This section describes HWTACACS attributes.

#### Overview of HWTACACS Attributes

[Table 1](#EN-US_CONCEPT_0000001563755933__tab_2) describes the HWTACACS attributes supported by the device. The device can only parse the attributes included in the table.

**Table 1** Common HWTACACS attributes
| Attribute Name | Description |
| --- | --- |
| acl | Authorization ACL ID. |
| addr | A network address. |
| autocmd | An auto-command to run after a user logs in to the device. |
| callback-line | Line number to use for a callback, such as a mobile number. |
| cmd | Command name for a shell command that is to be run. The maximum length is 251 characters. The complete command is encapsulated when the command is recorded and the first keyword is encapsulated when the command is authorized. |
| cmd-arg | Parameter in the command line to be authorized. The cmd-arg=<cr> is added at the end of the command line. |
| disc\_cause | Disconnection cause. Only Accounting-Request(Stop) packets carry this attribute:  * 1 (a user requests to go offline) * 2 (data forwarding is interrupted) * 3 (service is interrupted) * 4 (idle timeout) * 5 (session timeout) * 7 (the administrator requests to go offline) * 9 (the NAS is faulty) * 10 (the NAS requests to go offline) * 12 (the port is suspended) * 17 (user information is incorrect) * 18 (a host requests to go offline) |
| disc\_cause\_ext | Extension of the disc-cause attribute to support vendor-specific disconnection causes. Only Accounting-Request(Stop) packets carry this attribute:  * 1022 (unknown reason) * 1020 (the EXEC terminal tears down the connection) * 1022 (an online Telnet user logs out this user) * 1023 (the user cannot be switched to the SLIP/PPP client due to no remote IP address) * 1042 (PPP PAP authentication fails) * 1045 (PPP receives a Terminate packet from the remote end) * 1046 (the upper-layer device requests the device to tear down the PPP connection) * 1063 (PPP handshake fails) * 1100 (session times out) |
| dnaverage | Average downstream rate, in bit/s. |
| dnpeak | Peak downstream rate, in bit/s. |
| dns-servers | IP address of the primary DNS server. |
| elapsed\_time | Online duration of a user, in seconds. |
| ftpdir | Initial directory of the FTP user. The value is a string of 1 to 63 characters. |
| gw-password | Password for the gateway during the tunnel authentication. The value is a string of 1 to 248 characters. If the value contains more than 248 characters, only the first 248 characters are valid. |
| idletime | Period after which an idle session is terminated, in seconds. If a user does not perform any operation within this period, the system disconnects the user. |
| nocallback-verify | No callback authentication is required. |
| nohangup | Whether the device automatically disconnects a user who has executed the **autocmd** command. This attribute is valid only after the **autocmd** attribute is configured. The value can be true or false:   * true: The user is not disconnected. * false: The user is disconnected. |
| paks\_in | Number of packets received by the device. |
| paks\_out | Number of packets sent by the device. |
| priv-lvl | User privilege level. |
| protocol | A protocol that is a subset of a service. It is valid only for PPP and connection services. Currently, four protocol types are supported: pad, telnet, ip, and vpdn.  * Connection service type: pad or telnet * PPP service type: ip or vpdn * Other service types: This attribute is not used. |
| task\_id | Task ID. The task IDs recorded when a task starts and ends must be the same. |
| timezone | Time zone for all timestamps included in this packet. |
| tunnel-id | User name used to authenticate a tunnel in establishment. The value is a string of 1 to 29 characters. If the value contains more than 29 characters, only the first 29 characters are valid. |
| service | Service type, which can be accounting or authorization. |
| source-ip | Local IP address of a tunnel. |
| upaverage | Average upstream rate, in bit/s. |
| uppeak | Peak upstream rate, in bit/s. |



#### HWTACACS Attributes Available in Packets

Depending on usage scenarios, HWTACACS authorization packets can be classified into EXEC authorization packets and command authorization packets. Different authorization packets carry different attributes. For details, see [Table 2](#EN-US_CONCEPT_0000001563755933__table-hwtacacs-1). The following describes the use of HWTACACS authorization packets for different usage scenarios:

* EXEC authorization packets: used by the HWTACACS server to control rights of the administrators logging in through Telnet, terminal, SSH, and FTP.
* Command authorization packets: used by the device to authorize each command executed by the user. Only authorized commands can be executed.

Depending on connection types, HWTACACS accounting packets can be classified into network accounting packets, connection accounting packets, EXEC accounting packets, system accounting packets, and command accounting packets. Different accounting packets carry different attributes. For details, see [Table 3](#EN-US_CONCEPT_0000001563755933__table-hwtacacs-2). The following describes the use of HWTACACS accounting packets for different connection types:

* Network accounting packets: used when networks are accessed by PPP users. For example, when a PPP user connects to a network, the server sends an accounting start packet; when the user is using network services, the server periodically sends interim accounting packets; when the user goes offline, the server sends an accounting stop packet.
* Connection accounting packets: used when users log in to the server through Telnet or STelnet clients. When a user connects to the device, the user can run commands to access a remote server and obtain files from the server. The device sends an accounting start packet when the user connects to the remote server and sends an accounting stop packet when the user is disconnected from the remote server.
* EXEC accounting packets: used when users log in to the device through Telnet or FTP. When a user connects to a network, the server sends an accounting start packet; when the user is using network services, the server periodically sends interim accounting packets; when the user goes offline, the server sends an accounting stop packet.
* System accounting packets: used during fault diagnosis. The server records the system-level events to help administrators monitor the device and locate network faults.
* Command accounting packets: When an administrator runs any command on the device, the device sends the command to the HWTACACS server through an accounting stop packet so that the server can record the operations performed by the administrator.

![](public_sys-resources/note_3.0-en-us.png) 

In [Table 2](#EN-US_CONCEPT_0000001563755933__table-hwtacacs-1) and [Table 3](#EN-US_CONCEPT_0000001563755933__table-hwtacacs-2):

* **Y**: The packet supports this attribute.
* **N**: The packet does not support this attribute.

**Table 2** HWTACACS attributes available in authorization packets
| Attribute | Command Authorization Packet | EXEC Authorization Response Packet |
| --- | --- | --- |
| acl | N | N |
| addr | N | N |
| addr-pool | N | N |
| autocmd | N | N |
| callback-line | N | N |
| cmd | Y | N |
| cmd-arg | Y | N |
| dnaverage | N | N |
| dnpeak | N | N |
| dns-servers | N | N |
| ftpdir | N | Y |
| gw-password | N | N |
| idletime | N | Y |
| ip-addresses | N | N |
| nocallback-verify | N | N |
| nohangup | N | N |
| priv-lvl | N | Y |
| source-ip | N | N |
| tunnel-type | N | N |
| tunnel-id | N | N |
| upaverage | N | N |


**Table 3** HWTACACS attributes available in accounting packets
| Attribute | Network Accounting Start Packet | Network Accounting Stop Packet | Network Interim Accounting Packet | Connection Accounting Start Packet | Connection Accounting Stop Packet | EXEC Accounting Start Packet | EXEC Accounting Stop Packet | EXEC Interim Accounting Packet | System Accounting Stop Packet | Command Accounting Stop Packet |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| addr | Y | Y | Y | Y | Y | N | N | N | N | N |
| bytes\_in | N | Y | Y | N | Y | N | Y | Y | N | N |
| bytes\_out | N | Y | Y | N | Y | N | Y | Y | N | N |
| cmd | N | N | N | Y | Y | N | N | N | N | Y |
| disc\_cause | N | Y | N | N | N | N | Y | Y | N | N |
| disc\_cause\_ext | N | Y | N | N | N | N | Y | Y | N | N |
| elapsed\_time | N | Y | Y | N | Y | N | Y | Y | Y | N |
| paks\_in | N | Y | Y | N | Y | N | Y | Y | N | N |
| paks\_out | N | Y | Y | N | Y | N | Y | Y | N | N |
| priv-lvl | N | N | N | N | N | N | N | N | N | Y |
| protocol | Y | Y | Y | Y | Y | N | N | N | N | N |
| service | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| task\_id | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| timezone | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| tunnel-id | N | N | N | N | N | N | N | N | N | N |
| tunnel-type | Y | N | N | N | N | N | N | N | N | N |
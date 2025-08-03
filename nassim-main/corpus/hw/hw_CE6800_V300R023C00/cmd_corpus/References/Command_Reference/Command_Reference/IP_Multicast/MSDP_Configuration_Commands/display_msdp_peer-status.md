display msdp peer-status
========================

display msdp peer-status

Function
--------



The **display msdp peer-status** command displays detailed information about Multicast Source Discovery Protocol (MSDP) peers.




Format
------

**display msdp** { **vpn-instance** *vpn-instance-name* | **all-instance** } **peer-status** [ *peer-address* ]

**display msdp peer-status** [ *peer-address* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays detailed information about MSDP peers in a specified VPN instance.  vpn-instance-name specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. The VPN instance name "\_public\_" cannot be used. The string can contain spaces if it is enclosed with double quotation marks ("). |
| **all-instance** | Displays detailed information about MSDP peers in all instances. | - |
| *peer-address* | Displays detailed information about a specified MSDP peer.  peer-address specifies the address of an MSDP peer. | The value is in dotted decimal notation. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

After MSDP peers establish a TCP connection, you can run the **display msdp peer-status** command to display detailed information about MSDP peers, such as the interface status, interface configuration, policy for filtering messages, and number of messages.

**Prerequisites**

MSDP peer relationships have been set up.

**Precautions**

If neither vpn-instance vpn-instance-name nor all-instance is specified, the command displays detailed information about MSDP peers in the public network instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the MSDP peer 10.110.11.11 in the public network instance
```
<HUAWEI> display msdp peer-status 10.110.11.11
MSDP Peer Information of VPN Instance: public net
  MSDP Peer 10.110.11.11, AS 100
  Description:
  Information about connection status:
    State: Up
    Up/down time: 14:41:08
    Resets: 0
    Connection interface: LoopBack0 (10.10.10.20)
    Number of sent/received messages: 867/947
    Number of discarded output messages: 0
    Elapsed time since last connection or counters clear: 14:42:40
  Information about (Source, Group)-based SA filtering policy:
    Import policy: none
    Export policy: none
  Information about SA-Requests:
    Policy to accept SA-Request messages: none
    Sending SA-Requests status: disable
  Minimum TTL to forward SA with encapsulated data: 0
  SAs learned from this peer: 0, SA-cache maximum for the peer: none
  Input queue size: 0, Output queue size: 0
  Counters for MSDP message:
    Count of RPF check failure: 0
    Incoming/outgoing SA messages: 0/0
    Incoming/outgoing SA requests: 0/0
    Incoming/outgoing SA responses: 0/0
    Incoming/outgoing data packets: 0/0
  Peer authentication: unconfigured
  Peer authentication: none

```

**Table 1** Description of the **display msdp peer-status** command output
| Item | Description |
| --- | --- |
| MSDP Peer | Address of the MSDP peer. |
| MSDP Peer Information of VPN Instance | Instance in which detailed information about the MSDP peer is displayed. |
| Peer authentication | Indicates whether MSDP authentication is configured.  Indicates MSDP authentication modes, including:   * none: indicates authentication is not configured. * MD5: indicates Message-digest algorithm 5 (MD5) authentication. * Keychain: indicates Keychain authentication. |
| Information about (Source, Group)-based SA filtering policy | * Import policy: Used to receive the filtering list of the SA messages of a specified MSDP peer. You can configure the policy by using the peer sa-policy import command and remove the policy by using the undo peer sa-policy import command.  By default, the messages received are not filtered. The MSDP peer receives all the source active (SA) messages. The item is expressed by none. * Export policy: Used to forward the filtering list of the SA messages of a specified MSDP peer. You can configure the policy by using the peer sa-policy export command and remove the policy by using the undo peer sa-policy export command.  By default, the messages forwarded are not filtered. The MSDP peer forwards all the source active (SA) messages. The item is expressed by none. * Local export policy: Used to configure a policy for filtering SA messages so that only the locally created SA messages that match the policy are sent to the specified MSDP peer. You can configure the policy by using the peer sa-policy local-export command and remove the policy by using the undo peer sa-policy local-export command.  By default, the device sends all locally created (S, G) messages. The item is expressed by none. |
| Information about SA-Requests | * Policy to accept SA-Request messages: restricts the SA request messages received from an MSDP peer by the Router. You can set the policy by using the peer sa-request-policy command and remove the configuration by using the undo peer sa-request-policy command.   By default, the Router receives all the SA request messages sent by the MSDP peer. The item is expressed by none.   * Sending SA-Requests status: enables or disables the Router to send SA request messages to a specified MSDP peer when the Router receives a Join message. You can configure the function by using the peer request-sa-enable command and remove the function by using the undo peer sa-request-policy command.   By default, when receiving a Join message, the Router does not sent the SA request message to its MSDP peers, but waits for the next SA message. |
| AS | Autonomous system (AS) number of the MSDP peer.  "?" indicates that the AS number is not obtained. |
| Up/down time | Time when the session becomes Up or Down. The time format is as follows:   * Time that is shorter than or equal to 24 hours: hour: minute: second. * Time that is longer than 24 hours but shorter than one week: day: hour. * Time that is longer than one week: week: day. |
| Connection interface | Interface and address used to set up the TCP connection with the peer address. |
| Number of sent/received messages | Number of MSDP messages sent and received through the connection. |
| Number of discarded output messages | Number of discarded messages to be sent. |
| Elapsed time since last connection or counters clear | Period from the time of the latest resetting of the statistics, and inputting and outputting the statistics to the current time. |
| Minimum TTL to forward SA with encapsulated data | If the SA message received is encapsulated with the multicast data packet, the Router forwards the SA message to other peers only when the TTL of the packet is not smaller than the minimum TTL. You can configure the function by using the peer minimum-ttl command and remove the function by using the undo peer minimum-ttl command. |
| SAs learned from this peer | Indicates the SA messages that pass through the MSDP peer and the number of SA entries in the cache. |
| SA-cache maximum for the peer | Indicates the maximum number of (S, G) entries in the cache when the Router receives the SA message from an MSDP peer. You can configure the maximum number of (S, G) entries in the cache by using the peer sa-cache-maximum command and remove the configuration by using the undo peer sa-cache-maximum command. By default, the number of (S, G) entries in the SA cache is 8192. |
| Input queue size | Indicates the length of the data added to the cache. |
| Output queue size | Indicates the length of the data removed from the cache. |
| Counters for MSDP message | * Count of Reverse Path Forwarding (RPF) check failure: indicates the number of SA messages discarded because of the RPF check failure. * Incoming/outgoing SA messages: indicates the number of sent or received SA messages. * Incoming/outgoing SA requests: indicates the number of sent or received SA-Request messages. * Incoming/outgoing SA responses: indicates the number of sent or received SA-Response messages. * Incoming/outgoing data packets: indicates the number of sent or received SA messages that are encapsulated with multicast data packets. |
| State | MSDP connection status.   * Up: The connection is set up and is in the Up state. * Listen: The connection is set up, and the local device acts as the server that is listening the clients. * Connect: The connection is not set up, and the local device acts as the client that has initiated a connection request. * Shutdown: The MSDP peer is shut down. * Down: The connection fails. |
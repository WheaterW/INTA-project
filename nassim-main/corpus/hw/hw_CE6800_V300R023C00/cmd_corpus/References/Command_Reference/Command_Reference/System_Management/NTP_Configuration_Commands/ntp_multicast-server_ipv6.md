ntp multicast-server ipv6
=========================

ntp multicast-server ipv6

Function
--------

The **ntp multicast-server ipv6** command configures an interface on the local device to send NTP multicast packets. The local device runs in the multicast server mode.

The **undo ntp multicast-server ipv6** command removes the local device from the NTP multicast server mode.

By default, the multicast service is not configured.



Format
------

**ntp multicast-server ipv6** [ *ipv6Addr* ] [ **authentication-keyid** *keyid* | **ttl** *ttl-number* | **port** *portNumber* ] \*

**undo ntp multicast-server ipv6** [ *ipv6Addr* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **authentication-keyid** *keyid* | Specifies a key ID used when sending messages to a multicast client. | The value is an integer ranging from:   * 1 to 4294967295 (version 1 to 3). * 1 to 65535 (version 4). |
| **ttl** *ttl-number* | Specifies the life span of multicast packets. | The value is an integer ranging from 1 to 255. |
| **port** *portNumber* | Specifies the port number to be used as the destination port in NTP multicast packets. | The number is an integer that can be 123, or ranges from 1025 to 65535. The default value is 123. |
| **ipv6** *ipv6Addr* | Specifies an IPv6 address. | The default value is FF0E::0101. |




Views
-----

100GE interface view,10GE interface view,25GE interface view,400GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

You can configure a device to determine whether NTP multicast packets need to be sent through an existing interface to a configured multicast group address or not. Based on this, the local device acts as multicast server and sends multicast messages periodically for time synchronization to multicast clients.

**Precautions**

If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when this command is deleted.

On an IPv6 network, multiple primary IPv6 addresses can be configured for a source interface. By default, the system uses the latest updated IPv6 address as the source address of the NTP multicast server. To ensure that the NTP multicast server can properly receive and process packets from clients, you need to configure this address as the listening source address of the NTP multicast server.If the source interface through which the configuration is delivered is deleted, the NTP multicast server is deleted.

Example
-------

# Configure Vlanif 100 to send NTP IPv6 multicast packets with the multicast address being FF0E::0101 and the ID of the encryption key being 4.
```
<HUAWEI> system-view
[~HUAWEI] ntp authentication-keyid 4 authentication-mode hmac-sha256 YsHsjx_202206
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ipv6 enable
[~HUAWEI-Vlanif100] ntp multicast-server ipv6 FF0E::0101 authentication-keyid 4

```
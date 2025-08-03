ntp manycast-client ipv6
========================

ntp manycast-client ipv6

Function
--------

The **ntp manycast-client ipv6** command enables the NTP manycast client mode.

The **undo ntp manycast-client ipv6** command disables the NTP manycast client configuration.

By default, the manycast client service is disabled.



Format
------

**ntp manycast-client ipv6** [ *ipv6-address* ] [ **authentication-keyid** *key-id* | **ttl** *ttl-number* | **port** *port-number* ] \*

**undo ntp manycast-client ipv6** [ *ipv6-address* ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **authentication-keyid** *key-id* | Specifies an authentication key ID number carried in messages to be sent to manycast clients. | The value is an integer in the range from 1 to 65535. |
| **ttl** *ttl-number* | Specifies the life span of the manycast packet. | The value is an integer ranging from 1 to 255. The default value is 255. |
| **port** *port-number* | Sets the port number to be used as the destination port in NTP manycast packets. | The value is 123 or an integer ranging from 1025 to 65535. The default value is 123. |
| **ipv6** *ipv6-address* | Specifies a manycast IPv6 address. The default value is FF0E:0000:0000:0000:0000:0000:0000:0101. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. By default, it is FF0E::0101. |




Views
-----

100GE interface view,10GE interface view,25GE interface view,400GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

An interface can be specified on the local device and used to send NTP manycast messages after a timeout period elapses. The local device runs in manycast client mode and periodically sends manycast messages to a manycast server. Based on the message sent by the manycast server, a dynamic client-server association is established.

**Precautions**

If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when this command is deleted.

On an IPv6 network, multiple primary IPv6 addresses can be configured for a source interface. By default, the system uses the latest updated IPv6 address as the source address of the NTP manycast server. To ensure that the server can receive and process packets from clients, you need to configure this address as the source address for listening on the NTP server.If the source interface delivered by the configuration is deleted, the NTP manycast client is deleted.

Example
-------

# Configure Vlanif 100 to receive NTP manycast packets with the sending port number being 5000.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[*HUAWEI-Vlanif100] ntp manycast-client ipv6 port 5000

```

# Configure Vlanif 100 to receive NTP manycast packets with the manycast IPv6 address being FF0E::111.
```
<HUAWEI> system-view
[~HUAWEI] ntp authentication-keyid 6 authentication-mode hmac-sha256 YsHsjx_202206
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ipv6 enable
[*HUAWEI-Vlanif100] ntp manycast-client ipv6 FF0E::111 authentication-keyid 6

```
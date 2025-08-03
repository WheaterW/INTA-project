ntp broadcast-server
====================

ntp broadcast-server

Function
--------

The **ntp broadcast-server** command configures the NTP broadcast server mode.

The **undo ntp broadcast-server** command cancels the NTP broadcast server mode.

By default, the broadcast service is not configured.



Format
------

**ntp broadcast-server** [ **authentication-keyid** *key-id* | **version** *version-number* | **port** *port-number* ] \*

**undo ntp broadcast-server**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **authentication-keyid** *key-id* | Specifies an authentication key number used to transmit message to broadcast clients. | The value is an integer ranging from 1 to 4294967295 (version 1 to 3), 1 to 65535 (version 4). By default, no authentication key is configured. |
| **version** *version-number* | Sets an NTP version number. | The value is an integer ranging from 1 to 4. The default value is 3. |
| **port** *port-number* | Specifies the port number to be used as the destination port in the NTP broadcast packet. | The number is an integer that can be 123, or ranges from 1025 to 65535. The default value is 123. |




Views
-----

100GE interface view,10GE interface view,25GE interface view,400GE interface view,Eth-Trunk interface view,Tunnel interface view,VLANIF interface view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

If a device is configured to send NTP broadcast packets through an existing interface, the local device automatically runs a broadcast server to transmit broadcast messages periodically to broadcast clients.

**Precautions**

If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command in the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file.

If the source interface delivered by the configuration is deleted, the NTP broadcast server is deleted.

Example
-------

# Enable Vlanif 100 to send NTP broadcast packets, encrypt the packets with key 4, and set the NTP version number to 3.
```
<HUAWEI> system-view
[~HUAWEI] ntp authentication-keyid 4 authentication-mode hmac-sha256 YsHsjx_202206
[~HUAWEI] vlan batch 100
[*HUAWEI] interface Vlanif 100
[*HUAWEI-Vlanif100] ip address 10.1.1.1 24
[*HUAWEI-Vlanif100] ntp broadcast-server authentication-keyid 4 version 3

```

# Configure Vlanif 100 to send NTP broadcast packets with the destination port number 5000.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ntp broadcast-server port 5000

```
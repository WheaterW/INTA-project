peer(VPN instance MSDP view/MSDP view of a public network instance)
===================================================================

peer(VPN instance MSDP view/MSDP view of a public network instance)

Function
--------



The **peer connect-interface** command configures a Multicast Source Discovery Protocol (MSDP) peer.

The **undo peer** connect-interface command restores the default setting.



By default, no MSDP peers are configured.


Format
------

**peer** *peer-address* **connect-interface** { *interface-type* *interface-number* | *interface-name* }

**undo peer** *peer-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the address of a remote MSDP peer. | The address is in dotted decimal notation. |
| *interface-type* *interface-number* | Specifies the type and number of an interface. The local router uses the primary address of the interface as the source IP address to set up a TCP connection with the remote MSDP peer. | - |
| *interface-name* | Specifies an interface name. | The value is a string of 1 to 63 case-sensitive characters, spaces not supported. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To set up an MSDP peer relationship and a TCP connection between peers, run the **peer connect-interface** command.Running the **peer connect-interface** command is the prerequisites for you to run other **peer** commands.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

You can run the peer peer-address connect-interface port-type port-number command repeatedly to configure multiple MSDP peers for the local router.You can specify the same interface for different parameter peer-address. That is, you can specify the same local interface for different remote peers.

**Precautions**

When configuring a static reverse path forwarding (RPF) peer, you must first run the **peer connect-interface** command to set the remote end as an MSDP peer and then the **static-rpf-peer** command to set the MSDP peer as a static RPF peer.Running the undo peer peer-address command deletes all the configurations related to a specified peer.


Example
-------

# Specify a source interface for sending MSDP packets and a source address for initiating a connection.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 10.10.7.6 connect-interface LoopBack 1

```
shutdown (VPN instance MSDP view/MSDP view of a public network instance)
========================================================================

shutdown (VPN instance MSDP view/MSDP view of a public network instance)

Function
--------



The **shutdown** command terminates a specified Multicast Source Discovery Protocol (MSDP) peer.

The **undo shutdown** command restores the default configuration.



By default, the MSDP peers are not closed after the peer relationship is established.


Format
------

**shutdown** *peer-address*

**undo shutdown** *peer-address*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peer-address* | Specifies the IP address of an MSDP peer. | The address is in dotted decimal notation. |



Views
-----

VPN instance MSDP view,MSDP view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **shutdown** command can be used to close the TCP connection between two MSDP peers whereas keep the MSDP peer relationship.

**Prerequisites**

The multicast routing-enable command has been run in the public network instance view or VPN instance view.The remote peer whose IP address is specified in the command must have set up an MSDP peer relationship with the device.

**Configuration Impact**

After this command is run, MSDP peers no longer transmit Source Active (SA) messages and no longer attempt to establish connections. When you run the display msdp brief or display msdp peer-status command to check the status of MSDP peers, the State field of the MSDP peer that was shut down is Shutdown.

**Precautions**

To restore the connection between MSDP peers, run the undo **shutdown** command to cancel the current shutdown configuration. You do not need to run the peer connect-interface command to reconfigure MSDP peers.


Example
-------

# In the public network instance, close MSDP peer 192.168.1.1
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] interface LoopBack 0
[*HUAWEI-LoopBack0] quit
[*HUAWEI] msdp
[*HUAWEI-msdp] peer 192.168.1.1 connect-interface LoopBack 0
[*HUAWEI-msdp] shutdown 192.168.1.1

```
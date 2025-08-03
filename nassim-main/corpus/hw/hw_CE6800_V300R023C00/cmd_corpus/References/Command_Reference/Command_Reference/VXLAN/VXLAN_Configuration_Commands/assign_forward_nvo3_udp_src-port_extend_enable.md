assign forward nvo3 udp src-port extend enable
==============================================

assign forward nvo3 udp src-port extend enable

Function
--------



The **assign forward nvo3 udp src-port extend enable** command enables a device to use the extension mode to encapsulate the outer UDP source port number of VXLAN packets.

The **undo assign forward nvo3 udp src-port extend enable** command disables a device from using the extension mode to encapsulate the outer UDP source port number of VXLAN packets.



By default, the extension mode is not used when the device encapsulates the outer UDP source port number of VXLAN packets.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H and CE6881H-K.



Format
------

**assign forward nvo3 udp src-port extend enable**

**undo assign forward nvo3 udp src-port extend enable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a device encapsulates the outer header of a VXLAN packet, the UDP source port number is the value calculated using the hash algorithm for the inner packet. The source port number can be used for load balancing on the network. If load balancing based on the UDP source port number is not ideal, you are advised to run this command to set the calculation mode of the UDP source port number to extension mode to improve the load balancing effect on the entire network.


Example
-------

# Enable the device to use the extension mode when encapsulating the outer UDP source port number of VXLAN packets.
```
<HUAWEI> system-view
[~HUAWEI] assign forward nvo3 udp src-port extend enable

```
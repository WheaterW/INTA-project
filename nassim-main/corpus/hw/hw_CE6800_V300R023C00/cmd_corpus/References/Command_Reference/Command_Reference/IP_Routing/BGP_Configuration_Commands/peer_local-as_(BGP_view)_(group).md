peer local-as (BGP view) (group)
================================

peer local-as (BGP view) (group)

Function
--------



The **peer local-as** command enables a device to use a fake AS number to establish a BGP peer relationship with a specified peer.

The **undo peer local-as** command cancels the existing configuration.



By default, a device uses an actual AS number to establish a BGP peer relationship with a peer.


Format
------

**peer** *group-name* **local-as** *local-as-value* [ **dual-as** ] [ **prepend-global-as** ] [ **prepend-local-as** ]

**undo peer** *group-name* **local-as**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *local-as-value* | Specifies an AS number. | For an AS number in integer format, the value ranges from 1 to 4294967295.  For an AS number in dotted notation, it is in the format of x.y, in which x and y are integers, with x ranging from 1 to 65535 and y ranging from 0 to 65535. |
| **dual-as** | Allows the local end to use either the actual AS number or the fake AS number to establish a connection with the peer end. | - |
| **prepend-global-as** | Adds the actual AS number to the AS\_Path in the messages to be sent. | - |
| **prepend-local-as** | Adds the fake AS number to the AS\_Path in received messages. | - |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If the **peer local-as** command is run, without dual-as, prepend-global-as, or prepend-local-as specified, the local end uses only the fake AS number to establish a BGP peer relationship with the specified peer and adds only the fake AS number to the AS\_Path of the routes to be advertised to the peer.The **peer local-as** command is used in a scenario where a carrier modifies network deployment. For example, in a carrier merger and acquisition scenario, if the acquirer's network and the acquiree's network belong to different ASs, BGP peers on the acquiree's network need to be shifted from their original AS to the AS of the acquirer's AS. If the customers of the acquiree do not want their BGP configurations to be changed or do not want them to be changed immediately during the shift, BGP peer relationships may be interrupted for a long time.If a device uses a fake AS number to establish a BGP peer relationship with an EBGP peer or confederation EBGP peer, it performs the following actions before sending routes to the EBGP peer or confederation EBGP peer:

* If prepend-global-as is not specified in the command, the device adds only the fake AS number to the AS\_Path of the routes that match a specified export policy.
* If prepend-global-as is specified in the command, the device adds the fake AS number followed by the global AS number to the AS\_Path of the routes that match a specified export policy.If a device uses a fake AS number to establish a BGP peer relationship with an EBGP peer or confederation EBGP peer, it performs the following actions after receiving routes from the EBGP peer or confederation EBGP peer:
* If prepend-local-as is not specified in the command, the device does not change the AS\_Path of the received routes.
* If prepend-local-as is specified in the command, the device adds the fake AS number to the AS\_Path of the received routes before filtering them using the specified import policy.The **peer local-as** command is valid only for EBGP peers. If the local device uses the actual AS number to establish an EBGP peer relationship with a remote device, the actual AS number is carried in the AS\_Path of the route to be sent to the remote device. If the local device uses the fake AS number to establish the EBGP peer relationship, the fake AS number is carried in the AS\_Path of the route to be sent to the remote device.

**Prerequisites**

Peers have been created using the **peer as-number** command.

**Configuration Impact**

If the peer fake-as command is run several times for a peer or a peer group, the latest configuration will overwrite the previous one.

**Precautions**

If the fake AS number configured on the local end is the same as the peer AS number and dual-as is configured, the peer cannot be added to the peer group. If the fake AS number configured on the local end is the same as the peer AS number and dual-as is not configured, the peer can be added to the peer group. Similarly, if the peer is added to a peer group, the fake AS number configured on the local end must be the same as the peer AS number, and dual-as cannot be configured. Confederation EBGP does not allow the fake AS number configured on the local end to be the same as the peer AS number configured on the peer. If the fake AS number configured on the local end is the same as the peer AS number configured on the peer, EBGP-specific configurations are not allowed. If the fake AS number is deleted, IBGP-specific configurations are not allowed. If the fake AS number configured on the local end is the same as the peer AS number configured on the peer and the dual-as parameter is configured, the type of the established connection may be EBGP or IBGP. Therefore, some IBGP or EBGP configurations may become invalid. Running the **peer local-as** command causes the re-establishment of the peer relationship. After the peer local-as [ dual-as ] [ prepend-global-as ] [ prepend-local-as ] command is run, if the dual-as or prepend-local-as configuration is modified again, the peer relationship is re-established. However, if the prepend-global-as configuration is modified again, the peer relationship is not re-established.A loop occurs in the following scenarios:

* The peer established based on the real AS number receives the route advertised by the peer established based on the fake AS number.
* The peer established based on the fake AS number receives the route advertised by the peer established based on the real AS number.You can configure the prepend-global-as parameter to prevent loops.

Example
-------

# Set a 2-byte fake AS number for a peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test local-as 99

```
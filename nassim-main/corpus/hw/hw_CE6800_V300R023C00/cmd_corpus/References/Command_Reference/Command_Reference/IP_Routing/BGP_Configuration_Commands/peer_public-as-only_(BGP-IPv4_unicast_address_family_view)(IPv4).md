peer public-as-only (BGP-IPv4 unicast address family view)(IPv4)
================================================================

peer public-as-only (BGP-IPv4 unicast address family view)(IPv4)

Function
--------



The **peer public-as-only** command configures the AS-Path attribute in a BGP Update message not to carry the private AS number. Only the public AS number is contained in the update messages.

The **undo peer public-as-only** command allows the AS-Path attribute in a BGP Update message to carry the private AS number.



By default, the AS-Path attribute in a BGP Update message is allowed to carry private AS numbers.


Format
------

**peer** *ipv4-address* **public-as-only**

**peer** *ipv4-address* **public-as-only** **force** [ **replace** ] [ **include-peer-as** ]

**peer** *ipv4-address* **public-as-only** **limited** [ **replace** ] [ **include-peer-as** ]

**undo peer** *ipv4-address* **public-as-only**

**undo peer** *ipv4-address* **public-as-only** **force** [ **replace** ] [ **include-peer-as** ]

**undo peer** *ipv4-address* **public-as-only** **limited** [ **replace** ] [ **include-peer-as** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | It is in dotted decimal notation. |
| **force** | Deletes all private AS numbers from the AS\_Path attribute. The AS\_Path attribute of a specified peer is ignored during the deletion. | - |
| **replace** | Replaces AS numbers with the local AS number.  If both force and replace are specified, all private AS numbers in the AS\_Path list are replaced with the local AS number, and the AS number of the specified peer is ignored during the replacement.  If both limited and replace are specified, the device replaces all private AS numbers in the AS\_Path list with the local AS number from the left, and stops the replacement until the local or public AS number is encountered. During the replacement, the device ignores the AS number of the specified peer. | - |
| **include-peer-as** | Deletes AS numbers.  If both force and include-peer-as are specified, all private AS numbers are forcibly deleted.  If force, replace, and include-peer-as are specified, private AS numbers in the AS\_Path list are replaced with the local AS number.  If both limited and include-peer-as are specified, the AS numbers on the left are deleted, and the deletion stops when the local or public AS number is encountered.  If limited, replace, and include-peer-as are specified at the same time, the private AS numbers in the AS\_Path list are replaced with the local AS number from the leftmost one, and the replacement stops when the local or public AS number is encountered. | - |
| **limited** | Deletes AS numbers from the leftmost one to the local or a public AS number. The AS number of a specified peer is ignored during the deletion. | - |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, AS numbers range from 1 to 4294967295, including public AS numbers, private AS numbers, and reserved AS numbers. If the **private-4-byte-as enable** command is not configured, the private AS number ranges from 64512 to 65534. 65535 is reserved for special applications. After the **private-4-byte-as enable** command is run, private AS numbers range from 64512 to 65534 and from 4200000000 to 4294967294. 65535 and 4294967295 are reserved for special applications.Public AS numbers can be directly used on the Internet. Private AS numbers cannot be directly advertised to the Internet. Otherwise, loops may occur. Therefore, private AS numbers are used only in internal routing domains.You can run this command to process private AS numbers and reserved AS numbers in the AS\_Path attribute of BGP routes as required. The processing of reserved AS numbers is the same as that of private AS numbers. The following describes how to process private AS numbers.If the **peer public-as-only** command is run without any optional parameter and the AS\_Path attribute of BGP routes contains only private AS numbers, BGP deletes these private AS numbers and then advertises the routes. BGP does not delete private AS numbers in the following situations:

* The AS\_Path attribute of a route contains the AS number of the peer. In this case, deleting the private AS number may cause routing loops.
* The AS\_Path list contains both public and private AS numbers. This list indicates that the route has passed through the public network. Deleting the private AS number may cause a forwarding error.To delete or replace private AS numbers in the AS\_Path list, set the following parameters:
* force: indicates that all private AS numbers are directly deleted. The AS numbers of the specified peer group are ignored during the deletion.
* force replace: replaces the private AS number in the AS\_Path list with the local AS number and ignores the AS number of the specified peer group.
* force include-peer-as: deletes all private AS numbers.
* force replace include-peer-as: replaces the private AS numbers in the AS\_Path list with the local AS number. The purpose of replacement is to ensure that the lengths of the AS\_Path lists are the same without affecting the route selection result.
* limited: deletes the AS numbers from the leftmost one until a local or public AS number is found. The AS number of the specified peer is ignored during the deletion.
* limited replace: replaces the private AS numbers in the AS\_Path list from the left with the local AS number until the local or public AS number is found. The AS number of the specified peer group is ignored during the replacement.
* limited include-peer-as: deletes the AS numbers from the leftmost AS number. The purpose is to delete the private AS numbers of the network where the local device resides.
* limited replace include-peer-as: replaces the private AS numbers in the AS\_Path list from the left with the local AS number until the local or public AS number is found.

**Configuration Impact**

If the **peer public-as-only** command is run for a peer group, the peers of the peer group inherit the configuration.

**Precautions**

Analyze the network structure with caution and select proper optional parameters to prevent routing loops or forwarding errors.This command takes effect after an export routing policy is configured.


Example
-------

# Configure a device to remove all private AS numbers from the AS\_Path attribute in the Update messages to be sent to a peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 10.1.1.1 public-as-only

```
ntp access
==========

ntp access

Function
--------



The **ntp access** command sets the access control authority of a local NTP service.

The **undo ntp access** command deletes the access control authority.



By default, no access authority is set.


Format
------

**ntp access** { **peer** | **query** | **server** | **synchronization** | **limited** } { { *acl-number* | **acl-name** *aclname* } [ **ipv6** { *acl6-number* | **acl6-name** *acl6name* } ] | **ipv6** { *acl6-number* | **acl6-name** *acl6name* } [ { *acl-number* | **acl-name** *aclname* } ] }

**undo ntp access** { { **peer** | **query** | **server** | **synchronization** | **limited** } | { **peer** | **query** | **server** | **synchronization** | **limited** } { { *acl-number* | **acl-name** *aclname* } [ **ipv6** { *acl6-number* | **acl6-name** *acl6name* } ] | **ipv6** [ { *acl6-number* | **acl6-name** *acl6name* } | { *acl6-number* | **acl6-name** *acl6name* } { *acl-number* | **acl-name** *aclname* } ] | **all** } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **peer** | Indicates to maximum access. Both time request and control query can be performed on the local NTP service, and the local clock can be synchronized to the remote server.  If the matching result is configured as permit for the source IP address configured in the ACL:   * The local clock can be synchronized with the peer clock. * The peer clock can be synchronized with the local clock. | - |
| **query** | Indicates to minimum access. Only control query can be performed on the local NTP service. | - |
| **server** | Permits server access and query. Both time requests and control query can be performed on the local NTP service, but the local clock cannot be synchronized to the remote server.  If the matching result is configured as permit for the source IP address configured in the ACL:   * The local clock cannot be synchronized with the peer clock. * The peer clock can be synchronized with the local clock. | - |
| **synchronization** | Permits server access only. Only time request can be performed on the local NTP service.  If the matching result is configured as permit for the source IP address configured in the ACL:   * The local clock cannot be synchronized with the peer clock. * The peer clock can be synchronized with the local clock. | - |
| **limited** | Controls the incoming packet rate and kiss code is sent when KoD is enabled. | - |
| *acl-number* | Specifies a basic ACL number for IPv4 addresses. | The value is a string of case-sensitive characters, spaces not supported. The value is an integer ranging from 2000 to 2999. |
| **acl-name** *aclname* | Specifies the name of a named basic ACL. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. The value must start with a digit ranging from 0 to 9 or a letter ranging from a to z (or A to Z). |
| **ipv6** *acl6-number* | Specifies the number of a basic IPv6 ACL. | The value is a string of case-sensitive characters, spaces not supported. The value is an integer ranging from 2000 to 2999. |
| **acl6-name** *acl6name* | Specifies the name of a named basic IPv6 ACL. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. The value must start with a digit ranging from 0 to 9 or a letter ranging from a to z (or A to Z). |
| **all** | Indicates the IP address can be of both IPv6 and IPv4 types. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



Compared with NTP authentication, the **ntp access** command provides a simple security measure. When receiving an access query, the NTP server matches it with peer, server, synchronization, and query in order, that is, from the minimum access restriction to the maximum access restriction. The first match takes priority.



**Precautions**

Based on the access limitation to be implemented, configure this command for devices accordingly. The details are as follows:

* Unicast NTP server/client mode: In this mode, the client cannot be synchronized with the server.
* Unicast NTP server/client mode: In this mode, the server cannot process time synchronization requests from the client.
* NTP peer mode: In this mode, the active peer cannot process time requests.
* NTP peer mode: In this mode, the passive peer cannot process time requests.
* NTP multicast mode: In this mode, the NTP multicast client cannot be synchronized with the server.
* NTP broadcast mode: In this mode, the NTP broadcast client cannot be synchronized with the server.
* NTP manycast mode: In this mode, the NTP manycast client cannot be synchronized with the server.
* NTP manycast mode: In this mode, the NTP manycast server cannot process time synchronization requests from the client.

If this command is the first NTP configuration command, the system automatically adds the ntp server disable and ntp ipv6 server disable commands to the configuration file to disable the NTP server function. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp server disable and ntp ipv6 server disable commands from the configuration file when you delete this command.Before configuring access control using an ACL, check the ACL rule settings.

* If the ACL rule is based on a source IP address and the permit mode is set, packets originating from this address are permitted.
* If the ACL rule is based on a source IP address and the deny mode is set, packets originating from this address are denied.
* If a source IP address does not match the ACL rule, packets originating from this address are denied.
* If no rule exists in the ACL or the referenced ACL does not exist, packets originating from all source IP addresses are denied.


Example
-------

# Enable a peer in IPv4 ACL 2000 to perform time request, query control, and time synchronization on a local device.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] ntp access peer 2000

```
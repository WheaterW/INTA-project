dhcp server bootp
=================

dhcp server bootp

Function
--------

The **dhcp server bootp** command enables the DHCP server to respond to a Bootstrap Protocol (BOOTP) request.

The **undo dhcp server bootp** command disables the DHCP server from responding to a BOOTP request.

By default, a DHCP server responds to a BOOTP request.



Format
------

**dhcp server bootp**

**undo dhcp server bootp**



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

**Usage Scenario**

A DHCP server and a BOOTP server may reside on the same network segment. The BOOTP server assigns static IP addresses to BOOTP clients. As defined in the DHCP protocol, a DHCP server can also respond to BOOTP requests to assign IP addresses to BOOTP clients. BOOTP clients may obtain IP addresses from the DHCP server but not the BOOTP server.

**Prerequisites**

DHCP has been enabled globally using the **dhcp enable** command in the system view.



Example
-------

# Disable the DHCP server to allocate IP addresses to BOOTP clients.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] undo dhcp server bootp

```
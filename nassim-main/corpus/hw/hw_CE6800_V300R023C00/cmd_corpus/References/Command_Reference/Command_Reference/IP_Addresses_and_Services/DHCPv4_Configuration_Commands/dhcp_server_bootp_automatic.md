dhcp server bootp automatic
===========================

dhcp server bootp automatic

Function
--------

The **dhcp server bootp automatic** command enables the DHCP server to dynamically allocate IP addresses to BOOTP clients.

The **undo dhcp server bootp automatic** command disables the DHCP server from dynamically allocating IP addresses to BOOTP clients.

By default, a DHCP server allocates IP addresses to BOOTP clients.



Format
------

**dhcp server bootp automatic**

**undo dhcp server bootp automatic**



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

This command applies to DHCP servers. When BOOTP clients need to obtain their IP addresses, DNS server's IP address, and gateway IP address from a DHCP server, you need to run the **dhcp server bootp automatic** command to enable the DHCP server to dynamically allocate IP addresses to BOOTP clients.

**Prerequisites**

DHCP has been enabled globally using the **dhcp enable** command in the system view.

**Precautions**

When the device functions as the DHCP server, the device can allocate IP addresses to BOOTP clients if the BOOTP clients reside on the same network as the DHCP server. You can run the **dhcp server bootp automatic** command to dynamically allocate IP addresses. You can also run the static-bind command or the dhcp server static-bind command to allocate IP addresses to BOOTP clients in the static binding mode.



Example
-------

# Disable the DHCP server to allocate IP addresses to BOOTP clients.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] undo dhcp server bootp automatic

```
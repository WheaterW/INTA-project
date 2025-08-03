vpn-instance (PKI domain view)
==============================

vpn-instance (PKI domain view)

Function
--------



The **vpn-instance** command adds a PKI to a specified VPN.

The **undo vpn-instance** command unbinds a PKI from a specified VPN.



By default, a PKI does not belong to any VPN.


Format
------

**vpn-instance** *vpn-instance-name*

**undo vpn-instance**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of a VPN instance.  This parameter is supported in the public system only. | The VPN instance name must exist. |



Views
-----

PKI domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

To obtain and verify certificates, the device needs to communicate with the CA server. When the CA server is in a VPN, add the PKI to the specified VPN.


Example
-------

# Add the PKI to the VPN named vrf1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] route-distinguisher 22:1
[*HUAWEI-vpn-instance-vrf1-af-ipv4] quit
[*HUAWEI-vpn-instance-vrf1] quit
[~HUAWEI] pki realm abc
[*HUAWEI-pki-realm-abc] vpn-instance vrf1

```
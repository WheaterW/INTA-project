vpn-instance(PKI cmp session view)
==================================

vpn-instance(PKI cmp session view)

Function
--------

The **vpn-instance** command adds a PKI to a specified VPN.

The **undo vpn-instance** command unbinds a PKI from a specified VPN.

By default, a PKI does not belong to any VPN.



Format
------

**vpn-instance vpn-name** *vpn-instance-name*

**undo vpn-instance**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-name** *vpn-instance-name* | Specifies the name of a VPN instance.  This parameter is supported in the public system only. | The value must be an existing VPN instance name and cannot contain backslashes (\), spaces, double quotation marks ("), single quotation marks ('), asterisks (\*), colons (:), question marks (?), or slashes (/). |




Views
-----

PKI CMP session view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

**Usage Scenario**

To obtain and verify certificates, the device needs to communicate with the CA server. When the CA server is in a VPN, add the PKI to the specified VPN.

**Precautions**

* The VPN instance bound to the interface specified by the **source** command in the CMP session view must be the same as the VPN instance configured in the vpn-instance. If they are inconsistent, either source or vpn-instance, which is configured later, cannot be executed successfully.


Example
-------

# Add the PKI to the VPN named vrf1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vrf1
[*HUAWEI-vpn-instance-vrf1] route-distinguisher 22:1
[*HUAWEI-vpn-instance-vrf1-af-ipv4] quit
[*HUAWEI-vpn-instance-vrf1] quit
[~HUAWEI] pki cmp session ab
[*HUAWEI-pki-cmp-session-ab] vpn-instance vpn-name vrf1

```
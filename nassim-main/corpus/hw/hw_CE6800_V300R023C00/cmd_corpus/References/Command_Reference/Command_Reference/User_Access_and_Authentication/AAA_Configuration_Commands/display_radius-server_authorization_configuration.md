display radius-server authorization configuration
=================================================

display radius-server authorization configuration

Function
--------



The **display radius-server authorization configuration** command displays the configuration of RADIUS authorization servers.




Format
------

**display radius-server authorization configuration**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

This command helps whether the RADIUS authorization server configuration is correct.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of RADIUS authorization servers.
```
<HUAWEI> display radius-server authorization configuration
 ------------------------------------------------------------------------------
 Attribute decode same as template    :  N
 Attribute encode same as template    :  Y
 User information match type          :  all
 Port                                 :  3799
 Bounce port disable                  :  Y                                      
 Down port disable                    :  N 
 ------------------------------------------------------------------------------
 ------------------------------------------------------------------------------
 IP-Address      Shared-key               Group                         Protect
 ------------------------------------------------------------------------------
 10.10.1.114     ****************         -                                  Y
 vpn-instance : -
 ------------------------------------------------------------------------------
 1 RADIUS authorization server(s) in total

```

**Table 1** Description of the **display radius-server authorization configuration** command output
| Item | Description |
| --- | --- |
| Attribute decode same as template | Whether the device parses attributes in the RADIUS dynamic authorization packet based on the configurations in the RADIUS server template. |
| Attribute encode same as template | Whether the device encapsulates attributes in the CoA or DM Response packet based on the configurations in the RADIUS server template. |
| User information match type | Method used by a device to perform a match check between the RADIUS attribute in the received CoA or DM Request packet and user information on the device. The values are as follows:   * all: The device performs a match check between all attributes in the received CoA or DM Request packet and user information on the device. * any: The device performs a match check between an attribute in the received CoA or DM Request packet and user information on the device. |
| Port | Port number of the RADIUS authorization server. |
| Bounce port disable | Whether the function of ignoring the authorization attribute indicating that the port is intermittently interrupted in a CoA packet is disabled. |
| Down port disable | Whether the function of ignoring the authorization attribute indicating that the port is disabled in a CoA packet is disabled. |
| IP-Address | IP address of a RADIUS authorization server. |
| Shared-key | Shared key of the RADIUS authorization server. |
| Group | RADIUS server group matching the RADIUS authorization server. |
| Protect | Whether the security hardening function is enabled. |
| vpn-instance | Name of the bound VPN instance. |
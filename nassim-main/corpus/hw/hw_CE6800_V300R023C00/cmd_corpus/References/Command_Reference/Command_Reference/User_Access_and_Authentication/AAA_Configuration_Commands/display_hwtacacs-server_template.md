display hwtacacs-server template
================================

display hwtacacs-server template

Function
--------



The **display hwtacacs-server template** command displays the configuration of an HWTACACS server template.




Format
------

**display hwtacacs-server template** [ **name** *template-name* [ **verbose** ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **name** *template-name* | Displays the configuration of a specified HWTACACS server template. | The HWTACACS server template must already exist. |
| **verbose** | Displays statistics about the HWTACACS server template. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The command output helps you check the configuration of HWTACACS server templates and isolate faults.

**Precautions**

The device determines whether its communication with the HWTACACS server is normal based on the response timeout mechanism of HWTACACS request packets, and always marks the status of the last HWTACACS server as Up.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configuration of the HWTACACS server template template0.
```
<HUAWEI> display hwtacacs-server template name template0
  ---------------------------------------------------------------------------
  HWTACACS-server template name        : template0
  HWTACACS-server template index        : 0
  Primary-authentication-server        : 1.1.1.1:49 Vrf:a Shared-key:* Status:UP [M]
  Primary-authentication-ipv6-server   : -:0 Vrf:- Status:-
  Primary-authorization-server         : -:0 Vrf:- Status:-
  Primary-authorization-ipv6-server    : -:0 Vrf:- Status:-
  Primary-accounting-server            : -:0 Vrf:- Status:-
  Primary-accounting-ipv6-server       : -:0 Vrf:- Status:-
  Secondary-authentication-server      : -:0 Vrf:- Status:-
  Secondary-authentication-ipv6-server : -:0 Vrf:- Status:-
  Secondary-authorization-server       : -:0 Vrf:- Status:-
  Secondary-authorization-ipv6-server  : -:0 Vrf:- Status:-
  Secondary-accounting-server          : -:0 Vrf:- Status:-
  Secondary-accounting-ipv6-server     : -:0 Vrf:- Status:-
  Third-authentication-server          : -:0 Vrf:- Status:-
  Third-authentication-ipv6-server     : -:0 Vrf:- Status:-
  Third-authorization-server           : -:0 Vrf:- Status:-
  Third-authorization-ipv6-server      : -:0 Vrf:- Status:-
  Third-accounting-server              : -:0 Vrf:- Status:-
  Third-accounting-ipv6-server         : -:0 Vrf:- Status:-
  Current-authentication-server        : 1.1.1.1:49 Vrf:a Shared-key:* Status:UP [M]
  Current-authentication-ipv6-server   : -:0 Vrf:- Status:-
  Current-authorization-server         : -:0 Vrf:- Status:-
  Current-authorization-ipv6-server    : -:0 Vrf:- Status:-
  Current-accounting-server            : -:0 Vrf:- Status:-
  Current-accounting-ipv6-server       : -:0 Vrf:- Status:-
  Source-IP-address                    : -
  Source-LoopBack                      : -
  Source-Vlanif                        : -
  Source-IPv6-address                  : -
  IPv6 Source-LoopBack                 : -
  IPv6 Source-Vlanif                   : -
  Shared-key                           : -
  Quiet-interval(min)                  : 5
  Response-timeout-Interval(sec)       : 5
  Domain-included                      : Original
  Traffic-unit                         : B
  ---------------------------------------------------------------------------

```

**Table 1** Description of the **display hwtacacs-server template** command output
| Item | Description |
| --- | --- |
| HWTACACS-server template name | Name of the HWTACACS server template. |
| Primary-authentication-server | IPv4 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the primary authentication server. |
| Primary-authentication-ipv6-server | IPv6 address, port number, VPN instance, status, and multiplexing mode of the primary authentication server. |
| Primary-authorization-server | IPv4 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the primary authorization server. |
| Primary-authorization-ipv6-server | IPv6 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the primary authorization server. |
| Primary-accounting-server | IPv4 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the primary accounting server. |
| Primary-accounting-ipv6-server | IPv6 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the primary accounting server. |
| Secondary-authentication-server | IPv4 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the second authentication server. |
| Secondary-authentication-ipv6-server | IPv6 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the second authentication server. |
| Secondary-authorization-server | IPv4 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the second authorization server. |
| Secondary-authorization-ipv6-server | IPv6 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the second authorization server. |
| Secondary-accounting-server | IPv4 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the second accounting server. |
| Secondary-accounting-ipv6-server | IPv6 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the second accounting server. |
| Third-authentication-server | IPv4 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the third authentication server. |
| Third-authentication-ipv6-server | IPv6 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the third authentication server. |
| Third-authorization-server | IPv4 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the third authorization server. |
| Third-authorization-ipv6-server | IPv6 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the third authorization server. |
| Third-accounting-server | IPv4 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the third accounting server. |
| Third-accounting-ipv6-server | IPv6 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the third accounting server. |
| Current-authentication-server | IPv4 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the current authentication server. |
| Current-authentication-ipv6-server | IPv6 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the current authentication server. |
| Current-authorization-server | IPv4 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the current authorization server. |
| Current-authorization-ipv6-server | IPv6 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the current authorization server. |
| Current-accounting-server | IPv4 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the current accounting server. |
| Current-accounting-ipv6-server | IPv6 address, port number, VPN instance, status, and whether the multiplexing mode is enabled for the current accounting server. |
| Source-IP-address | Source IPv4 address for communication between the device and the HWTACACS server. |
| Source-LoopBack | Number of the loopback interface. The IPv4 address of the loopback interface is used as the source IPv4 address for communication between the device and the HWTACACS server. |
| Source-Vlanif | Number of a VLANIF interface. The IPv4 address of the VLANIF interface is used as the source IPv4 address for communication between the device and HWTACACS server. |
| Source-IPv6-address | Source IPv6 address for communication between the device and the HWTACACS server. |
| IPv6 Source-LoopBack | Number of the loopback interface. The IPv6 address of the loopback interface is used as the source IPv6 address for communication between the device and the HWTACACS server. |
| IPv6 Source-Vlanif | Number of a VLANIF interface. The IPv6 address of the VLANIF interface is used as the source IPv6 address for communication between the device and HWTACACS server. |
| Shared-key | Shared key of the HWTACACS server. |
| Quiet-interval(min) | Interval for the primary server to return to the active state, in minutes. |
| Response-timeout-Interval(sec) | Response timeout interval of the HWTACACS server, in seconds. |
| Domain-included | Whether the HWTACACS user name contains an authentication domain name.   * Yes: The user name contains the domain name. * No: The user name does not contain the domain name. * Original: The device does not modify the user name entered by the user. |
| Traffic-unit | Traffic unit used by the HWTACACS server, in bytes. |
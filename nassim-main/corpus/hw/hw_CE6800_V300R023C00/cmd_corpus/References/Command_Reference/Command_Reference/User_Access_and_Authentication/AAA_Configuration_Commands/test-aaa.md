test-aaa
========

test-aaa

Function
--------



The **test-aaa** command tests the connectivity between the device and the authentication server or accounting server, and tests whether a user can be authenticated using authentication server and whether the accounting server can charge a user.




Format
------

**test-aaa** *user-name* *user-password* **hwtacacs-template** *template-name* [ **accounting** [ **start** | **realtime** | **stop** ] ]

**test-aaa** *user-name* *user-password* **ldap-template** *template-name*

**test-aaa** *user-name* *user-password* **radius-template** *template-name* [ **chap** | **pap** | **accounting** [ **start** | **realtime** | **stop** ] ] [ **called-station-id** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *user-name* | Specifies a user name. | The value is a string of 1 to 253 case-insensitive characters. When the user name contains spaces, it must be enclosed in double quotation marks (""). |
| *user-password* | Specifies a user password. | The value is a string of 1 to 128 case-sensitive characters. It cannot contain spaces. |
| **radius-template** *template-name* | Specifies the name of a RADIUS server template. | The RADIUS server template must already exist. |
| **chap** | Indicates Challenge Handshake Authentication Protocol (CHAP) authentication.  The NAS device sends the user name, encrypted password, and 16-byte random code to the RADIUS server. The RADIUS server searches for the database according to the user name and obtains the password that is the same as the encrypted password at the user side. The RADIUS server then encrypts the received 16-byte random code and compares the result with the password. If they are the same, the user is authenticated. If they are different, the user fails to be authenticated. In addition, if the user is authenticated, the RADIUS server generates a 16-byte random code to challenge the user. | - |
| **pap** | Indicates Password Authentication Protocol (PAP) authentication.  The NAS device adds the user name and encrypted password to the corresponding fields of authentication request packets, and then sends the packets to the RADIUS server. The NAS device determines whether to allow the user go online based on the result returned by the RADIUS server. | - |
| **accounting** | Indicates accounting. By default, an accounting-start packet is sent. | - |
| **start** | Indicates that the sent packet is an accounting-start packet. | - |
| **realtime** | Indicates that the sent packet is a real-time accounting packet. | - |
| **stop** | Indicates that the sent packet is an accounting-stop packet. | - |
| **hwtacacs-template** *template-name* | Specifies the name of an HWTACACS server template. | The HWTACACS server template must already exist. |
| **ldap-template** *template-name* | Specifies the name of an LDAP server template. | The LDAP server template must already exist. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The **test-aaa** command tests service reachability of the server. The device sends an authentication or accounting request packet to the server. If the server returns an authentication or accounting success packet, the device and server can communicate with each other. If the server's response times out, the device and server cannot communicate with each other.In PAP authentication mode, passwords are transmitted in clear text. In CHAP authentication mode, passwords are transmitted after being encrypted. Both the PAP and CHAP authentication modes pose security risks.

**Prerequisites**

An authentication server template or accounting server template has been created, an authentication server or accounting server has been specified in the authentication server template or accounting server template, and the authentication server or accounting server has been configured.

**Follow-up Procedure**

If the test result indicates that the user fails to be authenticated by using authentication server or the accounting server fails to charge the user, check whether the configuration of the authentication server template and the authentication server is correct, and check the connectivity between the device and the authentication server.

**Precautions**



Before running this command, you only need to create a server template and configure the authentication server.When the user name is enclosed in double quotation marks (""), the double quotation marks ("") are not sent to the LDAP server as a part of the user name during LDAP server detection.When the user name is enclosed in double quotation marks (""), the double quotation marks ("") are sent to the RADIUS or HWTACACS server as a part of the user name during RADIUS or HWTACACS server detection.




Example
-------

# Test whether the user user1 can be authenticated using CHAP authentication in the RADIUS server template huawei.
```
<HUAWEI> test-aaa user1 YsHsjx_202206 radius-template huawei chap

```
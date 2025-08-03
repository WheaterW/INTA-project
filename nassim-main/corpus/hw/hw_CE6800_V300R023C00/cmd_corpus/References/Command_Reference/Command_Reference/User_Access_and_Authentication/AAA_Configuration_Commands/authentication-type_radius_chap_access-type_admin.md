authentication-type radius chap access-type admin
=================================================

authentication-type radius chap access-type admin

Function
--------



The **authentication-type radius chap access-type admin** command replaces PAP authentication with CHAP authentication when RADIUS authentication is performed on administrators.

The **undo authentication-type radius chap access-type admin** command restores PAP authentication when RADIUS authentication is performed on administrators.



By default, PAP authentication is used when RADIUS authentication is performed on administrators.


Format
------

**authentication-type radius chap access-type admin** [ **ftp** | **ssh** | **telnet** | **terminal** | **http** | **md-cli** | **snmp** ] \*

**undo authentication-type radius chap access-type admin**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ftp** | Replaces PAP authentication with CHAP authentication when RADIUS authentication is performed on administrators who access the device using FTP. | - |
| **ssh** | Replaces PAP authentication with CHAP authentication when RADIUS authentication is performed on administrators who access the device using SSH. | - |
| **telnet** | Replaces PAP authentication with CHAP authentication when RADIUS authentication is performed on administrators who access the device using Telnet. | - |
| **terminal** | Replaces PAP authentication with CHAP authentication when RADIUS authentication is performed on administrators who access the device using a terminal. | - |
| **http** | Replaces PAP authentication with CHAP authentication when RADIUS authentication is performed on administrators who access the device using HTTP. | - |
| **md-cli** | Replaces PAP authentication with CHAP authentication when RADIUS authentication is performed on administrators who access the device using MD-CLI. | - |
| **snmp** | Replaces PAP authentication with CHAP authentication when RADIUS authentication is performed on administrators who access the device using SNMP. | - |



Views
-----

Authentication scheme view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

CHAP is ciphertext authentication protocol. During CHAP authentication, the NAS device sends the user name, encrypted password, and 16-byte random code to the RADIUS server. The RADIUS server searches for the database according to the user name and obtains the password that is the same as the encrypted password at the user side. The RADIUS server then encrypts the received 16-byte random code and compares the result with the password. If they are the same, the user is authenticated. If they are different, the user fails to be authenticated. In addition, if the user is authenticated, the RADIUS server generates a 16-byte random code to challenge the user. CHAP is more secure and reliable than PAP. If no parameter is specified when you run the **authentication-type radius chap access-type admin** command, the configuration takes effect for all types of administrators that can be configured. When the device is connected to the RADIUS server that supports CHAP authentication, this function needs to be configured.In PAP authentication mode, passwords are transmitted in clear text. In CHAP authentication mode, passwords are encrypted for transmission. Both the PAP and CHAP authentication modes pose security risks.

**Precautions**



After the FIPS mode is enabled, the command becomes unavailable.




Example
-------

# Replace PAP authentication with CHAP authentication when RADIUS authentication is performed on administrators who access the device using FTP.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] authentication-scheme scheme1
[*HUAWEI-aaa-authen-scheme1] authentication-type radius chap access-type admin ftp

```
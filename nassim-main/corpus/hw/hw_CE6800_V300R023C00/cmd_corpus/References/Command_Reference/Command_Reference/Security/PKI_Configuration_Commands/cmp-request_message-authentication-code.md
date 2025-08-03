cmp-request message-authentication-code
=======================================

cmp-request message-authentication-code

Function
--------



The **cmp-request message-authentication-code** command configures the reference value and secret value of the message authentication code (MAC).

The **undo cmp-request message-authentication-code** command deletes the reference value and secret value of the MAC.



By default, the reference value and secret value of the MAC are not configured.


Format
------

**cmp-request message-authentication-code** *reference-value* [ *secret-value* ]

**undo cmp-request message-authentication-code**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *reference-value* | Specifies the reference value of the MAC. | The value is a string of 1 to 128 case-sensitive characters without spaces or question marks (?). The character string can contain spaces if it is enclosed with double quotation marks (""). |
| *secret-value* | Specifies the secret value of the MAC. | The length of the plaintext ranges from 1 to 128. The length of the encrypted ciphertext ranges from 128 to 268. The value is a case-sensitive character string without question marks. |



Views
-----

PKI CMP session view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When a device is configured to use MAC for initial request (IR), you need to check the reference value and secret value of the MAC from the CMPv2 server in out-of-band mode, and then run this command to set the values on the device.If you directly specify the reference value and secret value of the MAC when running the **cmp-request message-authentication-code** command, you do not need to enter the secret value of the MAC again. If you only specify the reference value of the MAC when running this command, you need to enter the secret value of the MAC twice.


Example
-------

# Configure the reference value and secret value of the MAC.
```
<HUAWEI> system-view
[~HUAWEI] pki cmp session test
[*HUAWEI-pki-cmp-session-test] cmp-request message-authentication-code YsHsjx_202206 YsHsjx_202206
[*HUAWEI-pki-cmp-session-test] quit
[~HUAWEI] pki cmp session test1
[*HUAWEI-pki-cmp-session-test1] cmp-request message-authentication-code YsHsjx_202206
Please enter the password:
Please enter the password again:
[*HUAWEI-pki-cmp-session-test1]

```
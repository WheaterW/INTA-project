hwtacacs-server shared-key
==========================

hwtacacs-server shared-key

Function
--------

The **hwtacacs-server shared-key** command configures the shared key of an HWTACACS server.

The **undo hwtacacs-server shared-key** command deletes the shared key of an HWTACACS server.

By default, no shared key of an HWTACACS server is configured.



Format
------

**hwtacacs-server shared-key cipher** *key-string*

**undo hwtacacs-server shared-key**



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *key-string* | Specifies the shared key of an HWTACACS server. | The value is a string of 1 to 255 case-sensitive characters in plaintext or a string of 128 to 428 case-sensitive characters in ciphertext. The string can contain spaces if it is enclosed in double quotation marks ("). |
| **cipher** | Indicates the shared key in cipher text. | - |




Views
-----

HWTACACS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

The shared key is used to encrypt the password and generate the response authenticator.

When exchanging authentication packets with an HWTACACS server, the device encrypts important data such as the password to ensure security of data transmission over the network. The device and HWTACACS server must use the same key to ensure their validity in the authentication.

**Precautions**

When HWTACACS authentication is used, you must configure the shared key of the HWTACACS server.

For security purposes, it is recommended that the shared key contain at least two types of the following characters: lowercase letters, uppercase letters, digits, and special characters. In addition, the shared key must contain at least 16 characters.You can modify this configuration only when the HWTACACS server template is not in use.

Example
-------

# Set the shared key of the HWTACACS server to YsHsjx\_202206YsHsjx\_202206 in cipher text.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template test1
[*HUAWEI-hwtacacs-test1] hwtacacs-server shared-key cipher YsHsjx_202206YsHsjx_202206

```
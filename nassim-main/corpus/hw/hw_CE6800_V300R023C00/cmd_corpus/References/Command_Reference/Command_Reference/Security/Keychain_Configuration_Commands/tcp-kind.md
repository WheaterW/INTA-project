tcp-kind
========

tcp-kind

Function
--------



Using the **tcp-kind** command, you can specify the option type to be used while sending packets with TCP Enhanced Authentication option.

Using the **undo tcp-kind** command, you can restore the TCP kind value to default.



By default, it is 254.


Format
------

**tcp-kind** *kind-value*

**undo tcp-kind**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *kind-value* | Specifies the TCP kind value to be used for that keychain. | The value ranges from 28 to 255. |



Views
-----

Keychain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



A keychain ensures a secure protocol packet transmission by changing the authentication algorithm and key dynamically. Packets to be transmitted over non-TCP and TCP connections are authenticated using the authentication and encryption algorithms corresponding to a key ID. The two connections differ in that the TCP connection needs to be authenticated to enhance the security.TCP connection request packets carry enhanced authentication options and are authenticated by a specified authentication algorithm. At present, different vendors use different kind values to specify the enhanced authentication option. Kind values configured for two communication devices must be identical.



**Prerequisites**



Two communication devices with the keychain authentication mode establish a TCP connection.



**Follow-up Procedure**



If TCP connection request packets carry enhanced authentication options, the kind value must be specified in the packets.



**Precautions**



When applications use enhanced TCP authentication options during authentication interaction, packets must carry a TCP kind value.




Example
-------

# Configure the TCP kind value as 252 for the keychain abc.
```
<HUAWEI> system-view
[~HUAWEI] keychain abc mode absolute
[*HUAWEI-keychain-abc] tcp-kind 252

```
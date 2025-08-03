ca-name
=======

ca-name

Function
--------



The **ca-name** command configures the name of the CA in the PKI realm.

The **undo ca-name** command removes the name of the CA in the PKI realm.



By default, a PKI realm does not have a CA name.


Format
------

**ca-name** { *ca-name* | **from-certificate** **filename** *file-name* }

**undo ca-name**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ca-name** *ca-name* | Specifies the name of the CA. | The value is a string of 1 to 255 case-sensitive characters, spaces not supported. If the string is enclosed in double quotation marks ("), spaces are allowed in the string. |
| **from-certificate** | Specifies the name of the CA certificate file through which the CA name is obtained. | - |
| **filename** *file-name* | Specifies the name of the CA certificate file through which the CA name is obtained. | It is a string of 1 to 64 characters and case insensitive, and the CA certificate must have been imported to the realm. |



Views
-----

PKI domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

After the CA name is specified in the PKI realm, associate the PKI realm with the specified CA. By using the CA name, you can determine the corresponding PKI realm and the check mode for the certificate revocation status.You can directly specify the CA name by running the **ca-name name-string** command. Ensure that the CN, O, and OU in the CA name are in the same sequence as those in the subject name. Alternatively, you can obtain the CA name from the CA certificate by running the **ca-name from-certificate filename file-name** command. This avoids errors caused by manual operation.


Example
-------

# For the PKI realm test, set the CA name to "CN=CA".
```
<HUAWEI> system-view
[~HUAWEI] pki realm test
[*HUAWEI-pki-realm-test] ca-name "CN=CA"

```
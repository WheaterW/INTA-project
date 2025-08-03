display pki credential-storage-path
===================================

display pki credential-storage-path

Function
--------



The **display pki credential-storage-path** command displays the default path where a PKI certificate is stored.



By default, the certificates of the system is stored in the "flash:/pki/public" directory.


Format
------

**display pki credential-storage-path**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



The display pki credential-storage-path command displays the default path where a PKI certificate is stored.You can also run the **cd pki** and **dir** commands in the user view in sequence to view the path where a PKI certificate is stored. An example is as follows:cd pkidirDirectory of flash:/pki/

Idx Attr Size(Byte) Date Time FileName0 drw- - Jul 06 2017 16:11:48 public //Directory in the system




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the default path where a PKI certificate is stored in the public system.
```
<HUAWEI> display pki credential-storage-path
 The pki credential-storage-path is flash:/pki/public.

```

**Table 1** Description of the **display pki credential-storage-path** command output
| Item | Description |
| --- | --- |
| The pki credential-storage-path | Path where a PKI certificate is stored. |
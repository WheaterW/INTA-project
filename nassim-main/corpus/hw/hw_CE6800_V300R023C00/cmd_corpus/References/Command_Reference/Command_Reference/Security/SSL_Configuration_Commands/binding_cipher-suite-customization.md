binding cipher-suite-customization
==================================

binding cipher-suite-customization

Function
--------



The **binding cipher-suite-customization** command configures a name for the SSL cipher suite bound to an SSL policy.

The **undo binding cipher-suite-customization** command deletes the name configured for the SSL cipher suite bound to an SSL policy.



By default, no name is configured for the SSL cipher suite bound to an SSL policy.


Format
------

**binding cipher-suite-customization** *customization-name*

**undo binding cipher-suite-customization** [ *customization-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *customization-name* | Specifies the name of an SSL cipher suite bound to an SSL policy. | The value is a string of 1 to 32 case-insensitive characters, spaces not supported. |



Views
-----

SSL policy view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

During client and server authentication, an algorithm list is provided for the client and server to perform SSL algorithm negotiation. To configure a name for the SSL cipher suite bound to an SSL policy, run the binding cipher-suite-customization command. If no SSL cipher suite is bound to an SSL policy, all the available algorithms can be used by default.

**Prerequisites**

* An SSL cipher suite has been created using the **ssl cipher-suite-list** command.
* The encryption algorithm supported by an SSL cipher suite has been configured using the **set cipher-suite** command.

**Precautions**

An SSL policy can bind only one SSL cipher suite.


Example
-------

# Configure test as the name of the SSL cipher suite bound to an SSL policy.
```
<HUAWEI> system-view
[~HUAWEI] ssl policy test
[*HUAWEI-ssl-policy-test] binding cipher-suite-customization test

```
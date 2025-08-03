peer-public-key end
===================

peer-public-key end

Function
--------



The **peer-public-key end** command enables the system to return to the system view from the public key view.



By default, no peer-public-key is configured.


Format
------

**peer-public-key end**


Parameters
----------

None

Views
-----

DSA public key view,ECC public key view,Public key view,sm2 public key view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

After a public key is configured, you can run the peer-public-key end command to return to the system view from the public key view.


Example
-------

# Return to the system view.
```
<HUAWEI> system-view
[~HUAWEI] rsa peer-public-key test
Enter "RSA public key" view, and you can return the system view with "peer-public-key end".
[*HUAWEI-rsa-public-key] peer-public-key end
[*HUAWEI]

```
clear master-key (User view)
============================

clear master-key (User view)

Function
--------



The **clear master-key** command deletes historical system master key.




Format
------

**clear master-key**


Parameters
----------

None

Views
-----

User view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

In an actual network environment, the network and devices are provided and maintained by network providers, and the data belongs to tenants. To provide secure data transmission and storage on the network, ensure that keys are under complete control of the specific tenant and cannot be obtained by network providers or other tenants. To be specific, tenants need to have their own key management schemes. Tenants can manually clear historical system master keys based on actual requirements to enhance data security and reliability.

**Precautions**

* The **clear master-key** command clears only historical automatically generated and user-defined master keys.
* After historical system master keys are cleared, only the configuration files generated using the current master key can be decrypted. For example, three system master keys A, B, and C are saved on the device, which correspond to three configuration files A.cfg, B.cfg, and C.cfg respectively. A and B are historical master keys, and C is the currently effective master key.
  + Before the **clear master-key** command is run, system master keys A, B, and C are saved on the device. In this case, the configuration files A.cfg and B.cfg generated using the historical master keys and the configuration file C.cfg generated using the current master key can be decrypted and used normally.
  + After the **clear master-key** command is run, the device saves only system master key C. In this case, the configuration files A.cfg and B.cfg generated using historical master keys cannot be decrypted or used. Only the configuration file C.cfg generated using the current master key can be decrypted and used normally.


Example
-------

# Clear historical system master keys.
```
<HUAWEI> clear master-key
Enter the user password:                                                        
Warning: This operation will delete all historical master keys. Are you sure you want to perform it? [Y/N]:y                                                    
Info: Operating, please wait for a moment...done.
Info: Operation succeeded.

```
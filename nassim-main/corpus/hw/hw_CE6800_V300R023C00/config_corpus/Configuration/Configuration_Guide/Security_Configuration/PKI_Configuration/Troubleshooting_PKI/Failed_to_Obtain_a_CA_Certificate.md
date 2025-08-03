Failed to Obtain a CA Certificate
=================================

Failed to Obtain a CA Certificate

#### Fault Symptom

A CA certificate has been manually obtained but does not exist in the device storage. The cause is that the configuration for CA certificate download using LDAP is incorrect.


#### Procedure

* Check whether the configuration for CA certificate download using LDAP is correct. If not, correct the configuration by running the [**pki ldap-server-template**](cmdqueryname=pki+ldap-server-template) *template-name* **attribute** *attr-value* *save-name* **dn** *dn-value* command.
Configuring Certificate Attribute-based Filtering to Implement Access Control
=============================================================================

Configuring Certificate Attribute-based Filtering to Implement Access Control

#### Context

Certificate attribute-based filtering is a method of certificate authentication. Configuring a certificate attribute-based access control policy allows only the certificates that meet specific attribute conditions to pass authentication, thereby implementing refined access control.

A certificate attribute-based access control policy consists of one or more certificate attribute groups, certificate attribute conditions, and certificate attribute-based control rules. The certificate attribute conditions are defined in the certificate attribute group. When a certificate matches all certificate attribute conditions, the configured certificate attribute-based control rule determines whether to permit the certificate.

The following table lists the certificate attribute conditions.

| Certificate Attribute Condition | Description |
| --- | --- |
| Start time and end time of the certificate validity period | Start time and end time of the validity period for the PKI entity's local certificate |
| FQDN | FQDN of the PKI entity's local certificate  An FQDN consists of a host name and a domain name, for example, www.example.com. |
| Certificate IP address | IP address of the PKI entity's local certificate |
| Certificate issuer name | Name of the issuer of the PKI entity's local certificate |
| Certificate subject name | Subject name of the PKI entity's local certificate |

A certificate attribute-based control rule contains two actions: permit and deny. This rule determines whether to permit or block certificates that meet the certificate attribute conditions.

The matching principles for access control through certificate attribute-based filtering are as follows:

* If a service has a specified certificate attribute-based access control policy, the specified certificate attribute-based access control policy is used. Otherwise, the default certificate attribute-based access control policy is used. By default, the action in the default policy is permit. That is, the certificate is allowed to pass authentication.
* If a certificate attribute-based access control policy contains multiple control rules with the OR relationship, the action in the policy is taken as long as the certificate to be authenticated matches one rule.
* If a certificate attribute group contains multiple certificate attribute conditions with the AND relationship, the action in the corresponding control rule is taken when the certificate to be authenticated matches all conditions.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the default certificate attribute-based access control policy.
   
   
   ```
   [pki certificate access-control-policy default](cmdqueryname=pki+certificate+access-control-policy+default) { deny | permit }
   ```
   
   
   
   By default, the action in the default policy is permit. That is, the certificate is allowed to pass authentication.
3. Enter the certificate attribute group view. If no certificate attribute group exists, create one first.
   
   
   ```
   [pki certificate attribute-group](cmdqueryname=pki+certificate+attribute-group) group-name
   ```
4. Configure certificate attribute conditions.
   
   
   
   | To... | Run... |
   | --- | --- |
   | Configure the start time and end time of the certificate validity period | [**attribute**](cmdqueryname=attribute) *id* **validity from** *begintime begindate*  **to** *endtime enddate* |
   | Configure the FQDN | [**attribute**](cmdqueryname=attribute) *id* **alt-subject-name** **fqdn** { **ctn** | **equ** | **nctn** | **nequ** } *attribute-value* |
   | Configure the certificate IP address | [**attribute**](cmdqueryname=attribute) *id* **alt-subject-name** **ip** { **ctn** | **equ** | **nctn** | **nequ** } *ip-address* |
   | Configure the certificate issuer name | [**attribute**](cmdqueryname=attribute) *id* **issuer-name** **dn** { **ctn** | **equ** | **nctn** | **nequ** } *attribute-value* |
   | Configure the certificate subject name | [**attribute**](cmdqueryname=attribute) *id* **subject-name** **dn** { **ctn** | **equ** | **nctn** | **nequ** } *attribute-value* |
5. Return to the system view.
   
   
   ```
   quit
   ```
6. Enter the certificate attribute-based access control policy view. If no certificate attribute-based access control policy exists, create one first.
   
   
   ```
   [pki certificate access-control-policy name](cmdqueryname=pki+certificate+access-control-policy+name) policy-name
   ```
   
   
   
   By default, no certificate attribute-based access control policy is created.
7. Configure a certificate attribute-based control rule.
   
   
   ```
   [rule](cmdqueryname=rule) id { permit | deny } group-name
   ```
   
   
   
   By default, no certificate attribute-based control rule is configured.
8. Configure the description of the certificate attribute-based access control policy.
   
   
   ```
   [description](cmdqueryname=description) description
   ```
   
   
   
   By default, a certificate attribute-based access control policy does not have a description.
9. Adjust the sequence of certificate attribute-based control rules.
   
   
   ```
   [pki certificate access-control-policy](cmdqueryname=pki+certificate+access-control-policy) [ policy-name policy-name ] rule move rule-id1 { before | after } rule-id2
   ```
   
   
   
   When you adjust the sequence of such rules, the sequence of rule IDs (*rule-id*) is unchanged, but the rule contents are swapped. For example:
   
   The certificate attribute-based access control policy **a** has the following rules:
   
   ```
   pki certificate access-control-policy name a
    rule 5 permit test1
    rule 20 permit test2
   ```
   
   After the **pki certificate access-control-policy policy-name a rule move 20 before 5** command is executed, the rules are changed as follows:
   
   ```
   pki certificate access-control-policy name a
    rule 5 permit test2
    rule 20 permit test1
   ```
10. Exit the certificate attribute-based access control policy view.
    
    
    ```
    [quit](cmdqueryname=quit)
    ```
11. Commit the configuration.
    
    
    ```
    [commit](cmdqueryname=commit)
    ```

#### Verifying the Configuration

* Run the [**display pki certificate access-control-policy**](cmdqueryname=display+pki+certificate+access-control-policy) **all** command in the user view to check information of all the access control policies.
* Run the [**display pki certificate attribute-group**](cmdqueryname=display+pki+certificate+attribute-group) **all** command in the user view to check information about all certificate attribute groups.
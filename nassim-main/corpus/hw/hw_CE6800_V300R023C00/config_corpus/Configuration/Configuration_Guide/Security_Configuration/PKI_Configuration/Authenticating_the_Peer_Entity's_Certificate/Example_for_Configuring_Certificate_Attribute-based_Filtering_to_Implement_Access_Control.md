Example for Configuring Certificate Attribute-based Filtering to Implement Access Control
=========================================================================================

Example for Configuring Certificate Attribute-based Filtering to Implement Access Control

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563766337__fig_dc_cfg_pki_004001), DeviceA functions as the gateway of network C (an enterprise network). DeviceA and those on networks A and B authenticate each other using certificates. Devices on networks A and B can set up connections with DeviceA and access resources on network C after successful certificate authentication.

A certificate attribute-based access control policy is required to allow certificates with the following certificate attributes to pass authentication:

* The certificate issuer name is **networkb\_ca**.
* The certificate subject name is **cert\_ca**.

**Figure 1** Network diagram of configuring certificate attribute-based filtering to implement access control  
![](figure/en-us_image_0000001513046042.png)
![](public_sys-resources/note_3.0-en-us.png) 

This example provides only the configurations related to certificate attribute-based access control policies.



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a certificate attribute group and specify the attributes issuer name and subject name.
2. Create a certificate attribute-based access control policy and allow certificates matching the specified attributes to pass authentication.

#### Procedure

1. Configure the action in the default certificate attribute-based access control policy to deny, indicating that certificates matching specified certificate attributes are not allowed to pass authentication.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] pki certificate access-control-policy default deny
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
2. Create a certificate attribute group named **group**.
   
   
   ```
   [~DeviceA] pki certificate attribute-group group
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
3. Specify the issuer name **networkb\_ca** and subject name **cert\_ca**.
   
   
   ```
   [~DeviceA-pki-attribute-group] attribute 1 issuer-name dn equ networkb_ca
   [*DeviceA-pki-attribute-group] attribute 2 subject-name dn equ cert_ca
   [*DeviceA-pki-attribute-group] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
4. Create a certificate attribute-based access control policy named **policy**.
   
   
   ```
   [~DeviceA] pki certificate access-control-policy name policy
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
5. Configure a certificate attribute-based control rule, allowing certificates matching the specified attributes in the certificate attribute group to pass the authentication.
   
   
   ```
   [~DeviceA-pki-access-policy] rule 1 permit group
   [*DeviceA-pki-access-policy] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

After the configurations are complete, only devices whose certificate issuer name is **networkb\_ca** and subject name is **cert\_ca** can set up an tunnel with DeviceA.


#### Configuration Scripts

```
#
sysname DeviceA
#
pki certificate access-control-policy default deny
#
pki certificate attribute-group group                                           
 attribute 1 issuer-name dn equ networkb_ca                                     
 attribute 2 subject-name dn equ cert_ca                                        
#                                                                               
pki certificate access-control-policy name policy                               
 rule 1 permit group                                                            
#
return
```
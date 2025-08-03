Overview of LDAP
================

Overview of LDAP

#### Definition

Lightweight Directory Access Protocol (LDAP) is a directory access protocol based on the TCP/IP protocol suite. LDAP is used to store the data that is not frequently changed, for example, email addresses and contact list. LDAP defines multiple operations, for example, the bind and search operations for user authentication and authorization. The bind and search operations of LDAP are carried out based on the client/server model. All directory information is stored on the LDAP server. LDAP does not support accounting.


#### LDAP Directory

In [Figure 1](#EN-US_CONCEPT_0000001513155626__fig_dc_fd_ldap_000101), the LDAP directory is tree-structured and consists of multiple entries. Each entry has a uniquely identified distinguished name (DN). LDAP carries out the bind and search operations based on DNs to implement user authentication and authorization.

* DC: Domain controller. It indicates the domain to which an object belongs. In general, one LDAP server is a domain controller.
* DN: Distinguished name. It indicates the location of an object on the AD or LDAP server. It starts from the object, to its upper-layers, until the root node. In [Figure 1](#EN-US_CONCEPT_0000001513155626__fig_dc_fd_ldap_000101), the DN of User1 in the directory is **CN=User1, OU=R&D, OU=People, dc=huawei, dc=com**.
* Base DN: DN of the root node. In [Figure 1](#EN-US_CONCEPT_0000001513155626__fig_dc_fd_ldap_000101), the Base DN is **dc=huawei, dc=com**.
* OU: Organization unit. It indicates the organization to which an object belongs. OUs are stored in a tree structure. An OU can contain OUs. In [Figure 1](#EN-US_CONCEPT_0000001513155626__fig_dc_fd_ldap_000101), User1 belongs to the OU **OU=R&D, OU=People**.
* CN: Common name. It indicates the object name. In [Figure 1](#EN-US_CONCEPT_0000001513155626__fig_dc_fd_ldap_000101), **CN=User1** is the object name.

**Figure 1** LDAP directory structure  
![](figure/en-us_image_0000001513035774.png)
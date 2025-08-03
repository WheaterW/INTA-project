Overview of Service Diagnosis
=============================

Overview of Service Diagnosis

#### Definition

Service diagnosis is a means of obtaining service information about specific users.


#### Purpose

On live networks, faults that occur during user access are difficult to locate by using debugging information. This is because debugging information about a specific user cannot be displayed when multiple users go online or offline simultaneously. The service diagnosis function is introduced to address this, as it allows maintenance personnel to obtain service information of specific users.

With service diagnosis, maintenance personnel can create a diagnosis object in the CLI. When a user matching the attributes of the diagnosis object goes online, the device automatically creates a diagnosis instance for the user, and monitors and exports information including status changes and protocol processing results during user access.

A diagnosis object is a set of users with the same attributes, for example, all users on a particular interface. Diagnosis objects can be defined based on the following attributes: physical interface number, VLAN ID, access mode, user name, IP address, and MAC address. A diagnosis instance is created for a single user based on the matching diagnosis object.

Currently, the device supports service diagnosis for Dynamic Host Configuration Protocol (DHCP). During service diagnosis, the device can export complete key information exchanged between modules during user access. The information helps maintenance personnel know about service implementation and troubleshoot service faults. [Table 1](#EN-US_CONCEPT_0000001512837654__table_01) describes key information exported during service diagnosis.

**Table 1** Key information exported during service diagnosis
| Service | | Key Information |
| --- | --- | --- |
| DHCP | DHCP server | Key information sent from DHCP servers during IP address allocation, release, and lease renewal. |
| DHCP client | Key information sent from DHCP clients during IP address request, release, lease renewal, and conflict. |
| DHCP relay agent | Key information exchanged between DHCP clients and servers during IP address request, release, and lease renewal. |
Configuring Default Microsegmentation Policies
==============================================

Configuring Default Microsegmentation Policies

#### Context

On a network, servers can be deployed in EPGs as needed. The servers that do not belong to any EPG are unknown EPG members and the servers that belong to EPGs are EPG members. Multiple servers can belong to the same EPG.

After EPGs are deployed, if no GBP is specified for the EPGs, the device uses the default policy to perform access control for servers. Based on EPG member roles of servers, the default microsegmentation policies include [configuring an access control policy for unknown EPG members](#EN-US_TASK_0000001563754857__step_unknown), [configuring the default access control policy for EPG members](#EN-US_TASK_0000001563754857__step_default), and [configuring the default access control policy for members in an EPG](#EN-US_TASK_0000001563754857__step_same).


#### Procedure

* Configure an access control policy for unknown EPG members. (This policy contains access control policies for unknown members and EPG members.)
  1. Enter the system view.
     
     
     ```
     system-view
     ```
  2. Configure an access control policy for unknown EPG members.
     
     
     ```
     [traffic-segment unknown-segment](cmdqueryname=traffic-segment+unknown-segment) { permit | deny }
     ```
     
     By default, the access control policy for unknown EPG members is permit; that is, unknown EPG members can communicate with each other.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the default access control policy for EPG members.
  1. Enter the system view.
     
     
     ```
     system-view
     ```
  2. Configure the default access control policy for EPG members.
     
     
     ```
     [traffic-segment default-policy](cmdqueryname=traffic-segment+default-policy) { permit | deny }
     ```
     
     By default, the access control policy for EPG members is deny.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure the default access control policy for members in an EPG.
  1. Enter the system view.
     
     
     ```
     system-view
     ```
  2. Configure the default access control policy for members in an EPG.
     
     
     ```
     [traffic-segment same-segment](cmdqueryname=traffic-segment+same-segment) { none | permit | deny }
     ```
     
     
     
     By default, the default access control policy for members in an EPG is none; that is, access control is not performed for members in an EPG. In this case, the device performs access control for members in the EPG according to the default access control policy.
  3. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
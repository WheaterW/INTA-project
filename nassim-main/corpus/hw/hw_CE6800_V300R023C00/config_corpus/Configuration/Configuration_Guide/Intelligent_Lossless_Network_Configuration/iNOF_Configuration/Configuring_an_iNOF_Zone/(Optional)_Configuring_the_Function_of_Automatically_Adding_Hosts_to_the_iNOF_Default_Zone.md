(Optional) Configuring the Function of Automatically Adding Hosts to the iNOF Default Zone
==========================================================================================

(Optional) Configuring the Function of Automatically Adding Hosts to the iNOF Default Zone

#### Context

An iNOF system has a default zone that does not support manual addition of hosts as zone members. The function of automatically adding hosts to the default zone is enabled by default, which allows newly connected SNSD-enabled hosts to be automatically added to the default zone as zone members. To save network and storage resources, disable this function.

![](public_sys-resources/note_3.0-en-us.png) 

* If the IP address of a host has been manually added to an iNOF customized zone using the [**host**](cmdqueryname=host) command, the host will not be automatically added to the default zone as a zone member.
* If the device is configured as an iNOF client, the locally configured function of automatically adding hosts to the default zone does not take effect. Instead, the configuration synchronized from the iNOF reflector takes effect.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the AI service and enter the AI service view.
   
   
   ```
   [ai-service](cmdqueryname=ai-service)
   ```
   
   By default, the AI service is disabled.
3. Enable iNOF and enter the iNOF view.
   
   
   ```
   [inof](cmdqueryname=inof)
   ```
   
   By default, iNOF is disabled.
4. Enable the function for automatically adding hosts to the iNOF default zone.
   
   
   ```
   [default-zone enable](cmdqueryname=default-zone+enable)
   ```
   
   By default, the function for automatically adding hosts to the iNOF default zone is enabled.
5. Exit the iNOF view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
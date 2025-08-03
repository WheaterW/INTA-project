(Optional) Configuring iNOF Zone Isolation
==========================================

(Optional) Configuring iNOF Zone Isolation

#### Context

After iNOF zone isolation takes effect, host communication is restricted.

* Hosts in different iNOF zones cannot communicate with each other. Hosts added to the default zone cannot communicate with hosts added to a customized zone.
* The communication rules between hosts added to the same iNOF zone vary depending on the host roles.
  
  Host roles are classified into the following types:
  
  + Initiator: initiates NVMe sessions and sends NVMe commands.
  + Target: transmits input and output data based on the commands from the initiator.
  + Initiator&Target: has both initiator and target capabilities.
  + Invalid: The host role is unknown or not obtained.
  
  As described in [Table 1](#EN-US_TASK_0000001564123445__table169822612910), hosts in the same iNOF zone cannot communicate with each other only if they are both initiators or both targets; in other cases, they can communicate with each other.
  
  A host can be added to multiple iNOF customized zones. As long as the zones to which two hosts are added overlap and the two hosts are not both initiators or both targets, they can communicate with each other.
  
  **Table 1** Communication rules between host roles
  | Host Role | Initiator | Target | Initiator&Target | Invalid |
  | --- | --- | --- | --- | --- |
  | Initiator | N | Y | Y | Y |
  | Target | Y | N | Y | Y |
  | Initiator&Target | Y | Y | Y | Y |
  | Invalid | Y | Y | Y | Y |
  | Y: Communication is allowed.  N: Communication is not allowed. | | | | |

![](public_sys-resources/note_3.0-en-us.png) 

If the device is configured as an iNOF client, the iNOF zone isolation function cannot be configured locally. Instead, the configuration synchronized from the iNOF reflector takes effect.



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
4. Enable iNOF zone isolation.
   
   
   ```
   [hard-zoning enable](cmdqueryname=hard-zoning+enable)
   ```
   
   By default, iNOF zone isolation is disabled.
5. Exit the iNOF view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
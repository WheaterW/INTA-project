Configuring BFD for iNOF
========================

Configuring BFD for iNOF

#### Context

BFD for iNOF can rapidly detect link faults in an iNOF system and promptly notify hosts in the same iNOF zone accordingly to implement link switchover.

![](public_sys-resources/note_3.0-en-us.png) 

* The device does not support BFD for iNOF when functioning as an iNOF client. The BFD for iNOF configuration on the client is synchronized from the iNOF reflector.
* If two iNOF reflectors exist in an iNOF system, their BFD for iNOF configurations must be the same to ensure successful data backup between them.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable BFD globally.
   
   
   ```
   [bfd](cmdqueryname=bfd)
   ```
3. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
4. Enable the AI service and enter the AI service view.
   
   
   ```
   [ai-service](cmdqueryname=ai-service)
   ```
5. Enable iNOF and enter the iNOF view.
   
   
   ```
   [inof](cmdqueryname=inof)
   ```
6. Enable BFD for iNOF and establish a BFD session in the iNOF system.
   
   
   ```
   [inof bfd enable](cmdqueryname=inof+bfd+enable)
   ```
   
   By default, BFD for iNOF is disabled.
7. (Optional) Set BFD parameters used to establish a BFD session.
   
   
   ```
   [inof bfd](cmdqueryname=inof+bfd) { min-tx-interval min-tx-interval | min-rx-interval min-rx-interval | detect-multiplier detect-multiplier } *
   ```
   
   By default, the minimum intervals for sending and receiving BFD packets in an iNOF system are both 1000 ms, and the local detection multiplier is 3.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
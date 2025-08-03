Configuring an Accounting Scheme
================================

Configuring an Accounting Scheme

#### Context

An accounting scheme defines the accounting methods used for user accounting. If an accounting scheme is configured, by default, users are allowed to go online after accounting fails. Local authentication does not support accounting.

![](public_sys-resources/note_3.0-en-us.png) 

By default, the accounting scheme named **default** is bound to the domain named **default\_admin**. Modifying this accounting scheme affects the domain configuration. Exercise caution when modifying this accounting scheme. Otherwise, user accounting fails.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the AAA view.
   
   
   ```
   [aaa](cmdqueryname=aaa)
   ```
3. Create an accounting scheme and enter the accounting scheme view.
   
   
   ```
   [accounting-scheme](cmdqueryname=accounting-scheme) accounting-scheme-name
   ```
4. Configure an accounting method.
   
   
   ```
   [accounting-mode](cmdqueryname=accounting-mode) { hwtacacs | none | radius | }
   ```
5. (Optional) Configure a policy used after accounting-start fails.
   
   
   ```
   [accounting start-fail](cmdqueryname=accounting+start-fail) { offline | online }
   ```
   
   By default, users are allowed to go online after accounting-start fails.
   
   * **online**: allows users to go online to prevent users from being affected by accounting failures caused by network faults.
   * **offline**: rejects users' access requests and stops providing services to users if accounting fails.
6. (Optional) Configure a policy used after real-time accounting fails.
   1. Enable real-time accounting and set the accounting interval.
      
      
      ```
      [accounting realtime](cmdqueryname=accounting+realtime) interval
      ```
      
      By default, the device performs duration-based accounting, and real-time accounting is disabled.
   2. Set the maximum number of times that the system does not respond to real-time accounting requests and the policy to be used after real-time accounting fails.
      
      
      ```
      [accounting interim-fail](cmdqueryname=accounting+interim-fail) [ max-times times ] { offline | online }
      ```
      
      By default, the maximum number of times that the system does not respond to real-time accounting requests is 3, and users are allowed to go online after real-time accounting fails.
7. (Optional) Configure a policy used after accounting-stop fails.
   
   
   * Enter the RADIUS server template view, configure the function of retransmitting RADIUS Accounting-Request(Stop) packets, and set the maximum number of times Accounting-Request(Stop) packets can be retransmitted.
     ```
     [radius-server accounting-stop-packet](cmdqueryname=radius-server+accounting-stop-packet) resend [ resend-times ]
     ```
     
     By default, the device is allowed to retransmit Accounting-Request(Stop) packets for a maximum of three times.
   * Enter the system view, configure the function of retransmitting HWTACACS Accounting-Request(Stop) packets, and set the maximum number of times Accounting-Request(Stop) packets can be retransmitted.
     ```
     [hwtacacs-server accounting-stop-packet](cmdqueryname=hwtacacs-server+accounting-stop-packet) resend { disable | enable number }
     ```
     
     By default, the device is allowed to retransmit Accounting-Request(Stop) packets for a maximum of three times.
8. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the **display accounting-scheme** [ **name** *accounting-scheme-name* ] command to check the accounting scheme configuration.
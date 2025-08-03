Configuring Centralized NAT Providing Backup for Distributed NAT
================================================================

Configuring centralized NAT providing backup for distributed NAT ensures the reliability of the NAT service on distributed NAT devices.

#### Context

When both the BRAS and CR exist on the live network, the BRAS supports distributed NAT, and the NAT device attached to the CR supports centralized NAT. If the service board of the BRAS becomes faulty, the BRAS distributes user traffic to the CR for NAT implementation, existing users do not go offline, and new users are allowed to go online. When the fault on the service board of the BRAS is rectified, the BRAS reestablishes NAT user tables, and user traffic is switched back to the BRAS for NAT implementation.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Only [dedicated boards](dc_ne_nat_feature_0008.html#EN-US_CONCEPT_0172359138__li1033371595) support this configuration.


![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this case, cold backup is used to distribute user traffic from distributed devices to centralized devices for NAT implementation. The IP addresses in the NAT address pool of the CR cannot duplicate with those in the NAT address pool of the BRAS.



#### Procedure

1. Configure centralized backup for distributed NAT on the BRAS.
   1. Create a NAT instance and bind it to a service-instance group. For details, see [Configuring Basic NAT Functions](dc_ne_nat_cfg_0010.html).
   2. Configure the distributed NAT traffic policy and conversion policy. For details, see [Configuring NAT for User Traffic in Distributed Mode](dc_ne_nat_cfg_0068_1.html#EN-US_TASK_0000001092997662).
   3. Configure the automatic switchover and switchback function for centralized NAT providing backup for distributed NAT based on the policy selected. (The following configurations are performed in the NAT instance view.)
      
      
      * Configure the automatic switchover and switchback function for centralized NAT providing backup for distributed NAT.
        
        1. Run the [**nat centralized-backup enable**](cmdqueryname=nat+centralized-backup+enable) command to enable the automatic switchover and switchback function for centralized NAT providing backup for distributed NAT.
           
           After the NAT function on the BRAS becomes unavailable, the BRAS switches user traffic to the NAT device attached to the CR for NAT implementation. After the NAT function on the BRAS is restored, user traffic is switched back to the BRAS for NAT implementation.
           
           ![](../../../../public_sys-resources/note_3.0-en-us.png) 
           
           The centralized NAT providing backup for distributed NAT function is mutually exclusive with inter-chassis backup, NAT Easy IP, and NAT traffic policy on the outbound interface.
      * Configure the manual switchover and automatic switchback function for centralized NAT providing backup for distributed NAT.
        
        1. Run the [**nat centralized-backup enable**](cmdqueryname=nat+centralized-backup+enable) command to enable the automatic switchover and switchback function for centralized NAT providing backup for distributed NAT.
        2. Run the [**nat centralized-backup manual switch**](cmdqueryname=nat+centralized-backup+manual+switch) command to enable the manual switchover function for centralized NAT providing backup for distributed NAT.
           
           After the manual switchover function for centralized NAT providing backup for distributed NAT is enabled, the NAT instance is in the switchover status regardless of whether the NAT service on the distributed device is running properly. In this case, user traffic is switched from the distributed NAT device to the centralized NAT device for NAT implementation.
      * Configure the automatic switchover and manual switchback function for centralized NAT providing backup for distributed NAT.
        
        1. Run the [**nat centralized-backup enable**](cmdqueryname=nat+centralized-backup+enable) command to enable the automatic switchover and switchback function for centralized NAT providing backup for distributed NAT.
        2. Run the [**nat centralized-backup auto switchover disable**](cmdqueryname=nat+centralized-backup+auto+switchover+disable) command to disable the automatic switchback function for centralized NAT providing backup for distributed NAT.
        3. Run the [**nat centralized-backup manual switchover**](cmdqueryname=nat+centralized-backup+manual+switchover) command to enable the manual switchback function for centralized NAT providing backup for distributed NAT.
           
           After the manual switchback function for centralized NAT providing backup for distributed NAT is enabled, given that at least one CPU of the service board bound to the NAT instance on the distributed NAT device is running properly, the NAT instance is in the switchback status, and user traffic is switched back from the centralized NAT device to the distributed NAT device for NAT implementation.
      * Configure the manual switchover and switchback function for centralized NAT providing backup for distributed NAT.
        
        1. Run the [**nat centralized-backup enable**](cmdqueryname=nat+centralized-backup+enable) command to enable the automatic switchover and switchback function for centralized NAT providing backup for distributed NAT.
        2. Run the [**nat centralized-backup auto switchover disable**](cmdqueryname=nat+centralized-backup+auto+switchover+disable) command to disable the automatic switchback function for centralized NAT providing backup for distributed NAT.
        3. Run the [**nat centralized-backup manual switch**](cmdqueryname=nat+centralized-backup+manual+switch) command to enable the manual switchover function for centralized NAT providing backup for distributed NAT.
           
           After the manual switchover function for centralized NAT providing backup for distributed NAT is enabled, the NAT instance is in the switchover status regardless of whether the NAT service on the distributed device is running properly. In this case, user traffic is switched from the distributed NAT device to the centralized NAT device for NAT implementation.
        4. Run the [**nat centralized-backup manual switchover**](cmdqueryname=nat+centralized-backup+manual+switchover) command to enable the manual switchback function for centralized NAT providing backup for distributed NAT.
           
           After the manual switchback function for centralized NAT providing backup for distributed NAT is enabled, given that at least one CPU of the service board bound to the NAT instance on the distributed NAT device is running properly, the NAT instance is in the switchback status, and user traffic is switched back from the centralized NAT device to the distributed NAT device for NAT implementation.
           
           Before the [**nat centralized-backup manual switchover**](cmdqueryname=nat+centralized-backup+manual+switchover) command is run, the manual switchover function must be disabled in centralized NAT providing backup for distributed NAT.
   4. (Optional) Run [**nat centralized-backup redirect-ip**](cmdqueryname=nat+centralized-backup+redirect-ip+vpn-instance) *ip-addr* [ **vpn-instance** *vpn-instance-name* ]
      
      
      
      A redirection IP address is configured for centralized NAT providing backup for distributed NAT.
      
      
      
      After a redirection IP address for centralized NAT providing backup for distributed NAT is configured, user traffic switched to the centralized NAT device for NAT processing is forwarded to the redirection IP address.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      The redirection VPN instance name for centralized NAT providing backup for distributed NAT must be the same as that configured on the centralized NAT device and CR.
   5. (Optional) Run [**nat centralized-backup switch down-number**](cmdqueryname=nat+centralized-backup+switch+down-number) *down-number*
      
      
      
      The maximum number of allowable CPU faults in centralized NAT providing backup for distributed NAT is configured.
      
      
      
      When *down-number* is less than or equal to the number of CPUs of service boards to which an instance is bound, the [**nat centralized-backup switch down-number**](cmdqueryname=nat+centralized-backup+switch+down-number) command may have the following impacts on the system:
      
      * When the number of CPU faults on the current service board in the NAT instance is greater than or equal to *down-number*, user traffic automatically switches to centralized devices for NAT implementation.
      * When the number of CPU faults on the current service board in the NAT instance is less than *down-number*, user traffic can be manually switched back to distributed devices for NAT implementation. During the switchback, if the CPUs in the NAT instance do not recover, users may be logged out.
      * When no CPU fault occurs on the current service board in the NAT instance, user traffic can automatically switch back to distributed devices for NAT implementation.If *down-number* is greater than the total number of service boards' CPUs to which a NAT instance is bound, running the [**nat centralized-backup switch down-number**](cmdqueryname=nat+centralized-backup+switch+down-number) command poses the following impacts:
      * If the maximum number of faulty CPUs allowed in a NAT instance is greater than the value of *down-number*, all CPUs on the service boards are faulty and user traffic automatically switches to centralized devices for NAT implementation.
      * Because the number of service boards' faulty CPUs in the NAT instance is always less than *down-number*, ensure that at least one CPU of a service board to which the NAT instance is bound is available. In this case, user traffic can be manually switched back to the distributed device for NAT processing.
   6. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) After the preceding operations are performed, configure a route advertisement policy.
      * For centralized NAT providing backup for distributed NAT in a non-tunnel deployment scenario, both the distributed and centralized NAT devices need to be deployed with a private routing policy. This leads to security risks, and the user IP addresses of different BRASs cannot overlap. The route advertisement policy in this scenario is as follows:
        
        + NAT public network address pool route advertisement: Both the distributed and centralized NAT devices advertise routes from the NAT public network address pool to the internet.
        + Private network address pool route advertisement: The distributed NAT device advertises routes from the private network address pool to the centralized NAT device.
        + Internet route advertisement: The centralized NAT device advertises internet routes to the distributed NAT device so that the internet traffic can be distributed to the centralized NAT device and then redirects traffic to the centralized NAT device.
      * For centralized NAT providing backup for distributed NAT in a tunnel deployment scenario, the devices between the distributed and centralized NAT devices do not need to be deployed with a private network routing policy. The user addresses of the distributed NAT device can overlap but a VPN needs to be deployed. The centralized NAT device needs to carry all VPN traffic by the distributed NAT device. In this case, a lot of L3VPNs need to be deployed. Such a complex network is not recommended. The route advertisement policy in this scenario is as follows:
        + NAT public network address pool route advertisement: Both the distributed and centralized NAT devices advertise routes from the NAT public network address pool to the internet.
        + Private network address pool route advertisement: Routes from the private network address pool on the distributed NAT device are advertised to the centralized NAT device in a VPN instance.
        + Internet route advertisement: The centralized NAT device advertises internet routes to the distributed NAT device so that the internet traffic can be distributed to the centralized NAT device.
2. Deploy the centralized NAT function on the centralized NAT device.
   1. Create a NAT instance and bind it to a service-instance group. For details, see [Configuring Basic NAT Functions](dc_ne_nat_cfg_0010.html).
   2. Configure a centralized NAT traffic policy and a conversion policy. For details, see [Centralized NAT for User Traffic](dc_ne_nat_cfg_0018.html).
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
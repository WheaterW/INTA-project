Configuring VRRP6 Time Parameters
=================================

Configuring VRRP6 Time Parameters

#### Context

A VRRP6 group performs a master/backup switchover if the master device fails or if a network is busy. After the original master device recovers or network communication is restored, the VRRP6 group reselects the master device based on device priorities.

Setting appropriate VRRP6 time parameters based on network flapping status. This minimizes the network interruptions or packet loss caused by frequent master/backup VRRP switchovers.


[Enabling VRRP6 Preemption and Configuring a Preemption Delay](vrp_vrrp6_cfg_0019.html)



[Configuring an Interval for Sending VRRP6 Advertisement Packets](vrp_vrrp6_cfg_0020.html)



[Configuring a VRRP6 Status Recovery Delay](vrp_vrrp6_cfg_0021.html)



[Configuring a Timeout Period for a Backup Device in a VRRP6 Group](vrp_vrrp6_cfg_0022.html)



[Configuring an Interval at Which the Master Device Sends NA Messages](vrp_vrrp6_cfg_0023.html)
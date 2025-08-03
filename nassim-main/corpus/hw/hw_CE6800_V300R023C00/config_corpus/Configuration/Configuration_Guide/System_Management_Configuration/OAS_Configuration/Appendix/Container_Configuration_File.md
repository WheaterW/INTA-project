Container Configuration File
============================

Container Configuration File

#### Format of the Container Configuration File

When a container is created, the default configuration file container\_conf.yaml is supported. The file format is as follows. For details about each field, see [Table 1](#EN-US_TOPIC_0000001564125865__table1764061811243).

```
kind: Container
spec:
    containers:
       image:        
       env:        
         - name:   
           value:  
         - name: 
           value:
       resources:      
           requests:        
             cpu:       
             memory:         
             cpuset-cpus:  
           limits:         
             cpu:        
             memory:       
             blkio-weight:       
           restartPolicy: 
           securityContext:        
             capabilities:        
               add:        
                   - 
                   - 
               drop:        
                   - 
                   - 
        network:
            manage-ip:
            business-ip:
            port-range:
        storage:
            volume-type:
            volume-size:
            volume-mount-path:
```

**Table 1** Parameters in the container configuration file
| Field | Description |
| --- | --- |
| kind: Container | Non-parameter and cannot be modified. |
| spec: | Non-parameter and cannot be modified. |
| containers: | Non-parameter and cannot be modified. |
| image: | Name of the image software package used by a container. |
| env: | Non-parameter, which indicates that the following content is used to set the container environment variables. *name* and *value* are a group of variables. Multiple groups of variables can be set. |
| - name:  value: | Parameter, which is used to set the environment variable name. |
| Parameter, which is used to set the environment variable value. |
| resources: | Non-parameter, which indicates that the following content is used to set the container running resources. |
| requests: | Non-parameter, which indicates that the following content is used to set lower limits for container running resources. |
| cpu: | Parameter, which is used to set the minimum number of CPUs required for startup. |
| memory: | Parameter, which is used to set the minimum memory required for startup. |
| cpuset-cpus: | Parameter, which indicates the ID of the CPU core bound to the application. |
| limits: | Non-parameter, which indicates that the following content is used to set upper limits for container running resources. |
| cpu: | Parameter, which is used in the **docker run --cpus** parameter to set the CPU limit. The **docker run --cpu-shares** parameter is set to the value of this parameter multiplied by 1024. |
| memory: | Parameter, which is used in the **docker run --memory** parameter to set the memory limit. The format is number+unit. The unit is MiB or GiB. MiB can be abbreviated to m, M, or MB, and GiB can be abbreviated to g, G, or GB. |
| blkio-weight: | Parameter, which is used in the **docker run --blkio-weight** parameter to set the I/O weight. |
| restartPolicy: | Parameter, which is used in the **docker run --restart** parameter to set the restart policy. This parameter specifies the self-healing mode when a container exits due to a fault. There are four types of status:  no: A container is not automatically restarted.  on-failure[:num]: If a container exits abnormally, it is restarted. You can determine whether to set the maximum number of restart times as required. For example, on-failure:5 indicates that a container can be restarted for a maximum of five times due to a fault.  always: If a container stops, it is always restarted.  unless-stopped: A container is always restarted when it exits. However, the container that has been stopped when the Docker daemon is started cannot be restarted.  NOTE:   * By default, the container restart policy is on-failure:5. * For details about the three types of restart policies, see the description of the **docker run --restart** command. |
| securityContext: | Non-parameter, which indicates that the following content is for security configuration. |
| capabilities: | Non-parameter, which indicates that the following content is used to set the container permission. |
| add: | Parameter, which is used in the **docker run --cap-add** parameter to add capability sets. You can add multiple capability sets. For details, see the **docker run --cap-add** command. |
| drop: | Parameter, which is used in the **docker run --cap-drop** parameter to delete capability sets. You can delete multiple capability sets. For details, see the **docker run --cap-drop** command. |
| network: | Non-parameter, which indicates the configuration items related to network interfaces. |
| manage-ip: | Parameter, which indicates the IP address of the management interface. |
| business-ip: | Parameter, which indicates the IP address of the service interface. |
| port-range: | Parameter, which indicates the range of ports that can be bound. |
| storage: | Parameter, which indicates the configuration items related to container storage. |
| volume-type: | Parameter, which indicates the type of the storage volume for the application. The value *internal* indicates that the built-in storage device is used, and *external* indicates that the external storage device is used. If this parameter is not set, the built-in storage device is used by default. |
| volume-size: | Parameter, which indicates the size of the persistent storage volume allocated to the application. The unit is MB. |
| volume-mount-path: | Parameter, which indicates the mount path of the storage volume in the container. If this parameter is not set, **/data** is used by default. |



#### Signature File of the Configuration File

To ensure the security of the configuration file, the Gnu Privacy Guard (GPG) signature is required for the configuration file. For details, see [Creating a Signature File for the Description File](vrp_OAS_cfg_0009.html).
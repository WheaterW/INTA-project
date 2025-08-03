Creating a Description File for an Image
========================================

Creating a Description File for an Image

#### Image Description File Format

The description file of an image is used to store information about the image created by users. The description file is in the format of [imageName]\_manifest.xml. The description file hellodocker\_manifest.xml of the hellodocker.tar image file is as follows. [Table 1](#EN-US_CONCEPT_0000001563885769__table7721433195814) describes the fields in the file.

```
<?xml version="1.0" encoding="UTF-8"?>
<Manifest>
              <ImageName>hellodocker</ImageName>
              <Version>1.0.0</Version>
              <ImageType>docker</ImageType>
              <Architecture>x86_64</Architecture>
              <CreatedTime>2021-03 20T14:15:14.712657565Z</CreatedTime>
              <Manufacturer>huawei</Manufacturer>
              <Description>hello docker</Description>
              <File>
                <Name>hellodocker.tar</Name>       
                <SHA256>f01a00d9c6b6516c5ed5f4d7824aff891ef7a02c61a44216f717ea515c7b8b2f</SHA256>
              </File>
</Manifest>
```

**Table 1** Fields in the description file
| Field | Description | Remarks | Mandatory (Yes/No) |
| --- | --- | --- | --- |
| ImageName | Image name. | The value can contain a maximum of 127 characters, including only letters, digits, and hyphens (-). Do not use special characters. | Yes |
| Version | Image version. | The value contains a maximum of 63 characters. | Yes |
| ImageType | Image class. | The value contains a maximum of 31 characters. Currently, only Docker images are supported. | Yes |
| Architecture | Architecture supported by the image. | The value contains a maximum of 31 characters. Currently, the x86\_64 and aarch64 architectures are supported. | Yes |
| CreatedTime | Time when an image is created. | The value contains a maximum of 63 characters. You can run the **docker inspect** command to obtain the value. | Yes |
| Manufacturer | Image vendor. | The value contains a maximum of 63 characters. | Yes |
| Description | Image details. | The value contains a maximum of 63 characters. | No |
| File | Name of the TAR image file and its SHA256 value. | - | Yes |
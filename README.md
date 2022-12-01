## Description
Using Django to create a service that on request:
```
GET /api/meta 
```
return a list of files and directories with the date of their creation that are located in the specified directory.

For instance:
```
{
    "data":[
        {
            "name": "src",
            "type": "folder",
            "time": 1665996554107
        },
        {
            "name": "file.py",
            "type": "file",
            "time": 1665996554108
        },
    ]
}
```
The root directory is located in config.py

The service must be started using docker-compose up.

### Prerequisites
All the modules for successful work are in 'requirements.txt'.  
Run the following command in CMD/Console to install:
```
pip install -r requirements.txt
```

### Links of author

[Git](https://github.com/aliksandrion)  
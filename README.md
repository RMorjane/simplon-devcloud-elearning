# E-Learning Web Platform

E-Learning Web Platform is a web application witch display videos you want to find depending on search criteria.

Just type criteria on search bar.

when you click on video item, it redirect you on youtube's link.

![image](https://user-images.githubusercontent.com/71873995/111239479-8cc4f100-85f9-11eb-9f46-9e4fccfa9b9a.png)

![image](https://user-images.githubusercontent.com/71873995/111239565-b716ae80-85f9-11eb-8388-612f408c06ae.png)

## Installation

docker-compose file : 
````
version: "3.1"

services:
  db:
    container_name: dbpostgres
    image: postgres
    restart: always
    env_file: .env
    networks: 
      - netbd
  
  flask_app:
    container_name: flask_video
    build: ./app
    depends_on: 
      - db   
    ports:
      - 3000:3000
    volumes:
      - .:/app
    networks:
      - netbd
    command: sh -c "python main.py"

networks: 
  netbd: {}`
````

Use the following command line :

```bash
docker-compose up --build
```

## Technologies

#### Back-End :
``
Python : language for loading web application,
Flask : creating recipe web application,
Jinja2 : transfering data from Back to Front,
render_template : rendering the web page
``
#### Front-End :
``
HTML5,
CSS3,
Javascript
``


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

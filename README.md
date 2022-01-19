# SAQ Scratcher
Is your favourite libation in stock? 

## Dependencies
### .env
* Create a file called `.env` similar to `.env.sample` in the project's root directory
* Include a product id

### Docker  :smile::whale:
* Install
  * [windows download](https://docs.docker.com/docker-for-windows/install/)
  * [macOS download](https://docs.docker.com/docker-for-mac/install/)
  * [ubuntu download](https://docs.docker.com/install/linux/docker-ce/ubuntu/)


## Run
1. open a terminal and navigate to **saq-scratcher** directory
2. run the following command
    ```bash
    docker-compose up
    ```

## Sample Output
```bash
Getting https://www.saq.com/en/12582247
Waiting for element to be visible
Waiting for element to be visible
{
    "in-store": [
        {
            "distance": "4,079 km",
            "quantity": "1",
            "store_id": "23208",
            "store_name": "Papineau - Crémazie",
            "store_type": "SAQ Sélection"
        }
    ],
    "online": {
        "count": "500"
    }
}
```

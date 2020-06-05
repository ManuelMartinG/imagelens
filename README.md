# Imagelens


## Project Set up
Image processing containerized microservices connected by Kafka topics with persistent images and logs storage in MongoDb and deployed in Kubernetes.

- Microservices:
    - **resizer-service**: Change the size of images
    - **basic-filtering-service**: Apply basic filters to images such as binarization
    - **text-detector-service**: Detect text chunks in the image
    - **object-detector-service**: Detect objects in the image
    - 
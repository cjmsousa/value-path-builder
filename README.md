Builder that allows to generate value path diagrams from a configuration file

## How to run the builder

    $ docker pull cjmsousa/value-path-builder
    $ docker run -p 50001:5000 -d cjmsousa/value-path-builder
    $ curl -F "file=@value-path.yaml" 0.0.0.0:50001 --output value-path.svg
